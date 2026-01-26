|    |       |                                                   |                                                           |
|---:|:------|:--------------------------------------------------|:----------------------------------------------------------|
|  0 | @code | {                                                 | nan                                                       |
|  1 | {     | protected override async Task                     | OnInitializedAsync()                                      |
|  2 | nan   | var client =                                      | factory.CreateClient("github");                           |
|  3 | nan   | var response = await response.EnsureStatusCode(); | client.GetAsync("repos/dotnet/docs/issues");              |
|  4 | nan   | nan                                               | var content = await response.Content.ReadAsStringAsync(); |