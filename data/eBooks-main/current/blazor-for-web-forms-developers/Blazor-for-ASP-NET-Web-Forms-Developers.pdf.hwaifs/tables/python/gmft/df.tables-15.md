|    |       |                                                   |                                                           |
|---:|:------|:--------------------------------------------------|:----------------------------------------------------------|
|  0 | @code | {                                                 |                                                           |
|  1 | {     | protected override async Task                     | OnInitializedAsync()                                      |
|  2 |       | var client =                                      | factory.CreateClient("github");                           |
|  3 |       | var response = await response.EnsureStatusCode(); | client.GetAsync("repos/dotnet/docs/issues");              |
|  4 |       |                                                   | var content = await response.Content.ReadAsStringAsync(); |