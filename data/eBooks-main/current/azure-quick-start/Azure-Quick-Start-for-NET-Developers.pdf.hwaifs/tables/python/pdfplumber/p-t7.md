|    | 0                | 1             | 2   | 3   | 4           | 5         | 6          | 7        | 8             | 9         |
|---:|:-----------------|:--------------|:----|:----|:------------|:----------|:-----------|:---------|:--------------|:----------|
|  0 |                  |               |     |     |             |           |            |          |               |           |
|  1 | App Service      |               |     |     | App Service | Azure     | Logic Apps | Virtual  | Azure         | Container |
|    | Web Apps         |               |     |     | Mobile      | Functions |            | Machines | Kubernetes    | Instances |
|    |                  |               |     |     | Apps        |           |            |          | Service (AKS) |           |
|  2 |                  |               |     |     |             |           |            | *        |               |           |
|  3 | Monolithic       |               |     |     |             |           |            |          |               |           |
|    | and N-Tier       |               |     |     |             |           |            |          |               |           |
|    | applications     |               |     |     |             |           |            |          |               |           |
|  4 |                  |               |     |     |             |           |            | *        |               |           |
|  5 | Mobile app       |               |     |     |             |           |            |          |               |           |
|    | back end         |               |     |     |             |           |            |          |               |           |
|  6 |                  |               |     |     |             |           |            |          |               |           |
|  7 |                  | Microservice  |     |     |             |           |            |          |               |           |
|  8 |                  | architecture- |     |     |             |           |            |          |               |           |
|  9 |                  | based         |     |     |             |           |            |          |               |           |
| 10 |                  | applications  |     |     |             |           |            |          |               |           |
| 11 |                  |               |     |     |             |           |            |          |               |           |
| 12 | Business process |               |     |     |             |           |            |          |               |           |
|    | orchestrations   |               |     |     |             |           |            |          |               |           |
|    | and workflows    |               |     |     |             |           |            |          |               |           |