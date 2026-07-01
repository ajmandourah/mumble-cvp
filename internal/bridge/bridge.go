package bridge

import (
	"encoding/json"
	"fmt"
	"io"
	"net/http"
	"os/exec"
	"path/filepath"
	"regexp"
	"strings"
	"time"
)

type Client struct {
	url    string
	client *http.Client
	cmd    *exec.Cmd
}

type Tree struct {
	Channel  Channel `json:"channel"`
	Children []Tree  `json:"children"`
	Users    []User  `json:"users"`
}

type User struct {
	Name               string         `json:"name"`
	Session            int            `json:"session"`
	ChannelID          int            `json:"channel_id"`
	Comment            string         `json:"comment"`
	Registered         bool           `json:"registered"`
	Mute               bool           `json:"mute"`
	Deaf               bool           `json:"deaf"`
	SelfMute           bool           `json:"self_mute"`
	SelfDeaf           bool           `json:"self_deaf"`
	Suppress           bool           `json:"suppress"`
	PrioritySpeaker    bool           `json:"priority_speaker"`
	Recording          bool           `json:"recording"`
	Flags              int            `json:"flags"`
	OnLine             bool           `json:"on_line"`
	LastSeen           int64          `json:"last_seen"`
	Version            string         `json:"version"`
	Platform           string         `json:"platform"`
	IP                 string         `json:"ip"`
	OnlineSecs         int            `json:"online_secs"`
	IdleSecs           int            `json:"idle_secs"`
	BytesPerSec        int            `json:"bytes_per_sec"`
	UDPPing            int            `json:"udp_ping"`
	TCPPing            int            `json:"tcp_ping"`
	TCPOnly            bool           `json:"tcp_only"`
	UserID             int            `json:"user_id"`
	Identity           string         `json:"identity"`
	Context            map[string]any `json:"context"`
	Version2           any            `json:"version2"`
	OnlineFormatted    string         `json:"online_formatted"`
	PingMs             int            `json:"ping_ms"`
	BandwidthFormatted string         `json:"bandwidth_formatted"`
}

type Channel struct {
	ID          int    `json:"id"`
	Parent      int    `json:"parent"`
	Name        string `json:"name"`
	Description string `json:"description"`
	Temporary   bool   `json:"temporary"`
	Position    int    `json:"position"`
	Links       []int  `json:"links"`
	MaxUsers    int    `json:"max_users"`
	PasswordSet bool   `json:"password_set"`
}

type ServerStats struct {
	Version  string `json:"version"`
	Uptime   int    `json:"uptime"`
	MaxUsers int    `json:"max_users"`
}

type LogEntry struct {
	Timestamp int64  `json:"timestamp"`
	Text      string `json:"text"`
}

type Ban struct {
	Address  string `json:"address"`
	Bits     int    `json:"bits"`
	Name     string `json:"name"`
	Hash     string `json:"hash"`
	Reason   string `json:"reason"`
	Start    int64  `json:"start"`
	Duration int    `json:"duration"`
	Expires  int64  `json:"expires"`
}

type ListeningInfo struct {
	UserSession int       `json:"user_session"`
	UserName    string    `json:"user_name"`
	Channels    []Channel `json:"channels"`
}

type ACL struct {
	UserID    int      `json:"user_id"`
	Group     string   `json:"group"`
	Allow     []string `json:"allow"`
	Deny      []string `json:"deny"`
	ApplyHere bool     `json:"apply_here"`
	ApplySubs bool     `json:"apply_subs"`
	Inherited bool     `json:"inherited"`
}

type ACLGroup struct {
	Name        string   `json:"name"`
	Inherit     bool     `json:"inherit"`
	Inheritable bool     `json:"inheritable"`
	Members     []string `json:"members"`
	InChannel   bool     `json:"in_channel"`
}

type ACLResult struct {
	ACLs    []ACL      `json:"acls"`
	Groups  []ACLGroup `json:"groups"`
	Inherit bool       `json:"inherit"`
}

type RegisteredUser struct {
	Name   string `json:"name"`
	UserID int    `json:"user_id"`
}

type RegistrationInfo map[string]string

var pythonVersionRe = regexp.MustCompile(`^Python (\d+)\.(\d+)`)

func checkPythonVersion() error {
	out, err := exec.Command("python3", "--version").CombinedOutput()
	if err != nil {
		return fmt.Errorf("python3 not found: %w (output: %s)", err, string(out))
	}
	matches := pythonVersionRe.FindStringSubmatch(string(out))
	if matches == nil {
		return fmt.Errorf("unable to parse python3 version: %s", string(out))
	}
	major := parseInt(matches[1])
	minor := parseInt(matches[2])
	if major < 3 || (major == 3 && minor < 14) {
		return fmt.Errorf("python 3.14 or higher required, found %s", matches[0])
	}
	return nil
}

func parseInt(s string) int {
	var n int
	for _, c := range s {
		n = n*10 + int(c-'0')
	}
	return n
}

func New(bridgeDir string, port int) (*Client, error) {
	if err := checkPythonVersion(); err != nil {
		return nil, fmt.Errorf("python version check: %w", err)
	}

	cmd := exec.Command("python3", filepath.Join(bridgeDir, "bridge.py"), fmt.Sprintf("%d", port))
	cmd.Stdout = nil
	cmd.Stderr = nil

	if err := cmd.Start(); err != nil {
		return nil, fmt.Errorf("start bridge: %w", err)
	}

	c := &Client{
		url: fmt.Sprintf("http://127.0.0.1:%d", port),
		client: &http.Client{
			Timeout: 15 * time.Second,
		},
		cmd: cmd,
	}

	for i := 0; i < 50; i++ {
		if _, err := c.client.Get(c.url + "/health"); err == nil {
			return c, nil
		}
		time.Sleep(500 * time.Millisecond)
	}

	return nil, fmt.Errorf("bridge did not start in time")
}

func (c *Client) Close() error {
	if c.cmd != nil {
		c.cmd.Process.Kill()
		c.cmd.Wait()
	}
	return nil
}

func (c *Client) doRequest(url string, out any) error {
	resp, err := c.client.Get(url)
	if err != nil {
		return err
	}
	defer resp.Body.Close()
	return decodeResponse(resp, out)
}

func (c *Client) doPost(url string, body any, out any) error {
	data, err := json.Marshal(body)
	if err != nil {
		return fmt.Errorf("marshal POST body: %w", err)
	}
	resp, err := c.client.Post(url, "application/json", strings.NewReader(string(data)))
	if err != nil {
		return err
	}
	defer resp.Body.Close()
	return decodeResponse(resp, out)
}

func decodeResponse(resp *http.Response, out any) error {
	body, err := io.ReadAll(resp.Body)
	if err != nil {
		return fmt.Errorf("read bridge body: %w", err)
	}
	if resp.StatusCode >= 400 {
		return fmt.Errorf("bridge %d: %s", resp.StatusCode, strings.TrimSpace(string(body)))
	}
	if err := json.Unmarshal(body, out); err != nil {
		return fmt.Errorf("decode bridge JSON: %w (body: %s)", err, strings.TrimSpace(string(body)))
	}
	return nil
}

func (c *Client) GetBootedServers(secret, host string, port int) ([]int, error) {
	var result struct {
		Servers []int `json:"servers"`
	}
	if err := c.doRequest(fmt.Sprintf("%s/ice/booted?secret=%s&host=%s&port=%d", c.url, secret, host, port), &result); err != nil {
		return nil, err
	}
	return result.Servers, nil
}

func (c *Client) GetTree(secret, host string, port, serverID int) (*Tree, error) {
	var result struct {
		Tree Tree `json:"tree"`
	}
	if err := c.doRequest(fmt.Sprintf("%s/ice/tree?secret=%s&host=%s&port=%d&server_id=%d", c.url, secret, host, port, serverID), &result); err != nil {
		return nil, err
	}
	return &result.Tree, nil
}

func (c *Client) GetUsers(secret, host string, port, serverID int) ([]User, error) {
	var result struct {
		Users []User `json:"users"`
	}
	if err := c.doRequest(fmt.Sprintf("%s/ice/users?secret=%s&host=%s&port=%d&server_id=%d", c.url, secret, host, port, serverID), &result); err != nil {
		return nil, err
	}
	return result.Users, nil
}

func (c *Client) GetChannels(secret, host string, port, serverID int) ([]Channel, error) {
	var result struct {
		Channels []Channel `json:"channels"`
	}
	if err := c.doRequest(fmt.Sprintf("%s/ice/channels?secret=%s&host=%s&port=%d&server_id=%d", c.url, secret, host, port, serverID), &result); err != nil {
		return nil, err
	}
	return result.Channels, nil
}

func (c *Client) GetServerName(secret, host string, port, serverID int) (string, error) {
	var result struct {
		Name string `json:"name"`
	}
	if err := c.doRequest(fmt.Sprintf("%s/ice/server_name?secret=%s&host=%s&port=%d&server_id=%d", c.url, secret, host, port, serverID), &result); err != nil {
		return "", err
	}
	return result.Name, nil
}

func (c *Client) ResolveServerID(secret, host string, port, serverID int) int {
	if serverID > 0 {
		return serverID
	}
	servers, err := c.GetBootedServers(secret, host, port)
	if err != nil || len(servers) == 0 {
		return 1
	}
	return servers[0]
}

func (c *Client) Health() error {
	resp, err := c.client.Get(c.url + "/health")
	if err != nil {
		return err
	}
	defer resp.Body.Close()
	io.Copy(io.Discard, resp.Body)
	return nil
}

func (c *Client) GetServerStats(secret, host string, port, serverID int) (*ServerStats, error) {
	var result struct {
		Stats ServerStats `json:"stats"`
	}
	if err := c.doRequest(fmt.Sprintf("%s/ice/stats?secret=%s&host=%s&port=%d&server_id=%d", c.url, secret, host, port, serverID), &result); err != nil {
		return nil, err
	}
	return &result.Stats, nil
}

func (c *Client) GetLog(secret, host string, port, serverID, first, last int) ([]LogEntry, error) {
	var result struct {
		Entries []LogEntry `json:"entries"`
	}
	if err := c.doRequest(fmt.Sprintf("%s/ice/log?secret=%s&host=%s&port=%d&server_id=%d&first=%d&last=%d", c.url, secret, host, port, serverID, first, last), &result); err != nil {
		return nil, err
	}
	return result.Entries, nil
}

func (c *Client) GetBans(secret, host string, port, serverID int) ([]Ban, error) {
	var result struct {
		Bans []Ban `json:"bans"`
	}
	if err := c.doRequest(fmt.Sprintf("%s/ice/bans?secret=%s&host=%s&port=%d&server_id=%d", c.url, secret, host, port, serverID), &result); err != nil {
		return nil, err
	}
	return result.Bans, nil
}

func (c *Client) GetListening(secret, host string, port, serverID int) ([]ListeningInfo, error) {
	var result struct {
		Listening []ListeningInfo `json:"listening"`
	}
	if err := c.doRequest(fmt.Sprintf("%s/ice/listening?secret=%s&host=%s&port=%d&server_id=%d", c.url, secret, host, port, serverID), &result); err != nil {
		return nil, err
	}
	return result.Listening, nil
}

func (c *Client) KickUser(secret, host string, port, serverID, session int, reason string) error {
	var result struct {
		Status string `json:"status"`
	}
	return c.doPost(fmt.Sprintf("%s/ice/kick?secret=%s&host=%s&port=%d&server_id=%d", c.url, secret, host, port, serverID),
		map[string]any{"session": session, "reason": reason}, &result)
}

func (c *Client) SetState(secret, host string, port, serverID, session, channel int, mute, deaf, suppress, priority bool) error {
	var result struct {
		Status string `json:"status"`
	}
	return c.doPost(fmt.Sprintf("%s/ice/set_state?secret=%s&host=%s&port=%d&server_id=%d", c.url, secret, host, port, serverID),
		map[string]any{
			"session":  session,
			"channel":  channel,
			"mute":     mute,
			"deaf":     deaf,
			"suppress": suppress,
			"priority": priority,
		}, &result)
}

func (c *Client) AddChannel(secret, host string, port, serverID int, name string, parent int) (int, error) {
	var result struct {
		ID int `json:"id"`
	}
	if err := c.doPost(fmt.Sprintf("%s/ice/add_channel?secret=%s&host=%s&port=%d&server_id=%d", c.url, secret, host, port, serverID),
		map[string]any{"name": name, "parent": parent}, &result); err != nil {
		return 0, err
	}
	return result.ID, nil
}

func (c *Client) RemoveChannel(secret, host string, port, serverID, id int) error {
	var result struct {
		Status string `json:"status"`
	}
	return c.doPost(fmt.Sprintf("%s/ice/remove_channel?secret=%s&host=%s&port=%d&server_id=%d", c.url, secret, host, port, serverID),
		map[string]any{"id": id}, &result)
}

func (c *Client) SetChannelState(secret, host string, port, serverID int, ch Channel) error {
	var result struct {
		Status string `json:"status"`
	}
	return c.doPost(fmt.Sprintf("%s/ice/set_channel_state?secret=%s&host=%s&port=%d&server_id=%d", c.url, secret, host, port, serverID),
		ch, &result)
}

func (c *Client) SendMessage(secret, host string, port, serverID, session int, text string) error {
	var result struct {
		Status string `json:"status"`
	}
	return c.doPost(fmt.Sprintf("%s/ice/send_message?secret=%s&host=%s&port=%d&server_id=%d", c.url, secret, host, port, serverID),
		map[string]any{"session": session, "text": text}, &result)
}

func (c *Client) SendMessageChannel(secret, host string, port, serverID, channelID int, tree bool, text string) error {
	var result struct {
		Status string `json:"status"`
	}
	return c.doPost(fmt.Sprintf("%s/ice/send_message_channel?secret=%s&host=%s&port=%d&server_id=%d", c.url, secret, host, port, serverID),
		map[string]any{"channel_id": channelID, "tree": tree, "text": text}, &result)
}

func (c *Client) AddBan(secret, host string, port, serverID int, address string, bits int, name, reason string, duration int) error {
	var result struct {
		Status string `json:"status"`
	}
	return c.doPost(fmt.Sprintf("%s/ice/add_ban?secret=%s&host=%s&port=%d&server_id=%d", c.url, secret, host, port, serverID),
		map[string]any{
			"address":  address,
			"bits":     bits,
			"name":     name,
			"reason":   reason,
			"duration": duration,
		}, &result)
}

func (c *Client) RemoveBan(secret, host string, port, serverID int, address string, bits int) error {
	var result struct {
		Status string `json:"status"`
	}
	return c.doPost(fmt.Sprintf("%s/ice/remove_ban?secret=%s&host=%s&port=%d&server_id=%d", c.url, secret, host, port, serverID),
		map[string]any{"address": address, "bits": bits}, &result)
}

func (c *Client) GetACL(secret, host string, port, serverID, channelID int) (*ACLResult, error) {
	var result ACLResult
	if err := c.doRequest(fmt.Sprintf("%s/ice/acl?secret=%s&host=%s&port=%d&server_id=%d&channel_id=%d", c.url, secret, host, port, serverID, channelID), &result); err != nil {
		return nil, err
	}
	return &result, nil
}

func (c *Client) GetEffectivePermissions(secret, host string, port, serverID, session, channelID int) ([]string, error) {
	var result struct {
		Permissions []string `json:"permissions"`
	}
	if err := c.doRequest(fmt.Sprintf("%s/ice/effective_permissions?secret=%s&host=%s&port=%d&server_id=%d&session=%d&channel_id=%d", c.url, secret, host, port, serverID, session, channelID), &result); err != nil {
		return nil, err
	}
	return result.Permissions, nil
}

func (c *Client) GetRegisteredUsers(secret, host string, port, serverID int, filter string) ([]RegisteredUser, error) {
	url := fmt.Sprintf("%s/ice/registered_users?secret=%s&host=%s&port=%d&server_id=%d", c.url, secret, host, port, serverID)
	if filter != "" {
		url += fmt.Sprintf("&filter=%s", filter)
	}
	var result struct {
		Users []RegisteredUser `json:"users"`
	}
	if err := c.doRequest(url, &result); err != nil {
		return nil, err
	}
	return result.Users, nil
}

func (c *Client) GetRegistration(secret, host string, port, serverID, userID int) (RegistrationInfo, error) {
	var result RegistrationInfo
	if err := c.doRequest(fmt.Sprintf("%s/ice/registration?secret=%s&host=%s&port=%d&server_id=%d&user_id=%d", c.url, secret, host, port, serverID, userID), &result); err != nil {
		return nil, err
	}
	return result, nil
}

func (c *Client) GetAllConf(secret, host string, port, serverID int) (map[string]string, error) {
	var result map[string]string
	if err := c.doRequest(fmt.Sprintf("%s/ice/all_conf?secret=%s&host=%s&port=%d&server_id=%d", c.url, secret, host, port, serverID), &result); err != nil {
		return nil, err
	}
	return result, nil
}

func (c *Client) SetConf(secret, host string, port, serverID int, key, value string) error {
	var result struct {
		Status string `json:"status"`
	}
	return c.doPost(fmt.Sprintf("%s/ice/set_conf?secret=%s&host=%s&port=%d&server_id=%d", c.url, secret, host, port, serverID),
		map[string]any{"key": key, "value": value}, &result)
}

func (c *Client) GetCertificateList(secret, host string, port, serverID, session int) ([]string, error) {
	var result struct {
		Certificates []string `json:"certificates"`
	}
	if err := c.doRequest(fmt.Sprintf("%s/ice/certificate_list?secret=%s&host=%s&port=%d&server_id=%d&session=%d", c.url, secret, host, port, serverID, session), &result); err != nil {
		return nil, err
	}
	return result.Certificates, nil
}
