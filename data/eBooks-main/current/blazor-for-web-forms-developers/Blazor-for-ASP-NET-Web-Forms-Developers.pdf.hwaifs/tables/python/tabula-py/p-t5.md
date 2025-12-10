|    | using BlazorApp1;                                                   |
|---:|:--------------------------------------------------------------------|
|  0 | using Microsoft.AspNetCore.Components.Web;                          |
|  1 | using Microsoft.AspNetCore.Components.WebAssembly.Hosting;          |
|  2 |                                                                     |
|  3 | var builder = WebAssemblyHostBuilder.CreateDefault(args);           |
|  4 | builder.RootComponents.Add<App>("#app");                            |
|  5 | builder.RootComponents.Add<HeadOutlet>("head::after");              |
|  6 |                                                                     |
|  7 | builder.Services.AddScoped(sp => new HttpClient { BaseAddress = new |
|  8 | Uri(builder.HostEnvironment.BaseAddress) });                        |
|  9 |                                                                     |
| 10 | await builder.Build().RunAsync();                                   |