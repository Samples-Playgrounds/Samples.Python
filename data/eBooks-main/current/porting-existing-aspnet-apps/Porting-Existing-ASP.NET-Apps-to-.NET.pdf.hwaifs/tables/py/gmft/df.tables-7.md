|    |            |                                                                                                                    |
|---:|:-----------|:-------------------------------------------------------------------------------------------------------------------|
|  0 | •          | Include is not a valid named attribute argument (2)                                                                |
|  1 | •          | HttpStatusCodeResult not found (3)                                                                                 |
|  2 | •          | HttpNotFound does not exist (3)                                                                                    |
|  3 | •          | SelectList not found (8)                                                                                           |
|  4 | Once       | more, let’s review these errors one by one. First, SelectList can be fixed by adding using                         |
|  5 | nan        | Microsoft.AspNetCore.Mvc.Rendering;, which eliminates half of the errors.                                          |
|  6 | All        | references to return HttpNotFound(); should be replaced with return NotFound();.                                   |
|  7 | All with   | references to return new HttpStatusCodeResult(HttpStatusCode.BadRequest); should be replaced return BadRequest();. |
|  8 | That this: | just leaves the use of Include with a [Bind] attribute on a couple of action methods that look like                |