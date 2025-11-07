|    | public void Configure(IApplicationBuilder app, IHostingEnvironment env)   |
|---:|:--------------------------------------------------------------------------|
|  0 | {                                                                         |
|  1 | if (env.IsDevelopment())                                                  |
|  2 | {                                                                         |
|  3 | app.UseDeveloperExceptionPage();                                          |
|  4 | }                                                                         |
|  5 | nan                                                                       |
|  6 | app.UseStaticFiles();                                                     |
|  7 | nan                                                                       |
|  8 | // ...                                                                    |
|  9 | }                                                                         |