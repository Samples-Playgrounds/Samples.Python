|    | Image                                | Comments                                                |
|---:|:-------------------------------------|:--------------------------------------------------------|
|  0 | mcr.microsoft.com/dotnet/runtime:7.0 | .NET 7 multi-architecture: Supports Linux and Windows   |
|    |                                      | Nano Server depending on the Docker host.               |
|  1 | mcr.microsoft.com/dotnet/aspnet:7.0  | ASP.NET Core 7.0 multi-architecture: Supports Linux and |
|    |                                      | Windows Nano Server depending on the Docker host.       |
|    |                                      | The aspnetcore image has a few optimizations for        |
|    |                                      | ASP.NET Core.                                           |
|  2 | mcr.microsoft.com/dotnet/aspnet:7.0- | .NET 7 runtime-only on Linux Debian distro              |
|    | bullseye-slim                        |                                                         |
|  3 | mcr.microsoft.com/dotnet/aspnet:7.0- | .NET 7 runtime-only on Windows Nano Server (Windows     |
|    | nanoserver-1809                      | Server version 1809)                                    |