|    | if (item != null)                                                             |
|---:|:------------------------------------------------------------------------------|
|  0 | {                                                                             |
|  1 | var webRoot = Server.MapPath("~/Pics"); // compiler error on this line        |
|  2 | var path = Path.Combine(webRoot, item.PictureFileName);                       |
|  3 | nan                                                                           |
|  4 | string imageFileExtension = Path.GetExtension(item.PictureFileName);          |
|  5 | string mimetype = GetImageMimeTypeFromImageFileExtension(imageFileExtension); |
|  6 | nan                                                                           |
|  7 | var buffer = System.IO.File.ReadAllBytes(path);                               |
|  8 | nan                                                                           |
|  9 | return File(buffer, mimetype);                                                |
| 10 | }                                                                             |