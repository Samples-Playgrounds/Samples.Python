|    | 1  FROM mcr.microsoft.com/dotnet/aspnet:7.0 AS base          |
|---:|:-------------------------------------------------------------|
|  0 | 2  WORKDIR /app                                              |
|  1 | 3  EXPOSE 80                                                 |
|  2 | 4                                                            |
|  3 | 5  FROM mcr.microsoft.com/dotnet/sdk:7.0 AS publish          |
|  4 | 6  WORKDIR /src                                              |
|  5 | 7  COPY . .                                                  |
|  6 | 8  RUN dotnet restore /ignoreprojectextensions:.dcproj       |
|  7 | 9  WORKDIR /src/src/Services/Catalog/Catalog.API             |
|  8 | 10  RUN dotnet publish Catalog.API.csproj -c Release -o /app |
|  9 | 11                                                           |
| 10 | 12  FROM base AS final                                       |
| 11 | 13  WORKDIR /app                                             |
| 12 | 14  COPY --from=publish /app .                               |
| 13 | 15  ENTRYPOINT ["dotnet", "Catalog.API.dll"]                 |