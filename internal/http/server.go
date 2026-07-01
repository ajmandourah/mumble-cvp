package http

import (
	"encoding/json"
	"net/http"
	"strconv"
	"strings"

	"github.com/ladis/mumble-cvp/internal/bridge"
	"github.com/ladis/mumble-cvp/internal/config"
)

type Server struct {
	bridge *bridge.Client
	cfg    config.MumbleConfig
	auth   config.HTTPConfig
}

func New(br *bridge.Client, cfg config.MumbleConfig, auth config.HTTPConfig) *Server {
	return &Server{bridge: br, cfg: cfg, auth: auth}
}

func (s *Server) authMiddleware(next http.HandlerFunc) http.HandlerFunc {
	return func(w http.ResponseWriter, r *http.Request) {
		if s.auth.User != "" && s.auth.Pass != "" {
			user, pass, ok := r.BasicAuth()
			if !ok || user != s.auth.User || pass != s.auth.Pass {
				w.Header().Set("WWW-Authenticate", `Basic realm="mumble-cvp"`)
				http.Error(w, "unauthorized", http.StatusUnauthorized)
				return
			}
		}
		next(w, r)
	}
}

func (s *Server) RegisterRoutes(mux *http.ServeMux) {
	// Monitoring endpoints
	mux.HandleFunc("GET /api/servers", s.authMiddleware(s.handleServers))
	mux.HandleFunc("GET /api/tree/{srv_id}", s.authMiddleware(s.handleTree))
	mux.HandleFunc("GET /api/users", s.authMiddleware(s.handleUsers))
	mux.HandleFunc("GET /api/channels", s.authMiddleware(s.handleChannels))
	mux.HandleFunc("GET /api/stats", s.authMiddleware(s.handleStats))
	mux.HandleFunc("GET /api/log", s.authMiddleware(s.handleLog))
	mux.HandleFunc("GET /api/bans", s.authMiddleware(s.handleBans))
	mux.HandleFunc("GET /api/listening", s.authMiddleware(s.handleListening))
	mux.HandleFunc("GET /api/server-name", s.authMiddleware(s.handleServerName))

	// Admin endpoints
	mux.HandleFunc("POST /api/admin/kick", s.authMiddleware(s.handleKick))
	mux.HandleFunc("POST /api/admin/set-state", s.authMiddleware(s.handleSetState))
	mux.HandleFunc("POST /api/admin/add-channel", s.authMiddleware(s.handleAddChannel))
	mux.HandleFunc("POST /api/admin/remove-channel", s.authMiddleware(s.handleRemoveChannel))
	mux.HandleFunc("POST /api/admin/set-channel", s.authMiddleware(s.handleSetChannel))
	mux.HandleFunc("POST /api/admin/send-message", s.authMiddleware(s.handleSendMessage))
	mux.HandleFunc("POST /api/admin/send-message-channel", s.authMiddleware(s.handleSendMessageChannel))
	mux.HandleFunc("POST /api/admin/add-ban", s.authMiddleware(s.handleAddBan))
	mux.HandleFunc("POST /api/admin/remove-ban", s.authMiddleware(s.handleRemoveBan))
	mux.HandleFunc("GET /api/admin/acl", s.authMiddleware(s.handleACL))
	mux.HandleFunc("GET /api/admin/permissions", s.authMiddleware(s.handlePermissions))
	mux.HandleFunc("GET /api/admin/registered", s.authMiddleware(s.handleRegistered))
	mux.HandleFunc("GET /api/admin/registration", s.authMiddleware(s.handleRegistration))
	mux.HandleFunc("GET /api/admin/config", s.authMiddleware(s.handleGetConfig))
	mux.HandleFunc("POST /api/admin/config", s.authMiddleware(s.handleSetConfig))
	mux.HandleFunc("GET /api/admin/certificates", s.authMiddleware(s.handleCertificates))

	// Widget endpoints
	mux.HandleFunc("GET /widget", s.authMiddleware(s.handleWidget))
	mux.HandleFunc("GET /widget2", s.authMiddleware(s.handleWidget2))
}

func (s *Server) handleServers(w http.ResponseWriter, r *http.Request) {
	servers, err := s.bridge.GetBootedServers(s.cfg.Secret, s.cfg.Host, s.cfg.Port)
	if err != nil {
		jsonError(w, err)
		return
	}
	jsonOK(w, servers)
}

func (s *Server) handleTree(w http.ResponseWriter, r *http.Request) {
	srvID, err := strconv.Atoi(r.PathValue("srv_id"))
	if err != nil {
		srvID = s.cfg.ServerID
	}
	srvID = s.bridge.ResolveServerID(s.cfg.Secret, s.cfg.Host, s.cfg.Port, srvID)
	tree, err := s.bridge.GetTree(s.cfg.Secret, s.cfg.Host, s.cfg.Port, srvID)
	if err != nil {
		jsonError(w, err)
		return
	}
	jsonOK(w, tree)
}

func (s *Server) handleUsers(w http.ResponseWriter, r *http.Request) {
	srvID := s.cfg.ServerID
	if q := r.URL.Query().Get("server_id"); q != "" {
		srvID, _ = strconv.Atoi(q)
	}
	srvID = s.bridge.ResolveServerID(s.cfg.Secret, s.cfg.Host, s.cfg.Port, srvID)
	users, err := s.bridge.GetUsers(s.cfg.Secret, s.cfg.Host, s.cfg.Port, srvID)
	if err != nil {
		jsonError(w, err)
		return
	}
	jsonOK(w, users)
}

func (s *Server) handleChannels(w http.ResponseWriter, r *http.Request) {
	srvID := s.cfg.ServerID
	if q := r.URL.Query().Get("server_id"); q != "" {
		srvID, _ = strconv.Atoi(q)
	}
	srvID = s.bridge.ResolveServerID(s.cfg.Secret, s.cfg.Host, s.cfg.Port, srvID)
	channels, err := s.bridge.GetChannels(s.cfg.Secret, s.cfg.Host, s.cfg.Port, srvID)
	if err != nil {
		jsonError(w, err)
		return
	}
	jsonOK(w, channels)
}

func (s *Server) handleStats(w http.ResponseWriter, r *http.Request) {
	srvID := s.cfg.ServerID
	srvID = s.bridge.ResolveServerID(s.cfg.Secret, s.cfg.Host, s.cfg.Port, srvID)
	stats, err := s.bridge.GetServerStats(s.cfg.Secret, s.cfg.Host, s.cfg.Port, srvID)
	if err != nil {
		jsonError(w, err)
		return
	}
	jsonOK(w, stats)
}

func (s *Server) handleLog(w http.ResponseWriter, r *http.Request) {
	srvID := s.cfg.ServerID
	srvID = s.bridge.ResolveServerID(s.cfg.Secret, s.cfg.Host, s.cfg.Port, srvID)
	first, _ := strconv.Atoi(r.URL.Query().Get("first"))
	last, _ := strconv.Atoi(r.URL.Query().Get("last"))
	if last == 0 {
		last = 100
	}
	entries, err := s.bridge.GetLog(s.cfg.Secret, s.cfg.Host, s.cfg.Port, srvID, first, last)
	if err != nil {
		jsonError(w, err)
		return
	}
	jsonOK(w, entries)
}

func (s *Server) handleBans(w http.ResponseWriter, r *http.Request) {
	srvID := s.cfg.ServerID
	srvID = s.bridge.ResolveServerID(s.cfg.Secret, s.cfg.Host, s.cfg.Port, srvID)
	bans, err := s.bridge.GetBans(s.cfg.Secret, s.cfg.Host, s.cfg.Port, srvID)
	if err != nil {
		jsonError(w, err)
		return
	}
	jsonOK(w, bans)
}

func (s *Server) handleListening(w http.ResponseWriter, r *http.Request) {
	srvID := s.cfg.ServerID
	srvID = s.bridge.ResolveServerID(s.cfg.Secret, s.cfg.Host, s.cfg.Port, srvID)
	listening, err := s.bridge.GetListening(s.cfg.Secret, s.cfg.Host, s.cfg.Port, srvID)
	if err != nil {
		jsonError(w, err)
		return
	}
	jsonOK(w, listening)
}

func (s *Server) handleServerName(w http.ResponseWriter, r *http.Request) {
	srvID := s.cfg.ServerID
	srvID = s.bridge.ResolveServerID(s.cfg.Secret, s.cfg.Host, s.cfg.Port, srvID)
	name, err := s.bridge.GetServerName(s.cfg.Secret, s.cfg.Host, s.cfg.Port, srvID)
	if err != nil {
		jsonError(w, err)
		return
	}
	jsonOK(w, map[string]string{"name": name})
}

// Admin handlers

func (s *Server) handleKick(w http.ResponseWriter, r *http.Request) {
	var raw map[string]any
	if err := json.NewDecoder(r.Body).Decode(&raw); err != nil {
		jsonError(w, err)
		return
	}
	session := 0
	if v, ok := raw["session"].(float64); ok {
		session = int(v)
	}
	reason := ""
	if v, ok := raw["reason"].(string); ok {
		reason = v
	}
	srvID := s.bridge.ResolveServerID(s.cfg.Secret, s.cfg.Host, s.cfg.Port, s.cfg.ServerID)
	if err := s.bridge.KickUser(s.cfg.Secret, s.cfg.Host, s.cfg.Port, srvID, session, reason); err != nil {
		jsonError(w, err)
		return
	}
	jsonOK(w, map[string]string{"status": "ok"})
}

func (s *Server) handleSetState(w http.ResponseWriter, r *http.Request) {
	var raw map[string]any
	if err := json.NewDecoder(r.Body).Decode(&raw); err != nil {
		jsonError(w, err)
		return
	}
	session := 0
	if v, ok := raw["session"].(float64); ok {
		session = int(v)
	}
	channel := 0
	if v, ok := raw["channel"].(float64); ok {
		channel = int(v)
	}
	mute := false
	if v, ok := raw["mute"].(bool); ok {
		mute = v
	}
	deaf := false
	if v, ok := raw["deaf"].(bool); ok {
		deaf = v
	}
	suppress := false
	if v, ok := raw["suppress"].(bool); ok {
		suppress = v
	}
	priority := false
	if v, ok := raw["priority"].(bool); ok {
		priority = v
	}
	srvID := s.bridge.ResolveServerID(s.cfg.Secret, s.cfg.Host, s.cfg.Port, s.cfg.ServerID)
	if err := s.bridge.SetState(s.cfg.Secret, s.cfg.Host, s.cfg.Port, srvID, session, channel, mute, deaf, suppress, priority); err != nil {
		jsonError(w, err)
		return
	}
	jsonOK(w, map[string]string{"status": "ok"})
}

func (s *Server) handleAddChannel(w http.ResponseWriter, r *http.Request) {
	var raw map[string]any
	if err := json.NewDecoder(r.Body).Decode(&raw); err != nil {
		jsonError(w, err)
		return
	}
	name := ""
	if n, ok := raw["name"].(string); ok {
		name = n
	}
	parent := 0
	if p, ok := raw["parent"].(float64); ok {
		parent = int(p)
	} else if p, ok := raw["parent"].(string); ok {
		parent, _ = strconv.Atoi(p)
	}
	srvID := s.bridge.ResolveServerID(s.cfg.Secret, s.cfg.Host, s.cfg.Port, s.cfg.ServerID)
	id, err := s.bridge.AddChannel(s.cfg.Secret, s.cfg.Host, s.cfg.Port, srvID, name, parent)
	if err != nil {
		jsonError(w, err)
		return
	}
	jsonOK(w, map[string]int{"id": id})
}

func (s *Server) handleRemoveChannel(w http.ResponseWriter, r *http.Request) {
	var raw map[string]any
	if err := json.NewDecoder(r.Body).Decode(&raw); err != nil {
		jsonError(w, err)
		return
	}
	id := 0
	if v, ok := raw["id"].(float64); ok {
		id = int(v)
	}
	srvID := s.bridge.ResolveServerID(s.cfg.Secret, s.cfg.Host, s.cfg.Port, s.cfg.ServerID)
	if err := s.bridge.RemoveChannel(s.cfg.Secret, s.cfg.Host, s.cfg.Port, srvID, id); err != nil {
		jsonError(w, err)
		return
	}
	jsonOK(w, map[string]string{"status": "ok"})
}

func (s *Server) handleSetChannel(w http.ResponseWriter, r *http.Request) {
	var raw map[string]any
	if err := json.NewDecoder(r.Body).Decode(&raw); err != nil {
		jsonError(w, err)
		return
	}
	ch := bridge.Channel{}
	if v, ok := raw["id"].(float64); ok {
		ch.ID = int(v)
	}
	if v, ok := raw["name"].(string); ok {
		ch.Name = v
	}
	if v, ok := raw["description"].(string); ok {
		ch.Description = v
	}
	if v, ok := raw["position"].(float64); ok {
		ch.Position = int(v)
	}
	srvID := s.bridge.ResolveServerID(s.cfg.Secret, s.cfg.Host, s.cfg.Port, s.cfg.ServerID)
	if err := s.bridge.SetChannelState(s.cfg.Secret, s.cfg.Host, s.cfg.Port, srvID, ch); err != nil {
		jsonError(w, err)
		return
	}
	jsonOK(w, map[string]string{"status": "ok"})
}

func (s *Server) handleSendMessage(w http.ResponseWriter, r *http.Request) {
	var raw map[string]any
	if err := json.NewDecoder(r.Body).Decode(&raw); err != nil {
		jsonError(w, err)
		return
	}
	session := 0
	if v, ok := raw["session"].(float64); ok {
		session = int(v)
	}
	text := ""
	if v, ok := raw["text"].(string); ok {
		text = v
	}
	srvID := s.bridge.ResolveServerID(s.cfg.Secret, s.cfg.Host, s.cfg.Port, s.cfg.ServerID)
	if err := s.bridge.SendMessage(s.cfg.Secret, s.cfg.Host, s.cfg.Port, srvID, session, text); err != nil {
		jsonError(w, err)
		return
	}
	jsonOK(w, map[string]string{"status": "ok"})
}

func (s *Server) handleSendMessageChannel(w http.ResponseWriter, r *http.Request) {
	var raw map[string]any
	if err := json.NewDecoder(r.Body).Decode(&raw); err != nil {
		jsonError(w, err)
		return
	}
	channelID := 0
	if v, ok := raw["channel_id"].(float64); ok {
		channelID = int(v)
	}
	tree := false
	if v, ok := raw["tree"].(bool); ok {
		tree = v
	}
	text := ""
	if v, ok := raw["text"].(string); ok {
		text = v
	}
	srvID := s.bridge.ResolveServerID(s.cfg.Secret, s.cfg.Host, s.cfg.Port, s.cfg.ServerID)
	if err := s.bridge.SendMessageChannel(s.cfg.Secret, s.cfg.Host, s.cfg.Port, srvID, channelID, tree, text); err != nil {
		jsonError(w, err)
		return
	}
	jsonOK(w, map[string]string{"status": "ok"})
}

func (s *Server) handleAddBan(w http.ResponseWriter, r *http.Request) {
	var raw map[string]any
	if err := json.NewDecoder(r.Body).Decode(&raw); err != nil {
		jsonError(w, err)
		return
	}
	address := ""
	if v, ok := raw["address"].(string); ok {
		address = v
	}
	bits := 32
	if v, ok := raw["bits"].(float64); ok {
		bits = int(v)
	}
	name := ""
	if v, ok := raw["name"].(string); ok {
		name = v
	}
	reason := ""
	if v, ok := raw["reason"].(string); ok {
		reason = v
	}
	duration := 0
	if v, ok := raw["duration"].(float64); ok {
		duration = int(v)
	}
	srvID := s.bridge.ResolveServerID(s.cfg.Secret, s.cfg.Host, s.cfg.Port, s.cfg.ServerID)
	if err := s.bridge.AddBan(s.cfg.Secret, s.cfg.Host, s.cfg.Port, srvID, address, bits, name, reason, duration); err != nil {
		jsonError(w, err)
		return
	}
	jsonOK(w, map[string]string{"status": "ok"})
}

func (s *Server) handleRemoveBan(w http.ResponseWriter, r *http.Request) {
	var raw map[string]any
	if err := json.NewDecoder(r.Body).Decode(&raw); err != nil {
		jsonError(w, err)
		return
	}
	address := ""
	if v, ok := raw["address"].(string); ok {
		address = v
	}
	bits := 32
	if v, ok := raw["bits"].(float64); ok {
		bits = int(v)
	}
	srvID := s.bridge.ResolveServerID(s.cfg.Secret, s.cfg.Host, s.cfg.Port, s.cfg.ServerID)
	if err := s.bridge.RemoveBan(s.cfg.Secret, s.cfg.Host, s.cfg.Port, srvID, address, bits); err != nil {
		jsonError(w, err)
		return
	}
	jsonOK(w, map[string]string{"status": "ok"})
}

func (s *Server) handleACL(w http.ResponseWriter, r *http.Request) {
	srvID := s.bridge.ResolveServerID(s.cfg.Secret, s.cfg.Host, s.cfg.Port, s.cfg.ServerID)
	channelID, _ := strconv.Atoi(r.URL.Query().Get("channelid"))
	acl, err := s.bridge.GetACL(s.cfg.Secret, s.cfg.Host, s.cfg.Port, srvID, channelID)
	if err != nil {
		jsonError(w, err)
		return
	}
	jsonOK(w, acl)
}

func (s *Server) handlePermissions(w http.ResponseWriter, r *http.Request) {
	srvID := s.bridge.ResolveServerID(s.cfg.Secret, s.cfg.Host, s.cfg.Port, s.cfg.ServerID)
	session, _ := strconv.Atoi(r.URL.Query().Get("session"))
	channelID, _ := strconv.Atoi(r.URL.Query().Get("channelid"))
	perms, err := s.bridge.GetEffectivePermissions(s.cfg.Secret, s.cfg.Host, s.cfg.Port, srvID, session, channelID)
	if err != nil {
		jsonError(w, err)
		return
	}
	jsonOK(w, perms)
}

func (s *Server) handleRegistered(w http.ResponseWriter, r *http.Request) {
	srvID := s.bridge.ResolveServerID(s.cfg.Secret, s.cfg.Host, s.cfg.Port, s.cfg.ServerID)
	filter := r.URL.Query().Get("filter")
	users, err := s.bridge.GetRegisteredUsers(s.cfg.Secret, s.cfg.Host, s.cfg.Port, srvID, filter)
	if err != nil {
		jsonError(w, err)
		return
	}
	jsonOK(w, users)
}

func (s *Server) handleRegistration(w http.ResponseWriter, r *http.Request) {
	srvID := s.bridge.ResolveServerID(s.cfg.Secret, s.cfg.Host, s.cfg.Port, s.cfg.ServerID)
	userID, _ := strconv.Atoi(r.URL.Query().Get("id"))
	info, err := s.bridge.GetRegistration(s.cfg.Secret, s.cfg.Host, s.cfg.Port, srvID, userID)
	if err != nil {
		jsonError(w, err)
		return
	}
	jsonOK(w, info)
}

func (s *Server) handleGetConfig(w http.ResponseWriter, r *http.Request) {
	srvID := s.bridge.ResolveServerID(s.cfg.Secret, s.cfg.Host, s.cfg.Port, s.cfg.ServerID)
	conf, err := s.bridge.GetAllConf(s.cfg.Secret, s.cfg.Host, s.cfg.Port, srvID)
	if err != nil {
		jsonError(w, err)
		return
	}
	jsonOK(w, conf)
}

func (s *Server) handleSetConfig(w http.ResponseWriter, r *http.Request) {
	var raw map[string]any
	if err := json.NewDecoder(r.Body).Decode(&raw); err != nil {
		jsonError(w, err)
		return
	}
	key := ""
	if v, ok := raw["key"].(string); ok {
		key = v
	}
	value := ""
	if v, ok := raw["value"].(string); ok {
		value = v
	} else if v, ok := raw["value"].(float64); ok {
		value = strconv.FormatFloat(v, 'f', -1, 64)
	} else if v, ok := raw["value"].(bool); ok {
		value = strconv.FormatBool(v)
	}
	srvID := s.bridge.ResolveServerID(s.cfg.Secret, s.cfg.Host, s.cfg.Port, s.cfg.ServerID)
	if err := s.bridge.SetConf(s.cfg.Secret, s.cfg.Host, s.cfg.Port, srvID, key, value); err != nil {
		jsonError(w, err)
		return
	}
	jsonOK(w, map[string]string{"status": "ok"})
}

func (s *Server) handleCertificates(w http.ResponseWriter, r *http.Request) {
	srvID := s.bridge.ResolveServerID(s.cfg.Secret, s.cfg.Host, s.cfg.Port, s.cfg.ServerID)
	session, _ := strconv.Atoi(r.URL.Query().Get("session"))
	certs, err := s.bridge.GetCertificateList(s.cfg.Secret, s.cfg.Host, s.cfg.Port, srvID, session)
	if err != nil {
		jsonError(w, err)
		return
	}
	jsonOK(w, certs)
}

func (s *Server) handleWidget(w http.ResponseWriter, r *http.Request) {
	srvID := s.cfg.ServerID
	if q := r.URL.Query().Get("server_id"); q != "" {
		srvID, _ = strconv.Atoi(q)
	}
	srvID = s.bridge.ResolveServerID(s.cfg.Secret, s.cfg.Host, s.cfg.Port, srvID)
	tree, err := s.bridge.GetTree(s.cfg.Secret, s.cfg.Host, s.cfg.Port, srvID)
	if err != nil {
		jsonError(w, err)
		return
	}
	widget := buildWidget(tree)
	jsonOK(w, widget)
}

func (s *Server) handleWidget2(w http.ResponseWriter, r *http.Request) {
	srvID := s.cfg.ServerID
	if q := r.URL.Query().Get("server_id"); q != "" {
		srvID, _ = strconv.Atoi(q)
	}
	srvID = s.bridge.ResolveServerID(s.cfg.Secret, s.cfg.Host, s.cfg.Port, srvID)
	tree, err := s.bridge.GetTree(s.cfg.Secret, s.cfg.Host, s.cfg.Port, srvID)
	if err != nil {
		jsonError(w, err)
		return
	}
	users := flattenUsers(tree)
	widget := buildWidget2(users)
	jsonOK(w, widget)
}

type WidgetUser struct {
	Name       string `json:"name"`
	Channel    string `json:"channel"`
	SelfMute   bool   `json:"self_mute"`
	SelfDeaf   bool   `json:"self_deaf"`
	Mute       bool   `json:"mute"`
	Deaf       bool   `json:"deaf"`
	Suppress   bool   `json:"suppress"`
	Priority   bool   `json:"priority"`
	Recording  bool   `json:"recording"`
	Registered bool   `json:"registered"`
	Version    string `json:"version"`
	Platform   string `json:"platform"`
}

func buildWidget(tree *bridge.Tree) *WidgetUser {
	users := flattenUsers(tree)
	if len(users) == 0 {
		return nil
	}
	u := users[0]
	return &WidgetUser{
		Name:       u.Name,
		Channel:    findChannelName(tree, u.ChannelID),
		SelfMute:   u.SelfMute,
		SelfDeaf:   u.SelfDeaf,
		Mute:       u.Mute,
		Deaf:       u.Deaf,
		Suppress:   u.Suppress,
		Priority:   u.PrioritySpeaker,
		Recording:  u.Recording,
		Registered: u.Registered,
		Version:    u.Version,
		Platform:   u.Platform,
	}
}

func buildWidget2(users []bridge.User) []WidgetUser {
	result := make([]WidgetUser, 0, len(users))
	for _, u := range users {
		result = append(result, WidgetUser{
			Name:       u.Name,
			SelfMute:   u.SelfMute,
			SelfDeaf:   u.SelfDeaf,
			Mute:       u.Mute,
			Deaf:       u.Deaf,
			Suppress:   u.Suppress,
			Priority:   u.PrioritySpeaker,
			Recording:  u.Recording,
			Registered: u.Registered,
		})
	}
	return result
}

func flattenUsers(tree *bridge.Tree) []bridge.User {
	var result []bridge.User
	result = append(result, tree.Users...)
	for _, child := range tree.Children {
		result = append(result, flattenUsers(&child)...)
	}
	return result
}

func findChannelName(tree *bridge.Tree, id int) string {
	if tree.Channel.ID == id {
		return tree.Channel.Name
	}
	for _, child := range tree.Children {
		if name := findChannelName(&child, id); name != "" {
			return name
		}
	}
	return ""
}

func jsonOK(w http.ResponseWriter, data any) {
	w.Header().Set("Content-Type", "application/json")
	json.NewEncoder(w).Encode(data)
}

func jsonError(w http.ResponseWriter, err error) {
	w.Header().Set("Content-Type", "application/json")
	w.WriteHeader(http.StatusInternalServerError)
	json.NewEncoder(w).Encode(map[string]string{"error": strings.ReplaceAll(err.Error(), "\n", " ")})
}
