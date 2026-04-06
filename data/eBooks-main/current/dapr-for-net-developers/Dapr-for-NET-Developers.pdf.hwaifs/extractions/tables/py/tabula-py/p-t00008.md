|    | version: '3.4                        |
|---:|:-------------------------------------|
|  0 | services:                            |
|  1 | myfrontend:                          |
|  2 | image: ${DOCKER_REGISTRY-}myfrontend |
|  3 | build:                               |
|  4 | context: .                           |
|  5 | dockerfile: MyFrontEnd/Dockerfile    |