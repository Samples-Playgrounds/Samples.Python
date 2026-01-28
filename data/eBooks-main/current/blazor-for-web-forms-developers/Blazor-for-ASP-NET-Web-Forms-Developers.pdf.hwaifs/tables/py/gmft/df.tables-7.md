|    | Directive   | Description                                          | Example                       | Web Forms equivalent                       |
|---:|:------------|:-----------------------------------------------------|:------------------------------|:-------------------------------------------|
|  0 | @layout     | Specifies a layout component for the component       | @layout MainLayout            | <%@ Page MasterPageFile="~/Site.Master" %> |
|  1 | @namespace  | Sets the namespace for the component                 | @namespa ce MyNamesp ace      | None                                       |
|  2 | @page       | Specifies the route for the component                | @page "/product/{i d}"        | <%@ Page %>                                |
|  3 | @typeparam  | Specifies a generic type parameter for the component | @typepara m TItem             | Use code-behind                            |
|  4 | @using      | Specifies a namespace to bring into scope            | @using MyCompon entNamesp ace | Add namespace in web.config                |