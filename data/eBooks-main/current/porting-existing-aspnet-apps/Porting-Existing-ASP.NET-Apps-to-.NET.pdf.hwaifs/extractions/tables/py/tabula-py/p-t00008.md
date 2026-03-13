|    | public void Configure(IApplicationBuilder app, IHostingEnvironment env)   |
|---:|:--------------------------------------------------------------------------|
|  0 | {                                                                         |
|  1 | if (env.IsDevelopment())                                                  |
|  2 | {                                                                         |
|  3 | app.UseDeveloperExceptionPage();                                          |
|  4 | }                                                                         |
|  5 |                                                                           |
|  6 | app.UseStaticFiles();                                                     |
|  7 |                                                                           |
|  8 | // ...                                                                    |
|  9 | }                                                                         |