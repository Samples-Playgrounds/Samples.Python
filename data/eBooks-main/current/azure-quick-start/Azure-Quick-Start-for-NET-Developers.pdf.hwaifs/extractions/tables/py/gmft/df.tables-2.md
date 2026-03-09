|    |                                                                                          |
|---:|:-----------------------------------------------------------------------------------------|
|  0 | image file is uploaded to Azure Storage. You then take that image, rename it, and        |
|  1 | output it to another Azure Storage account.                                              |
|  2 | This is very easy to do. You just write the code to rename the image. Azure Functions    |
|  3 | takes care of getting the input image when the function is triggered. And it takes care  |
|  4 | writing the image to the other storage account. It takes care of all the plumbing, and   |
|  5 | you just write the code.                                                                 |
|  6 | Azure Functions even handles scaling for you. So it doesn’t matter if there are          |
|  7 | images that trigger the function at the same time. Azure Functions transparently spins   |
|  8 | more functions to deal with it and they go away when the code is done executing.         |
|  9 | Because of this, you only pay for the code that you execute, not for a service that runs |
| 10 | the time, waiting to be triggered.                                                       |
| 11 | Azure Functions are great for executing small pieces of code that perform one or two     |
| 12 | steps on an input and an output. If you want to perform more steps of a larger process,  |
| 13 | you can use Durable Functions.                                                           |