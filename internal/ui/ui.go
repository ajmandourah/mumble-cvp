package ui

import (
	"embed"
	"io/fs"
	"net/http"
)

//go:embed assets/*
var assetsFS embed.FS

func RegisterRoutes(mux *http.ServeMux) {
	fsys, err := fs.Sub(assetsFS, "assets")
	if err != nil {
		return
	}
	mux.HandleFunc("GET /", func(w http.ResponseWriter, r *http.Request) {
		http.ServeFileFS(w, r, fsys, "index.html")
	})
	mux.Handle("GET /assets/", http.FileServer(http.FS(fsys)))
}
