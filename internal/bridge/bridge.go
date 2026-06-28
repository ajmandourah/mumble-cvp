package bridge

import (
	"encoding/json"
	"fmt"
	"io"
	"net/http"
	"os/exec"
	"path/filepath"
	"regexp"
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
	Name            string `json:"name"`
	Session         int    `json:"session"`
	ChannelID       int    `json:"channel_id"`
	Comment         string `json:"comment"`
	Registered      bool   `json:"registered"`
	Mute            bool   `json:"mute"`
	Deaf            bool   `json:"deaf"`
	SelfMute        bool   `json:"self_mute"`
	SelfDeaf        bool   `json:"self_deaf"`
	Suppress        bool   `json:"suppress"`
	PrioritySpeaker bool   `json:"priority_speaker"`
	Recording       bool   `json:"recording"`
	Flags           int    `json:"flags"`
	OnLine          bool   `json:"on_line"`
	LastSeen        int64  `json:"last_seen"`
	Version         string `json:"version"`
	Platform        string `json:"platform"`
	IP              string `json:"ip"`
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
			Timeout: 10 * time.Second,
		},
		cmd: cmd,
	}

	// Wait for bridge to be ready
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

func (c *Client) GetBootedServers(secret, host string, port int) ([]int, error) {
	resp, err := c.client.Get(fmt.Sprintf("%s/ice/booted?secret=%s&host=%s&port=%d", c.url, secret, host, port))
	if err != nil {
		return nil, err
	}
	defer resp.Body.Close()

	var result struct {
		Servers []int `json:"servers"`
	}
	if err := json.NewDecoder(resp.Body).Decode(&result); err != nil {
		return nil, err
	}
	return result.Servers, nil
}

func (c *Client) GetTree(secret, host string, port, serverID int) (*Tree, error) {
	resp, err := c.client.Get(fmt.Sprintf("%s/ice/tree?secret=%s&host=%s&port=%d&server_id=%d", c.url, secret, host, port, serverID))
	if err != nil {
		return nil, err
	}
	defer resp.Body.Close()

	var result struct {
		Tree Tree `json:"tree"`
	}
	if err := json.NewDecoder(resp.Body).Decode(&result); err != nil {
		return nil, err
	}
	return &result.Tree, nil
}

func (c *Client) GetUsers(secret, host string, port, serverID int) ([]User, error) {
	resp, err := c.client.Get(fmt.Sprintf("%s/ice/users?secret=%s&host=%s&port=%d&server_id=%d", c.url, secret, host, port, serverID))
	if err != nil {
		return nil, err
	}
	defer resp.Body.Close()

	var result struct {
		Users []User `json:"users"`
	}
	if err := json.NewDecoder(resp.Body).Decode(&result); err != nil {
		return nil, err
	}
	return result.Users, nil
}

func (c *Client) GetChannels(secret, host string, port, serverID int) ([]Channel, error) {
	resp, err := c.client.Get(fmt.Sprintf("%s/ice/channels?secret=%s&host=%s&port=%d&server_id=%d", c.url, secret, host, port, serverID))
	if err != nil {
		return nil, err
	}
	defer resp.Body.Close()

	var result struct {
		Channels *[]Channel `json:"channels"`
	}
	if err := json.NewDecoder(resp.Body).Decode(&result); err != nil {
		return nil, err
	}
	if result.Channels == nil {
		return []Channel{}, nil
	}
	return *result.Channels, nil
}

func (c *Client) GetServerName(secret, host string, port, serverID int) (string, error) {
	resp, err := c.client.Get(fmt.Sprintf("%s/ice/server_name?secret=%s&host=%s&port=%d&server_id=%d", c.url, secret, host, port, serverID))
	if err != nil {
		return "", err
	}
	defer resp.Body.Close()

	var result struct {
		Name string `json:"name"`
	}
	if err := json.NewDecoder(resp.Body).Decode(&result); err != nil {
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
