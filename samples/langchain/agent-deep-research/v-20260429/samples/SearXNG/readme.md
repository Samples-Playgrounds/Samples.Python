
```
docker-compose \
    -f docker-compose.yml \
    up
```


open http://127.0.0.1:8080


```shell
docker run \
    --name searxng \
        -d \
        -p 8888:8080 \
            -v "./config/:/etc/searxng/" \
            -v "./data/:/var/cache/searxng/" \
            docker.io/searxng/searxng:latest

```

```shell
open http://127.0.0.1:8888
```

*   https://docs.langchain.com/oss/python/integrations/providers/searx


```shell
docker stop searxng
docker rm searxng

```