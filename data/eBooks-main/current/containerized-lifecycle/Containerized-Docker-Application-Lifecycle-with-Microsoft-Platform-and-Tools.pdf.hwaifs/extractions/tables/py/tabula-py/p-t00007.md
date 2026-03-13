|    | Note                                                                                                   |
|---:|:-------------------------------------------------------------------------------------------------------|
|  0 | When taking into account the “outer-loop DevOps workflow”, the images will be created by an            |
|  1 | automated build process whenever you push your source code to a Git repository (Continuous             |
|  2 | Integration), so the images will be created in that global environment from your source code.          |
|  3 | But before you consider going to that outer-loop route, you need to ensure that the Docker             |
|  4 | application is actually working properly so that they don’t push code that might not work properly to  |
|  5 | the source control system (Git, etc.).                                                                 |
|  6 | Therefore, each developer first needs to do the entire inner-loop process to test locally and continue |
|  7 | developing until they want to push a complete feature or change to the source control system.          |