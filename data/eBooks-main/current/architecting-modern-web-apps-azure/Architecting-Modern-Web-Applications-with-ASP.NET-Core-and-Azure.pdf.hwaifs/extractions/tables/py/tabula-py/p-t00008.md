|    | [Route("Home")]                                                    |
|---:|:-------------------------------------------------------------------|
|  0 | public class HomeController : Controller                           |
|  1 | {                                                                  |
|  2 | [Route("")] // Combines to define the route template "Home"        |
|  3 | [Route("Index")] // Combines to define route template "Home/Index" |
|  4 | [Route("/")] // Does not combine, defines the route template ""    |
|  5 | public IActionResult Index() {}                                    |
|  6 | }                                                                  |