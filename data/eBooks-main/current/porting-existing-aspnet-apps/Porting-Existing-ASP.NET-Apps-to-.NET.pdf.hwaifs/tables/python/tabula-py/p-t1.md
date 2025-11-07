|    | var builder = WebApplication.CreateBuilder(args);                                |
|---:|:---------------------------------------------------------------------------------|
|  0 | nan                                                                              |
|  1 | // Add services to the container.                                                |
|  2 | builder.Services.AddRazorPages();                                                |
|  3 | nan                                                                              |
|  4 | var app = builder.Build();                                                       |
|  5 | nan                                                                              |
|  6 | // Configure the HTTP request pipeline.                                          |
|  7 | if (!app.Environment.IsDevelopment())                                            |
|  8 | {                                                                                |
|  9 | app.UseExceptionHandler("/Error");                                               |
| 10 | // The default HSTS value is 30 days. You may want to change this for production |
| 11 | scenarios, see https://aka.ms/aspnetcore-hsts.                                   |
| 12 | app.UseHsts();                                                                   |
| 13 | }                                                                                |
| 14 | nan                                                                              |
| 15 | app.UseHttpsRedirection();                                                       |
| 16 | app.UseStaticFiles();                                                            |
| 17 | nan                                                                              |
| 18 | app.UseRouting();                                                                |
| 19 | nan                                                                              |
| 20 | app.UseAuthorization();                                                          |
| 21 | nan                                                                              |
| 22 | app.MapRazorPages();                                                             |
| 23 | nan                                                                              |
| 24 | app.Run();                                                                       |