|    | FROM mcr.microsoft.com/dotnet/sdk:8.0 AS build   |
|---:|:-------------------------------------------------|
|  0 | WORKDIR /app                                     |
|  1 |                                                  |
|  2 | COPY *.sln .                                     |
|  3 | COPY . .                                         |
|  4 | WORKDIR /app/src/Web                             |
|  5 | RUN dotnet restore                               |