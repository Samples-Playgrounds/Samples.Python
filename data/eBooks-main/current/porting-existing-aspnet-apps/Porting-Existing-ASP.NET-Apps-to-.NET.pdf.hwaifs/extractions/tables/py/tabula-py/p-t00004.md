|    | public class MvcApplication : System.Web.HttpApplication          |
|---:|:------------------------------------------------------------------|
|  0 | {                                                                 |
|  1 | public static void RegisterRoutes(RouteCollection routes)         |
|  2 | {                                                                 |
|  3 | routes.IgnoreRoute("{resource}.axd/{*pathInfo}");                 |
|  4 | routes.MapRoute(                                                  |
|  5 | name: "Default",                                                  |
|  6 | url: "{controller}/{action}/{id}",                                |
|  7 | defaults: new { controller = "Home", action = "Index", id = "" }, |
|  8 | constraints: new { id = "\\d+" }                                  |
|  9 | );                                                                |
| 10 | }                                                                 |
| 11 |                                                                   |
| 12 | protected void Application_Start()                                |
| 13 | {                                                                 |