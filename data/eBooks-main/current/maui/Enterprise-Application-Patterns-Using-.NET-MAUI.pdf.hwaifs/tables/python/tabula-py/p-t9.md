|    | public static class MauiProgram       |
|---:|:--------------------------------------|
|  0 | {                                     |
|  1 | public static MauiApp CreateMauiApp() |
|  2 | => MauiApp.CreateBuilder()            |
|  3 | .UseMauiApp<App>()                    |
|  4 | // Omitted for brevity                |
|  5 | .RegisterAppServices()                |
|  6 | .RegisterViewModels()                 |
|  7 | .RegisterViews()                      |
|  8 | .Build();                             |
|  9 | }                                     |