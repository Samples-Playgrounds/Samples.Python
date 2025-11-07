|    | version: '3.4'                                                     |
|---:|:-------------------------------------------------------------------|
|  0 |                                                                    |
|  1 | services:                                                          |
|  2 |                                                                    |
|  3 | webmvc:                                                            |
|  4 | image: eshop/web                                                   |
|  5 | environment:                                                       |
|  6 | - CatalogUrl=http://catalog-api                                    |
|  7 | - OrderingUrl=http://ordering-api                                  |
|  8 | ports:                                                             |
|  9 | - "80:80"                                                          |
| 10 | depends_on:                                                        |
| 11 | - catalog-api                                                      |
| 12 | - ordering-api                                                     |
| 13 |                                                                    |
| 14 | catalog-api:                                                       |
| 15 | image: eshop/catalog-api                                           |
| 16 | environment:                                                       |
| 17 | - ConnectionString=Server=sqldata;Port=1433;Database=CatalogDB;... |
| 18 | ports:                                                             |
| 19 | - "81:80"                                                          |
| 20 | depends_on:                                                        |
| 21 | - sqldata                                                          |
| 22 |                                                                    |
| 23 | ordering-api:                                                      |
| 24 | image: eshop/ordering-api                                          |