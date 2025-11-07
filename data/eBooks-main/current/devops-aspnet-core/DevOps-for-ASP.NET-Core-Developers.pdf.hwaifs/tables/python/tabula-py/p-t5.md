|    | Feature    | Description             | GitHub Actions   | Azure Pipelines   |
|---:|:-----------|:------------------------|:-----------------|:------------------|
|  0 | Approvals  | Define approval         | Yes              | Yes               |
|    |            | conditions before       |                  |                   |
|    |            | moving further in the   |                  |                   |
|    |            | pipeline                |                  |                   |
|  1 | Artifacts  | Upload, store, and      | Yes              | Yes               |
|    |            | download artifacts      |                  |                   |
|    |            | from jobs               |                  |                   |
|  2 | Caching    | Cache folders or files  | Yes              | Yes               |
|    |            | for subsequent runs     |                  |                   |
|  3 | Conditions | Specify conditions      | Yes              | Yes               |
|    |            | for steps or jobs       |                  |                   |
|  4 | Container  | Run jobs inside a       | Yes              | Yes               |
|    | Jobs       | container               |                  |                   |
|  5 | Demands    | Specify demands         | Yes              | Yes               |
|    |            | that must be met to     |                  |                   |
|    |            | match jobs to agents    |                  |                   |
|  6 | Dependenci | Specify                 | Yes              | Yes               |
|    | es         | dependencies            |                  |                   |
|    |            | between jobs or         |                  |                   |
|    |            | stages                  |                  |                   |
|  7 | Deployment | A logical set of target | No               | Yes               |
|    | Groups     | machines for            |                  |                   |
|    |            | deployments             |                  |                   |
|  8 | Deployment | Job that targets a      | No               | Yes               |
|    | Jobs       | deployment group        |                  |                   |