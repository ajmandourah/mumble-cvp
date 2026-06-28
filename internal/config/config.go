package config

import (
	"os"

	"gopkg.in/yaml.v3"
)

type Config struct {
	Mumble MumbleConfig `yaml:"mumble"`
	HTTP   HTTPConfig   `yaml:"http"`
	Log    LogConfig    `yaml:"log"`
}

type MumbleConfig struct {
	Host     string `yaml:"host"`
	Port     int    `yaml:"port"`
	Secret   string `yaml:"secret"`
	ServerID int    `yaml:"server_id"`
}

type HTTPConfig struct {
	Host string `yaml:"host"`
	Port int    `yaml:"port"`
}

type LogConfig struct {
	Level  string `yaml:"level"`
	Format string `yaml:"format"`
}

func Load(path string) (*Config, error) {
	cfg := DefaultConfig()

	if path == "" {
		path = os.Getenv("MUMBLE_CVP_CONFIG")
	}
	if path == "" {
		path = "configs/config.yaml"
	}

	data, err := os.ReadFile(path)
	if err != nil {
		if os.IsNotExist(err) {
			return cfg, nil
		}
		return nil, err
	}

	if err := yaml.Unmarshal(data, cfg); err != nil {
		return nil, err
	}

	return cfg, nil
}

func DefaultConfig() *Config {
	return &Config{
		Mumble: MumbleConfig{
			Host:     "127.0.0.1",
			Port:     6502,
			Secret:   "",
			ServerID: 0,
		},
		HTTP: HTTPConfig{
			Host: "0.0.0.0",
			Port: 4000,
		},
		Log: LogConfig{
			Level:  "info",
			Format: "json",
		},
	}
}
