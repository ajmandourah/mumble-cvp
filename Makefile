.PHONY: all build css run test vet clean

all: css build

css:
	npm run build:css

build: css
	go build -trimpath -ldflags="-s -w" -o mumble-cvp ./cmd/mumble-cvp/

run: build
	./mumble-cvp

test:
	go test ./internal/... -v -race

vet:
	go vet ./...

clean:
	rm -f mumble-cvp
	rm -rf node_modules
