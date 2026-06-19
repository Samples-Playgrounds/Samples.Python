

```shell
mkdir -p ./searxng/core-config/
cd ./searxng/

# Fetch the latest compose template
curl -fsSL \
    -O https://raw.githubusercontent.com/searxng/searxng/master/container/docker-compose.yml \
    -O https://raw.githubusercontent.com/searxng/searxng/master/container/.env.example

cp -i .env.example .env

# nano or your preferred text editor...
nano .env
# Start & stop the services:
docker compose up -d
docker compose down
```

*   https://github.com/YPares/agent-skills/blob/main/searxng-search

```shell
brew install podman
brew install podman-compose
brew install podman-tui
```


```shell
md SearXNG
cd SearXNG

code -n podman-compose.yml
code -n settings.yml
```