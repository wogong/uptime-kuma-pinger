# Uptime Kuma Pinger

A lightweight service that pings an Uptime Kuma server from inside a NAT LAN and reports request times.

## Usage

### Docker Compose (Recommended)

```bash
docker-compose up -d
```

Configure in `docker-compose.yml`:
- `UPTIME_KUMA_URL`: Push URL from Uptime Kuma
- `PING_INTERVAL`: Interval in seconds between pings

### Docker

```bash
docker run -d \
  -e UPTIME_KUMA_URL="https://example.com/api/push/abc123" \
  -e PING_INTERVAL=60 \
  ghcr.io/your-org/uptimekuma-pinger:latest
```

## Environment Variables

- `UPTIME_KUMA_URL`: Uptime Kuma push URL (required)
- `PING_INTERVAL`: Ping interval in seconds (default: 60)
