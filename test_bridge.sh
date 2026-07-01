#!/bin/bash
# Diagnostic script for mumble-cvp bridge
# Tests each layer: Python bridge -> Go API -> Frontend

set -e

PORT=${1:-4001}
BASE="http://127.0.0.1:$PORT"

# Read config
CONFIG=""
for p in config.yaml configs/config.yaml; do
	if [ -f "$p" ]; then
		CONFIG="$p"
		break
	fi
done

if [ -z "$CONFIG" ]; then
	echo "ERROR: No config.yaml found"
	exit 1
fi

SECRET=$(grep 'secret:' "$CONFIG" | head -1 | awk '{print $2}' | tr -d '"' | tr -d "'")
HOST=$(grep 'host:' "$CONFIG" | head -1 | awk '{print $2}' | tr -d '"' | tr -d "'")
MPORT=$(grep 'port:' "$CONFIG" | head -1 | awk '{print $2}')

echo "=== mumble-cvp bridge diagnostic ==="
echo "Config: host=$HOST mumble_port=$MPORT secret=${SECRET:-(empty)}"
echo "Bridge: $BASE"
echo

# 1. Health
echo "--- 1. Python bridge health ---"
curl -sf "$BASE/health" | python3 -m json.tool
echo

# 2. Booted servers
echo "--- 2. Booted servers ---"
curl -sf "$BASE/ice/booted?secret=$SECRET&host=$HOST&port=$MPORT" | python3 -m json.tool
echo

# 3. Users
echo "--- 3. Users ---"
curl -sf "$BASE/ice/users?secret=$SECRET&host=$HOST&port=$MPORT&server_id=1" | python3 -m json.tool
echo

# 4. Channels
echo "--- 4. Channels ---"
curl -sf "$BASE/ice/channels?secret=$SECRET&host=$HOST&port=$MPORT&server_id=1" | python3 -m json.tool
echo

# 5. Stats
echo "--- 5. Stats ---"
curl -sf "$BASE/ice/stats?secret=$SECRET&host=$HOST&port=$MPORT&server_id=1" | python3 -m json.tool
echo

# 6. Bans
echo "--- 6. Bans ---"
curl -sf "$BASE/ice/bans?secret=$SECRET&host=$HOST&port=$MPORT&server_id=1" | python3 -m json.tool
echo

# 7. Server name
echo "--- 7. Server name ---"
curl -sf "$BASE/ice/server_name?secret=$SECRET&host=$HOST&port=$MPORT&server_id=1" | python3 -m json.tool
echo

# 8. Log
echo "--- 8. Log ---"
curl -sf "$BASE/ice/log?secret=$SECRET&host=$HOST&port=$MPORT&server_id=1&first=0&last=5" | python3 -m json.tool
echo

echo "=== All tests passed ==="
