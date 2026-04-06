|    | [Route("[controller]")]                      |
|---:|:---------------------------------------------|
|  0 | public class ProductsController : Controller |
|  1 | {                                            |
|  2 | [Route("")] // Matches 'Products'            |
|  3 | [Route("Index")] // Matches 'Products/Index' |
|  4 | public IActionResult Index() {}              |
|  5 | }                                            |