|    | FROM mcr.microsoft.com/dotnet/aspnet:7.0 AS base                 |
|---:|:-----------------------------------------------------------------|
|  0 | WORKDIR /app                                                     |
|  1 | EXPOSE 80                                                        |
|  2 | EXPOSE 44                                                        |
|  3 | FROM mcr.microsoft.com/dotnet/sdk:7.0 AS build                   |
|  4 | WORKDIR /src                                                     |
|  5 | COPY ["MyFrontEnd/MyFrontEnd.csproj", "MyFrontEnd/"]             |
|  6 | RUN dotnet restore "MyFrontEnd/MyFrontEnd.csproj"                |
|  7 | COPY . .                                                         |
|  8 | WORKDIR "/src/MyFrontEnd"                                        |
|  9 | RUN dotnet build "MyFrontEnd.csproj" -c Release -o /app/buil     |
| 10 | FROM build AS publish                                            |
| 11 | RUN dotnet publish "MyFrontEnd.csproj" -c Release -o /app/publis |
| 12 | FROM base AS final                                               |
| 13 | WORKDIR /app                                                     |
| 14 | COPY --from=publish /app/publish .                               |
| 15 | ENTRYPOINT ["dotnet", "MyFrontEnd.dll"]                          |