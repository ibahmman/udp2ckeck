#!/usr/bin/env python3
import socket, argparse

parser = argparse.ArgumentParser(description="UDP Echo Server")
parser.add_argument("--host", default="0.0.0.0", help="Host to bind")
parser.add_argument("--port", type=int, default=9999, help="Port to listen on")
args = parser.parse_args()

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((args.host, args.port))
print(f"UDP server listening on {args.host}:{args.port}")

try:
    while True:
        data, addr = sock.recvfrom(1024)
        print(f"Received from {addr}: {data.decode(errors='ignore')}")
        sock.sendto(data, addr)
except KeyboardInterrupt:
    print("\nServer stopped.")
