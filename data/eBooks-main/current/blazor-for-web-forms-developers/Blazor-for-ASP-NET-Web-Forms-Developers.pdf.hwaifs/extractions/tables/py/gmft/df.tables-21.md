|    |                                                                                                                                 |                    |
|---:|:--------------------------------------------------------------------------------------------------------------------------------|:-------------------|
|  0 | @inject IAuthorizationService AuthorizationService                                                                              | nan                |
|  1 | <button @onclick="@DoSomething">Do something important</button>                                                                 | nan                |
|  2 | @code {                                                                                                                         | nan                |
|  3 | [CascadingParameter] private Task<AuthenticationState> authenticationStateTask { get; set; } private async Task DoSomething() { | nan                |
|  4 | var user = (await authenticationStateTask).User;                                                                                | nan                |
|  5 | if (user.Identity.IsAuthenticated)                                                                                              | nan                |
|  6 | { // Perform an action only available to authenticated (signed-in) } if (user.IsInRole("admin"))                                | users.             |
|  7 | { // Perform an action only available to users in the 'admin' }                                                                 | role.              |
|  8 | if ((await AuthorizationService.AuthorizeAsync(user, .Succeeded)                                                                | "content-editor")) |
|  9 | { // Perform an action only available to users satisfying the // 'content-editor' policy.                                       | nan                |