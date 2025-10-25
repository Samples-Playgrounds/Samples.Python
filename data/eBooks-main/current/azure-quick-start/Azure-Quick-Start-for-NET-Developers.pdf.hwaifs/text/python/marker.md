# **Azure**

Azure Quick Start Guide for .NET Developers

![](_page_0_Picture_2.jpeg)

# Contents

# Azure for .NET developers

What can Azure do for you?

# Getting Started with Azure services

- Running your .NET applications in Azure
- Azure App Services
- There are several different types of App Service apps.
- Azure Functions
- Azure Logic Apps
- Azure Virtual Machines
- A word about microservices and containers
- Which frameworks and technologies can you use in which Azure service?

# Storing your data in Azure

- Azure SQL Database
- Azure Cosmos DB
- Azure Storage
- Let's explore the different types of Azure Storage:
- Azure Databases for MySQL, PostgreSQL, and MariaDB
- Azure SQL Data Warehouse and Azure Data Lake Store

![](_page_1_Picture_19.jpeg)

# Securing your .NET applications in Azure

- Azure Active Directory
- Azure Key Vault
- Managed Service Identity
- Azure Advisor

# Other Azure services

- Enhance your application with performance
- Machine Learning
- Internet of Things (IoT)
- Data Analytics
- Messaging
- Media Services
- Monitoring

# Tools for developing, debugging and troubleshooting

- Visual Studio and Azure
- Cloud Explorer
- Publish to Azure
- Snapshot Debugger
- Azure Storage Explorer
- Azure Storage Emulator

![](_page_2_Picture_20.jpeg)

- Azure Command-Line Interface
- Azure Functions Core Tools
- Cosmos DB Emulator
- Azure DevOps for build and deployment

# Summary and how to get started for free

Keep learning with an Azure free account

# About the team

![](_page_3_Picture_7.jpeg)

![](_page_3_Picture_8.jpeg)

![](_page_4_Picture_0.jpeg)

# Azure for .NET developers

If you are a .NET developer or architect who wants to get started with Microsoft Azure, this book is for you! Written by developers for developers in the .NET ecosystem, this guide will show you how to get started with Azure and which services you can use to run your .NET applications and store your data in a more efficient and secure way.

Before we dive in, let's take a moment to see what the cloud, and Microsoft Azure in particular, can do for you.

# What can Azure do for you?

Azure provides services that can help you accomplish many things. These range from the mundane—such as adding search functionality to your application or spinning up a new SQL database to connect to your recent .NET app—to more exotic projects such as implementing continuous integration (CI) and continuous deployment (CD) workflows. You also can automatically tune your database or set up push notifications to mobile devices, easily and quickly. These are just a few examples of some common projects that developers have repeatedly had to create for themselves but that are now available as a service. And you can use these services with little effort—almost like flipping a light switch! You can then focus on the pieces of your application that make it unique—the features that provide real added value for your users.

Besides services, Azure offers compute resources in the form of virtual machines (VMs), containers, databases, web app services, and mobile services. You can use these to host applications or to provide a complete infrastructure for your users, most of which you can do through Visual Studio.

The power of the cloud is that services and resources are incredibly robust and resilient. It is very unlikely that they will fail to run, because the cloud is smart and self-healing. With Azure, there are datacenters all over the world, filled with tens of thousands of servers. If one server fails, another takes over. If an entire datacenter were to fail (a highly unlikely scenario), another would take over. All this is possible because of the massive scale of the cloud.

![](_page_5_Picture_0.jpeg)

One of the most compelling arguments in favor of the cloud is that you can scale up your services and resources almost infinitely, with just a few clicks of a button. You can't do that with on-premises resources unless you're prepared to spend enormous sums of money on capital equipment which would remain largely idle and staff to administer it all. You can scale globally without having to build data centers around the world by putting your services anywhere in the world eliminating latency and providing a highperformance experience to your users, regardless of where they are. It also means that you can keep your data where you need it to be, observing data residency requirements.

Equally important, when you use cloud resources, you can scale back your services and resources when there is no longer high demand. This allows you to scale up and down even during the course of a normal day keeping applications economical and performant.

In addition to massive scalability, off-the-shelf intelligent services, and pay-per-use efficiency, the cloud offers increased security. The cloud is used by millions of people, 24x7, worldwide. Of course, it is also attacked by many people. Reputable and experienced cloud providers like Microsoft recognize the usage patterns of normal users and those of malicious actors. This means we know how to protect against both the most common and most unique attacks out there. Intelligent monitoring tools, machine learning algorithms, and artificial intelligence give cloud providers the ability to detect attacks in real time and stop them in their tracks.

[Decades of experience in security](https://azure.microsoft.com/overview/trusted-cloud/) [a](https://azure.microsoft.com/overview/trusted-cloud/)nd massive-scale traffic, combined with top industry security expertise, make the cloud a much more secure environment than any onpremises datacenter.

#### **More info**

To read more about how Azure secures your applications and data, [read the official Azure](https://docs.microsoft.com/azure/security/security-get-started-overview) [Security blog, Azure Security Overview,](https://docs.microsoft.com/azure/security/security-get-started-overview) and [how to get started with Azure Security](https://docs.microsoft.com/en-us/azure/security/azure-security) . We've briefly explored reasons to begin y[ou](https://docs.microsoft.com/en-us/azure/security/azure-security)r migration to the cloud and Micros[of](https://docs.microsoft.com/en-us/azure/security/azure-security)t Azure. Now, let's examine which Azure services are useful for you for running and securing your applications and storing your data.

![](_page_5_Picture_7.jpeg)

![](_page_6_Picture_0.jpeg)

# Getting Started with Azure services

Let's explore some of the services that you can use for running your applications in Azure, storing your data in Azure, and securing your application with Azure.

# Running your .NET applications in Azure

One of the first decisions that you need to make when you start with Azure is which service(s) to use to run your applications in Azure. There are many options. Let's start by laying out which Azure services are most suitable for which application types in Table 1.

**Table 1:** Which Azure services are best suited for which types of applications?

|                                                        | 3                       |                               |                    |            |                     |                                      |                        |
|--------------------------------------------------------|-------------------------|-------------------------------|--------------------|------------|---------------------|--------------------------------------|------------------------|
|                                                        | App Service<br>Web Apps | App Service<br>Mobile<br>Apps | Azure<br>Functions | Logic Apps | Virtual<br>Machines | Azure<br>Kubernetes<br>Service (AKS) | Container<br>Instances |
| Monolithic<br>and N-Tier<br>applications               | <b>/</b>                |                               |                    |            | *                   |                                      | <b>/</b>               |
| Mobile app<br>back end                                 |                         | <b>✓</b>                      |                    |            | *                   |                                      |                        |
| Microservice<br>architecture-<br>based<br>applications |                         |                               | <b>✓</b>           |            |                     | <b>✓</b>                             |                        |
| Business process orchestrations and workflows          |                         |                               | <b>/</b>           | <b>/</b>   |                     |                                      |                        |

<sup>\*</sup> For lifting and shifting existing applications to Azure.

# **Azure App Services**

One of the easiest and most powerful ways to host your applications in Azure is in <u>Azure App Service</u>. Azure App Service is a group of services that takes care of hosting your application and abstracting away the complexities of the operating system and infrastructure. They are highly available by default and will stay up and running for at least <u>99.95%</u> of the time.

![](_page_7_Picture_0.jpeg)

They share powerful features like automatic scaling, zero-downtime deployments, and easy authentication and authorization. They also allow you to debug your application while it is running in production (with the Snapshot Debugger) and work very well with Application Insights, which you can use to monitor every aspect of your app, from performance to usage.

# There are several different types of App Service apps.

#### **Azure Web Apps**

Running a .NET web application in Azure is very easy in [Azure Web Apps.](https://azure.microsoft.com/services/app-service/web/) Web Apps act as a web server as a service, like [IIS.](https://www.iis.net/) And you can simply deploy your ASP.NET or ASP.NET Core application with Visual Studio to Web Apps and run it. These can be websites, APIs, or any other HTTP-driven application including Node.js, Python and Java applications.

Once your application runs in an App Service web app, you can [scale it up or down,](https://docs.microsoft.com/azure/app-service/web-sites-scale) add [easy authentication,](https://docs.microsoft.com/azure/app-service/app-service-authentication-overview) use [deployment slots,](https://docs.microsoft.com/azure/app-service/web-sites-staged-publishing) enable [continuous deployment,](https://docs.microsoft.com/azure/app-service/app-service-continuous-deployment) and use any of the other App Service features. By default, your application is available on the internet, without you needing to set up a domain name or configure DNS settings, although you can do that.

![](_page_7_Picture_6.jpeg)

**Try it now**- [Get started by creating an ASP.NET Core](https://docs.microsoft.com/en-us/azure/app-service/app-service-web-get-started-dotnet?view=azure-dotnet) web app in Azure

#### **Containers on App Services**

Developers who want the power of App Services but need to maintain a higher level of control over their environments can also [run containers.](https://azure.microsoft.com/services/app-service/containers/) Both [Linux](https://docs.microsoft.com/en-us/azure/app-service/containers/quickstart-docker-go) and [Windows](https://docs.microsoft.com/en-us/azure/app-service/app-service-web-get-started-windows-container)  [containers](https://docs.microsoft.com/en-us/azure/app-service/app-service-web-get-started-windows-container) are supported. You can deploy your own containers from the [Azure](https://azure.microsoft.com/services/container-registry/)  [Container Registry,](https://azure.microsoft.com/services/container-registry/) a private Docker registry or public containers from the Docker Hub. This allows you to run a wide range of pre-configured applications from WordPress to Redis which can be deployed either as single containers or as part of a [multi-container](https://docs.microsoft.com/en-us/azure/app-service/containers/quickstart-multi-container)  [application.](https://docs.microsoft.com/en-us/azure/app-service/containers/quickstart-multi-container) Windows container support also helps you migrate existing ASP.NET apps and WCF services that need access to the Windows OS, install custom components, or use the Global Assembly Cache (GAC).

![](_page_8_Picture_0.jpeg)

#### **Azure Mobile Apps**

If you are building mobile applications, you will need a back end that the mobile app connects to. Usually, this is some sort of API that your app can use to retrieve and store data. [Azure Mobile Apps](https://azure.microsoft.com/services/app-service/mobile/) provides you with such a back end. You can write it in C# or use any of the Quickstart applications.

A mobile back end that runs in Azure Mobile Apps provides unique capabilities. For instance, you can use [offline sync,](https://docs.microsoft.com/azure/app-service-mobile/app-service-mobile-offline-data-sync) which enables the mobile app to continue working when there is no connection to the back end and sync changes once the connection is restored. And with push notifications you can send notifications to the mobile apps using C# code, regardless of the platform it runs on (iOS, Android, Windows). In addition to these unique features, Mobile Apps shares all the other features of Azure App Service.

![](_page_8_Picture_4.jpeg)

[Get started by creating an Android app with an Azure mobile app back end.](https://docs.microsoft.com/azure/app-service-mobile/app-service-mobile-android-get-started)

# Azure Functions (also known as serverless compute)

[Azure Function apps](https://docs.microsoft.com/azure/azure-functions/functions-overview) enable you to create Azure Functions in C# and many other languages in Visual Studio and other IDEs and editors. Each Functions app contains one or more Azure Functions and provides integration with authentication and deployment slots.

The Azure Functions that run in Azure Function apps are small pieces of code that you write, without you having to worry about the underlying infrastructure or about scaling. Many refer to this deployment model as Functions as a Service (FaaS).

Function applications can be simply triggered by a wide variety of events originating both inside and outside of Azure. HTTP triggers allow web requests to be served by a function app. [Event Grid](https://docs.microsoft.com/en-us/azure/azure-functions/functions-bindings-event-grid) events can trigger Azure Functions when changes are made to Azure resources such as the container registry and virtual machines.

![](_page_9_Picture_0.jpeg)

Here is an example: You write an Azure Functions app that executes every time a new image file is uploaded to Azure Storage. You then take that image, rename it, and output it to another Azure Storage account.

This is very easy to do. You just write the code to rename the image. Azure Functions takes care of getting the input image when the function is [triggered.](https://docs.microsoft.com/azure/azure-functions/functions-triggers-bindings) And it takes care of writing the image to the other storage account. It takes care of all the plumbing, and you just write the code.

Azure Functions even [handles scaling for you.](https://docs.microsoft.com/azure/azure-functions/functions-scale) So it doesn't matter if there are 1,000 images that trigger the function at the same time. Azure Functions transparently spins up more functions to deal with it and they go away when the code is done executing. Because of this, you only pay for the code that you execute, not for a service that runs all the time, waiting to be triggered.

Azure Functions are great for executing small pieces of code that perform one or two steps on an input and an output. If you want to perform more steps of a larger process, you can use [Durable Functions.](https://docs.microsoft.com/en-us/azure/azure-functions/durable/durable-functions-overview)

Durable Functions provide a stateful experience on top of a series of Azure Functions. They enable complex patterns such as scatter/gather and function chaining. A Durable Function orchestration may be as simple as coupling together two functions, one after another, or as complex as coordinating tens of thousands of function calls over weeks.

![](_page_9_Picture_6.jpeg)

[Get started by creating your first Azure Function with Visual Studio.](https://docs.microsoft.com/azure/azure-functions/functions-create-your-first-function-visual-studio)

# Azure Logic Apps

Durable Functions are a fantastic orchestration tool for developers who are comfortable with writing every step of the process inside a series of Functions. For those looking for a lower code solution Logic Applications may be better. With Azure Logic Apps, you can orchestrate a process just by weaving API calls together in a visual designer in Visual Studio or the Azure portal. Visual Studio offers a specific Logic Apps project template to get started.

![](_page_10_Picture_0.jpeg)

A logic app has a trigger, just like an Azure function does. This can be an outside trigger, like when a new blob is added, or a certain text is tweeted. Or it can be a manual trigger or a trigger on a schedule such as every 15 minutes.

Once triggered, a logic app takes its input and calls APIs with it to complete a process. You just click this together by choosing APIs from a large list of available ones and choosing the input and output for those APIs. Azure Functions can also be used for APIs in a logic app. And you can use your own ASP.NET Core APIs.

# **Here's an[example:](https://docs.microsoft.com/azure/logic-apps/logic-apps-examples-and-scenarios)**

A logic app gets triggered by a new blob that is written in [Azure Blob storage](https://azure.microsoft.com/services/storage/blobs/). It takes the Blob input, which is an image file, and resizes the image by calling an Azure function that does just that. Next, it takes the resized image and writes it to another storage account. And finally, it calls the [Office 365 API](https://docs.microsoft.com/azure/connectors/connectors-create-api-office365-outlook) to send an email to the administrator that there is a new, resized image available.

![](_page_10_Picture_5.jpeg)

Just like Azure functions, logic apps scale automatically, you just create the process. It will trigger as many times as it is needed and always executes the complete process and has reliability features, like retry policies, built in. And because it only runs when it is triggered, you only pay for when it runs—you don't pay for owning it.

![](_page_10_Picture_7.jpeg)

[Get started by building your first logic app workflow in the Azure portal.](https://docs.microsoft.com/azure/logic-apps/quickstart-create-first-logic-app-workflow)

**Note:** Azure Logic Apps and Azure Functions work very well with the [Azure Event Grid](https://azure.microsoft.com/services/event-grid/) service. Event Grid allows you to subscribe to events, like when something happens in your application, and to push that information as an event that can trigger a Logic App or an Azure Function.

# Azure Virtual Machines

A very different way of running your application is by taking advantage of [Azure Virtual](https://azure.microsoft.com/services/virtual-machines/)  [Machines.](https://azure.microsoft.com/services/virtual-machines/) This is an easy way to get started, because you can lift-and-shift existing applications from virtual machines that you run in your datacenter to VMs that run in Azure. There are many predefined VM images that you can use, like Windows Server 2019 that runs IIS and has ASP.NET installed and preconfigured on it. You can even bring your own software licenses if you already have one (like for SQL Server).

![](_page_11_Picture_0.jpeg)

Running your application in a VM doesn't provide you the features like zero-downtime deployments and easy authentication. You are also responsible for patching the operating system and for making sure that antivirus software is up to date.

On the other hand, it does provide you with the ability to easily scale your VM to a bigger size or automatically scale it down when it isn't used that much. [Virtual Machine](https://docs.microsoft.com/en-us/azure/virtual-machine-scale-sets/)  [Scale Sets](https://docs.microsoft.com/en-us/azure/virtual-machine-scale-sets/) allow for scaling out VMs to a large number of nodes and load balancing work between them. And it offers you the reliability of running something in Azure. It is very unlikely that your VM will stop running, and Microsoft guarantees this uptime with a [comprehensive SLA.](https://azure.microsoft.com/support/legal/sla/virtual-machines/v1_6/)

And if you're not ready to run your production VMs in Azure you can still take advantage of streamlined DevOps and testing with Azure DevTest Labs.

![](_page_11_Picture_4.jpeg)

[Get started by Creating a Windows virtual machine with the Azure portal.](https://docs.microsoft.com/azure/virtual-machines/windows/quick-create-portal)

# A word about microservices and containers

You can run your applications in [containers,](https://azure.microsoft.com/overview/containers/) which are very lightweight and start and stop in seconds. Containers isolate your application and its dependencies in a way that guarantees that you'll never run into library version conflicts. They can be based on numerous popular Linux distributions or Windows Server so no matter the platform your application uses it can run in a container.

A popular approach for containers is to use them to run a [microservices architecture.](https://docs.microsoft.com/azure/architecture/guide/architecture-styles/microservices) This means that you create many small, isolated, services that each have their own function and each have separate development and deployment lifecycles. Containers can also be used to lift and shift existing applications to run at scale in the cloud.

Azure provides several services to support running a [microservices architecture i](https://docs.microsoft.com/azure/architecture/guide/architecture-styles/microservices)n containers. Running the increasingly popular orchestration engine Kubernetes, [Azure](https://docs.microsoft.com/en-us/azure/aks/intro-kubernetes)  [Kubernetes](https://docs.microsoft.com/en-us/azure/aks/intro-kubernetes) Service [\(](https://docs.microsoft.com/en-us/azure/aks/intro-kubernetes)AKS) provides a powerful tool to run anything from a handful of containers to hundreds of thousands of the[m.](https://azure.microsoft.com/en-us/services/service-fabric/) AKS can all run and orchestrate containers. Orchestration of containers is quite different from orchestrating a process, like Logic Apps does. Orchestrating containers means that you manage their lifecycles. Provision new ones, scale up or down, manage failures, and so on.

![](_page_12_Picture_0.jpeg)

![](_page_12_Picture_1.jpeg)

# You can learn more about microservices by reading: .NET Microservices [Architecture Guidance](https://dotnet.microsoft.com/learn/web/microservices-architecture)

# Which frameworks and technologies can you use in which Azure service?

Now that you know what the options are for running your application in Azure, it is extremely useful to know which version of .NET you can run in these services and what kind of containers they support. Table 2 explains this by showing which framework and container types you can use in which services in Azure.

**Table 2:** Which framework and technology can you use in which Azure service

|                              | Web Apps | Mobile<br>Apps | Functions | Azure VMs | Azure<br>Container<br>Instance | Azure<br>Kubernetes<br>Service<br>(AKS) |
|------------------------------|----------|----------------|-----------|-----------|--------------------------------|-----------------------------------------|
| .NET Framework<br>apps       |          |                |           |           |                                |                                         |
| .NET Core apps               |          |                |           |           |                                |                                         |
| Linux Containers             |          |                |           |           |                                |                                         |
| Windows Server<br>Containers |          |                |           |           |                                |                                         |

![](_page_13_Picture_0.jpeg)

# Storing your data in Azure

Data is a particularly important aspect of any modern .NET application, and it comes in all shapes and sizes. Azure provides many types of data stores that can help you maintain and retrieve data in any scenario.

**Table 3** shows which data service to use for which scenario.

|                                   | Database | Cosmos DB | Blob | Table | File | PostgreSQL,<br>MySQL | SQL Data<br>Warehouse | Data Lake<br>Store |
|-----------------------------------|----------|-----------|------|-------|------|----------------------|-----------------------|--------------------|
| Relational data                   |          |           |      |       |      |                      |                       |                    |
| Unstructured<br>data              |          |           |      |       |      |                      |                       |                    |
| Semistructured<br>data            |          |           |      |       |      |                      |                       |                    |
| Files on disk                     |          |           |      |       |      |                      |                       |                    |
| Store large data                  |          |           |      |       |      |                      |                       |                    |
| Store small<br>data               |          |           |      |       |      |                      |                       |                    |
| Geographic<br>data<br>replication |          |           |      |       |      |                      |                       |                    |
| Tunable data<br>consistency       |          |           |      |       |      |                      |                       |                    |

![](_page_14_Picture_0.jpeg)

![](_page_14_Picture_1.jpeg)

# Azure SQL Database

If you are familiar with .NET, you will likely be familiar with [SQL Server.](https://www.microsoft.com/sql-server/sql-server-2017) In Azure, you can run your SQL Server workload in [Azure SQL Database.](https://azure.microsoft.com/services/sql-database/) This is SQL Server in the cloud. It is the same thing that you run on-premises but it offers a lot of advantages.

You can do [\(almost\)](https://docs.microsoft.com/azure/sql-database/sql-database-transact-sql-information) everything with it that you can do with on-premises SQL Server. And, in fact, new SQL Server features are incorporated in Azure SQL Database first and later in the on-premises SQL Server.

You can use Azure SQL Databases with your favorite tools, like [Azure Data Studio,](https://docs.microsoft.com/en-us/sql/azure-data-studio/download?view=sql-server-2017) [Server](https://docs.microsoft.com/azure/vs-azure-tools-storage-resources-server-explorer-browse-manage)  [Explorer](https://docs.microsoft.com/azure/vs-azure-tools-storage-resources-server-explorer-browse-manage) and [SQL Server Data Tools](https://www.visualstudio.com/vs/ssdt/) in Visual Studio and [SQL Server Management](https://docs.microsoft.com/sql/ssms/sql-server-management-studio-ssms)  [Studio.](https://docs.microsoft.com/sql/ssms/sql-server-management-studio-ssms)

Because they run in the cloud, Azure SQL Databases are fully managed, scalable, and high performing. They are automatically backed up and have many advanced features, such as:

- **Single-click Geo-replication**, which replicates data to other geographical regions in real time, incredibly easily. [\(Get started with geo-replication.\)](https://docs.microsoft.com/azure/sql-database/sql-database-geo-replication-transact-sql)
- **Dynamic data masking**, which masks sensitive data for certain users at runtime. [\(Get started with dynamic data masking.](https://docs.microsoft.com/azure/sql-database/sql-database-dynamic-data-masking-get-started))
- **Auditing**, which provides a complete audit trail of all the actions that happen to the data. [\(Get started with Azure SQL Database auditing.](https://docs.microsoft.com/azure/sql-database/sql-database-auditing))
- **Automatic database tuning**, which monitors the performance of your database and tunes it automatically. [\(Get started with Azure SQL Database automatic tuning.](https://docs.microsoft.com/azure/sql-database/sql-database-automatic-tuning))

![](_page_15_Picture_0.jpeg)

In addition to all these features, Azure SQL Databases are exceptionally reliable by default. Without configuring anything, transaction log backups are made every 5-10 minutes and differential backups every 12 hours. These backups are stored three times in the local datacenter and three times in another datacenter. And you can restore backups from 35 days ago, [depending on the pricing tier](https://docs.microsoft.com/azure/sql-database/sql-database-automated-backups#how-long-do-you-keep-my-backups) that you use.

It is very easy to use Azure SQL Databases from a .NET application. You can, for instance, use the [Entity Framework](https://docs.microsoft.com/ef/) (or [Entity Framework Core\)](https://docs.microsoft.com/ef/core/) to access the database and write and read data to and from it. For the [most part](https://docs.microsoft.com/en-us/azure/sql-database/sql-database-connectivity-issues) accessing data programmatically is no different from accessing data in an on-premises SQL Server.

![](_page_15_Picture_3.jpeg)

#### [Get started by creating an Azure SQL Database in the Azure Portal](https://docs.microsoft.com/en-us/azure/sql-database/sql-database-get-started-portal) .

# Azure Cosmos DB

[Azure Cosmos DB](https://azure.microsoft.com/services/cosmos-db/) is a new kind of database that is globally distributed and cloud native. Here are some of its key features:

- **A [99.99% SLA](https://azure.microsoft.com/roadmap/azure-cosmos-db-sla-99-999-percent-read-availability-at-global-scale/)** [\(99.999% for read operations\) t](https://azure.microsoft.com/roadmap/azure-cosmos-db-sla-99-999-percent-read-availability-at-global-scale/)hat includes low latencies (less than 10 ms on reads; less than 15 ms on writes).
- **Geo-replication**, which replicates data to other geographical regions in real time [\(How to distribute data globally with Azure Cosmos DB\)](https://docs.microsoft.com/azure/cosmos-db/distribute-data-globally).
- **[Tunable data consistency levels](https://docs.microsoft.com/azure/cosmos-db/consistency-levels)**[,](https://docs.microsoft.com/azure/cosmos-db/consistency-levels) so you can choose data consistency, enabling a truly globally distributed data system. You can, for instance, choose **strong consistency**, **eventual consistency**, or **session consistency**.
- **Traffic management**, which sends users to the data replica to which they are closest.
- **Limitless global scale**. You pay only for the throughput and storage that you need.
- **[Automatic indexing of data](https://docs.microsoft.com/azure/cosmos-db/indexing-policies)**. No need to maintain or tune the database anymore.

In addition to all these features, Cosmos DB offers different APIs with which you can store and retrieve data, including SQL, Gremlin, MongoDB, Azure Table Storage, and Apache Cassandra. Different APIs handle data in different ways. You can use documents as data as well as unstructured tables, graphs, and blobs. You use the API that fits your

![](_page_16_Picture_0.jpeg)

needs, and Cosmos DB takes care of the rest. If your application already uses one of these protocols switching to Cosmos DB is as simple as changing a connection string.

You benefit from cloud-grade performance, scalability, and reliability, and still use the programming model to which you're accustomed.

You can use Cosmos DB from .NET Framework and .NET Core. For example, you can use its SQL API through the NuGet package [Microsoft.Azure.DocumentDB](https://www.nuget.org/packages/Microsoft.Azure.DocumentDB) [o](https://www.nuget.org/packages/Microsoft.Azure.DocumentDB)r [Microsoft.Azure.DocumentDB.Core](https://www.nuget.org/packages/Microsoft.Azure.DocumentDB.Core) [\(](https://www.nuget.org/packages/Microsoft.Azure.DocumentDB.Core)for .NET Core).

![](_page_16_Picture_4.jpeg)

[Get started with Azure Cosmos DB with the SQL API and .NET Core.](https://docs.microsoft.com/azure/cosmos-db/sql-api-dotnetcore-get-started)

# Azure Storage

With [Azure Storage,](https://azure.microsoft.com/services/storage/) one of the most fundamental services in Azure, you can store data in different forms. It is easy to use, fast, and inexpensive. Azure Storage offers several types of storage that you can use for different scenarios. All these storage types share common features like [encryption for data at rest,](https://docs.microsoft.com/azure/storage/common/storage-service-encryption) security through [shared access](https://docs.microsoft.com/azure/storage/common/storage-dotnet-shared-access-signature-part-1)  [signatures,](https://docs.microsoft.com/azure/storage/common/storage-dotnet-shared-access-signature-part-1) and [firewalls and virtual networks.](https://docs.microsoft.com/azure/storage/common/storage-network-security)

Azure Storage is also [very reliable.](https://docs.microsoft.com/azure/storage/common/storage-redundancy) By default, data is replicated three times within the datacenter. You can also choose geo-replicated storage, which, in addition to the three local replicas, replicates the data three times to another datacenter. You can create your application in such a manner that it reads from this geo-replicated data, which is close to your users, so that it is geographically high performing.

You can use Azure Storage from your .NET Framework and .NET Core applications by using the [WindowsAzure.Storage NuGet package](https://www.nuget.org/packages/WindowsAzure.Storage/) and referencing the specific API that you need, like **Microsoft.WindowsAzure.Storage.Blob** (for Blob storage) in a using statement in your code.

# Let's explore the different types of Azure Storage:

![](_page_17_Picture_1.jpeg)

#### **File Storage**

[Azure File storage](https://azure.microsoft.com/services/storage/files/) uses the SMB protocol, which makes it very suitable for lifting and shifting your file server into the cloud. When you have files in Azure Files, you can [mount](https://docs.microsoft.com/azure/virtual-machines/windows/mount-azure-file-storage)  [an Azure file share to a VM](https://docs.microsoft.com/azure/virtual-machines/windows/mount-azure-file-storage) or even to your own Windows machine, to use as external storage.

![](_page_17_Picture_4.jpeg)

#### [Get started with Azure Files.](https://docs.microsoft.com/azure/storage/files/storage-dotnet-how-to-use-files)

[Azure Disk Storage](https://azure.microsoft.com/services/storage/unmanaged-disks/) is a [similar service](https://docs.microsoft.com/en-us/azure/storage/common/storage-decide-blobs-files-disks) to Azure File but is dedicated to a single machine. It is available in four different performance levels from Standard HDD to Ultra SSD. The high performance tiers are suitable for heavy I/O workloads such as running SAP HANA or complex analytical models.

#### **Table Storage**

[Azure Table storage](https://azure.microsoft.com/services/storage/tables/) is an inexpensive and extremely fast NoSQL key-value store that you can use to store data in flexible tables. A table can contain one row describing an order and another row describing customer information. You don't need to define a data schema. This makes Table Storage very flexible.

![](_page_17_Picture_9.jpeg)

#### [Get started with Azure Table storage.](https://azure.microsoft.com/resources/samples/storage-table-dotnet-getting-started/)

#### **Blob Storage**

You can use [Azure Blob storage](https://azure.microsoft.com/services/storage/blobs/) to store large unstructured data—literally, blobs of data. This can be video, image, audio, text, or even virtual hard drive (VHD) files for VMs. Additionally, you can use [Blob tiers](https://docs.microsoft.com/azure/storage/blobs/storage-blob-storage-tiers) to reduce your storage costs. By default, blobs are written to the **hot tier**, which means that they are written and read very fast. You can also put blobs in the **cool tier** if you have data that is infrequently accessed and stored for at least 30 days. The **cool tier** is less expensive than the **hot tier**. And finally, you can store blobs in the **archive tier**, that is the least expensive. The **archive tier** is for data

![](_page_18_Picture_0.jpeg)

that is rarely accessed and stored for at least 180 days. Reading data from the archive tier can take hours. Blob tiering is a great way to save costs if you are storing large amounts of data.

![](_page_18_Picture_2.jpeg)

#### [Get started with Azure Blob storage.](https://docs.microsoft.com/azure/storage/blobs/storage-dotnet-how-to-use-blobs)

#### **Queue Storage**

[Azure Queue storage](https://azure.microsoft.com/en-us/services/storage/queues/) [i](https://azure.microsoft.com/en-us/services/storage/queues/)s an unusual type of storage in that it is used to store small messages of data, but its main purpose is to serve as a queue. You put messages on the queue and other processes pick it up. [This pattern](https://azure.microsoft.com/en-us/services/storage/queues/) decouples the message sender from the message processor and results in performance and reliability benefits. Azure Queue storage is similar to [Microsoft Message Queuing](https://msdn.microsoft.com/library/ms711472(v=vs.85).aspx) that you can find in Windows.

![](_page_18_Picture_6.jpeg)

#### [Get started with Azure Queue storage.](https://docs.microsoft.com/azure/storage/queues/storage-dotnet-how-to-use-queues)

**|Note**: Azure Service Bus [Topics a](https://docs.microsoft.com/azure/service-bus-messaging/service-bus-dotnet-how-to-use-topics-subscriptions)nd [Queues](https://docs.microsoft.com/azure/service-bus-messaging/service-bus-dotnet-get-started-with-queues) also provide queuing mechanisms, with slightly different properties than Azure Storage queues.

# Azure Databases for MySQL, PostgreSQL, and MariaDB

As a .NET developer, you encounter many different open-source database types in your job. Some of them can now be used in a managed version in Azure.

Azure provides [MySQL,](https://azure.microsoft.com/services/mysql/) [PostgreSQL,](https://azure.microsoft.com/services/postgresql/) and [MariaDB](https://azure.microsoft.com/blog/mariadb-postgresql-and-mysql-more-choices-on-microsoft-azure/) [d](https://azure.microsoft.com/blog/mariadb-postgresql-and-mysql-more-choices-on-microsoft-azure/)atabases as managed databases, which means that you just spin them up and don't have to worry about any of the underlying infrastructure. Just like Azure SQL Databases and Cosmos DB, these databases are universally available, scalable, highly secure, and fully managed.

Each of these is suited for slightly different use cases, but in general, their functionality overlaps a lot. You would use Azure Databases for MySQL, PostgreSQL, and MariaDB when you are already using one of their on-premises versions and want the advantage of having that run fully managed in the cloud. Migrating apps that use these databases is much easier when the data can remain in its original platform. Azure also provides an out of the box backend for services like WordPress which rely on open source databases.

![](_page_19_Picture_0.jpeg)

![](_page_19_Picture_1.jpeg)

# [Get started with Azure Database for MySQL by creating a MySQL server](https://docs.microsoft.com/azure/mysql/quickstart-create-mysql-server-database-using-azure-portal) [by using the Azure portal.](https://docs.microsoft.com/azure/mysql/quickstart-create-mysql-server-database-using-azure-portal)

# Azure SQL Data Warehouse and Azure Data Lake Store

Since we are talking about storing data in Azure, we can't leave out the data stores for big data and data analytics. These are not typical stores that you use with your application, but rather stores that you use for data analytics and reporting.

Azure provides two data stores that are very suitable for storing large amounts of data for data analytics purposes: the [Azure SQL Data Warehouse](https://azure.microsoft.com/services/sql-data-warehouse/) and the [Azure Data Lake](https://azure.microsoft.com/services/data-lake-store/)  [Store.](https://azure.microsoft.com/services/data-lake-store/)

Each of these can hold petabytes of data. In fact, Azure Data Lake Store doesn't even have limits on the amount of data and the file sizes that you can store.

You use Azure SQL Data Warehouse when you know the questions that you want to answer with data analytics. You define a data schema that determines what your data will look like and how it can be used.

You use Azure Data Lake Store when you don't know the questions that you want to answer yet. You do not have to define a data schema for the Data Lake Store. You store data in its native format.

You can work with each of these data stores with tools in Visual Studio. And you can use any SQL tool, like SQL Server Management Studio, to work with Azure SQL Data Warehouse. You can even create eye-popping business intelligence dashboards and reports as a non-developer in [Power BI.](https://powerbi.microsoft.com/en-us/)

Additionally, you can use the [Azure Management SDK for .NET](https://www.nuget.org/packages?q=Microsoft.Azure.Management) to perform management operations on these services. You can, for instance, [create a new Data Lake Store](https://docs.microsoft.com/azure/data-lake-store/data-lake-store-get-started-net-sdk)  [account.](https://docs.microsoft.com/azure/data-lake-store/data-lake-store-get-started-net-sdk)

![](_page_19_Picture_11.jpeg)

Get started [with Azure SQL Data Warehouse by creating and query](https://docs.microsoft.com/azure/sql-data-warehouse/create-data-warehouse-portal) [a warehouse in the Azure portal.](https://docs.microsoft.com/azure/sql-data-warehouse/create-data-warehouse-portal)

![](_page_20_Picture_0.jpeg)

![](_page_20_Picture_1.jpeg)

#### [Get started with Azure Data Lake Store using the Azure portal.](https://docs.microsoft.com/azure/data-lake-store/data-lake-store-get-started-portal)

# Securing your .NET applications in Azure

Besides running your application and storing data, you need to secure it. Azure can help you with that by providing authentication and authorization through [Azure Active](https://docs.microsoft.com/azure/active-directory/active-directory-whatis)  [Directory](https://docs.microsoft.com/azure/active-directory/active-directory-whatis) [a](https://docs.microsoft.com/azure/active-directory/active-directory-whatis)nd by helping you to keep secrets safe with [Azure Key Vault](https://azure.microsoft.com/services/key-vault/) and inserting credentials into your application with [Managed Service Identity.](https://docs.microsoft.com/azure/active-directory/msi-overview) Let's examine these services.

# Azure Active Directory

An important part of your application's security is authenticating users before they can use it. Authentication is not an easy thing to implement. You need to store user identities and credentials, implement password management, create a secure authentication handshake, and so on.

[Azure Active Directory](https://docs.microsoft.com/azure/active-directory/active-directory-whatis) provides all these things and more out of the box. You store your user identities in Azure Active Directory and have users authenticate against it, redirecting them to your application only after they are authenticated. Azure Active Directory takes care of password management, including common scenarios like "I forgot my password." Azure Active Directory is used by millions of applications every day, including the [Azure portal,](https://portal.azure.com/) [Outlook.com,](https://outlook.live.com/owa/) and [Office 365.](https://products.office.com/compare-all-microsoft-office-products) Because of this, it is able to more readily detect malicious behavior and act on it. For instance, if a user were to sign in to an application from a location in Europe and then one minute later sign in from Australia, Azure Active Directory would flag this as malicious behavior and ask the user for additional credentials through multifactor authentication.

To programmatically talk to Azure Active Directory, you can use the [Active Directory](https://github.com/AzureAD/azure-activedirectory-library-for-dotnet)  [Authenticating Library \(ADAL\) for .NET Framework and .NET Core.](https://github.com/AzureAD/azure-activedirectory-library-for-dotnet)

![](_page_21_Picture_0.jpeg)

![](_page_21_Picture_1.jpeg)

#### [Get started by integrating Azure AD into an ASP.NET Core web app.](https://azure.microsoft.com/resources/samples/active-directory-dotnet-webapp-openidconnect-aspnetcore/)

# Azure Key Vault

It is important to keep secrets such as passwords and connection strings out of source code. So where do you put them? In [Azure Key Vault.](https://azure.microsoft.com/services/key-vault/)

Azure Key Vault is a safe place to store passwords, connection strings, access codes, and certificate keys. It is fully managed by Azure, so you don't have to worry about the underlying infrastructure. You just spin it up and use it.

You can use it as a configuration store in your applications, just like you would use a **web.config** file. An administrator can populate the values in the Azure Key Vault, and your application just pulls it out at startup time or whenever it needs it. This way, passwords will never be in source code and are the responsibility of the Azure Key Vault administrator.

You can use Azure Key Vault using the [Microsoft.Azure.KeyVault NuGet package](https://www.nuget.org/packages/Microsoft.Azure.KeyVault) that you can use from the .NET Framework and .NET Core. There is even a [special syntax](https://azure.microsoft.com/en-us/blog/simplifying-security-for-serverless-and-web-apps-with-azure-functions-and-app-service/) which allows pulling secrets from KeyVault in App Services with zero code changes. For more complex scenarios where configuration changes based on location, release or some other custom dimension Microsoft is introducing [Azure App Configuration](https://channel9.msdn.com/Shows/Azure-Friday/Getting-started-with-Azure-App-Configuration) a service dedicated to providing a centralized configuration location which can be used from everything form App Services to a DevOps pipeline.

![](_page_21_Picture_8.jpeg)

[Get Started by using Azure Key Vault from an ASP.NET application.](https://docs.microsoft.com/azure/key-vault/key-vault-use-from-web-application)

# Managed Service Identity

Even when you use Azure Key Vault, your application must have some credentials in its configuration. Something that you use to connect to Azure Active Directory or to Azure Key Vault. Well, it doesn't have to anymore. You can now use [Azure Managed Service](https://docs.microsoft.com/azure/active-directory/msi-overview)  [Identity.](https://docs.microsoft.com/azure/active-directory/msi-overview)

![](_page_22_Picture_0.jpeg)

You can use Managed Service Identity from a lot of services in Azure, including from Azure App Service. From there, you can enable it to inject credentials into your application at runtime and use those credentials to access other services, like Azure Key Vault.

You can use the Managed Service Identity from the .NET Framework and .NET Core using the [Microsoft.Azure.Services.AppAuthentication NuGet package.](https://www.nuget.org/packages/Microsoft.Azure.Services.AppAuthentication)

![](_page_22_Picture_3.jpeg)

[Get started by using Key Vault from App Service with](https://github.com/Azure-Samples/app-service-msi-keyvault-dotnet) [Managed Service Identity.](https://github.com/Azure-Samples/app-service-msi-keyvault-dotnet)

# Azure Advisor

There are a lot of moving parts in Azure so Microsoft provides a tool called [Azure](https://azure.microsoft.com/en-ca/services/advisor/)  [Advisor](https://azure.microsoft.com/en-ca/services/advisor/) which examines your Azure resources and makes recommendations. The recommendations include how to save money by making more efficient use of Azure resources and suggestions on how to make your Azure resources more secure. The security advisor will catch and rank problems like world readable Blob Storage and give instructions on how to better secure your environment.

# Other Azure services

# Enhance your application performance

Azure can also help you to boost your applications' performance. One service that helps with this is [Azure Redis Cache,](https://azure.microsoft.com/services/cache/) which provides high-performance, in-memory, key-value storage. Another is [Azure Content Delivery](https://azure.microsoft.com/services/cdn/) Networ[k,](https://azure.microsoft.com/services/cdn/) or CDN, which can replicate your static content, like images and video files to points-of-presence all over the world, making sure that it is as close to your users as possible. And finally, [Azure Traffic](https://azure.microsoft.com/services/traffic-manager/)  [Manager](https://azure.microsoft.com/services/traffic-manager/) can improve application responsiveness by routing users to locations with the lowest latency.

# Machine Learning

Azure provides an industry leading suite of services that can make your application more intelligent. [Azure Cognitive Services](https://azure.microsoft.com/services/cognitive-services/) [a](https://azure.microsoft.com/services/cognitive-services/)re a suite of APIs that can do things which would be nearly impossible using traditional programming approaches. You can quickly build

![](_page_23_Picture_0.jpeg)

applications which can recognize faces, convert speech to text and understand the meaning of text. Using the [Language Understanding](https://azure.microsoft.com/en-ca/services/cognitive-services/language-understanding-intelligent-service/) service you can create [bots](https://azure.microsoft.com/en-ca/services/bot-service/) which can intelligently respond to requests in Slack, Microsoft Teams and other forums. You can also create your own machine learning algorithms with [Azure Machine Learning.](https://docs.microsoft.com/en-us/azure/architecture/data-guide/technology-choices/data-science-and-machine-learning)  Training jobs created in popular tools such as Tensorflow can be submitted to run on a cluster of GPU-enabled Virtual Machines, vastly decreasing the time to train models.

# Internet of Things (IoT)

When you are building a solution based on the Internet of Things, Azure can help you with services like [Azure IoT Hub,](https://azure.microsoft.com/services/iot-hub/) which can ingest massive amounts of messages from IoT devices and manage the devices. [Azure IoT Suite](https://azure.microsoft.com/suites/iot-suite/) [m](https://azure.microsoft.com/suites/iot-suite/)akes it possible for you to manage your IoT devices without doing everything yourself. And if you have limited IoT experience, you can use [Azure IoT Central,](https://www.microsoft.com/iot-central) which is a SaaS solution that enables you to use IoT with minimal customization. And finally, there is [Azure IoT Edge,](https://azure.microsoft.com/services/iot-edge/) which allows IoT devices to do some of the calculations locally, instead of having to communicate with the cloud for every operation. Trained ML models can even be deployed to edge devices enabling capabilities such as image recognition in disconnected hardware.

# Data Analytics

There are many services in Azure for doing data analytics, including [Azure Data Factory](https://azure.microsoft.com/services/data-factory/) for moving and transforming data; [Azure Analysis Services,](https://azure.microsoft.com/services/analysis-services/) which provides an inmemory data analytics platform; and [Azure Data Lake Analytics,](https://azure.microsoft.com/services/data-lake-analytics/) which can perform U-SQL jobs on [Azure Data Lake Store.](https://azure.microsoft.com/services/data-lake-store/) You can also take advantage of [Azure Stream](https://azure.microsoft.com/services/stream-analytics/)  [Analytics](https://azure.microsoft.com/services/stream-analytics/) to analyze data on the fly and [Azure Time Series I](https://azure.microsoft.com/en-us/services/time-series-insights/)nsights, which provides a unique data analytics platform for time-based data that can store and analyze data and can show information using its own data visualization engine. In addition, there is [Azure](https://databricks.com/azure)  [Databricks,](https://databricks.com/azure) which offers a managed cluster of enhanced [Apache Spark](https://databricks.com/spark/about)–based analytics engines, and [Azure HDInsight,](https://azure.microsoft.com/services/hdinsight/) which you can use to spin up managed clusters of opensource data analytics platforms and tools, like [Apache Storm,](https://docs.microsoft.com/azure/hdinsight/storm/apache-storm-overview) [Apache Kafka,](https://docs.microsoft.com/azure/hdinsight/kafka/apache-kafka-introduction) and [Apache HBase.](https://docs.microsoft.com/azure/hdinsight/hbase/apache-hbase-overview)

# Messaging

Azure also provides services that can help you build scalable architectures with events and messages. [Azure Queue Storage](https://azure.microsoft.com/services/storage/queues/) and [Azure Service Bus Topics](https://docs.microsoft.com/azure/service-bus-messaging/service-bus-dotnet-how-to-use-topics-subscriptions) [a](https://docs.microsoft.com/azure/service-bus-messaging/service-bus-dotnet-how-to-use-topics-subscriptions)nd [Queues](https://docs.microsoft.com/azure/service-bus-messaging/service-bus-dotnet-get-started-with-queues) [c](https://docs.microsoft.com/azure/service-bus-messaging/service-bus-dotnet-get-started-with-queues)an help with that by providing queuing mechanisms that decouple your services. [Azure Event](https://azure.microsoft.com/services/event-grid/)  [Grid](https://azure.microsoft.com/services/event-grid/) [c](https://azure.microsoft.com/services/event-grid/)an help by subscribing to events, like blobs being added and pushing an event to whoever is subscribed to it. And [Azure Event Hubs](https://azure.microsoft.com/services/event-hubs/) can ingest massive amounts of data, which you can process, filter, and store in your own time. Using messaging to communicate between services in Azure allows you to handle load smoothly while also preventing data loss in the event a service is unavailable.

# Media Services

Working with (streaming) media can be challenging. [Azure Media Services](https://azure.microsoft.com/en-us/services/media-services/) can help you by providing services like [encoding,](https://azure.microsoft.com/services/media-services/encoding/) which encodes your media files into the file formats and screen sizes they need to be. [Azure Content Protection](https://azure.microsoft.com/services/media-services/content-protection/) [e](https://azure.microsoft.com/services/media-services/content-protection/)nables you to use DRM technologies like [PlayReady](https://www.microsoft.com/playready/) [t](https://www.microsoft.com/playready/)o make sure that your content is only used by authorized users. With [live streaming](https://docs.microsoft.com/azure/media-services/media-services-manage-channels-overview) you can stream media worldwide at massive scale. And by using [Media Analytics](https://azure.microsoft.com/services/media-services/media-analytics/) [y](https://azure.microsoft.com/services/media-services/media-analytics/)ou can enhance media by doing intelligent things like creating subtitles for a movie based on speech.

# Monitoring

And finally, you need to monitor your applications that run in Azure, to make sure that they run smoothly. The monitoring tools in Azure fall under the umbrella of [Azure](https://docs.microsoft.com/azure/monitoring-and-diagnostics/monitoring-overview)  [Monitor.](https://docs.microsoft.com/azure/monitoring-and-diagnostics/monitoring-overview) There are services like [Azure Application Insights](https://azure.microsoft.com/services/application-insights/) that can help you to monitor every aspect of your application. There is also [Azure Log Analytics,](https://azure.microsoft.com/services/log-analytics/) which plugs into every [Azure Service](https://azure.microsoft.com/services/network-watcher/) to gather diagnostics information, and [Azure Network Watcher,](https://azure.microsoft.com/en-us/services/network-watcher/) which can inspect network traffic from your VMs and over your [Virtual Networks.](https://docs.microsoft.com/azure/virtual-network/virtual-networks-overview)

![](_page_25_Picture_0.jpeg)

![](_page_25_Picture_1.jpeg)

![](_page_25_Figure_2.jpeg)

[Visual Studio App Center](https://www.visualstudio.com/app-center/) provides logging and monitoring as part of a fully featured suite of tools for mobile applications. [Azure Security Center,](https://azure.microsoft.com/services/security-center/) which is your one-stopshop for all the security aspects of all your services in Azure. Your logs can be visualized using [Azure Dashboards](https://docs.microsoft.com/en-us/azure/azure-monitor/learn/tutorial-app-dashboards) or [Power BI](https://docs.microsoft.com/en-us/azure/azure-monitor/visualizations) and you can even trigger custom actions from log events using [Logic Apps.](https://docs.microsoft.com/en-us/azure/azure-monitor/app/automate-with-logic-apps)

![](_page_25_Picture_4.jpeg)

![](_page_26_Picture_0.jpeg)

# Tools for developing, debugging and troubleshooting

As .NET developers and architects, we are spoiled with the incredible tooling of Visual Studio. This extends into the world of Azure, which includes many tools that can make developing and troubleshooting in Azure easier and fun. Let's explore these tools.

# Visual Studio and Azure

We all love Visual Studio and Azure does too! If you run any version of Visual Studio 2019 or 2017 and [enable the Azure workload,](https://www.visualstudio.com/vs/support/selecting-workloads-visual-studio-2017/) you'll be able to seamlessly work with Azure. And if you can't upgrade, that's OK, we have you covered there, too. If you are using Visual Studio 2015, you can download the Visual [Studio 2015 Tools for Azure.](https://www.microsoft.com/web/handlers/webpi.ashx/getinstaller/VWDOrVs2015AzurePack.appids)

#### **Project templates**

Out of the box, you get lots of project templates to work with. You can create web applications for the cloud, [Azure Cloud Services applications,](https://azure.microsoft.com/services/cloud-services/) [Azure Functions,](https://docs.microsoft.com/azure/azure-functions/functions-overview) [Azure](https://docs.microsoft.com/azure/app-service/web-sites-create-web-jobs)  [WebJobs,](https://docs.microsoft.com/azure/app-service/web-sites-create-web-jobs) and much more.

![](_page_27_Picture_0.jpeg)

**Figure 2**: Azure project templates in Visual Studio 2019 with Azure workload installed

![](_page_27_Figure_2.jpeg)

# Cloud Explorer

As part of the Azure workload in Visual Studio, you get Cloud Explorer. You can use this to navigate through all your Azure subscriptions and resources and take action, as in Figure 3, where you can attach a debugger to an App Service Web App.

From Cloud Explorer, you can also do things like open an Azure SQL Database in the Visual Studio Server Explorer and upload files to Azure Storage.

You can even connect to services to see their streaming logs and change application settings and connection strings in App Service.

![](_page_27_Picture_7.jpeg)

[Get started by managing your Azure resources with Cloud Explorer.](https://docs.microsoft.com/azure/vs-azure-tools-resources-managing-with-cloud-explorer)

**Figure 3**: Cloud Explorer in Visual Studio

![](_page_28_Picture_2.jpeg)

# Publish to Azure

Once you have the Azure workload enabled in Visual Studio, you can easily publish to Azure from various project types. The publish wizard has an option to publish to [Azure](https://azure.microsoft.com/services/app-service/)  [App Service](https://azure.microsoft.com/services/app-service/) [\(](https://azure.microsoft.com/services/app-service/)for example, host a web site). Or you can directly publish to specific services like [Azure Cloud Services.](https://azure.microsoft.com/services/cloud-services/) All with a few clicks.

![](_page_28_Picture_5.jpeg)

[Get started by using the Visual Studio Publish Azure Application wizard.](https://docs.microsoft.com/azure/vs-azure-tools-publish-azure-application-wizard)

![](_page_29_Picture_1.jpeg)

![](_page_29_Figure_2.jpeg)

For a more repeatable process you can set up an Azure DevOps pipeline from inside Visual Studio 2019 which will build, test, and deploy your application to Azure. The Pipeline will be kicked off every time there is a check-in to your source control ensuring your application is always up to date.

![](_page_30_Picture_0.jpeg)

![](_page_30_Picture_1.jpeg)

![](_page_30_Picture_2.jpeg)

# Snapshot Debugger

The [Snapshot Debugger](https://blogs.msdn.microsoft.com/visualstudio/2017/12/06/snapshot-debugging-with-visual-studio-2017-now-ready-for-production/) allows you to debug your application while it is running live in production, without affecting its performance. This is great, because now you can debug production without pausing the app when you hit a breakpoint. Debugging provides a lot more information than diagnostic logs typically do.

![](_page_31_Picture_0.jpeg)

Note that you do need Visual Studio Enterprise to use the Snapshot Debugger. Here's how it works:

- 1. Attach the **snapshot debugger** to your application process in Azure.
- 2. Add a **snappoint** (different from a breakpoint).
- 3. When the **snappoint** is hit, a **snapshot** is taken.
  - The debugger quickly gathers all the information it needs about the call stack and variables and lets the app continue to run.
- 4. You can now view the **snapshot** and inspect everything that you normally would when debugging, without holding up the application.

![](_page_31_Picture_7.jpeg)

[Get started by debugging snapshots on exceptions in .NET apps.](https://docs.microsoft.com/azure/application-insights/app-insights-snapshot-debugger)

# Azure Storage Explorer

The [Azure Storage Explorer](https://azure.microsoft.com/features/storage-explorer/) [i](https://azure.microsoft.com/features/storage-explorer/)s a tool for managing your Azure Storage accounts. It's a free, standalone application from Microsoft that you can [download here.](https://azure.microsoft.com/features/storage-explorer/) You can use it to create new blob containers, upload files, query through [Table storage,](https://azure.microsoft.com/services/storage/tables/) and more. You can even use it to manage your [Cosmos DB storage](https://docs.microsoft.com/azure/cosmos-db/storage-explorer) and create databases and collections.

![](_page_31_Picture_11.jpeg)

[Get started with Storage Explorer.](https://docs.microsoft.com/azure/vs-azure-tools-storage-manage-with-storage-explorer)

**Figure 6**: Storage Explorer

![](_page_32_Figure_2.jpeg)

# Azure Storage Emulator

In the Visual Studio Azure workload or in the [Azure SDK,](https://azure.microsoft.com/downloads/) you'll find the [Azure storage](https://docs.microsoft.com/azure/storage/common/storage-use-emulator)  [emulator,](https://docs.microsoft.com/azure/storage/common/storage-use-emulator) which you can use to develop locally against Azure Storage. You can access it through Cloud Explorer just like you can access it in the Azure portal or through other tools such as [Storage Explorer.](https://docs.microsoft.com/azure/vs-azure-tools-storage-manage-with-storage-explorer)

The Azure storage emulator works the same as Azure Storage in the cloud, including how you authenticate to it. There are some obvious differences, like file size limitations and the lack of geo-redundant scaling. And the emulator doesn't support [Azure Files.](https://azure.microsoft.com/services/storage/files/)

Once you are done developing and testing locally, you can publish your application to the cloud and use Azure Storage there.

![](_page_32_Figure_7.jpeg)

[Get started by configuring and using the storage emulator](https://docs.microsoft.com/azure/vs-azure-tools-storage-emulator-using) [with Visual Studio.](https://docs.microsoft.com/azure/vs-azure-tools-storage-emulator-using)

# Azure Command-Line Interface

You can do everything you need to do in Azure from Visual Studio and the [Azure](https://portal.azure.com/)  [portal.](https://portal.azure.com/) But sometimes you want to run scripts to perform command-level operations, like when you are working with containers. You can do that using the [Azure Command-](https://docs.microsoft.com/cli/azure/)[Line Interface,](https://docs.microsoft.com/cli/azure/) or CLI. You can install the Azure CLI on your local development

![](_page_33_Picture_0.jpeg)

computer, use a pre-built Docker container, or use it from within the Azure portal, where it is a part of [Azure Cloud Shell.](https://azure.microsoft.com/features/cloud-shell/)

Using the CLI in the Azure portal through Cloud Shell is very easy. You don't have to install anything and you don't have to [log in to your Azure Subscription](https://docs.microsoft.com/cli/azure/authenticate-azure-cli) because you've already done that to get into the portal.

**Figure 7**: Azure Cloud Shell in the Azure portal

![](_page_33_Figure_4.jpeg)

Azure Cloud Shell supports Bash and PowerShell as scripting languages. These might not be things that you use daily as a .NET developer, but they are worth diving into because they are powerful tools.

Once you are in the CLI, you can do anything from listing all the Azure resources you have to provisioning new resources.

You can also access Cloud Shell directly in the browser at [https://shell.azure.com](https://shell.azure.com/) or via mobile devices such as iOS and Android.

# Azure Functions Core Tools

![](_page_34_Picture_1.jpeg)

[Azure Functions](https://azure.microsoft.com/services/functions/) run inside Azure App Service Function Apps and are powerful. You can use them to run small pieces of code that get triggered by outside sources and bind to things like [Azure Blob storage](https://azure.microsoft.com/services/storage/blobs/) [o](https://azure.microsoft.com/services/storage/blobs/)r [Azure Cosmos DB.](https://azure.microsoft.com/services/cosmos-db/)

The [Azure Functions Core Tools](https://docs.microsoft.com/azure/azure-functions/functions-run-local) enable you to develop Azure Functions locally. You can run the local version of Azure Functions runtime on your development computer.

With the Azure Functions Core Tools, you can develop and test your Azure Functions locally. And when you're done, you can publish them to Azure or use [continuous](https://docs.microsoft.com/azure/azure-functions/functions-continuous-deployment)  [integration and continuous delivery](https://docs.microsoft.com/azure/azure-functions/functions-continuous-deployment) to check your Azure Functions code and publish it automatically to Azure.

![](_page_34_Picture_5.jpeg)

[Get started by creating your first function using Visual Studio and](https://docs.microsoft.com/azure/azure-functions/functions-create-your-first-function-visual-studio) [test it locally.](https://docs.microsoft.com/azure/azure-functions/functions-create-your-first-function-visual-studio)

# Cosmos DB Emulator

When you are using [Azure Cosmos DB,](https://azure.microsoft.com/services/cosmos-db/) you can use the [Azure Cosmos DB Emulator](https://aka.ms/cosmosdb-emulator) to develop locally. The emulator acts just like Cosmos DB would and even provides the same interface as Cosmos DB does in the Azure portal.

**Figure 8:** Cosmos DB Emulator local interface

![](_page_34_Picture_10.jpeg)

![](_page_35_Picture_0.jpeg)

The Cosmos DB Emulator also shows up in the Cloud Explorer in Visual Studio, so that you can easily manage it from there.

By developing locally against the Cosmos DB emulator, you can develop without incurring costs from a Cosmos DB in Azure. And when you are ready, you can deploy your application to Azure and run it against Cosmos DB there, just by changing your connection string.

![](_page_35_Picture_3.jpeg)

[Get started by using the Azure Cosmos DB Emulator](https://docs.microsoft.com/azure/cosmos-db/local-emulator)  [for local development and testing.](https://docs.microsoft.com/azure/cosmos-db/local-emulator)

# Azure DevOps for build and deployment

Once you are working on your application, it is vital to integrate your work with the work of other developers (continuous integration).

It is vital to deploy that work to a central location, like an [Azure Web App,](https://azure.microsoft.com/services/app-service/web/) so that you can see that it works, and so that it can be tested and promoted through the different environments and can be deployed to production (continuous delivery).

To make this work, you need to automatically integrate everybody's work and deploy it. Ideally, you would do these things continuously, whenever somebody commits new work.

[Azure DevOps,](https://dev.azure.com/) can help with that. It is an application lifecycle management system that manages your work items and sprints, stores and manages your source code, builds your code, and deploys it to wherever you want. The best part is, it is very easy to set up.

You can put your source code in DevOps and manage it using the [TFS or Git](https://docs.microsoft.com/en-us/azure/devops/repos/tfvc/comparison-git-tfvc?view=azure-devops) protocols. Once you start committing changes, you can have those built by a simple build pipeline that executes something like a [Visual Studio build,](https://docs.microsoft.com/en-us/azure/devops/pipelines/tasks/build/visual-studio-build?view=azure-devops) just like you would on your local development computer. You can create such a pipeline by just adding tasks in the DevOps portal, like in Figure 9.

![](_page_36_Picture_0.jpeg)

![](_page_36_Picture_1.jpeg)

![](_page_36_Figure_2.jpeg)

You can set your build up to compile your code and run your unit tests every time somebody commits. This is continuous integration.

And once the build is done, it can kick off a release pipeline that deploys your code to environments including development, test, staging, and production. You can deploy your code to anywhere: to on-premises resources or to the cloud. You can even have [permissions gates](https://docs.microsoft.com/vsts/build-release/concepts/definitions/release/approvals/approvals) [t](https://docs.microsoft.com/vsts/build-release/concepts/definitions/release/approvals/approvals)hat require somebody like a product owner to approve the deployment to production, putting them in control.

You create a release pipeline in the same way as you create a build pipeline—by adding tasks in the Azure DevOps portal, like in Figure 10.

![](_page_37_Picture_0.jpeg)

![](_page_37_Picture_1.jpeg)

![](_page_37_Figure_2.jpeg)

Azure DevOps is a powerful tool that every .NET developer should have in their arsenal. Now you no longer have an excuse to not do continuous integration and continuous deployment.

![](_page_37_Figure_4.jpeg)

![](_page_37_Figure_5.jpeg)

![](_page_38_Picture_0.jpeg)

# Summary and how to get started for free

In this guide, we've introduced the power that Azure can bring to your applications. Using Azure, you can do incredible things with your applications—facial and speech recognition, manage your devices on the Internet of Things in the cloud, scale as much as you want, and pay for what you use.

You've seen that Azure is a great place for .NET developers and architects and it provides tools that have the same world-class quality and depth that you are used to working with today. The days of having to write complicated "plumbing" yourself are over. Now you can take advantage of a wealth of prebuilt solutions. Free yourself up to work on the things that matter, and let Azure take care of the solved problems.

# Keep learning with an Azure free account

Do you have a Visual Studio Subscription? [Activate your monthly Azure credit.](https://account.azure.com/signup?offer=Azure_MSDN&appId=102&correlationId=dc672587-208a-41ec-922e-0a7f3c96f357)

Sign up for an [Azure free account](https://azure.microsoft.com/free/dotnet) and receive:

- A \$200 credit to use on any Azure product for 30 days
- Free access to our most popular products for 12 months, including compute, storage, networking, and database
- More than 25 products that are always free, including Text Translator, Functions and Active Directory B2C

![](_page_38_Figure_10.jpeg)

[Download and install language-specific SDKs and tools](https://azure.microsoft.com/en-us/downloads/) at: <https://azure.microsoft.com/downloads/>

![](_page_38_Picture_12.jpeg)

![](_page_39_Picture_0.jpeg)

# About the team

Cesar, Michael, Beth and Barry are passionate about Microsoft Azure and would encourage you to reach out to them on Twitter for questions regarding this book.

![](_page_39_Picture_3.jpeg)

Cesar de la Torre works for Microsoft Corp in Redmond, Seattle, in the .NET product team, focusing on .NET, Azure, Containers & Microservice-based architectures and creating [.NET Application Architecture guidance.](https://www.microsoft.com/net/learn/architecture)

You can reach him on Twitter @cesardelatorre or by following his blog at [https://blogs.msdn.microsoft.com/cesardelatorre/.](https://blogs.msdn.microsoft.com/cesardelatorre/)

![](_page_39_Picture_6.jpeg)

Michael Crump works at Microsoft on the Azure platform and is a coder, blogger, and international speaker on various cloud development topics. He's passionate about helping developers understand the benefits of the cloud in a no-nonsense way.

You can reach him on Twitter [@mbcrump](http://twitter.com/mbcrump) [o](http://twitter.com/mbcrump)r by following his blog at [https://www.michaelcrump.net.](https://www.michaelcrump.net/)

![](_page_39_Picture_9.jpeg)

Barry Luijbregts is an independent architect and software developer focused on preparing business applications and solutions for the cloud. A Microsoft Azure MVP, Barry is a skilled educator and active member of the community providing Pluralsight cloud and developer-focused courses and on-site private training sessions for corporate groups. He records podcasts, founded an active .NET User

Group, and leads technology bootcamps. Barry has a lifelong passion for technology and for IT in particular. Technology drives his curiosity as he stays current and gains unique access to new technology through Microsoft early adoption programs. Understanding that software is an investment, Barry uses his knowledge of cloud direction to advise clients on forward-looking and sustainable long-term solutions. You can reach Barry on Twitter [@AzureBarry](https://twitter.com/AzureBarry) [a](https://twitter.com/AzureBarry)nd through his website at [https://www.azurebarry.com.](https://www.azurebarry.com/)

![](_page_39_Picture_12.jpeg)

Beth Massi is the Product Marketing Manager for the .NET Platform and Languages at Microsoft. She's a long-time community champion for .NET developers and on the Board of Directors for the .NET Foundation. You can reach her on Twitter [@BethMassi.](https://twitter.com/bethmassi)