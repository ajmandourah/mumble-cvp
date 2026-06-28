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
}

func New(br *bridge.Client, cfg config.MumbleConfig) *Server {
	return &Server{bridge: br, cfg: cfg}
}

func (s *Server) RegisterRoutes(mux *http.ServeMux) {
	mux.HandleFunc("GET /api/servers", s.handleServers)
	mux.HandleFunc("GET /api/tree/{srv_id}", s.handleTree)
	mux.HandleFunc("GET /api/users", s.handleUsers)
	mux.HandleFunc("GET /api/channels", s.handleChannels)
	mux.HandleFunc("GET /widget", s.handleWidget)
	mux.HandleFunc("GET /widget2", s.handleWidget2)
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
