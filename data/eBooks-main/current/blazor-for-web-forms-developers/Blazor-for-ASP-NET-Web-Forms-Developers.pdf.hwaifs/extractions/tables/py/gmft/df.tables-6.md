|    | Directive   | Description                                   | Example                    | Web Forms equivalent                        |
|---:|:------------|:----------------------------------------------|:---------------------------|:--------------------------------------------|
|  0 | @attribute  | Adds a class-level attribute to the component | @attribute [Authorize]     | None                                        |
|  1 | @code       | Adds class members to the component           | @code { ... }              | <script runat="server">...</script>         |
|  2 | @implements | Implements the specified interface            | @impleme nts IDisposable   | Use code-behind                             |
|  3 | @inherits   | Inherits from the specified base class        | @inherits MyCompon entBase | <%@ Control Inherits="MyUserControlBase" %> |
|  4 | @inject     | Injects a service into the component          | @inject IJSRuntime JS      | None                                        |