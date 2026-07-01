package main

import (
	"context"
	"fmt"
	"net/http"
	"os"
	"os/signal"
	"path/filepath"
	"syscall"
	"time"

	"github.com/charmbracelet/log"

	"github.com/ladis/mumble-cvp/internal/bridge"
	"github.com/ladis/mumble-cvp/internal/config"
	httppkg "github.com/ladis/mumble-cvp/internal/http"
	"github.com/ladis/mumble-cvp/internal/ui"
)

func main() {
	cfg, err := config.Load("")
	if err != nil {
		log.Fatalf("load config: %v", err)
	}

	level, _ := log.ParseLevel(cfg.Log.Level)
	log.SetLevel(level)
	log.SetReportTimestamp(true)

	log.Info("starting mumble-cvp", "mumble_host", cfg.Mumble.Host, "mumble_port", cfg.Mumble.Port)

	bridgeDir := filepath.Join(filepath.Dir(os.Args[0]), "bridge")
	bridgePort := 4001 + cfg.HTTP.Port
	br, err := bridge.New(bridgeDir, bridgePort)
	if err != nil {
		log.Fatalf("start bridge: %v", err)
	}
	defer br.Close()

	log.Info("bridge started", "port", bridgePort)

	mux := http.NewServeMux()
	srv := httppkg.New(br, cfg.Mumble, cfg.HTTP)
	srv.RegisterRoutes(mux)
	ui.RegisterRoutes(mux)

	httpSrv := &http.Server{
		Addr:    fmt.Sprintf("%s:%d", cfg.HTTP.Host, cfg.HTTP.Port),
		Handler: mux,
	}

	go func() {
		log.Info("http server listening", "addr", httpSrv.Addr)
		if err := httpSrv.ListenAndServe(); err != nil && err != http.ErrServerClosed {
			log.Fatalf("http server: %v", err)
		}
	}()

	quit := make(chan os.Signal, 1)
	signal.Notify(quit, syscall.SIGINT, syscall.SIGTERM)
	<-quit

	log.Info("shutting down...")
	ctx, cancel := context.WithTimeout(context.Background(), 5*time.Second)
	defer cancel()
	httpSrv.Shutdown(ctx)
	log.Info("server stopped")
}
