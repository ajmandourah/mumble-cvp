.PHONY: build test vet clean

build:
	go build -trimpath -ldflags="-s -w" -o mumble-cvp ./cmd/mumble-cvp/

test:
	go test ./internal/... -v -race

vet:
	go vet ./...

clean:
	rm -f mumble-cvp
