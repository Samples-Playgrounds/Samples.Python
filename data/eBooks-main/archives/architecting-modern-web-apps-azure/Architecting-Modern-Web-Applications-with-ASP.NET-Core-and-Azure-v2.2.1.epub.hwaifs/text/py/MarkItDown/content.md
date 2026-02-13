**Title:** Architecting Modern Web Apps with ASP.NET Core 2 and Azure
**Authors:** Steve "ardalis" Smith
**Language:** en
**Publisher:** Microsoft Corporation
**Date:** 0101-01-01T00:00:00+00:00
**Identifier:** 573427a1-ad4c-4ac5-a462-9b5b8c81905b

EDITION v2.2

DOWNLOAD available at: <https://aka.ms/webappebook>

PUBLISHED BY

DevDiv, .NET and Visual Studio product teams

A division of Microsoft Corporation

One Microsoft Way

Redmond, Washington 98052-6399

Copyright © 2019 by Microsoft Corporation

All rights reserved. No part of the contents of this book may be reproduced or transmitted in any form or by any means without the written permission of the publisher.

This book is provided “as-is” and expresses the author’s views and opinions. The views, opinions and information expressed in this book, including URL and other Internet website references, may change without notice.

Some examples depicted herein are provided for illustration only and are fictitious. No real association or connection is intended or should be inferred.

Microsoft and the trademarks listed at http://www.microsoft.com on the “Trademarks” webpage are trademarks of the Microsoft group of companies. All other marks are property of their respective owners.

Author:

Steve Smith (<http://ardalis.com>)

Editor:

Maira Wenzel

Participants and reviewers:

Scott Hanselman, .NET product team, Microsoft

Cesar de la Torre, .NET product team, Microsoft

Contents

**Introduction****1**

Version      1

Purpose      2

Who should use this guide      2

How you can use this guide      2

**Characteristics of Modern Web Applications****3**

Summary      3

Reference Application: eShopOnWeb      3

Cloud-Hosted and Scalable      4

Cross Platform      4

Modular and Loosely Coupled      5

Easily Tested with Automated Tests      5

Traditional and SPA Behaviors Supported      5

Simple Development and Deployment      6

Traditional ASP.NET and Web Forms      6

**Choosing Between Traditional Web Apps and Single Page Apps (SPAs)****7**

Summary      7

Razor Components      8

Project Templates      8

When to choose traditional web apps      11

When to choose SPAs      12

Decision table – Traditional Web or SPA      13

**Architectural Principles****14**

Summary      14

Common design principles      14

Separation of Concerns      14

Encapsulation      15

Dependency Inversion      15

Explicit Dependencies      17

Single Responsibility      17

Don’t Repeat Yourself (DRY)      18

Persistence Ignorance      19

Bounded Contexts      20

**Common Web Application Architectures****21**

Summary      21

What is a monolithic application?      21

All-in-One applications      21

What are layers?      22

Traditional “N-Layer” architecture applications      24

Clean architecture      28

Monolithic Applications and Containers      34

Monolithic application deployed as a container      36

Docker support      38

**Common Client-Side Web Technologies****40**

Summary      40

HTML      40

CSS      41

JavaScript      42

Legacy Web Apps with jQuery      42

jQuery vs a SPA Framework      42

Angular SPAs      43

React      44

Choosing a SPA Framework      44

**Developing ASP.NET Core Apps****46**

Summary      46

MVC and Razor Pages      46

Why Razor Pages?      47

When to use MVC      48

Mapping Requests to Responses      48

Working with Dependencies      51

Declare Your Dependencies      52

Structuring the Application      53

Feature Organization      54

Cross-Cutting Concerns      56

Security      59

Authentication      59

Authorization      61

Client Communication      64

Domain-Driven Design – Should You Apply It?      65

When Should You Apply DDD      66

When Shouldn’t You Apply DDD      66

Deployment      67

**Working with Data in ASP.NET Core Apps****69**

Summary      69

Entity Framework Core (for relational databases)      69

The DbContext      70

Configuring EF Core      70

Fetching and Storing Data      72

Fetching Related Data      73

Encapsulating Data      74

Resilient Connections      75

EF Core or micro-ORM?      77

SQL or NoSQL      79

Azure Cosmos DB      80

Other Persistence Options      81

Caching      81

ASP.NET Core Response Caching      81

Data Caching      82

**Testing ASP.NET Core MVC Apps****86**

Summary      86

Kinds of Automated Tests      86

Unit Tests      86

Integration Tests      87

Functional Tests      88

Testing Pyramid      89

What to Test      90

Organizing Test Projects      90

Test Naming      92

Unit Testing ASP.NET Core Apps      93

Integration Testing ASP.NET Core Apps      95

Functional Testing ASP.NET Core Apps      95

**Development process for Azure-hosted ASP.NET Core applications****99**

Vision      99

Development environment for ASP.NET Core apps      99

Development tools choices: IDE or editor      99

Development workflow for Azure-hosted ASP.NET Core apps      100

Initial Setup      100

Workflow for developing Azure-hosted ASP.NET Core applications      102

References      103

**Azure Hosting Recommendations for ASP.NET Core Web Apps****104**

Summary      104

Web Applications      104

App Service Web Apps      105

Azure Container Instances      110

Azure Virtual Machines      111

Logical Processes      112

Data      112

Architecture Recommendations      112

Introduction

.NET Core and ASP.NET Core offer several advantages over traditional .NET development. You should use .NET Core for your server applications if some or all of the following are important to your application’s success:

* Cross-platform support
* Use of microservices
* Use of Docker containers
* High performance and scalability requirements
* Side-by-side versioning of .NET versions by application on the same server

Traditional .NET applications can and do support many of these requirements, but ASP.NET Core and .NET Core have been optimized to offer improved support for the above scenarios.

More and more organizations are choosing to host their web applications in the cloud using services like Microsoft Azure. You should consider hosting your application in the cloud if the following are important to your application or organization:

* Reduced investment in data center costs (hardware, software, space, utilities, server management, etc.)
* Flexible pricing (pay based on usage, not for idle capacity)
* Extreme reliability
* Improved app mobility; easily change where and how your app is deployed
* Flexible capacity; scale up or down based on actual needs

Building web applications with ASP.NET Core, hosted in Azure, offers many competitive advantages over traditional alternatives. ASP.NET Core is optimized for modern web application development practices and cloud hosting scenarios. In this guide, you’ll learn how to architect your ASP.NET Core applications to best take advantage of these capabilities.

## Version

This eBook has been revised to cover version 2.2 of ASP.NET Core and .NET Core.

# Purpose

This guide provides end-to-end guidance on building *monolithic* web applications using ASP.NET Core and Azure. In this context, “monolithic” refers to the fact that these applications are deployed as a single unit, not as a collection of interacting services and applications.

![Image](images/image3.tiff)This guide is complementary to the “.NET Microservices: Architecture for Containerized .NET Applications” eBook which focuses more on Docker, Microservices, and Deployment of Containers to host enterprise applications.

## Who should use this guide

The audience for this guide is mainly developers, development leads, and architects who are interested in building modern web applications using Microsoft technologies and services in the cloud.

A secondary audience is technical decision makers who are already familiar ASP.NET and/or Azure and are looking for information on whether it makes sense to upgrade to ASP.NET Core for new or existing projects.

## How you can use this guide

This guide has been condensed into a relatively small document that focuses on building web applications with modern .NET technologies and Windows Azure. As such, it can be read in its entirety to provide a foundation of understanding such applications and their technical considerations. The guide, along with its sample application, can also serve as a starting point or reference. Use the associated sample application as a template for your own applications, or to see how you might organize your application’s component parts. Refer back to the guide’s principles and coverage of architecture and technology options and decision considerations when you’re weighing these choices for your own application.

![A screenshot of a cell phone  Description automatically generated](images/image4.tiff)Feel free to forward this guide to your team to help ensure a common understanding of these considerations and opportunities. Having everybody working from a common set of terminology and underlying principles helps ensure consistent application of architectural patterns and practices.

Characteristics of Modern Web Applications

“… with proper design, the features come cheaply. This approach is arduous, but continues to succeed.”

Dennis Ritchie

# Summary

Modern web applications have higher user expectations and greater demands than ever before. Today’s web apps are expected to be available 24/7 from anywhere in the world, and usable from virtually any device or screen size. Web applications must be secure, flexible, and scalable to meet spikes in demand. Increasingly, complex scenarios should be handled by rich user experiences built on the client using JavaScript and communicating efficiently through web APIs.

ASP.NET Core is optimized for modern web applications and cloud-based hosting scenarios. Its modular design enables applications to depend on only those features they actually use, improving application security and performance while reducing hosting resource requirements.

# Reference Application: eShopOnWeb

This guidance includes a reference application, *eShopOnWeb*, which demonstrates some of the principles and recommendations. The application is a simple online store which supports browsing through a catalog of shirts, coffee mugs, and other marketing items. The reference application is deliberately simple in order to make it easy to understand.

![Image](images/image5.png)

**Figure 2-1.** eShopOnWeb

![A screenshot of a social media post  Description automatically generated](images/image6.tiff)

# Cloud-Hosted and Scalable

ASP.NET Core is optimized for the cloud (public cloud, private cloud, any cloud) because it is low-memory and high-throughput. The smaller footprint of ASP.NET Core applications means you can host more of them on the same hardware, and you pay for fewer resources when using pay-as-you go cloud hosting services. The higher-throughput means you can serve more customers from an application given the same hardware, further reducing the need to invest in servers and hosting infrastructure.

# Cross Platform

ASP.NET Core is cross-platform and can run on Linux, macOS, and Windows. This opens up many new options for both development and deployment of apps built with ASP.NET Core. Docker containers - both Linux and Windows - can host ASP.NET Core applications, allowing them to take advantage of the benefits of [containers and microservices](https://aka.ms/microservicesebook).

# Modular and Loosely Coupled

NuGet packages are first-class citizens in .NET Core, and ASP.NET Core apps are composed of many libraries through NuGet. This granularity of functionality helps ensure apps only depend on and deploy functionality they actually require, reducing their footprint and security vulnerability surface area.

ASP.NET Core also fully supports [dependency injection](https://deviq.com/dependency-injection/), both internally and at the application level. Interfaces can have multiple implementations that can be swapped out as needed. Dependency injection allows apps to loosely couple to those interfaces, rather than specific implementations, making them easier to extend, maintain, and test.

# Easily Tested with Automated Tests

ASP.NET Core applications support unit testing, and their loose coupling and support for dependency injection makes it easy to swap infrastructure concerns with fake implementations for test purposes. ASP.NET Core also ships a TestServer that can be used to host apps in memory. Functional tests can then make requests to this in-memory server, exercising the full application stack (including middleware, routing, model binding, filters, etc.) and receiving a response, all in a fraction of the time it would take to host the app on a real server and make requests through the network layer. These tests are especially easy to write, and valuable, for APIs, which are increasingly important in modern web applications.

# Traditional and SPA Behaviors Supported

Traditional web applications have involved little client-side behavior, but instead have relied on the server for all navigation, queries, and updates the app might need to make. Each new operation made by the user would be translated into a new web request, with the result being a full page reload in the end user’s browser. Classic Model-View-Controller (MVC) frameworks typically follow this approach, with each new request corresponding to a different controller action, which in turn would work with a model and return a view. Some individual operations on a given page might be enhanced with AJAX (Asynchronous JavaScript and XML) functionality, but the overall architecture of the app used many different MVC views and URL endpoints. In addition, ASP.NET Core MVC also supports Razor Pages, a simpler way to organize MVC-style pages.

Single Page Applications (SPAs), by contrast, involve very few dynamically generated server-side page loads (if any). Many SPAs are initialized within a static HTML file that loads the necessary JavaScript libraries to start and run the app. These apps make heavy usage of web APIs for their data needs and can provide much richer user experiences.

Many web applications involve a combination of traditional web application behavior (typically for content) and SPAs (for interactivity). ASP.NET Core supports both MVC (View or Page based) and Web APIs in the same application, using the same set of tools and underlying framework libraries.

# Simple Development and Deployment

ASP.NET Core applications can be written using simple text editors and command line interfaces, or full-featured development environments like Visual Studio. Monolithic applications are typically deployed to a single endpoint. Deployments can easily be automated to occur as part of a continuous integration (CI) and continuous delivery (CD) pipeline. In addition to traditional CI/CD tools, Windows Azure has integrated support for Git repositories and can automatically deploy updates as they are made to a specified Git branch or tag.

# Traditional ASP.NET and Web Forms

In addition to ASP.NET Core, traditional ASP.NET 4.x continues to be a robust and reliable platform for building web applications. ASP.NET supports MVC and Web API development models, as well as Web Forms, which is well-suited to page-based application development and features a rich third-party component ecosystem. Windows Azure has great longstanding support for ASP.NET 4.x applications, and many developers are familiar with this platform.

![Image](images/image7.tiff)

Choosing Between Traditional Web Apps and Single Page Apps (SPAs)

“Atwood’s Law: Any application that can be written in JavaScript, will eventually be written in JavaScript.”

Jeff Atwood

# Summary

There are two general approaches to building web applications today: traditional web applications that perform most of the application logic on the server, and single page applications (SPAs) that perform most of the user interface logic in a web browser, communicating with the web server primarily using web APIs. A hybrid approach is also possible, the simplest being the host one or more rich SPA-like sub-applications within a larger traditional web application.

You should use traditional web applications when:

* Your application’s client-side requirements are simple or even read-only.
* Your application needs to function in browsers without JavaScript support.
* Your team is unfamiliar with JavaScript or TypeScript development techniques.

You should use a SPA when:

* Your application must expose a rich user interface with many features.
* Your team is familiar with JavaScript and/or TypeScript development.
* Your application must already expose an API for other (internal or public) clients.

Additionally, SPA frameworks require greater architectural and security expertise. They experience greater churn due to frequent updates and new frameworks than traditional web applications. Configuring automated build and deployment processes and utilizing deployment options like containers are more difficult with SPA applications than traditional web apps.

Improvements in user experience made possible by the SPA model must be weighed against these considerations.

## Razor Components

ASP.NET Core 3.0 introduces a new model for building rich, interactive, and composable UI called Razor Components. Razor Components allow developers to build UI with Razor on the server and for this code to be delivered to the browser and executed client-side using a JavaScript library called WebAssembly. ASP.NET Core 3.0 is still under development, but you should expect to see more on this technology in the 3.0 update to this eBook. [Learn more about Razor Components (code-named Blazor).](https://blazor.net/docs/get-started.html)

## Project Templates

ASP.NET Core (2.0+) ships several web application templates that are available from Visual Studio or the dotnet CLI which can be used to get started building traditional or SPA-style applications. These are just a few of the templates that are shipped and these are just starting points. You may find useful 3rd party and open source templates or create your own:

* ASP.NET Core Web App (Razor Pages)
* ASP.NET Core Web App (Model-View-Controller)
* ASP.NET Core Web API (no UI)
* ASP.NET Core with Angular (SPA)
* ASP.NET Core with React.js (SPA)
* ASP.NET Core with React.js and Redux (SPA)

The recommended approach for many traditional applications is Razor Pages, which offer the same architectural advantages of ASP.NET Core MVC, but with fewer files and folders. You can also choose the MVC template, which will be very familiar to developers with experience using ASP.NET MVC or ASP.NET Core MVC 1.x. If you don’t require any server-side rendering of pages or views, you can use the Web API template, and create your application using static files that use JavaScript to call your API methods. The eShopOnWeb sample application includes two web projects, demonstrating both MVC and Razor Pages approaches to organizing the UI project. It’s important to point out that Razor Pages is a page-based model that builds on *top* of the MVC Model. You can add more Pages OR more Controllers for either HTML or Web APIs and mix and match as you like.

You’ll find built-in templates for Angular as well as React and Redux to help you get started building a SPA. These templates set up the necessary files and client-side build tools to allow you to get started quickly. These templates use npm (node package manager) to install their client-side dependencies.

![Image](images/image8.png)

**Figure 3-1.** Installing the Angular project template from dotnet CLI.

Make sure you have the latest version of nodejs installed, then build and run the app (dotnet run from the command prompt).

![Image](images/image9.png)

**Figure 3-2.** Running the Angular project template from dotnet CLI.

The angular template provides a simple SPA that includes navigation and routing and examples of implementing client-side and server-side behavior.

![Image](images/image10.png)

**Figure 3-3.** The Angular SPA in the browser.

# When to choose traditional web apps

The following is a more detailed explanation of the previously stated reasons for picking traditional web applications.

Your application has simple, possibly read-only, client-side requirements

Many web applications are primarily consumed in a read-only fashion by the vast majority of their users. Read-only (or read-mostly) applications tend to be much simpler than those that maintain and manipulate a great deal of state. For example, a search engine might consist of a single entry point with a textbox and a second page for displaying search results. Anonymous users can easily make requests, and there is little need for client-side logic. Likewise, a blog or content management system’s public-facing application usually consists mainly of content with little client-side behavior. Such applications are easily built as traditional server-based web applications which perform logic on the web server and render HTML to be displayed in the browser. The fact that each unique page of the site has its own URL that can be bookmarked and indexed by search engines (by default, without having to add this as a separate feature of the application) is also a clear benefit in such scenarios.

Your application needs to function in browsers without JavaScript support

Web applications that need to function in browsers with limited or no JavaScript support should be written using traditional web app workflows (or at least be able to fall back to such behavior). SPAs require client-side JavaScript in order to function; if it’s not available, SPAs are not a good choice.

Your team is unfamiliar with JavaScript or TypeScript development techniques

If your team is unfamiliar with JavaScript or TypeScript but is familiar with server-side web application development, then they will probably be able to deliver a traditional web app more quickly than a SPA. Unless learning to program SPAs is a goal, or the user experience afforded by a SPA is required, traditional web apps are a more productive choice for teams who are already familiar with building them.

# When to choose SPAs

The following is a more detailed explanation of when to choose a Single Page Applications style of development for your web app.

Your application must expose a rich user interface with many features

SPAs can support rich client-side functionality that doesn’t require reloading the page as users take actions or navigate between areas of the app. SPAs can load more quickly, fetching data in the background, and individual user actions are more responsive since full page reloads are rare. SPAs can support incremental updates, saving partially completed forms or documents without the user having to click a button to submit a form. SPAs can support rich client-side behaviors, such as drag-and-drop, much more readily than traditional applications. SPAs can be designed to run in a disconnected mode, making updates to a client-side model that are eventually synchronized back to the server once a connection is re-established. You should choose a SPA style application if your app’s requirements include rich functionality that goes beyond what typical HTML forms offer.

Note that frequently SPAs need to implement features that are built-in to traditional web apps, such as displaying a meaningful URL in the address bar reflecting the current operation (and allowing users to bookmark or deep link to this URL to return to it). SPAs also should allow users to use the browser’s back and forward buttons with results that won’t surprise them.

Your team is familiar with JavaScript and/or TypeScript development

![Image](images/image11.tiff)Writing SPAs requires familiarity with JavaScript and/or TypeScript and client-side programming techniques and libraries. Your team should be competent in writing modern JavaScript using a SPA framework like Angular.

Your application must already expose an API for other (internal or public) clients

If you’re already supporting a web API for use by other clients, it may require less effort to create a SPA implementation that leverages these APIs rather than reproducing the logic in server-side form. SPAs make extensive use of web APIs to query and update data as users interact with the application.

# Decision table – Traditional Web or SPA

![Image](images/image12.tiff)The following decision table summarizes some of the basic factors to consider when choosing between a traditional web application and a SPA.

Architectural Principles

“If builders built buildings the way programmers wrote programs, then the first woodpecker that came along would destroy civilization.”

Gerald Weinberg

# Summary

You should architect and design software solutions with maintainability in mind. The principles outlined in this section can help guide you toward architectural decisions that will result in clean, maintainable applications. Generally, these principles will guide you toward building applications out of discrete components that are not tightly coupled to other parts of your application, but rather communicate through explicit interfaces or messaging systems.

# Common design principles

## Separation of Concerns

A guiding principle when developing is **Separation of Concerns**. This principle asserts that software should be separated based on the kinds of work it performs. For instance, consider an application that includes logic for identifying noteworthy items to display to the user, and which formats such items in a particular way to make them more noticeable. The behavior responsible for choosing which items to format should be kept separate from the behavior responsible for formatting the items, since these are separate concerns that are only coincidentally related to one another.

Architecturally, applications can be logically built to follow this principle by separating core business behavior from infrastructure and user interface logic. Ideally, business rules and logic should reside in a separate project, which should not depend on other projects in the application. This helps ensure that the business model is easy to test and can evolve without being tightly coupled to low-level implementation details. Separation of concerns is a key consideration behind the use of layers in application architectures.

## Encapsulation

Different parts of an application should use **encapsulation** to insulate them from other parts of the application. Application components and layers should be able to adjust their internal implementation without breaking their collaborators as long as external contracts are not violated. Proper use of encapsulation helps achieve loose coupling and modularity in application designs, since objects and packages can be replaced with alternative implementations so long as the same interface is maintained.

In classes, encapsulation is achieved by limiting outside access to the class’s internal state. If an outside actor wants to manipulate the state of the object, it should do so through a well-defined function (or property setter), rather than having direct access to the private state of the object. Likewise, application components and applications themselves should expose well-defined interfaces for their collaborators to use, rather than allowing their state to be modified directly. This frees the application’s internal design to evolve over time without worrying that doing so will break collaborators, so long as the public contracts are maintained.

## Dependency Inversion

The direction of dependency within the application should be in the direction of abstraction, not implementation details. Most applications are written such that compile-time dependency flows in the direction of runtime execution. This produces a direct dependency graph. That is, if module A calls a function in module B, which calls a function in module C, then at compile time A will depend on B which will depend on C, as shown in Figure 4-1.

![Image](images/image13.png)

Figure 4-1. *Direct dependency graph. Control flow mirrors references.*

Applying the dependency inversion principle allows A to call methods on an abstraction that B implements, making it possible for A to call B at run time, but for B to depend on an interface controlled by A at compile time (thus, *inverting* the typical compile-time dependency). At runtime, the flow of program execution remains unchanged, but the introduction of interfaces means that different implementations of these interfaces can easily be plugged in. Figure 4-2 demonstrates this design.

![image4-2.png](images/image.png)

Figure 4-2. *Inverted dependency graph.*

Dependency inversion is a key part of building loosely-coupled applications, since implementation details can be written to depend on and implement higher level abstractions, rather than the other way around. The resulting applications are more testable, modular, and maintainable as a result. The practice of *dependency injection* is made possible by following the dependency inversion principle.

## Explicit Dependencies

**Methods and classes should explicitly require any collaborating objects they need in order to function correctly.** Class constructors provide an opportunity for classes to identify the things they need in order to be in a valid state and to function properly. If you define classes that can be constructed and called, but which will only function properly if certain global or infrastructure components are in place, these classes are being *dishonest* with their clients. The constructor contract is telling the client that it only needs the things specified (possibly nothing if the class is just using a default constructor), but then at runtime it turns out the object really did need something else.

By following the explicit dependencies principle, your classes and methods are being honest with their clients about what they need in order to function. This makes your code more self-documenting and your coding contracts more user-friendly, since users will come to trust that as long as they provide what’s required in the form of method or constructor parameters, the objects they’re working with will behave correctly at run time.

## Single Responsibility

The single responsibility principle applies to object-oriented design but can also be considered as an architectural principle similar to separation of concerns. It states that objects should have only one responsibility and that they should have only one reason to change. Specifically, the only situation in which the object should change is if the manner in which it performs its one responsibility must be updated. Following this principle helps to produce more loosely-coupled and modular systems, since many kinds of new behavior can be implemented as new classes, rather than by adding additional responsibility to existing classes. Adding new classes is always safer than changing existing classes, since no code yet depends on the new classes.

In a monolithic application, we can apply the single responsibility principle at a high level to the layers in the application. Presentation responsibility should remain in the UI project, while data access responsibility should be kept within an infrastructure project. Business logic should be kept in the application core project, where it can be easily tested and can evolve independently from other responsibilities.

When this principle is applied to application architecture, and taken to its logical endpoint, you get microservices. A given microservice should have a single responsibility. If you need to extend the behavior of a system, it’s usually better to do it by adding additional microservices, rather than by adding responsibility to an existing one.

[Learn more about microservices architecture](http://aka.ms/MicroservicesEbook)

## Don’t Repeat Yourself (DRY)

The application should avoid specifying behavior related to a particular concept in multiple places as this is a frequent source of errors. At some point, a change in requirements will require changing this behavior and the likelihood that at least one instance of the behavior will fail to be updated will result in inconsistent behavior of the system.

Rather than duplicating logic, encapsulate it in a programming construct. Make this construct the single authority over this behavior and have any other part of the application that requires this behavior use the new construct.

**Note:** Avoid binding together behavior that is only coincidentally repetitive. For example, just because two different constants both have the same value, that doesn’t mean you should have only one constant, if conceptually they’re referring to different things.

## Persistence Ignorance

**Persistence ignorance** (PI) refers to types that need to be persisted, but whose code is unaffected by the choice of persistence technology. Such types in .NET are sometimes referred to as Plain Old CLR Objects (POCOs), because they do not need to inherit from a particular base class or implement a particular interface. Persistence ignorance is valuable because it allows the same business model to be persisted in multiple ways, offering additional flexibility to the application. Persistence choices might change over time, from one database technology to another, or additional forms of persistence might be required in addition to whatever the application started with (for example, using a Redis cache or Azure Cosmos DB in addition to a relational database).

Some examples of violations of this principle include:

* A required base class
* A required interface implementation
* Classes responsible for saving themselves (such as the Active Record pattern)
* Required default constructor
* Properties requiring virtual keyword
* Properties forced to use certain types (for example, collection properties must expose ICollection, not just IEnumerable)
* Persistence-specific required attributes

The requirement that classes have any of the above features or behaviors adds coupling between the types to be persisted and the choice of persistence technology, making it more difficult to adopt new data access strategies in the future.

## Bounded Contexts

**Bounded contexts** are a central pattern in Domain-Driven Design. They provide a way of tackling complexity in large applications or organizations by breaking it up into separate conceptual modules. Each conceptual module then represents a context which is separated from other contexts (hence, bounded), and can evolve independently. Each bounded context should ideally be free to choose its own names for concepts within it and should have exclusive access to its own persistence store.

![Image](images/image15.tiff)At a minimum, individual web applications should strive to be their own bounded context, with their own persistence store for their business model, rather than sharing a database with other applications. Communication between bounded contexts occurs through programmatic interfaces, rather than through a shared database, which allows for business logic and events to take place in response to changes that take place. Bounded contexts map closely to microservices, which also are ideally implemented as their own individual bounded contexts.

Separation of Concerns

[https://deviq.com/separation-of-concerns/](http://deviq.com/separation-of-concerns/)

Encapsulation

[https://deviq.com/encapsulation/](http://deviq.com/encapsulation/)

Dependency Inversion Principle

[https://deviq.com/dependency-inversion-principle/](http://deviq.com/dependency-inversion-principle/)

Explicit Dependencies Principle

[https://deviq.com/explicit-dependencies-principle/](http://deviq.com/explicit-dependencies-principle/)

Don’t Repeat Yourself

[https://deviq.com/don-t-repeat-yourself/](http://deviq.com/don-t-repeat-yourself/)

Persistence Ignorance

[https://deviq.com/persistence-ignorance/](http://deviq.com/persistence-ignorance/)

Bounded Context

<https://martinfowler.com/bliki/BoundedContext.html>

Domain-Driven Design Fundamentals

https://www.pluralsight.com/courses/domain-driven-design-fundamentals

SOLID Principles of Object Oriented Design

https://www.pluralsight.com/courses/principles-oo-design

Common Web Application Architectures

“If you think good architecture is expensive, try bad architecture.”

Brian Foote and Joseph Yoder

# Summary

Most traditional .NET applications are deployed as single units corresponding to an executable or a single web application running within a single IIS appdomain. This is the simplest deployment model and serves many internal and smaller public applications very well. However, even given this single unit of deployment, most non-trivial business applications benefit from some logical separation into several layers.

# What is a monolithic application?

A monolithic application is one that is entirely self-contained, in terms of its behavior. It may interact with other services or data stores in the course of performing its operations, but the core of its behavior runs within its own process and the entire application is typically deployed as a single unit. If such an application needs to scale horizontally, typically the entire application is duplicated across multiple servers or virtual machines.

# All-in-One applications

The smallest possible number of projects for an application architecture is one. In this architecture, the entire logic of the application is contained in a single project, compiled to a single assembly, and deployed as a single unit.

A new ASP.NET Core project, whether created in Visual Studio or from the command line, starts out as a simple “all-in-one” monolith. It contains all of the behavior of the application, including presentation, business, and data access logic. Figure 5-1 shows the file structure of a single-project app.

![Image](images/image16.png)

**Figure 5-1.** A single project ASP.NET Core app

In a single project scenario, separation of concerns is achieved through the use of folders. The default template includes separate folders for MVC pattern responsibilities of Models, Views, and Controllers, as well as additional folders for Data and Services. In this arrangement, presentation details should be limited as much as possible to the Views folder, and data access implementation details should be limited to classes kept in the Data folder. Business logic should reside in services and classes within the Models folder.

Although simple, the single-project monolithic solution has some disadvantages. As the project’s size and complexity grows, the number of files and folders will continue to grow as well. User Interface (UI) concerns (models, views, controllers) reside in multiple folders, which are not grouped together alphabetically. This issue only gets worse when additional UI-level constructs, such as Filters or ModelBinders, are added in their own folders. Business logic is scattered between the Models and Services folders, and there’s no clear indication of which classes in which folders should depend on which others. This lack of organization at the project level frequently leads to [spaghetti code](http://deviq.com/spaghetti-code/).

To address these issues, applications often evolve into multi-project solutions, where each project is considered to reside in a particular *layer* of the application.

# What are layers?

As applications grow in complexity, one way to manage that complexity is to break the application up according to its responsibilities or concerns. This follows the separation of concerns principle and can help keep a growing codebase organized so that developers can easily find where certain functionality is implemented. Layered architecture offers a number of advantages beyond just code organization, though.

By organizing code into layers, common low-level functionality can be reused throughout the application. This reuse is beneficial because it means less code needs to be written and because it can allow the application to standardize on a single implementation, following the [Don’t Repeat Yourself principle](https://deviq.com/don-t-repeat-yourself/).

With a layered architecture, applications can enforce restrictions on which layers can communicate with other layers. This helps to achieve encapsulation. When a layer is changed or replaced, only those layers that work with it should be impacted. By limiting which layers depend on which other layers, the impact of changes can be mitigated so that a single change doesn’t impact the entire application.

Layers (and encapsulation) make it much easier to replace functionality within the application. For example, an application might initially use its own SQL Server database for persistence, but later could choose to use a cloud-based persistence strategy, or one behind a web API. If the application has properly encapsulated its persistence implementation within a logical layer, that SQL Server specific layer could be replaced by a new one implementing the same public interface.

In addition to the potential of swapping out implementations in response to future changes in requirements, application layers can also make it easier to swap out implementations for testing purposes. Instead of having to write tests that operate against the real data layer or UI layer of the application, these layers can be replaced at test time with fake implementations that provide known responses to requests. This typically makes tests much easier to write and much faster to run when compared to running tests again the application’s real infrastructure.

Logical layering is a common technique for improving the organization of code in enterprise software applications, and there are several ways in which code can be organized into layers.

**Note:** *Layers* represent logical separation within the application. In the event that application logic is physically distributed to separate servers or processes, these separate physical deployment targets are referred to as *tiers*. It’s possible, and quite common, to have an N-Layer application that is deployed to a single tier.

# Traditional “N-Layer” architecture applications

The most common organization of application logic into layers is shown in Figure 5-2.

![Image](images/image17.png) **Figure 5-2.** Typical application layers.

These layers are frequently abbreviated as UI, BLL (Business Logic Layer), and DAL (Data Access Layer). Using this architecture, users make requests through the UI layer, which interacts only with the BLL. The BLL, in turn, can call the DAL for data access requests. The UI layer shouldn’t make any requests to the DAL directly, nor should it interact with persistence directly through other means. Likewise, the BLL should only interact with persistence by going through the DAL. In this way, each layer has its own well-known responsibility.

One disadvantage of this traditional layering approach is that compile-time dependencies run from the top to the bottom. That is, the UI layer depends on the BLL, which depends on the DAL. This means that the BLL, which usually holds the most important logic in the application, is dependent on data access implementation details (and often on the existence of a database). Testing business logic in such an architecture is often difficult, requiring a test database. The dependency inversion principle can be used to address this issue, as you’ll see in the next section.

Figure 5-3 shows an example solution, breaking the application into three projects by responsibility (or layer).

![Image](images/image18.png) Figure 5-3. A simple monolithic application with three projects.

Although this application uses several projects for organizational purposes, it is still deployed as a single unit and its clients will interact with it as a single web app. This allows for very simple deployment process. Figure 5-4 shows how such an app might be hosted using Azure.

![https://camo.githubusercontent.com/0a28487424adffaad267906742fe50021a39c2cb/68747470733a2f2f77686974657061706572736865616c74682e626c6f622e636f72652e77696e646f77732e6e65742f617070736572766963652f696d616765322e706e67](images/image-1.png)

Figure 5-4. *Simple deployment of Azure Web App*

As application needs grow, more complex and robust deployment solutions may be required. Figure 5-5 shows an example of a more complex deployment plan that supports additional capabilities.

![https://docs.microsoft.com/en-us/azure/architecture/reference-architectures/_images/blueprints/paas-basic-web-app.png](images/image-2.png)

Figure 5-5. *Deploying a web app to an Azure App Service*

Internally, this project’s organization into multiple projects based on responsibility improves the maintainability of the application.

This unit can be scaled up or out to take advantage of cloud-based on-demand scalability. *Scaling up* means adding additional CPU, memory, disk space, or other resources to the server(s) hosting your app. *Scaling out* means adding additional instances of such servers, whether these are physical servers, virtual machines, or containers. When your app is hosted across multiple instances, a load balancer is used to assign requests to individual app instances.

The simplest approach to scaling a web application in Azure is to configure scaling manually in the application’s App Service Plan. Figure 5-6 shows the appropriate Azure dashboard screen to configure how many instances are serving an app.

![https://docs.microsoft.com/en-us/azure/app-service-web/media/app-service-web-scale-a-web-app-in-an-app-service-environment/aseappscale-manualscale.png](images/image-3.png)

Figure 5-6. *App Service Plan scaling in Azure.*

# Clean architecture

Applications that follow the Dependency Inversion Principle as well as the Domain-Driven Design (DDD) principles tend to arrive at a similar architecture. This architecture has gone by many names over the years. One of the first names was Hexagonal Architecture, followed by Ports-and-Adapters. More recently, it’s been cited as the [Onion Architecture](http://jeffreypalermo.com/blog/the-onion-architecture-part-1/) or [Clean Architecture](https://8thlight.com/blog/uncle-bob/2012/08/13/the-clean-architecture.html). The most recent name, Clean Architecture, is used to describe this architecture in this e-book.

**Note:** The term Clean Architecture can be applied to applications that are built using DDD Principles as well as to those that are not built using DDD. In the case of the former, this combination may be referred to as “Clean DDD Architecture”.

Clean architecture puts the business logic and application model at the center of the application. Instead of having business logic depend on data access or other infrastructure concerns, this dependency is inverted: infrastructure and implementation details depend on the Application Core. This is achieved by defining abstractions, or interfaces, in the Application Core, which are then implemented by types defined in the Infrastructure layer. A common way of visualizing this architecture is to use a series of concentric circles, similar to an onion. Figure 5-7 shows an example of this style of architectural representation.

![C:\Users\steve_000\AppData\Local\Microsoft\Windows\INetCache\Content.Word\CleanArchitectureOnion.png](images/image-4.png)

**Figure 5-7.** Clean Architecture; onion view

In this diagram, dependencies flow toward the innermost circle. The Application Core takes its name from its position at the core of this diagram. It has no dependencies on other application layers. The application’s entities and interfaces are at the very center. Just outside, but still in the Application Core, are domain services, which typically implement interfaces defined in the inner circle. Outside of the Application Core, both the UI and the Infrastructure layers depend on the Application Core, but not on one another (necessarily).

Figure 5-8 shows a more traditional horizontal layer diagram that better reflects the dependency between the UI and other layers.

![Image](images/image23.png)

Figure 5-8. *Clean Architecture; horizontal layer view*

Note that the solid arrows represent compile-time dependencies, while the dashed arrow represents a runtime-only dependency. With the clean architecture, the UI layer works with interfaces defined in the Application Core at compile time, and ideally shouldn’t know about the implementation types defined in the Infrastructure layer. At run time, however, these implementation types are required for the app to execute, so they need to be present and wired up to the Application Core interfaces via dependency injection.

Figure 5-9 shows a more detailed view of an ASP.NET Core application’s architecture when built following these recommendations.

![ASPNET Core Architecture](images/image24.png)

Figure 5-9. *ASP.NET Core architecture diagram following Clean Architecture.*

Because the Application Core doesn’t depend on Infrastructure, it’s very easy to write automated unit tests for this layer. Figures 5-10 and 5-11 show how tests fit into this architecture.

![UnitTestCore](images/image25.png)

Figure 5-10. *Unit testing Application Core in isolation.*

![IntegrationTests](images/image26.png)

Figure 5-11. *Integration testing Infrastructure implementations with external dependencies.*

Since the UI layer doesn’t have any direct dependency on types defined in the Infrastructure project, it’s likewise very easy to swap out implementations, either to facilitate testing or in response to changing application requirements. ASP.NET Core’s built-in use of and support for dependency injection makes this architecture the most appropriate way to structure non-trivial monolithic applications.

For monolithic applications the Application Core, Infrastructure, and UI projects are all run as a single application. The runtime application architecture might look something like Figure 5-12.

![ASPNET Core Architecture 2](images/image27.png)

Figure 5-12. *A sample ASP.NET Core app’s runtime architecture.*

### Organizing Code in Clean Architecture

In a Clean Architecture solution, each project has clear responsibilities. As such, certain types belong in each project and you’ll frequently find folders corresponding to these types in the appropriate project.

![Image](images/image28.tiff)The Application Core holds the business model, which includes entities, services, and interfaces. These interfaces include abstractions for operations that will be performed using Infrastructure, such as data access, file system access, network calls, etc. Sometimes services or interfaces defined at this layer will need to work with non-entity types that have no dependencies on UI or Infrastructure. These can be defined as simple Data Transfer Objects (DTOs).

The Infrastructure project typically includes data access implementations. In a typical ASP.NET Core web application, these implementations include the Entity Framework (EF) DbContext, any EF Core Migration types that have been defined, and data access implementation classes. The most common way to abstract data access implementation code is through the use of the [Repository design pattern](http://deviq.com/repository-pattern/).

![Image](images/image29.tiff)In addition to data access implementations, the Infrastructure project should contain implementations of services that must interact with infrastructure concerns. These services should implement interfaces defined in the Application Core, and so Infrastructure should have a reference to the Application Core project. If you find that you have services defined in Infrastructure that do not depend on any infrastructure-related types, see if you can move them into your Application Core project. *Generally, if you can move services into Application Core (without adding dependencies to this project), you should do so.*

![Image](images/image30.tiff)The user interface layer in an ASP.NET Core MVC-based application is the entry point for the application. This layer consists of an ASP.NET Core MVC (or Razor Pages) project. This project should reference the Application Core project, and its types should interact with infrastructure strictly through interfaces defined in Application Core. No direct instantiation of (or static calls to) Infrastructure layer types should be permitted in the UI layer. Your application can [avoid referencing the Infrastructure project](https://ardalis.com/avoid-referencing-infrastructure-in-visual-studio-solutions), while still using its types at runtime. Only services that work with UI layer types (such as ViewModel types) should be defined in this layer. Move any other services into Infrastructure or Application Core layers, and avoid defining business logic in the UI layer.

The Startup class is responsible for configuring the application, and for wiring up implementation types to interfaces, allowing dependency injection to work properly at run time.

**Note:** To wire up dependency injection in ConfigureServices in the Startup.cs file of the UI project, the project may need to reference the Infrastructure project. This dependency can be eliminated, most easily by using a custom DI container. For the purposes of this sample, the simplest approach is to allow the UI project to reference the Infrastructure project.

# Monolithic Applications and Containers

You can build a single and monolithic-deployment based Web Application or Service and deploy it as a container. Within the application, it might not be monolithic but organized into several libraries, components or layers. Externally it is a single container like a single process, single web application or single service.

To manage this model, you deploy a single container to represent the application. To scale, just add additional copies with a load balancer in front. The simplicity comes from managing a single deployment in a single container or VM.

![Image](images/image-5.png)

Figure 5-13. *Monolithic application architecture example*

Figure 5-13. *Monolithic application architecture example*

You can include multiple components/libraries or internal layers within each container, as illustrated in Figure 5-13. But, following the container principle of *“a container does one thing, and does it in one process*”, the monolithic pattern might be a conflict.

The downside of this approach comes if/when the application grows, requiring it to scale. If the entire application scales, it’s not really a problem. However, in most cases, a few parts of the application are the choke points requiring scaling, while other components are used less.

Using the typical eCommerce example, what you likely need to scale is the product information component. Many more customers browse products than purchase them. More customers use their basket than use the payment pipeline. Fewer customers add comments or view their purchase history. And you likely only have a handful of employees, in a single region, that need to manage the content and marketing campaigns. By scaling the monolithic design, all the code is deployed multiple times.

In addition to the scale everything problem, changes to a single component require complete retesting of the entire application, and a complete redeployment of all the instances.

The monolithic approach is common, and many organizations are developing with this architectural approach. Many are having good enough results, while others are hitting limits. Many designed their applications in this model, because the tools and infrastructure were too difficult to build service oriented architectures (SOA), and they didn’t see the need - until the app grew. If you find you’re hitting the limits of the monolithic approach, breaking up the app to enable it to better leverage containers and microservices may be the next logical step.

![Image](images/image32.png)Deploying monolithic applications in Microsoft Azure can be achieved using dedicated VMs for each instance. Using [Azure VM Scale Sets](https://azure.microsoft.com/en-us/documentation/services/virtual-machine-scale-sets/), you can easily scale the VMs. [Azure App Services](https://azure.microsoft.com/en-us/services/app-service/) can run monolithic applications and easily scale instances without having to manage the VMs. Azure App Services can run single instances of Docker containers as well, simplifying the deployment. Using Docker, you can deploy a single VM as a Docker host, and run multiple instances. Using the Azure balancer, as shown in the Figure 5-14, you can manage scaling.

Figure 5-14. *Multiple hosts scaling-out a single Docker application*

Figure 5-14. *Multiple hosts scaling-out a single Docker application*

The deployment to the various hosts can be managed with traditional deployment techniques. The Docker hosts can be managed with commands like docker run performed manually, or through automation such as Continuous Delivery (CD) pipelines.

## Monolithic application deployed as a container

There are benefits of using containers to manage monolithic application deployments. Scaling the instances of containers is far faster and easier than deploying additional VMs. Even when using virtual machine scale sets to scale VMs, they take time to instance. When deployed as app instances, the configuration of the app is managed as part of the VM.

Deploying updates as Docker images is far faster and network efficient. Docker Images typically start in seconds, speeding rollouts. Tearing down a Docker instance is as easy as issuing a docker stop command, typically completing in less than a second.

As containers are inherently immutable by design, you never need to worry about corrupted VMs, whereas update scripts might forget to account for some specific configuration or file left on disk.

You can use Docker containers for monolithic deployment of simpler web applications. This improves continuous integration and continuous deployment pipelines and helps achieve deployment-to-production success. No more “It works in my machine, why does it not work in production?”

A microservices-based architecture has many benefits, but those benefits come at a cost of increased complexity. In some cases, the costs outweigh the benefits, so a monolithic deployment application running in a single container or in just a few containers is a better option.

A monolithic application might not be easily decomposable into well-separated microservices. Microservices should work independently of each other to provide a more resilient application. If you can't deliver independent feature slices of the application, separating it only adds complexity.

An application might not yet need to scale features independently. Many applications, when they need to scale beyond a single instance, can do so through the relatively simple process of cloning that entire instance. The additional work to separate the application into discrete services provides minimal benefit when scaling full instances of the application is simple and cost-effective.

Early in the development of an application, you might not have a clear idea where the natural functional boundaries are. As you develop a minimum viable product, the natural separation might not yet have emerged. Some of these conditions might be temporary. You might start by creating a monolithic application, and later separate some features to be developed and deployed as microservices. Other conditions might be essential to the application’s problem space, meaning that the application might never be broken into multiple microservices.

Separating an application into many discrete processes also introduces overhead. There's more complexity in separating features into different processes. The communication protocols become more complex. Instead of method calls, you must use asynchronous communications between services. As you move to a microservices architecture, you need to add many of the building blocks implemented in the microservices version of the eShopOnContainers application: event bus handling, message resiliency and retries, eventual consistency, and more.

The much simpler [eShopOnWeb reference application](https://github.com/dotnet-architecture/eShopOnWeb) supports single-container monolithic container usage. The application includes one web application that includes traditional MVC views, web APIs, and Razor Pages. This application can be launched from the solution root using the `docker-compose build` and `docker-compose up` commands. This command configures a container for the web instance, using the `Dockerfile` found in the web project's root, and runs the container on a specified port. You can download the source for this application from GitHub and run it locally. Even this monolithic application benefits from being deployed in a container environment.

For one, the containerized deployment means that every instance of the application runs in the same environment. This includes the developer environment where early testing and development take place. The development team can run the application in a containerized environment that matches the production environment.

In addition, containerized applications scale out at lower cost. Using a container environment enables greater resource sharing than traditional VM environments.

Finally, containerizing the application forces a separation between the business logic and the storage server. As the application scales out, the multiple containers will all rely on a single physical storage medium. This storage medium would typically be a high-availability server running a SQL Server database.

## Docker support

The eShopOnWeb project runs on .NET Core. Therefore, it can run in either Linux-based or Windows-based containers. Note that for Docker deployment, you want to use the same host type for SQL Server. Linux-based containers allow a smaller footprint and are preferred.

You can use Visual Studio 2017 or later to add Docker support to an existing application by right-clicking on a project in Solution Explorer and choosing **Add > Docker Support**. This adds the files required and modifies the project to use them. The current eShopOnWeb sample already has these files in place.

The solution-level `docker-compose.yml` file contains information about what images to build and what containers to launch. The file allows you to use the `docker-compose` command to launch multiple applications at the same time. In this case, it is only launching the Web project. You can also use it to configure dependencies, such as a separate database container.

version: '3'

services:

eshopwebmvc:

image: eshopwebmvc

build:

context: .

dockerfile: src/Web/Dockerfile

environment:

- ASPNETCORE\_ENVIRONMENT=Development

ports:

- "5106:5106"

networks:

default:

external:

name: nat

The `docker-compose.yml` file references the `Dockerfile` in the `Web` project. The `Dockerfile` is used to specify which base container will be used and how the application will be configured on it. The `Web`' `Dockerfile`:

FROM mcr.microsoft.com/dotnet/core/sdk:2.2 AS build

WORKDIR /app

COPY \*.sln .

COPY . .

WORKDIR /app/src/Web

RUN dotnet restore

RUN dotnet publish -c Release -o out

FROM mcr.microsoft.com/dotnet/core/aspnet:2.2 AS runtime

WORKDIR /app

COPY --from=build /app/src/Web/out ./

# Optional: Set this here if not setting it from docker-compose.yml

# ENV ASPNETCORE\_ENVIRONMENT Development

### ENTRYPOINT ["dotnet", "Web.dll"]Troubleshooting Docker problems

Once you run the containerized application, it continues to run until you stop it. You can view which containers are running with the `docker ps` command. You can stop a running container by using the `docker stop` command and specifying the container ID.

Note that running Docker containers may be bound to ports you might otherwise try to use in your development environment. If you try to run or debug an application using the same port as a running Docker container, you'll get an error stating that the server can't bind to that port. Once again, stopping the container should resolve the issue.

![A picture containing screenshot  Description automatically generated](images/image33.tiff)If you want to add Docker support to your application using Visual Studio, make sure Docker Desktop is running when you do so. The wizard won't run correctly if Docker Desktop isn't running when you start the wizard. In addition, the wizard examines your current container choice to add the correct Docker support. If you want to add support for Windows Containers, you need to run the wizard while you have Docker Desktop running with Windows Containers configured. If you want to add support for Linux containers, run the wizard while you have Docker running with Linux containers configured.

Creating N-Tier Applications in C#

<https://www.pluralsight.com/courses/n-tier-apps-part1>

The Clean Architecture

<https://8thlight.com/blog/uncle-bob/2012/08/13/the-clean-architecture.html>

The Onion Architecture

<http://jeffreypalermo.com/blog/the-onion-architecture-part-1/>

The Repository Pattern

[https://deviq.com/repository-pattern/](http://deviq.com/repository-pattern/)

Clean Architecture Solution Sample

<https://github.com/ardalis/cleanarchitecture>

Architecting Microservices eBook

<http://aka.ms/MicroservicesEbook>

Common Client-Side Web Technologies

“Websites should look good from the inside and out.”

Paul Cookson

# Summary

ASP.NET Core applications are web applications and they typically rely on client-side web technologies like HTML, CSS, and JavaScript. By separating the content of the page (the HTML) from its layout and styling (the CSS), and its behavior (via JavaScript), complex web apps can leverage the Separation of Concerns principle. Future changes to the structure, design, or behavior of the application can be made more easily when these concerns are not intertwined.

While HTML and CSS are relatively stable, JavaScript, by means of the application frameworks and utilities developers work with to build web-based applications, is evolving at breakneck speed. This chapter looks at a few ways JavaScript is used by web developers as part of developing applications, as provides a high-level overview of the Angular and React client-side libraries.

# HTML

HTML (HyperText Markup Language) is the standard markup language used to create web pages and web applications. Its elements form the building blocks of pages, representing formatted text, images, form inputs, and other structures. When a browser makes a request to a URL, whether fetching a page or an application, the first thing that is returned is an HTML document. This HTML document may reference or include additional information about its look and layout in the form of CSS, or behavior in the form of JavaScript.

# CSS

CSS (Cascading Style Sheets) is used to control the look and layout of HTML elements. CSS styles can be applied directly to an HTML element, defined separately on the same page, or defined in a separate file and referenced by the page. Styles cascade based on how they are used to select a given HTML element. For instance, a style might apply to an entire document, but would be overridden by a style that applied to a particular element. Likewise, an element-specific style would be overridden by a style that applied to a CSS class that was applied to the element, which in turn would be overridden by a style targeting a specific instance of that element (via its id). Figure 7-1.

![Image](images/image34.png) Figure 6-1. CSS Specificity rules, in order.

It’s best to keep styles in their own separate stylesheet files, and to use selection-based cascading to implement consistent and reusable styles within the application. Placing style rules within HTML should be avoided and applying styles to specific individual elements (rather than whole classes of elements, or elements that have had a particular CSS class applied to them) should be the exception, not the rule.

### CSS Preprocessors

CSS stylesheets lack support for conditional logic, variables, and other programming language features. Thus, large stylesheets often include a lot of repetition, as the same color, font, or other setting is applied to many different variations of HTML elements and CSS classes. CSS preprocessors can help your stylesheets follow the [DRY principle](http://deviq.com/don-t-repeat-yourself/) by adding support for variables and logic.

The most popular CSS preprocessors are Sass and LESS. Both extend CSS and are backward compatible with it, meaning that a plain CSS file is a valid Sass or LESS file. Sass is Ruby-based and LESS is JavaScript based, and both typically run as part of your local development process. Both have command line tools available, as well as built-in support in Visual Studio for running them using Gulp or Grunt tasks.

# JavaScript

JavaScript is a dynamic, interpreted programming language that has been standardized in the ECMAScript language specification. It is the programming language of the web. Like CSS, JavaScript can be defined as attributes within HTML elements, as blocks of script within a page, or in separate files. Just like CSS, it’s generally recommended to organize JavaScript into separate files, keeping it separated as much as possible from the HTML found on individual web pages or application views.

When working with JavaScript in your web application, there are a few tasks that you’ll commonly need to perform:

* Selecting an HTML element and retrieving and/or updating its value
* Querying a Web API for data
* Sending a command to a Web API (and responding to a callback with its result)
* Performing validation

You can perform all of these tasks with JavaScript alone, but many libraries exist to make these tasks easier. One of the first and most successful of these libraries is jQuery, which continues to be a popular choice for simplifying these tasks on web pages. For Single Page Applications (SPAs), jQuery doesn’t provide many of the desired features that Angular and React offer.

## Legacy Web Apps with jQuery

Although ancient by JavaScript framework standards, jQuery continues to be a very commonly used library for working with HTML/CSS and building applications that make AJAX calls to web APIs. However, jQuery operates at the level of the browser document object model (DOM), and by default offers only an imperative, rather than declarative, model.

For example, imagine that if a textbox’s value exceeds 10, an element on the page should be made visible. In jQuery, this would typically be implemented by writing an event handler with code that would inspect the textbox’s value and set the visibility of the target element based on that value. This is an imperative, code-based approach. Another framework might instead use databinding to bind the visibility of the element to the value of the textbox declaratively. This would not require writing any code, but instead only requires decorating the elements involved with data binding attributes. As client-side behaviors grow more complex, data binding approaches frequently result in simpler solutions with less code and conditional complexity.

## jQuery vs a SPA Framework

![Image](images/image35.tiff) Most of the features jQuery lacks intrinsically can be added with the addition of other libraries. However, a SPA framework like Angular provides these features in a more integrated fashion, since it’s been designed with all of them in mind from the start. Also, jQuery is a very imperative library, meaning that you need to call jQuery functions in order to do anything with jQuery. Much of the work and functionality that SPA frameworks provide can be done declaratively, requiring no actual code to be written.

Data binding is a great example of this. In jQuery, it usually only takes one line of code to get the value of a DOM element, or to set an element’s value. However, you have to write this code any time you need to change the value of the element, and sometimes this will occur in multiple functions on a page. Another common example is element visibility. In jQuery, there might be many different places where you would write code to control whether certain elements were visible. In each of these cases, when using data binding, no code would need to be written. You would simply bind the value or visibility of the element(s) in question to a *viewmodel* on the page, and changes to that viewmodel would automatically be reflected in the bound elements.

## Angular SPAs

AngularJS quickly became one of the world’s most popular JavaScript frameworks. With Angular 2, the team rebuilt the framework from the ground up (using [TypeScript](https://www.typescriptlang.org/)) and rebranded from AngularJS to simply Angular. Currently on version 6, Angular continues to be a robust framework for building Single Page Applications.

Angular applications are built from components. Components combine HTML templates with special objects and control a portion of the page. A simple component from Angular’s docs is shown here:

import { Component } from '@angular/core';

@Component({

selector: 'my-app',

template: `<h1>Hello {{name}}</h1>`

})

export class AppComponent { name = 'Angular'; }

Components are defined using the @Component decorator function, which takes in metadata about the component. The selector property identifies the id of the element on the page where this component will be displayed. The template property is a simple HTML template that includes a placeholder that corresponds to the component’s name property, defined on the last line.

By working with components and templates, instead of DOM elements, Angular apps can operate at a higher level of abstraction and with less overall code than apps written using just JavaScript (also called “vanilla JS”) or with jQuery. Angular also imposes some order on how you organize your client-side script files. By convention, Angular apps use a common folder structure, with module and component script files located in an app folder. Angular scripts concerned with building, deploying, and testing the app are typically located in a higher-level folder.

Angular also makes great use of command line interface (CLI) tooling. Getting started with Angular development locally (assuming you already have git and npm installed) consists of simply cloning a repo from GitHub and running `npm install` and `npm start`. Beyond this, Angular ships its own CLI tool which can create projects, add files, and assist with testing, bundling, and deployment tasks. This CLI tooling friendliness makes Angular especially compatible with ASP.NET Core, which also features great CLI support.

Microsoft has developed a reference application, [eShopOnContainers](http://aka.ms/MicroservicesArchitecture), which includes an Angular SPA implementation. This app includes Angular modules to manage the online store’s shopping basket, load and display items from its catalog, and handle order creation. You can view and download the sample application from [GitHub](https://github.com/dotnet-architecture/eShopOnContainers/tree/master/src/Web/WebSPA).

## React

Unlike Angular, which offers a full Model-View-Controller pattern implementation, React is only concerned with views. It’s not a framework, just a library, so to build a SPA you’ll need to leverage additional libraries.

One of React’s most important features is its use of a virtual DOM. The virtual DOM provides React with several advantages, including performance (the virtual DOM can optimize which parts of the actual DOM need to be updated) and testability (no need to have a browser to test React and its interactions with its virtual DOM).

React is also unusual in how it works with HTML. Rather than having a strict separation between code and markup (with references to JavaScript appearing in HTML attributes perhaps), React adds HTML directly within its JavaScript code as JSX. JSX is HTML-like syntax that can compile down to pure JavaScript. For example:

<ul>

{ authors.map(author =>

<li key={author.id}>{author.name}</li>

)}

</ul>

If you already know JavaScript, learning React should be easy. There isn’t nearly as much learning curve or special syntax involved as with Angular or other popular libraries.

Because React isn’t a full framework, you’ll typically want other libraries to handle things like routing, web API calls, and dependency management. The nice thing is, you can pick the best library for each of these, but the disadvantage is that you need to make all of these decisions and verify all of your chosen libraries work well together when you’re done. If you want a good starting point, you can use a starter kit like React Slingshot, which prepackages a set of compatible libraries together with React.

## Choosing a SPA Framework

When considering which JavaScript framework will work best to support your SPA, keep in mind the following considerations:

* Is your team familiar with the framework and its dependencies (including TypeScript in some cases)?
* How opinionated is the framework, and do you agree with its default way of doing things?
* Does it (or a companion library) include all the features your app requires?
* Is it well-documented?
* How active is its community? Are new projects building built with it?
* How active is its core team? Are issues being resolved and new versions shipped regularly?

![A picture containing screenshot  Description automatically generated](images/image36.tiff)JavaScript frameworks continue to evolve with breakneck speed. Use the considerations listed above to help mitigate the risk of choosing a framework you’ll later regret being dependent upon. If you’re particularly risk-averse, consider a framework that offers commercial support and/or is being developed by a large enterprise.

HTML and CSS

<https://www.w3.org/standards/webdesign/htmlcss>

Sass vs. LESS

https://www.keycdn.com/blog/sass-vs-less/

Styling ASP.NET Core Apps with LESS, Sass, and Font Awesome

<https://docs.microsoft.com/en-us/aspnet/core/client-side/less-sass-fa>

Client-Side Development in ASP.NET Core

<https://docs.microsoft.com/en-us/aspnet/core/client-side/>

jQuery

https://jquery.com/

jQuery vs AngularJS

https://www.airpair.com/angularjs/posts/jquery-angularjs-comparison-migration-walkthrough

Angular

https://angular.io/

React

<https://facebook.github.io/react/>

React Slingshot

<https://github.com/coryhouse/react-slingshot>

React vs Angular 2 Comparison

<https://www.codementor.io/codementorteam/react-vs-angular-2-comparison-beginners-guide-lvz5710ha>

5 Best JavaScript Frameworks of 2017

https://hackernoon.com/5-best-javascript-frameworks-in-2017-7a63b3870282

Developing ASP.NET Core Apps

“It’s not important to get it right the first time. It’s vitally important to get it right the last time.”

Andrew Hunt and David Thomas

# Summary

ASP.NET Core is a cross-platform, open-source framework for building modern cloud-optimized web applications. ASP.NET Core apps are lightweight and modular, with built-in support for dependency injection, enabling greater testability and maintainability. Combined with the ASP.NET Core MVC framework, which supports building modern web APIs in addition to both view-based and page-based apps, ASP.NET Core is a powerful framework with which to build enterprise web applications.

# MVC and Razor Pages

ASP.NET Core MVC offers many features that are useful for building web-based APIs and apps. The term MVC stands for “Model-View-Controller”, a UI pattern that breaks up the responsibilities of responding to user requests into several parts. In addition to following this pattern, you can also implement features in your ASP.NET Core apps as Razor Pages. Razor Pages are built into ASP.NET Core MVC, and use the same features for routing, model binding, etc. However, instead of having separate folders and files for Controllers, Views, etc. and using attribute-based routing, Razor Pages are placed in a single folder (“/Pages”), route based on their relative location in this folder, and handle requests with *handlers* instead of controller actions.

When you create a new ASP.NET Core App, you should have a plan in mind for the kind of app you want to build. In Visual Studio, you will choose from several templates like those shown in Figure 7-1.

![Image](images/image37.png)

Figure 7-1. ASP.NET Core Project Templates in Visual Studio

The three most common project templates are Web API, Web Application, and Web Application (Model-View-Controller). Although you can only make this decision when you first create a project, it’s not an irrevocable decision. The Web API project uses standard Model-View-Controller controllers – it just lacks Views by default. Likewise, the default Web Application template uses Razor Pages, and so also lacks a Views folder. You can add a Views folder to these projects later to support view-based behavior. Neither the Web API nor the Model-View-Controller project include a Pages folder by default, but you can add one later to support Razor Pages-based behavior. You can think of these three templates as supporting three different kinds of default user interaction: data (web API), page-based, and view-based. However, you can mix and match any or all of these within a single project if you wish.

## Why Razor Pages?

As you saw in Figure 7-1, Razor Pages is the default approach for new web applications in Visual Studio. Razor Pages offer a significantly simpler means of building page-based application features, such as non-SPA forms. Using controllers and views, it was common for applications to have very large controllers that worked with many different dependencies and view models and returned many different views. This resulted in a lot of complexity and often resulted in controllers that didn’t follow the Single Responsibility Principle or Open/Closed Principles effectively. Razor Pages addresses this issue by encapsulating the server-side logic for a given logical “page” in a web application with its Razor markup. A Razor Page that has no server-side logic can simply consist of a Razor file (for instance, “Index.cshtml”). However, most non-trivial Razor Pages will have an associated *page model* class, which by convention is named the same as the Razor file with a “.cs” extension (for example, “Index.cshtml.cs”).

A Razor Page’s page model combines the responsibilities of an MVC controller and a viewmodel. Instead of handling requests with controller action methods, page model handlers like “OnGet()” are executed, rendering their associated page by default. Razor pages simplify the process of building individual pages in an ASP.NET Core app, while still providing all the architectural features of ASP.NET Core MVC. They are a good default choice for new page-based functionality.

## When to use MVC

If you’re building web APIs, the MVC pattern makes more sense than trying to use Razor Pages. If your project will only expose web API endpoints, you should ideally start from the Web API project template, but otherwise it’s easy to add controllers and associated API endpoints to any ASP.NET Core app. You should also use the view-based MVC approach if you’re migrating an existing application from ASP.NET MVC 5 or earlier to ASP.NET Core MVC and you want to do so with the least amount of effort. Once you’ve made the initial migration, you can evaluate whether it makes sense to adopt Razor Pages for new features or even as a wholesale migration.

Whether you choose to build your web app using Razor Pages or MVC views, your app will have similar performance and will include support for dependency injection, filters, model binding and validation, etc.

# Mapping Requests to Responses

At its heart, ASP.NET Core apps map incoming requests to outgoing responses. At a low level, this is done with middleware, and simple ASP.NET Core apps and microservices may be comprised solely of custom middleware. When using ASP.NET Core MVC, you can work at a somewhat higher level, thinking in terms of *pages and handlers or routes*, *controllers*, and *actions*. Each incoming request is compared with the application’s routing table, and if a matching route is found, the associated page handler (belonging to a Razor Page) or action method (belonging to a controller) is called to handle the request. If no matching route is found, an error handler (in this case, returning a NotFound result) is called.

Razor Pages use a convention-based routing system (based on the file’s location within the Pages folder) and HTTP verb-specific handler methods. For example, a page named Index.cshtml located in the root of the Pages folder will be routed to the root of the web application (“/”) or to its name (“/Index”). A page named “Customers.cshtml” would route to “/Customers”. You can specify custom routes for Razor Pages when you configure MVC in Startup, if desired.

ASP.NET Core MVC apps can use conventional routes, attribute routes, or both. Conventional routes are defined in code, specifying routing *conventions* using syntax like in the example below:

app.UseMvc(routes =>

{

routes.MapRoute("default","{controller=Home}/{action=Index}/{id?}");

});

In this example, a route named “default” has been added to the routing table. It defines a route template with placeholders for *controller*, *action*, and *id*. The controller and action placeholders have default specified (“Home” and “Index”, respectively), and the id placeholder is optional (by virtue of a “?” applied to it). The convention defined here states that the first part of a request should correspond to the name of the controller, the second part to the action, and then if necessary a third part will represent an id parameter. Conventional routes are typically defined in one place for the application, such as in the Configure method in the Startup class.

Attribute routes are applied to controllers and actions directly, rather than specified globally. This has the advantage of making them much more discoverable when you’re looking at a particular method, but does mean that routing information is not kept in one place in the application. With attribute routes, you can easily specify multiple routes for a given action, as well as combine routes between controllers and actions. For example:

[Route("Home")]

public class HomeController : Controller

{

[Route("")] // Combines to define the route template "Home"

[Route("Index")] // Combines to define route template "Home/Index"

[Route("/")] // Does not combine, defines the route template ""

public IActionResult Index() {}

Routes can be specified on [HttpGet] and similar attributes, avoiding the need to add separate [Route] attributes. Attribute routes can also use tokens to reduce the need to repeat controller or action names, as shown below:

[Route("[controller]")]

public class ProductsController : Controller

{

[Route("")] // Matches 'Products'

[Route("Index")] // Matches 'Products/Index'

public IActionResult Index()

}

Razor Pages don’t use attribute routing. You can specify additional route template information for a Razor Page as part of its @page directive:

@page “{id:int}”

In the above example, the page in question would match a route with an integer id parameter. For example, the Products.cshtml page located in the root of /Pages would have this route:

“/Products/123”

Once a given request has been matched to a route, but before the action method (or handler) is called, ASP.NET Core MVC will perform [model binding](https://docs.microsoft.com/en-us/aspnet/core/mvc/models/model-binding) and [model validation](https://docs.microsoft.com/en-us/aspnet/core/mvc/models/validation) on the request. Model binding is responsible for converting incoming HTTP data into the .NET types specified as parameters of the action method to be called. For example, if the action method expects an int id parameter, model binding will attempt to provide this parameter from a value provided as part of the request. To do so, model binding looks for values in a posted form, values in the route itself, and query string values. Assuming an id value is found, it will be converted to an integer before being passed into the action method.

After binding the model but before calling the action method, model validation occurs. Model validation uses optional attributes on the model type, and can help ensure that the provided model object conforms to certain data requirements. Certain values may be specified as required, or limited to a certain length or numeric range, etc. If validation attributes are specified but the model does not conform to their requirements, the property ModelState.IsValid will be false, and the set of failing validation rules will be available to send to the client making the request.

If you are using model validation, you should be sure to always check that the model is valid before performing any state-altering commands, to ensure your app is not corrupted by invalid data. You can use a [filter](https://docs.microsoft.com/en-us/aspnet/core/mvc/controllers/filters) to avoid the need to add code for this in every action. ASP.NET Core MVC filters offer a way of intercepting groups of requests, so that common policies and cross-cutting concerns can be applied on a targeted basis. Filters can be applied to individual actions, whole controllers, or globally for an application.

For web APIs, ASP.NET Core MVC supports [content negotiation](https://docs.microsoft.com/en-us/aspnet/core/mvc/models/formatting), allowing requests to specify how responses should be formatted. Based on headers provided in the request, actions returning data will format the response in XML, JSON, or another supported format. This feature enables the same API to be used by multiple clients with different data format requirements.

![Image](images/image38.tiff)Web API projects should consider using the [ApiController] attribute, which can be applied to individual controllers, to a base controller class, or to the entire assembly. This attribute adds automatic model validation checking and any action with an invalid model will return a BadRequest with the details of the validation errors. The attribute also requires all actions have an attribute route, rather than using a conventional route, and returns more detailed ProblemDetails information in response to errors.

Routing to Controller Actions

<https://docs.microsoft.com/en-us/aspnet/core/mvc/controllers/routing>

Model Binding

https://docs.microsoft.com/en-us/aspnet/core/mvc/models/model-binding

Model Validation

<https://docs.microsoft.com/en-us/aspnet/core/mvc/models/validation>

Filters

<https://docs.microsoft.com/en-us/aspnet/core/mvc/controllers/filters>

ApiController Attribute

https://docs.microsoft.com/en-us/aspnet/core/web-api/?view=aspnetcore-2.2

# Working with Dependencies

ASP.NET Core has built-in support for and internally makes use of a technique known as [dependency injection](https://docs.microsoft.com/en-us/aspnet/core/fundamentals/dependency-injection). Dependency injection is a technique that enables loose coupling between different parts of an application. Looser coupling is desirable because it makes it easier to isolate parts of the application, allowing for testing or replacement. It also makes it less likely that a change in one part of the application will have an unexpected impact somewhere else in the application. Dependency injection is based on the [dependency inversion principle](http://deviq.com/dependency-inversion-principle/), and is often key to achieving the [open/closed principle](http://deviq.com/open-closed-principle/). When evaluating how your application works with its dependencies, beware of the [static cling](http://deviq.com/static-cling/) code smell, and remember the aphorism “[new is glue](http://ardalis.com/new-is-glue).”

Static cling occurs when your classes make calls to static methods, or access static properties, which have side effects or dependencies on infrastructure. For example, if you have a method that calls a static method, which in turn writes to a database, your method is tightly coupled to the database. Anything that breaks that database call will break your method. Testing such methods is notoriously difficult, since such tests either require commercial mocking libraries to mock the static calls, or can only be tested with a test database in place. Static calls that don’t have any dependence on infrastructure, especially those that are completely stateless, are fine to call and have no impact on coupling or testability (beyond coupling code to the static call itself).

Many developers understand the risks of static cling and global state but will still tightly couple their code to specific implementations through direct instantiation. “New is glue” is meant to be a reminder of this coupling, and not a general condemnation of the use of the new keyword. Just as with static method calls, new instances of types that have no external dependencies typically do not tightly couple code to implementation details or make testing more difficult. But each time a class is instantiated, take just a brief moment to consider whether it makes sense to hard-code that specific instance in that particular location, or if it would be a better design to request that instance as a dependency.

## Declare Your Dependencies

ASP.NET Core is built around having methods and classes declare their dependencies, requesting them as arguments. ASP.NET applications are typically set up in a Startup class, which itself is configured to support dependency injection at several points. If your Startup class has a constructor, it can request dependencies through the constructor, like so:

public class Startup // ASP.NET Core 1.x template

{

public Startup(IHostingEnvironment env)

{

var builder = new ConfigurationBuilder()

.SetBasePath(env.ContentRootPath)

.AddJsonFile("appsettings.json", optional: false, reloadOnChange: true)

.AddJsonFile($"appsettings.{env.EnvironmentName}.json", optional: true);

// additional code omitted

}

}

The Startup class is interesting in that there are no explicit type requirements for it. It doesn’t inherit from a special Startup base class, nor does it implement any particular interface. You can give it a constructor, or not, and you can specify as many parameters on the constructor as you want. When the web host you’ve configured for your application starts, it will call the Startup class you’ve told it to use, and will use dependency injection to populate any dependencies the Startup class requires. Of course, if you request parameters that aren’t configured in the services container used by ASP.NET Core, you’ll get an exception, but if you stick to dependencies the container knows about, you can request anything you want.

In ASP.NET Core 2.0, configuration defaults are typically set in Program.cs and then passed into the Startup class. Thus, the Startup class in the default templates looks like this:

public class Startup // ASP.NET Core 2.x template

{

public Startup(IConfiguration configuration)

{

      Configuration = configuration;

}

}

Dependency injection is built into your ASP.NET Core apps right from the start, when you create the Startup instance. It doesn’t stop there for the Startup class. You can also request dependencies in the Configure method:

public void Configure(IApplicationBuilder app,

IHostingEnvironment env,

ILoggerFactory loggerFactory)

{

// code omitted

}

The ConfigureServices method is the exception to this behavior; it must take just one parameter of type IServiceCollection. It doesn’t really need to support dependency injection, since on the one hand it is responsible for adding objects to the services container, and on the other it has access to all currently configured services via the IServiceCollection parameter. Thus, you can work with dependencies defined in the ASP.NET Core services collection in every part of the Startup class, either by requesting the needed service as a parameter or by working with the IServiceCollection in ConfigureServices.

Note: If you need to ensure certain services are available to your Startup class, you can configure them using WebHostBuilder and its ConfigureServices method.

The Startup class is a model for how you should structure other parts of your ASP.NET Core application, from Controllers to Middleware to Filters to your own Services. In each case, you should follow the [Explicit Dependencies Principle](http://deviq.com/explicit-dependencies-principle/), requesting your dependencies rather than directly creating them, and leveraging dependency injection throughout your application. Be careful of where and how you directly instantiate implementations, especially services and objects that work with infrastructure or have side effects. Prefer working with abstractions defined in your application core and passed in as arguments to hardcoding references to specific implementation types.

# Structuring the Application

Monolithic applications typically have a single entry point. In the case of an ASP.NET Core web application, the entry point will be the ASP.NET Core web project. However, that doesn’t mean the solution should consist of just a single project. It’s useful to break up the application into different layers to follow separation of concerns. Once broken up into layers, it’s helpful to go beyond folders to separate projects, which can help achieve better encapsulation. The best approach to achieve these goals with an ASP.NET Core application is a variation of the Clean Architecture discussed in chapter 5. Following this approach, the application’s solution will be comprised of separate libraries for the UI, Infrastructure, and ApplicationCore.

In addition to these projects, separate test projects are included as well (Testing is discussed in Chapter 9).

The application’s object model and interfaces should be placed in the ApplicationCore project. This project will have as few dependencies as possible, and the other projects in the solution will reference it. Business entities that need to be persisted are defined in the ApplicationCore project, as are services that do not directly depend on infrastructure.

Implementation details, such as how persistence is performed or how notifications might be sent to a user, are kept in the Infrastructure project. This project will reference implementation-specific packages such as Entity Framework Core, but should not expose details about these implementations outside of the project. Infrastructure services and repositories should implement interfaces that are defined in the ApplicationCore project, and its persistence implementations are responsible for retrieving and storing entities defined in ApplicationCore.

The ASP.NET Core UI project is responsible for any UI level concerns, but should not include business logic or infrastructure details. In fact, ideally it shouldn’t even have a dependency on the Infrastructure project, which will help ensure no dependency between the two projects is introduced accidentally. This can be achieved using a third-party DI container like Autofac, which allows you to define DI rules in [Module classes](https://autofaccn.readthedocs.io/en/latest/configuration/modules.html) in each project.

Another approach to decoupling the application from implementation details is to have the application call microservices, perhaps deployed in individual Docker containers. This provides even greater separation of concerns and decoupling than leveraging DI between two projects, but has additional complexity.

## Feature Organization

By default, view-based ASP.NET Core MVC applications organize their folder structure to include Controllers and Views, and frequently ViewModels (see below for Razor Pages organization). Client-side code to support these server-side structures is typically stored separately in the wwwroot folder. However, large applications may encounter problems with this organization, since working on any given feature often requires jumping between these folders. This gets more and more difficult as the number of files and subfolders in each folder grows, resulting in a great deal of scrolling through Solution Explorer. One solution to this problem is to organize application code by feature instead of by file type. This organizational style is typically referred to as feature folders or [feature slices](https://msdn.microsoft.com/en-us/magazine/mt763233.aspx) (see also: [Vertical Slices](http://bit.ly/2abpJ7t)).

ASP.NET Core MVC supports Areas for this purpose. Using areas, you can create separate sets of Controllers and Views folders (as well as any associated models) in each Area folder. Figure 7-2 shows an example folder structure, using Areas.

![Image](images/image39.png)

Figure 7-2 Sample Area Organization

When using Areas, you must use attributes to decorate your controllers with the name of the area to which they belong:

[Area(“Catalog”)]

public class HomeController

{}

You also need to add area support to your routes:

app.UseMvc(routes =>

{

// Areas support

routes.MapRoute(

name: "areaRoute",

template: "{area:exists}/{controller=Home}/{action=Index}/{id?}");

routes.MapRoute(

name: "default",

template: "{controller=Home}/{action=Index}/{id?}");

});

In addition to the built-in support for Areas, you can also use your own folder structure, and conventions in place of attributes and custom routes. This would allow you to have feature folders that didn’t include separate folders for Views, Controllers, etc., keeping the hierarchy flatter and making it easier to see all related files in a single place for each feature.

ASP.NET Core uses built-in convention types to control its behavior. You can modify or replace these conventions. For example, you can create a convention that will automatically get the feature name for a given controller based on its namespace (which typically correlates to the folder in which the controller is located):

FeatureConvention : IControllerModelConvention

{

public void Apply(ControllerModel controller)

{

controller.Properties.Add("feature",

GetFeatureName(controller.ControllerType));

}

private string GetFeatureName(TypeInfo controllerType)

{

string[] tokens = controllerType.FullName.Split('.');

if (!tokens.Any(t => t == "Features")) return "";

string featureName = tokens

.SkipWhile(t => !t.Equals("features",

StringComparison.CurrentCultureIgnoreCase))

.Skip(1)

.Take(1)

.FirstOrDefault();

return featureName;

}

}

You then specify this convention as an option when you add support for MVC to your application in ConfigureServices:

services.AddMvc(o => o.Conventions.Add(new FeatureConvention()));

ASP.NET Core MVC also uses a convention to locate views. You can override it with a custom convention so that views will be in your feature folders (using the feature name provided by the FeatureConvention, above). You can learn more about this approach and download a working sample from the MSDN article, [Feature Slices for ASP.NET Core MVC](https://msdn.microsoft.com/en-us/magazine/mt763233.aspx).

### Razor Pages

Razor Pages offer many of the same organization benefits as feature folders or areas. When using Razor Pages, you no longer need separate folders and files for controllers, views, and viewmodels. You also will not have many different views for a given controller. Instead, you will create a single page file for each logical page the user interacts with. Any logic associated with this page will be specified in its Page Model, along with any view data that the page requires (often as a nested class within the page model). Razor Pages and their page models are grouped together by Visual Studio, so navigating between razor markup and the corresponding code and data model doesn’t require moving between folders within your project. As the number of pages in your application grows, you can easily organize them within the Pages folder by using subfolders that correspond to your application’s URL structure. Learn more about building [Simpler ASP.NET Core MVC Apps with Razor Pages in MSDN magazine](https://msdn.microsoft.com/en-us/magazine/mt842512.aspx).

## Cross-Cutting Concerns

As applications grow, it becomes increasingly important to factor out cross-cutting concerns to eliminate duplication and maintain consistency. Some examples of cross-cutting concerns in ASP.NET Core applications are authentication, model validation rules, output caching, and error handling, though there are many others. ASP.NET Core MVC [filters](https://docs.microsoft.com/en-us/aspnet/core/mvc/controllers/filters) allow you to run code before or after certain steps in the request processing pipeline. For instance, a filter can run before and after model binding, before and after an action, or before and after an action’s result. You can also use an authorization filter to control access to the rest of the pipeline. Figures 7-3 shows how request execution flows through filters, if configured.

![The request is processed through Authorization Filters, Resource Filters, Model Binding, Action Filters, Action Execution and Action Result Conversion, Exception Filters, Result Filters, and Result Execution. On the way out, the request is only processed by Result Filters and Resource Filters before becoming a response sent to the client.](images/image-6.png)

Figure 7-3 Request execution through filters and request pipeline.

Filters are usually implemented as attributes, so you can apply them to controllers or actions (or even globally). When added in this fashion, filters specified at the action level override or build upon filters specified at the controller level, which themselves override global filters. For example, the [Route] attribute can be used to build up routes between controllers and actions. Likewise, authorization can be configured at the controller level, and then overridden by individual actions, as the following sample demonstrates:

[Authorize]

public class AccountController : Controller

{

[AllowAnonymous] // overrides the authorize attribute

public async Task<IActionResult> Login() {}

public async Task<IActionResult> ForgotPassword() {}

}

The first method, Login, uses the AllowAnonymous filter (attribute) to override the Authorize filter set at the controller level. The ForgotPassword action (and any other action in the class that doesn’t have an AllowAnonymous attribute) will require an authenticated request.

Filters can be used to eliminate duplication in the form of common error handling policies for APIs. For example, a typical API policy is to return a NotFound response to requests referencing keys that do not exist, and a BadRequest response if model validation fails. The following example demonstrates these two policies in action:

[HttpPut("{id}")]

public async Task<IActionResult> Put(int id, [FromBody]Author author)

{

if ((await \_authorRepository.ListAsync()).All(a => a.Id != id))

{

return NotFound(id);

}

if (!ModelState.IsValid)

{

return BadRequest(ModelState);

}

author.Id = id;

await \_authorRepository.UpdateAsync(author);

return Ok();

}

Don’t allow your action methods to become cluttered with conditional code like this. Instead, pull the policies into filters that can be applied on an as-needed basis. In this example, the model validation check, which should occur any time a command is sent to the API, can be replaced by the following attribute:

public class ValidateModelAttribute : ActionFilterAttribute

{

public override void OnActionExecuting(ActionExecutingContext context)

{

if (!context.ModelState.IsValid)

{

context.Result = new BadRequestObjectResult(context.ModelState);

}

}

}

You can add the ValidateModelAttribute to your project as a Nuget dependency by including the [Ardalis.ValidateModel package](https://www.nuget.org/packages/Ardalis.ValidateModel).For APIs, you can use the [ApiController] attribute to enforce this behavior without the need for a separate [ValidateModel] filter.

Likewise, a filter can be used to check if a record exists and return a 404 before the action is executed, eliminating the need to perform these checks in the action. Once you’ve pulled out common conventions and organized your solution to separate infrastructure code and business logic from your UI, your MVC action methods should be extremely thin:

// PUT api/authors2/5

[HttpPut("{id}")]

[ValidateAuthorExists]

public async Task<IActionResult> Put(int id, [FromBody]Author author)

{

await \_authorRepository.UpdateAsync(author);

return Ok();

}

![Image](images/image41.tiff)You can read more about implementing filters and download a working sample from the MSDN article, [Real World ASP.NET Core MVC Filters](https://msdn.microsoft.com/en-us/magazine/mt767699.aspx).

MSDN – Feature Slices for ASP.NET Core MVC

<https://msdn.microsoft.com/en-us/magazine/mt763233.aspx>

MSDN – Simpler ASP.NET MVC Apps with Razor Pages

<https://msdn.microsoft.com/en-us/magazine/mt842512.aspx>

New is Glue

<https://www.weeklydevtips.com/005>

MSDN – Real World ASP.NET Core MVC Filters

<https://msdn.microsoft.com/en-us/magazine/mt767699.aspx>

Areas

https://docs.microsoft.com/en-us/aspnet/core/mvc/controllers/areas

Filters

<https://docs.microsoft.com/en-us/aspnet/core/mvc/controllers/filters>
ValidateModel Nuget Package

https://www.nuget.org/packages/Ardalis.ValidateModel

# Security

Securing web applications is a large topic, with many considerations. At its most basic level, security involves ensuring you know who a given request is coming from, and then ensuring that that request only has access to resources it should. Authentication is the process of comparing credentials provided with a request to those in a trusted data store, to see if the request should be treated as coming from a known entity. Authorization is the process of restricting access to certain resources based on user identity. A third security concern is protecting requests from eavesdropping by third parties, for which you should at least [ensure that SSL is used by your application](https://docs.microsoft.com/en-us/aspnet/core/security/enforcing-ssl).

## Authentication

ASP.NET Core Identity is a membership system you can use to support login functionality for your application. It has support for local user accounts as well as external login provider support from providers like Microsoft Account, Twitter, Facebook, Google, and more. In addition to ASP.NET Core Identity, your application can use windows authentication, or a third-party identity provider like [Identity Server](https://github.com/IdentityServer/IdentityServer4).

ASP.NET Core Identity is included in new project templates if the Individual User Accounts option is selected. This template includes support for registration, login, external logins, forgotten passwords, and additional functionality.

![Image](images/image42.png)

Figure 7-4. *Select Individual User Accounts to have Identity preconfigured.*

Identity support is configured in Startup, both in ConfigureServices and Configure:

public void ConfigureServices(IServiceCollection services)

{

services.AddDbContext<ApplicationDbContext>(options =>

options.UseSqlServer(Configuration.GetConnectionString("DefaultConnection")));

services.AddIdentity<ApplicationUser, IdentityRole>()

.AddEntityFrameworkStores<ApplicationDbContext>()

.AddDefaultTokenProviders();

services.AddMvc()

}

public void Configure(IApplicationBuilder app,
 IHostingEnvironment env)

{

if (env.IsDevelopment())

{

app.UseDeveloperExceptionPage();

app.UseBrowserLink();

app.UseDatabaseErrorPage();

}

else

{

app.UseExceptionHandler("/Error");

}

app.UseStaticFiles();

app.UseAuthentication();

app.UseMvc(routes =>

{

routes.MapRoute(

name: "default",

template: "{controller}/{action=Index}/{id?}");

});

}

It’s important that UseAuthentication appear before UseMvc in the Configure method. When configuring Identity in ConfigureServices, you’ll notice a call to AddDefaultTokenProviders. This has nothing to do with tokens that may be used to secure web communications, but instead refers to providers that create prompts that can be sent to users via SMS or email for them to confirm their identity.

You can learn more about [configuring two-factor authentication](https://docs.microsoft.com/en-us/aspnet/core/security/authentication/2fa) and [enabling external login providers](https://docs.microsoft.com/en-us/aspnet/core/security/authentication/social/) from the official ASP.NET Core docs.

## Authorization

The simplest form of authorization involves restricting access to anonymous users. When using Razor Pages, controlling access to individual pages or folders is done when configuring MVC in Startup:

services.AddMvc()

.AddRazorPagesOptions(options =>

{

options.Conventions.AuthorizeFolder("/Order");

});

When using controllers, and views, apply the [Authorize] attribute to certain controllers or actions. If roles are being used, the attribute can be further extended to restrict access to users who belong to certain roles, as shown:

[Authorize(Roles = "HRManager,Finance")]

public class SalaryController : Controller

{

}

In this case, users belonging to either the HRManager or Finance roles (or both) would have access to the SalaryController. To require that a user belong to multiple roles (not just one of several), you can apply the attribute multiple times, specifying a required role each time.

Specifying certain sets of roles as strings in many different controllers and actions can lead to undesirable repetition. You can configure authorization policies, which encapsulate authorization rules, and then specify the policy instead of individual roles when applying the [Authorize] attribute:

[Authorize(Policy = "CanViewPrivateReport")]

public IActionResult ExecutiveSalaryReport()

{

return View();

}

Using policies in this way, you can separate the kinds of actions being restricted from the specific roles or rules that apply to it. Later, if you create a new role that needs to have access to certain resources, you can just update a policy, rather than updating every list of roles on every [Authorize] attribute.

### Claims

Claims are name value pairs that represent properties of an authenticated user. For example, you might store users’ employee number as a claim. Claims can then be used as part of authorization policies. You could create a policy called “EmployeeOnly” that requires the existence of a claim called “EmployeeNumber”, as shown in this example:

public void ConfigureServices(IServiceCollection services)

{

services.AddMvc();

services.AddAuthorization(options =>

{

options.AddPolicy("EmployeeOnly", policy => policy.RequireClaim("EmployeeNumber"));

});

}

This policy could then be used with the [Authorize] attribute to protect any controller and/or action, as described above.

### Securing Web APIs

Most web APIs should implement a token-based authentication system. Token authentication is stateless and designed to be scalable. In a token-based authentication system, the client must first authenticate with the authentication provider. If successful, the client is issued a token, which is simply a cryptographically meaningful string of characters. When the client then needs to issue a request to an API, it adds this token as a header on the request. The server then validates the token found in the request header before completing the request. Figure 7-5 demonstrates this process.

![TokenAuth](images/image43.png)

Figure 7-5. *Token-based authentication for Web APIs.*

You can create your own authentication service, [integrate with Azure AD and OAuth](https://docs.microsoft.com/en-us/azure/api-management/api-management-howto-protect-backend-with-aad), or implement a service using an open source tool like [IdentityServer](https://github.com/IdentityServer).

### Custom Security

Be especially careful about “rolling your own” implementation of cryptography, user membership, or token generation system. There are many commercial and open source alternatives available which will almost certainly have better security than a custom implementation.

![Image](images/image44.tiff)Security Docs Overview

https://docs.microsoft.com/en-us/aspnet/core/security/

Enforcing SSL in an ASP.NET Core App

<https://docs.microsoft.com/en-us/aspnet/core/security/enforcing-ssl>

Introduction to Identity

<https://docs.microsoft.com/en-us/aspnet/core/security/authentication/identity>

Introduction to Authorization

<https://docs.microsoft.com/en-us/aspnet/core/security/authorization/introduction>

Authentication and Authorization for API Apps in Azure App Service

<https://docs.microsoft.com/en-us/azure/app-service-api/app-service-api-authentication>

Identity Server

https://github.com/IdentityServer

# Client Communication

In addition to serving pages and responding to requests for data via web APIs, ASP.NET Core apps can communicate directly with connected clients. This outbound communication can use a variety of transport technologies, the most common being WebSockets. ASP.NET Core SignalR is a library that makes it simple to add real-time server-to-client communication functionality to your applications. SignalR supports a variety of transport technologies, including WebSockets, and abstracts away many of the implementation details from the developer.

ASP.NET Core SignalR has been available with ASP.NET Core since version 2.1.

Real-time client communication, whether using WebSockets directly or other techniques, are useful in a variety of application scenarios. Some examples include:

* Live chat room applications
* Monitoring applications
* Job progress updates
* Notifications
* Interactive forms applications

When building client communication into your applications, there are typically two components:

* Server-side connection manager (SignalR Hub, WebSocketManager WebSocketHandler)
* Client-side library

Clients are not limited to browsers – mobile apps, console apps, and other native apps can also communicate using SignalR/WebSockets. The following simple program echoes all content sent to a chat application to the console, as part of a WebSocketManager sample application:

public class Program

{

private static Connection \_connection;

public static void Main(string[] args)

{

StartConnectionAsync();

\_connection.On("receiveMessage", (arguments) =>

{

Console.WriteLine($"{arguments[0]} said: {arguments[1]}");

});

Console.ReadLine();

StopConnectionAsync();

}

public static async Task StartConnectionAsync()

{

\_connection = new Connection();

await \_connection.StartConnectionAsync("ws://localhost:65110/chat");

}

public static async Task StopConnectionAsync()

{

await \_connection.StopConnectionAsync();

}

![Image](images/image45.tiff)Consider ways in which your applications communicate directly with client applications, and consider whether real-time communication would improve your app’s user experience.

ASP.NET Core SignalR

<https://github.com/aspnet/SignalR>

WebSocket Manager

https://github.com/radu-matei/websocket-manager

# Domain-Driven Design – Should You Apply It?

Domain-Driven Design (DDD) is an agile approach to building software that emphasizes focusing on the *business domain*. It places a heavy emphasis on communication and interaction with business domain expert(s) who can relate to the developers how the real-world system works. For example, if you’re building a system that handles stock trades, your domain expert might be an experienced stock broker. DDD is designed to address large, complex business problems, and is often not appropriate for smaller, simpler applications, as the investment in understanding and modeling the domain is not worth it.

When building software following a DDD approach, your team (including non-technical stakeholders and contributors) should develop a *ubiquitous language* for the problem space. That is, the same terminology should be used for the real-world concept being modeled, the software equivalent, and any structures that might exist to persist the concept (for example, database tables). Thus, the concepts described in the ubiquitous language should form the basis for your *domain model*.

Your domain model is comprised of objects that interact with one another to represent the behavior of the system. These objects may fall into the following categories:

* [Entities](http://deviq.com/entity/), which represent objects with a thread of identity. Entities are typically stored in persistence with a key by which they can later be retrieved.
* [Aggregates](http://deviq.com/aggregate-pattern/), which represent groups of objects that should be persisted as a unit.
* [Value objects](http://deviq.com/value-object/), which represent concepts that can be compared based on the sum of their property values. For example, DateRange consisting of a start and end date.
* [Domain events](https://martinfowler.com/eaaDev/DomainEvent.html), which represent things happening within the system that are of interest to other parts of the system.

Note that a DDD domain model should encapsulate complex behavior within the model. Entities, in particular, should not merely be collections of properties. When the domain model lacks behavior and merely represents the state of the system, it is said to be an [anemic model](http://deviq.com/anemic-model/), which is undesirable in DDD.

In addition to these model types, DDD typically employs a variety of patterns:

* [Repository](http://deviq.com/repository-pattern/), for abstracting persistence details.
* [Factory](https://en.wikipedia.org/wiki/Factory_method_pattern), for encapsulating complex object creation.
* Domain events, for decoupling dependent behavior from triggering behavior.
* [Services](http://gorodinski.com/blog/2012/04/14/services-in-domain-driven-design-ddd/), for encapsulating complex behavior and/or infrastructure implementation details.
* [Command](https://en.wikipedia.org/wiki/Command_pattern), for decoupling issuing commands and executing the command itself.
* [Specification](http://deviq.com/specification-pattern/), for encapsulating query details.

DDD also recommends the use of the Clean Architecture discussed previously, allowing for loose coupling, encapsulation, and code that can easily be verified using unit tests.

## When Should You Apply DDD

DDD is well-suited to large applications with significant business (not just technical) complexity. The application should require the knowledge of domain experts. There should be significant behavior in the domain model itself, representing business rules and interactions beyond simply storing and retrieving the current state of various records from data stores.

## When Shouldn’t You Apply DDD

DDD involves investments in modeling, architecture, and communication that may not be warranted for smaller applications or applications that are essentially just CRUD (create/read/update/delete). If you choose to approach your application following DDD, but find that your domain has an anemic model with no behavior, you may need to rethink your approach. Either your application may not need DDD, or you may need assistance refactoring your application to encapsulate business logic in the domain model, rather than in your database or user interface.

![Image](images/image46.tiff)A hybrid approach would be to only use DDD for the transactional or more complex areas of the application, but not for simpler CRUD or read-only portions of the application. For instance, you needn’t have the constraints of an Aggregate if you’re querying data to display a report or to visualize data for a dashboard. It’s perfectly acceptable to have a separate, simpler read model for such requirements.

Domain-Driven Design Fundamentals (course)

https://www.pluralsight.com/courses/domain-driven-design-fundamentalsDesign Patterns Library (course)

https://www.pluralsight.com/courses/patterns-libraryDDD in Plain English (StackOverflow Answer)

<http://bit.ly/2pmVgK2>

#

# Deployment

There are a few steps involved in the process of deploying your ASP.NET Core application, regardless of where it will be hosted. The first step is to publish the application, which can be done using the dotnet publish CLI command. This will compile the application and place all of the files needed to run the application into a designated folder. When you deploy from Visual Studio, this step is performed for you automatically. The publish folder contains .exe and .dll files for the application and its dependencies. A self-contained application will also include a version of the .NET runtime. ASP.NET Core applications will also include configuration files, static client assets, and MVC views.

ASP.NET Core applications are console applications that must be started when the server boots and restarted if the application (or server) crashes. A process manager can be used to automate this process. The most common process managers for ASP.NET Core are Nginx and Apache on Linux and IIS or Windows Service on Windows.

In addition to a process manager, ASP.NET Core applications hosted in the Kestrel web server can benefit from the use of a reverse proxy server (this was a requirement for ASP.NET Core 1.x). A reverse proxy server receives HTTP requests from the internet and forwards them to Kestrel after some preliminary handling. Reverse proxy servers provide a layer of security for the application, and are used for edge deployments (exposed to traffic from the Internet). As of ASP.NET Core 2.0, Kestrel now supports edge deployments directly. However, Kestrel also doesn’t support hosting multiple applications on the same port, so techniques like host headers cannot be used with it to enable hosting multiple applications on the same port and IP address (a scenario IIS supports).

![Kestrel to Internet](images/image-7.png)

Figure 7-6. *ASP.NET Core hosted in Kestrel behind a reverse proxy server*

Another scenario in which a reverse proxy can be helpful is to secure multiple applications using SSL/HTTPS. In this case, only the reverse proxy would need to have SSL configured. Communication between the reverse proxy server and Kestrel could take place over HTTP, as shown in Figure 7-7.

![Image](images/image48.png)

Figure 7-7. *ASP.NET Core hosted behind an HTTPS-secured reverse proxy server*

An increasingly popular approach is to host your ASP.NET Core application in a Docker container, which then can be hosted locally or deployed to Azure for cloud-based hosting. The Docker container could contain your application code, running on Kestrel, and would be deployed behind a reverse proxy server, as shown above.

If you’re hosting your application on Azure, you can use Microsoft Azure Application Gateway as a dedicated virtual appliance to provide several services. In addition to acting as a reverse proxy for individual applications, Application Gateway can also offer the following features:

* HTTP load balancing
* SSL offload (SSL only to Internet)
* End to End SSL
* Multi-site routing (consolidate up to 20 sites on a single Application Gateway)
* Web application firewall
* Websocket support
* Advanced diagnostics

Learn more about Azure deployment options in Chapter 10.

![Image](images/image49.tiff)

Hosting and Deployment Overview

<https://docs.microsoft.com/en-us/aspnet/core/publishing/>

When to use Kestrel with a reverse proxy

[https://docs.microsoft.com/en-us/aspnet/core/fundamentals/servers/kestrel#when-to-use-kestrel-with-a-reverse-proxy](https://docs.microsoft.com/en-us/aspnet/core/fundamentals/servers/kestrel)

Host ASP.NET Core apps in Docker

https://docs.microsoft.com/en-us/aspnet/core/publishing/docker

Introducing Azure Application Gateway

<https://docs.microsoft.com/en-us/azure/application-gateway/application-gateway-introduction>

Working with Data in ASP.NET Core Apps

“Data is a precious thing and will last longer than the systems themselves.”

Tim Berners-Lee

# Summary

Data access is an important part of almost any software application. ASP.NET Core supports a variety of data access options, including Entity Framework Core (and Entity Framework 6 as well), and can work with any .NET data access framework. The choice of which data access framework to use depends on the application’s needs. Abstracting these choices from the ApplicationCore and UI projects, and encapsulating implementation details in Infrastructure, helps to produce loosely coupled, testable software.

# Entity Framework Core (for relational databases)

If you’re writing a new ASP.NET Core application that needs to work with relational data, then Entity Framework Core (EF Core) is the recommended way for your application to access its data. EF Core is an object-relational mapper (O/RM) that enables .NET developers to persist objects to and from a data source. It eliminates the need for most of the data access code developers would typically need to write. Like ASP.NET Core, EF Core has been rewritten from the ground up to support modular cross-platform applications. You add it to your application as a NuGet package, configure it in Startup, and request it through dependency injection wherever you need it.

If you’re using ASP.NET Core 2.0 or greater and you have a reference to the Microsoft.AspNetCore.All metapackage, you already have references to EF Core and its SqlServer and InMemory packages. If you’re not using this metapackage, you can add references to Entity Framework Core using the instructions below:

To use EF Core with a SQL Server database, run the following dotnet CLI command:

dotnet add package Microsoft.EntityFrameworkCore.SqlServer

To add support for an InMemory data source, for testing:

dotnet add package Microsoft.EntityFrameworkCore.InMemory

## The DbContext

To work with EF Core, you need a subclass of DbContext. This class holds properties representing collections of the entities your application will work with. The eShopOnWeb sample includes a CatalogContext with collections for items, brands, and types:

public class CatalogContext : DbContext

{

public CatalogContext(DbContextOptions<CatalogContext> options) : base(options)

{

}

public DbSet<CataloGitem> CataloGitems { get; set; }

public DbSet<CatalogBrand> CatalogBrands { get; set; }

public DbSet<CatalogType> CatalogTypes { get; set; }

}

Your DbContext must have a constructor that accepts DbContextOptions and pass this argument to the base DbContext constructor. Note that if you have only one DbContext in your application, you can pass an instance of DbContextOptions, but if you have more than one you must use the generic DbContextOptions<T> type, passing in your DbContext type as the generic parameter.

## Configuring EF Core

In your ASP.NET Core application, you’ll typically configure EF Core in your ConfigureServices method. EF Core uses a DbContextOptionsBuilder, which supports several helpful extension methods to streamline its configuration. Tp configure CatalogContext to use a SQL Server database with a connection string defined in Configuration, you would add the following code to ConfigureServices:

services.AddDbContext<CatalogContext>(options => options.UseSqlServer(Configuration.GetConnectionString("DefaultConnection")));

To use the in-memory database:

services.AddDbContext<CatalogContext>(options =>

options.UseInMemoryDatabase(“Catalog”));

You must specify a name for your in-memory database. This name should be unique to its associated DbContext.

Once you have installed EF Core, created a DbContext child type, and configured it in ConfigureServices, you are ready to use EF Core. You can request an instance of your DbContext type in any service that needs it and start working with your persisted entities using LINQ as if they were simply in a collection. EF Core does the work of translating your LINQ expressions into SQL queries to store and retrieve your data.

You can see the queries EF Core is executing by configuring a logger and ensuring its level is set to at least Information, as shown in Figure 8-1.

![Image](images/image50.png)

Figure 8-1. *Logging EF Core queries to the console*

You can configure logging during development in a default app template by editing the appsettings-Development.json file. For example:

{

"Logging": {

"IncludeScopes": false,

"LogLevel": {

"Default": "Debug",

"System": "Information",

"Microsoft": "Information"

}

}

}

## Fetching and Storing Data

To retrieve data from EF Core, you access the appropriate property and use LINQ to filter the result. You can also use LINQ to perform projection, transforming the result from one type to another. The following example would retrieve CatalogBrands, ordered by name, filtered by their Enabled property, and projected onto a SelectListItem type:

var brandItems = await \_context.CatalogBrands

.Where(b => b.Enabled)

.OrderBy(b => b.Name)

.Select(b => new SelectListItem {
Value = b.Id, Text = b.Name })
 .ToListAsync();

It’s important in the above example to add the call to ToListAsync in order to execute the query immediately. Otherwise, the statement will assign an IQueryable<SelectListItem> to brandItems, which will not be executed until it is enumerated. There are pros and cons to returning IQueryable results from methods. It allows the query EF Core will construct to be further modified, but can also result in errors that only occur at runtime, if operations are added to the query that EF Core cannot translate. It’s generally safer to pass any filters into the method performing the data access, and return back an in-memory collection (for example, List<T>) as the result. These filters can be further encapsulated by using the [Specification pattern](http://deviq.com/specification-pattern/).

EF Core tracks changes on entities it fetches from persistence. To save changes to a tracked entity, you just call the SaveChanges method on the DbContext, making sure it’s the same DbContext instance that was used to fetch the entity. Adding and removing entities is done directly on the appropriate DbSet property, again with a call to SaveChanges to execute the database commands. The following example demonstrates adding, updating, and removing entities from persistence.

// create

var newBrand = new CatalogBrand() { Brand = "Acme" };

\_context.Add(newBrand);

await \_context.SaveChangesAsync();

// read and update

var existingBrand = \_context.CatalogBrands.Find(1);

existingBrand.Brand = "Updated Brand";

await \_context.SaveChangesAsync();

// read and delete (alternate Find syntax)

var brandToDelete = \_context.Find<CatalogBrand>(2);

\_context.CatalogBrands.Remove(brandToDelete);

await \_context.SaveChangesAsync();

EF Core supports both synchronous and async methods for fetching and saving. In web applications, it’s recommended to use the async/await pattern with the async methods, so that web server threads are not blocked while waiting for data access operations to complete.

## Fetching Related Data

When EF Core retrieves entities, it populates all of the properties that are stored directly with that entity in the database. Navigation properties, such as lists of related entities, are not populated and may have their value set to null. This ensures EF Core is not fetching more data than is needed, which is especially important for web applications, which must quickly process requests and return responses in an efficient manner. To include relationships with an entity using *eager loading*, you specify the property using the Include extension method on the query, as shown:

// .Include requires using Microsoft.EntityFrameworkCore

var brandsWithItems = await \_context.CatalogBrands

.Include(b => b.Items)

.ToListAsync();

You can include multiple relationships, and you can also include sub-relationships using ThenInclude. EF Core will execute a single query to retrieve the resulting set of entities. Alternately you can include navigation properties of navigation properties by passing a ‘.’-separated string to the .Include() extension method, like so:

.Include(“Items.Products”)

In addition to encapsulating filtering logic, specification can specify the shape of the data to be returned, including which properties to populate. The eShopOnWeb sample includes several specifications that demonstrate encapsulating eager loading information within the specification. You can see how the specification is used as part of a query [here](https://github.com/dotnet-architecture/eShopOnWeb/blob/master/src/Infrastructure/Data/SpecificationEvaluator.cs):

// Includes all expression-based includes

query = specification.Includes.Aggregate(query,

(current, include) => current.Include(include));

// Include any string-based include statements

query = specification.IncludeStrings.Aggregate(query,(current, include) => current.Include(include));

Another option for loading related data is to use *explicit loading*. Explicit loading allows you to load additional data into an entity that has already been retrieved. Since this involves a separate request to the database, it’s not recommended for web applications, which should minimize the number of database round trips made per request.

Lazy loading is a feature that automatically loads related data as it is referenced by the application. EF Core has added support for lazy loading in version 2.1. Lazy loading is not enabled by default and requires installing the `Microsoft.EntityFrameworkCore.Proxies` package. As with explicit loading, [lazy loading should typically be avoided for web applications](https://ardalis.com/avoid-lazy-loading-entities-in-asp-net-applications). Enabling it can result in web requests that issue dozens or more requests to the database, especially when looping through entities and their navigation properties.

## Encapsulating Data

EF Core supports several features that allow your model to properly encapsulate its state. A common problem in domain models is that they expose collection navigation properties as publicly accessible list types. This allows any collaborator to manipulate the contents of these collection types, which may bypass important business rules related to the collection, possibly leaving the object in an invalid state. The solution to this is to expose read-only access to related collections, and explicitly provide methods defining ways in which clients can manipulate them, as in this example:

public class Basket : BaseEntity

{

public string BuyerId { get; set; }

private readonly List<BasketItem> \_items = new List<BasketItem>();

public IReadOnlyCollection<BasketItem> Items => \_items.AsReadOnly();

public void AddItem(int catalogItemId, decimal unitPrice, int quantity = 1)

{

if (!Items.Any(i => i.CatalogItemId == catalogItemId))

{

\_items.Add(new BasketItem()

{

CatalogItemId = catalogItemId,

Quantity = quantity,

UnitPrice = unitPrice

});

return;

}

var existingItem = Items
.FirstOrDefault(i => i.CatalogItemId == catalogItemId);

existingItem.Quantity += quantity;

}

}

Note that this entity type doesn’t expose a public List or ICollection property, but instead exposes an IReadOnlyCollection type that wraps the underlying List type. When using this pattern, you can indicate to Entity Framework Core to use the backing field like so:

private void ConfigureBasket(EntityTypeBuilder<Basket> builder)

{

var navigation = builder.Metadata.FindNavigation(nameof(Basket.Items));

navigation.SetPropertyAccessMode(PropertyAccessMode.Field);

}

Another way in which you can improve your domain model is through the use of value objects for types that lack identity and are only distinguished by their properties. Using such types as properties of your entities can help keep logic specific to the value object where it belongs, and can avoid duplicate logic between multiple entities that use the same concept. In Entity Framework Core, you can persist value objects in the same table as their owning entity by configuring the type as an owned entity, like so:

private void ConfigureOrder(EntityTypeBuilder<Order> builder)

{

builder.OwnsOne(o => o.ShipToAddress);

}

In this example, the ShipToAddress property is of type Address. Address is a value object with several properties (Street, City, etc.). EF Core will map the Order object to its table with one column per Address property, prefixing each column name with the name of the property. For example, the Order table in this case would include columns “ShipToAddress\_Street”, “ShipToAddress\_City”, etc.

EF Core 2.2 introduces support for [collections of owned entities](https://docs.microsoft.com/en-us/ef/core/what-is-new/ef-core-2.2).

## Resilient Connections

External resources like SQL databases may occasionally be unavailable. In cases of temporary unavailability, applications can use retry logic to avoid raising an exception. This technique is commonly referred to as connection resiliency. You can implement your [own retry with exponential backoff](https://docs.microsoft.com/en-us/azure/architecture/patterns/retry) technique by attempting to retry with an exponentially increasing wait time, until a maximum retry count has been reached. This technique embraces the fact that cloud resources might intermittently be unavailable for short periods of time, resulting in failure of some requests.

For Azure SQL DB, Entity Framework Core already provides internal database connection resiliency and retry logic. But you need to enable the Entity Framework execution strategy for each DbContext connection if you want to have resilient EF Core connections.

For instance, the following code at the EF Core connection level enables resilient SQL connections that are retried if the connection fails.

// Startup.cs from any ASP.NET Core Web API

public class Startup

{

public IServiceProvider ConfigureServices(IServiceCollection services)

{

//...

services.AddDbContext<OrderingContext>(options =>

{

options.UseSqlServer(Configuration["ConnectionString"],

sqlServerOptionsAction: sqlOptions =>

{

sqlOptions.EnableRetryOnFailure(

maxRetryCount: 5,

maxRetryDelay: TimeSpan.FromSeconds(30),

errorNumbersToAdd: null);

});

});

}

//...

### Execution strategies and explicit transactions using BeginTransaction and multiple DbContexts

When retries are enabled in EF Core connections, each operation you perform using EF Core becomes its own retriable operation. Each query and each call to SaveChanges will be retried as a unit if a transient failure occurs.

However, if your code initiates a transaction using BeginTransaction, you are defining your own group of operations that need to be treated as a unit—everything inside the transaction has be rolled back if a failure occurs. You will see an exception like the following if you attempt to execute that transaction when using an EF execution strategy (retry policy) and you include several SaveChanges from multiple DbContexts in it.

System.InvalidOperationException: The configured execution strategy 'SqlServerRetryingExecutionStrategy' does not support user initiated transactions. Use the execution strategy returned by 'DbContext.Database.CreateExecutionStrategy()' to execute all the operations in the transaction as a retriable unit.

The solution is to manually invoke the EF execution strategy with a delegate representing everything that needs to be executed. If a transient failure occurs, the execution strategy will invoke the delegate again. The following code shows how to implement this approach:

// Use of an EF Core resiliency strategy when using multiple DbContexts

// within an explicit transaction

// See:

// https://docs.microsoft.com/en-us/ef/core/miscellaneous/connection-resiliency

var strategy = \_catalogContext.Database.CreateExecutionStrategy();

await strategy.ExecuteAsync(async () =>

{

// Achieving atomicity between original Catalog database operation and the

// IntegrationEventLog thanks to a local transaction

using (var transaction = \_catalogContext.Database.BeginTransaction())

{

\_catalogContext.CatalogItems.Update(cataloGitem);

await \_catalogContext.SaveChangesAsync();

// Save to EventLog only if product price changed

if (raiseProductPriceChangedEvent) {

await \_integrationEventLogService.SaveEventAsync(priceChangedEvent);

}

transaction.Commit();

}

});

![Image](images/image51.tiff)The first DbContext is the \_catalogContext and the second DbContext is within the \_integrationEventLogService object. Finally, the Commit action would be performed multiple DbContexts and using an EF Execution Strategy.

EF Core Docs

<https://docs.microsoft.com/en-us/ef/>

EF Core: Related Data

<https://docs.microsoft.com/en-us/ef/core/querying/related-data>
Avoid Lazy Loading Entities in ASP.NET Applications

http://ardalis.com/avoid-lazy-loading-entities-in-asp-net-applications

# EF Core or micro-ORM?

While EF Core is a great choice for managing persistence, and for the most part encapsulates database details from application developers, it is not the only choice. Another popular open source alternative is [Dapper](https://github.com/StackExchange/Dapper), a so-called micro-ORM. A micro-ORM is a lightweight, less full-featured tool for mapping objects to data structures. In the case of Dapper, its design goals focus on performance, rather than fully encapsulating the underlying queries it uses to retrieve and update data. Because it doesn’t abstract SQL from the developer, Dapper is “closer to the metal” and lets developers write the exact queries they want to use for a given data access operation.

EF Core has two significant features it provides which separate it from Dapper but also add to its performance overhead. The first is translation from LINQ expressions into SQL. These translations are cached, but even so there is overhead in performing them the first time. The second is change tracking on entities (so that efficient update statements can be generated). This behavior can be [turned off for specific queries](https://docs.microsoft.com/en-us/ef/core/querying/tracking) by using the AsNoTracking extension. EF Core also generates SQL queries that usually are very efficient and in any case perfectly acceptable from a performance standpoint, but if you need fine control over the precise query to be executed, you can pass in custom SQL (or execute a stored procedure) using EF Core, too. In this case, Dapper still outperforms EF Core, but only slightly. Julie Lerman presents some performance data in her May 2016 MSDN article [Dapper, Entity Framework, and Hybrid Apps](https://msdn.microsoft.com/en-us/magazine/mt703432.aspx). Additional performance benchmark data for a variety of data access methods can be found on [the Dapper site](https://github.com/StackExchange/Dapper).

To see how the syntax for Dapper varies from EF Core, consider these two versions of the same method for retrieving a list of items:

// EF Core

private readonly CatalogContext \_context;

public async Task<IEnumerable<CatalogType>> GetCatalogTypes()

{

return await \_context.CatalogTypes.ToListAsync();

}

// Dapper

private readonly SqlConnection \_conn;

public async Task<IEnumerable<CatalogType>> GetCatalogTypesWithDapper()

{

return await \_conn.QueryAsync<CatalogType>("SELECT \* FROM CatalogType");

}

If you need to build more complex object graphs with Dapper, you need to write the associated queries yourself (as opposed to adding an Include as you would in EF Core). This is supported through a variety of syntaxes, including a feature called Multi Mapping that lets you map individual rows to multiple mapped objects. For example, given a class Post with a property Owner of type User, the following SQL would return all the necessary data:

select \* from #Posts p

left join #Users u on u.Id = p.OwnerId

Order by p.Id

Each returned row includes both User and Post data. Since the User data should be attached to the Post data via its Owner property, the following function is used:

(post, user) => { post.Owner = user; return post; }

The full code listing to return a collection of posts with their Owner property populated with the associated user data would be:

var sql = @"select \* from #Posts p

left join #Users u on u.Id = p.OwnerId

Order by p.Id";

var data = connection.Query<Post, User, Post>(sql,

(post, user) => { post.Owner = user; return post;});

Because it offers less encapsulation, Dapper requires developers know more about how their data is stored, how to query it efficiently, and write more code to fetch it. When the model changes, instead of simply creating a new migration (another EF Core feature), and/or updating mapping information in one place in a DbContext, every query that is impacted must be updated. These queries have no compile time guarantees, so they may break at runtime in response to changes to the model or database, making errors more difficult to detect quickly. In exchange for these tradeoffs, Dapper offers extremely fast performance.

For most applications, and most parts of almost all applications, EF Core offers acceptable performance. Thus, its developer productivity benefits are likely to outweigh its performance overhead. For queries that can benefit from caching, the actual query may only be executed a tiny percentage of the time, making relatively small query performance differences moot.

# SQL or NoSQL

Traditionally, relational databases like SQL Server have dominated the marketplace for persistent data storage, but they are not the only solution available. NoSQL databases like [MongoDB](https://www.mongodb.com/what-is-mongodb) offer a different approach to storing objects. Rather than mapping objects to tables and rows, another option is to serialize the entire object graph, and store the result. The benefits of this approach, at least initially, are simplicity and performance. It’s certainly simpler to store a single serialized object with a key than to decompose the object into many tables with relationships and update and rows that may have changed since the object was last retrieved from the database. Likewise, fetching and deserializing a single object from a key-based store is typically much faster and easier than complex joins or multiple database queries required to fully compose the same object from a relational database. The lack of locks or transactions or a fixed schema also makes NoSQL databases very amenable to scaling across many machines, supporting very large datasets.

On the other hand, NoSQL databases (as they are typically called) have their drawbacks. Relational databases use normalization to enforce consistency and avoid duplication of data. This reduces the total size of the database and ensures that updates to shared data are available immediately throughout the database. In a relational database, an Address table might reference a Country table by ID, such that if a country’s name were changed, the address records would benefit from the update without themselves having to be updated. However, in a NoSQL database, Address and its associated Country might be serialized as part of many stored objects. An update to a country name would require all such objects to be updated, rather than a single row. Relational databases can also ensure relational integrity by enforcing rules like foreign keys. NoSQL databases typically do not offer such constraints on their data.

Another complexity NoSQL databases must deal with is versioning. When an object’s properties change, it may not be able to be deserialized from past versions that were stored. Thus, all existing objects that have a serialized (previous) version of the object must be updated to conform to its new schema. This is not conceptually different from a relational database, where schema changes sometimes require update scripts or mapping updates. However, the number of entries that must be modified is often much greater in the NoSQL approach, because there is more duplication of data.

It’s possible in NoSQL databases to store multiple versions of objects, something fixed schema relational databases typically do not support. However, in this case your application code will need to account for the existence of previous versions of objects, adding additional complexity.

NoSQL databases typically do not enforce [ACID](http://en.wikipedia.org/wiki/ACID), which means they have both performance and scalability benefits over relational databases. They’re well-suited to extremely large datasets and objects that are not well-suited to storage in normalized table structures. There is no reason why a single application cannot take advantage of both relational and NoSQL databases, using each where it is best suited.

# Azure Cosmos DB

Azure Cosmos DB is storage globally distributed, multi-model database. Cosmos DB is built for fast and predictable performance, high availability, elastic scaling, and global distribution. It includes support for multiple models, including the schema-less JSON engine DocumentDB. Despite being a NoSQL database, developers can use rich and familiar SQL query capabilities on JSON data with the DocumentDB API. All resources in DocumentDB are stored as JSON documents. Resources are managed as *items*, which are documents containing metadata, and *feeds*, which are collections of items. Figure 8-2 shows the relationship between different DocumentDB resources.

![The hierarchical relationship between resources in DocumentDB, a NoSQL JSON database](images/image-8.png)

Figure 8-2. *DocumentDB resource organization.*

The DocumentDB query language is a simple yet powerful interface for querying JSON documents. The language supports a subset of ANSI SQL grammar and adds deep integration of JavaScript object, arrays, object construction, and function invocation.

Azure Cosmos DB supports the MongoDB API, which can be used with existing MongoDB libraries and tools. It also offers a Table API, for key-value storage, and a Graph API built following the Apache [TinkerPop](http://tinkerpop.apache.org/) specification.

References – Azure Cosmos DB

* Cosmos DB Introduction
  https://docs.microsoft.com/en-us/azure/cosmos-db/introduction

# Other Persistence Options

In addition to relational and NoSQL storage options, ASP.NET Core applications can use Azure Storage to store a variety of data formats and files in a cloud-based, scalable fashion. Azure Storage is massively scalable, so you can start out storing small amounts of data and scale up to storing hundreds or terabytes if your application requires it. Azure Storage supports four kinds of data:

* Blob Storage for unstructured text or binary storage, also referred to as object storage.
* Table Storage for structured datasets, accessible via row keys.
* Queue Storage for reliable queue-based messaging.
* File Storage for shared file access between Azure virtual machines and on-premises applications.

References – Azure Storage

* Azure Storage Introduction
  <https://docs.microsoft.com/en-us/azure/storage/storage-introduction>

# Caching

In web applications, each web request should be completed in the shortest time possible. One way to achieve this is to limit the number of external calls the server must make to complete the request. Caching involves storing a copy of data on the server (or another data store that is more easily queried than the source of the data). Web applications, and especially non-SPA traditional web applications, need to build the entire user interface with every request. This frequently involves making many of the same database queries repeatedly from one user request to the next. In most cases, this data changes rarely, so there is little reason to constantly request it from the database. ASP.NET Core supports response caching, for caching entire pages, and data caching, which supports more granular caching behavior.

When implementing caching, it’s important to keep in mind separation of concerns. Avoid implementing caching logic in your data access logic, or in your user interface. Instead, encapsulate caching in its own classes, and use configuration to manage its behavior. This follows the Open/Closed and Single Responsibility principles, and will make it easier for you to manage how you use caching in your application as it grows.

## ASP.NET Core Response Caching

ASP.NET Core supports two levels of response caching. The first level does not cache anything on the server, but adds HTTP headers that instruct clients and proxy servers to cache responses. This is implemented by adding the ResponseCache attribute to individual controllers or actions:

[ResponseCache(Duration = 60)]

public IActionResult Contact()

{ }

ViewData["Message"] = "Your contact page.";

return View();

}

The above example will result in the following header being added to the response, instructing clients to cache the result for up to 60 seconds.

Cache-Control: public,max-age=60

In order to add server-side in-memory caching to the application, you must reference the Microsoft.AspNetCore.ResponseCaching NuGet package, and then add the Response Caching middleware. This middleware is configured in both ConfigureServices and Configure in Startup:

public void ConfigureServices(IServiceCollection services)

{

services.AddResponseCaching();

}

public void Configure(IApplicationBuilder app)

{
 app.UseResponseCaching();

}

The Response Caching Middleware will automatically cache responses based on a set of conditions, which you can customize. By default, only 200 (OK) responses requested via GET or HEAD methods are cached. In addition, requests must have a response with a Cache-Control: public header, and cannot include headers for Authorization or Set-Cookie. See a [complete list of the caching conditions used by the response caching middleware](https://docs.microsoft.com/en-us/aspnet/core/performance/caching/middleware).

## Data Caching

Rather than (or in addition to) caching full web responses, you can cache the results of individual data queries. For this, you can use in memory caching on the web server, or use [a distributed cache](https://docs.microsoft.com/en-us/aspnet/core/performance/caching/distributed). This section will demonstrate how to implement in memory caching.

You add support for memory (or distributed) caching in ConfigureServices:

public void ConfigureServices(IServiceCollection services)

{

services.AddMemoryCache();

services.AddMvc();

}

Be sure to add the Microsoft.Extensions.Caching.Memory NuGet package as well.

Once you’ve added the service, you request IMemoryCache via dependency injection wherever you need to access the cache. In this example, the CachedCatalogService is using the Proxy (or Decorator) design pattern, by providing an alternative implementation of ICatalogService that controls access to (or adds behavior to) the underlying CatalogService implementation.

public class CachedCatalogService : ICatalogService

{

private readonly IMemoryCache \_cache;

private readonly CatalogService \_catalogService;

private static readonly string \_brandsKey = "brands";

private static readonly string \_typesKey = "types";

private static readonly string \_itemsKeyTemplate = "items-{0}-{1}-{2}-{3}";

private static readonly TimeSpan \_defaultCacheDuration = TimeSpan.FromSeconds(30);

public CachedCatalogService(IMemoryCache cache,

CatalogService catalogService)

{

\_cache = cache;

\_catalogService = catalogService;

}

public async Task<IEnumerable<SelectListItem>> GetBrands()

{

return await \_cache.GetOrCreateAsync(\_brandsKey, async entry =>

{

entry.SlidingExpiration = \_defaultCacheDuration;

return await \_catalogService.GetBrands();

});

}

public async Task<Catalog> GetCatalogItems(int pageIndex, int itemsPage, int? brandID, int? typeId)

{

string cacheKey = String.Format(\_itemsKeyTemplate, pageIndex, itemsPage, brandID, typeId);

return await \_cache.GetOrCreateAsync(cacheKey, async entry =>

{

entry.SlidingExpiration = \_defaultCacheDuration;

return await \_catalogService.GetCatalogItems(pageIndex, itemsPage, brandID, typeId);

});

}

public async Task<IEnumerable<SelectListItem>> GetTypes()

{

return await \_cache.GetOrCreateAsync(\_typesKey, async entry =>

{

entry.SlidingExpiration = \_defaultCacheDuration;

return await \_catalogService.GetTypes();

});

}

}

To configure the application to use the cached version of the service, but still allow the service to get the instance of CatalogService it needs in its constructor, you would add the following in ConfigureServices:

services.AddMemoryCache();

services.AddScoped<ICatalogService, CachedCatalogService>();

services.AddScoped<CatalogService>();

With this in place, the database calls to fetch the catalog data will only be made once per minute, rather than on every request. Depending on the traffic to the site, this can have a very significant impact on the number of queries made to the database, and the average page load time for the home page that currently depends on all three of the queries exposed by this service.

An issue that arises when caching is implemented is *stale data* – that is, data that has changed at the source but an out of date version remains in the cache. A simple way to mitigate this issue is to use small cache durations, since for a busy application there is limited additional benefit to extending the length data is cached. For example, consider a page that makes a single database query, and is requested 10 times per second. If this page is cached for one minute, it will result in the number of database queries made per minute to drop from 600 to 1, a reduction of 99.8%. If instead the cache duration were made one hour, the overall reduction would be 99.997%, but now the likelihood and potential age of stale data are both increased dramatically.

Another approach is to proactively remove cache entries when the data they contain is updated. Any individual entry can be removed if its key is known:

\_cache.Remove(cacheKey);

If your application exposes functionality for updating entries that it caches, you can remove the corresponding cache entries in your code that performs the updates. Sometimes there may be many different entries that depend on a particular set of data. In that case, it can be useful to create dependencies between cache entries, by using a CancellationChangeToken. With a CancellationChangeToken, you can expire multiple cache entries at once by cancelling the token.

// configure CancellationToken and add entry to cache

var cts = new CancellationTokenSource();

\_cache.Set(“cts”, cts);

\_cache.Set(cacheKey,

itemToCache,

new CancellationChangeToken(cts.Token));

// elsewhere, expire the cache by cancelling the token
\_cache.Get<CancellationTokenSource>(“cts”).Cancel();

Caching can dramatically improve the performance of web pages that repeatedly request the same values from the database. Be sure to measure data access and page performance before applying caching, and only apply caching where you see a need for improvement. Caching consumes web server memory resources and increases the complexity of the application, so it’s important you don’t prematurely optimize using this technique.

Testing ASP.NET Core MVC Apps

“If you don’t like unit testing your product, most likely your customers won’t like to test it, either.”

Anonymous

# Summary

Software of any complexity can fail in unexpected ways in response to changes. Thus, testing after making changes is required for all but the most trivial (or least critical) applications. Manual testing is the slowest, least reliable, most expensive way to test software. Unfortunately, if applications are not designed to be testable, it can be the only means available. Applications written following the architectural principles laid out in chapter 4 should be unit testable, and ASP.NET Core applications support automated integration and functional testing as well.

# Kinds of Automated Tests

There are many kinds of automated tests for software applications. The simplest, lowest level test is the unit test. At a slightly higher level there are integration tests and functional tests. Other kinds of tests, like UI tests, load tests, stress tests, and smoke tests, are beyond the scope of this document.

## Unit Tests

A unit test tests a single part of your application’s logic. One can further describe it by listing some of the things that it isn’t. A unit test doesn’t test how your code works with dependencies or infrastructure – that’s what integration tests are for. A unit test doesn’t test the framework your code is written on – you should assume it works or, if you find it doesn’t, file a bug and code a workaround. A unit test runs completely in memory and in process. It doesn’t communicate with the file system, the network, or a database. Unit tests should only test your code.

Unit tests, by virtue of the fact that they test only a single unit of your code, with no external dependencies, should execute extremely quickly. Thus, you should be able to run test suites of hundreds of unit tests in a few seconds. Run them frequently, ideally before every push to a shared source control repository, and certainly with every automated build on your build server.

If you’re testing methods that rely on other services, ideally defined as interfaces and injected as constructor or method arguments, you’ll likely use fake or mock implementations of these interfaces in your unit test. Remember, your goal is only to test the code in a single unit (ideally a single method) of your application, not code this unit references.

## Integration Tests

Although it’s a good idea to encapsulate your code that interacts with infrastructure like databases and file systems, you will still have some of that code, and you will probably want to test it. Additionally, you should verify that your code’s layers interact as you expect when your application’s dependencies are fully resolved. This is the responsibility of integration tests. Integration tests tend to be slower and more difficult to set up than unit tests, because they often depend on external dependencies and infrastructure. Thus, you should avoid testing things that could be tested with unit tests in integration tests. If you can test a given scenario with a unit test, you should test it with a unit test. If you can’t, then consider using an integration test.

Because the purpose of integration tests is to verify that multiple pieces work together, including real infrastructure code, you’ll rarely want to use fake or mock implementations in integration tests. If you do need fake or mock implementations, make sure you’re not accidentally testing these implementations, instead of the real behavior you’re trying to test.

Integration tests will often have more complex setup and teardown procedures than unit tests. For example, an integration test that goes against an actual database will need a way to return the database to a known state before each test run. As new tests are added, and the production database schema evolves, these test scripts will tend to grow in size and complexity. In many large systems, it is impractical to run full suites of integration tests on developer workstations before checking in changes to shared source control. In these cases, integration tests may be run on a build server.

The eShopOnWeb sample includes an OrderRepository that is responsible for fetching and saving Order data. It defines a GetById method. An example integration test for this method is shown below:

public class GetById

{

private readonly CatalogContext \_catalogContext;

private readonly OrderRepository \_orderRepository;

private OrderBuilder OrderBuilder { get; } = new OrderBuilder();

private readonly ITestOutputHelper \_output;

public GetById(ITestOutputHelper output)

{

\_output = output;

var dbOptions = new DbContextOptionsBuilder<CatalogContext>()

.UseInMemoryDatabase(databaseName: "TestCatalog")

.Options;

\_catalogContext = new CatalogContext(dbOptions);

\_orderRepository = new OrderRepository(\_catalogContext);

}

[Fact]

public void GetsExistingOrder()

{

var existingOrder = OrderBuilder.WithDefaultValues();

\_catalogContext.Orders.Add(existingOrder);

\_catalogContext.SaveChanges();

int orderId = existingOrder.Id;

\_output.WriteLine($"OrderId: {orderId}");

var orderFromRepo = \_orderRepository.GetById(orderId);

Assert.Equal(OrderBuilder.TestBuyerId, orderFromRepo.BuyerId);

// Note: Using InMemoryDatabase OrderItems is available. Will be null if using SQL DB.

var firstItem = orderFromRepo.OrderItems.FirstOrDefault();

Assert.Equal(OrderBuilder.TestUnits, firstItem.Units);

}

}

Note that in the above test, an in memory database is used. Entity Framework Core supports using in memory databases for integration testing scenarios where they are helpful because of their fast execution speed and ease of setup. No external database is required to run these integration tests. In the test method, the CatalogContext type is used to set up the database with a known good existing order. Then, the repository implementation type is used to fetch an order by its id. Finally, the test asserts that the Order type returned by the repository was the expected one that was added.

A note of caution when testing with InMemoryDatabase, however, is that it will not validate that eager loading is functioning properly. Navigation properties will be instantiated when using InMemoryDatabase, but may be null when the same code is run against a relational database. To test this scenario, you need to use a real relational database instance in your integration tests.

## Functional Tests

Integration tests are written from the perspective of the developer, to verify that some components of the system work correctly together. Functional tests are written from the perspective of the user, and verify the correctness of the system based on its requirements. The following excerpt offers a useful analogy for how to think about functional tests, compared to unit tests:

“Many times the development of a system is likened to the building of a house. While this analogy isn't quite correct, we can extend it for the purposes of understanding the difference between unit and functional tests. Unit testing is analogous to a building inspector visiting a house's construction site. He is focused on the various internal systems of the house, the foundation, framing, electrical, plumbing, and so on. He ensures (tests) that the parts of the house will work correctly and safely, that is, meet the building code. Functional tests in this scenario are analogous to the homeowner visiting this same construction site. He assumes that the internal systems will behave appropriately, that the building inspector is performing his task. The homeowner is focused on what it will be like to live in this house. He is concerned with how the house looks, are the various rooms a comfortable size, does the house fit the family's needs, are the windows in a good spot to catch the morning sun. The homeowner is performing functional tests on the house. He has the user's perspective. The building inspector is performing unit tests on the house. He has the builder's perspective.”

Source: [Unit Testing versus Functional Tests](http://www.softwaretestingtricks.com/2007/01/unit-testing-versus-functional-tests.html)

I’m fond of saying “As developers, we fail in two ways: we build the thing wrong, or we build the wrong thing.” Unit tests ensure you are building the thing right; functional tests ensure you are building the right thing.

Since functional tests operate at the system level, they may require some degree of UI automation. Like integration tests, they usually work with test infrastructure as well. This makes them slower and more brittle than unit and integration tests. You should have only as many functional tests as you need to be confident the system is behaving as users expect.

In ASP.NET Core applications, unit and integration tests do not typically exercise the full MVC stack, and thus may not test features like routing, model binding, model validation, etc. Functional tests can be used to verify that these UI framework features are implemented correctly. An example of this kind of test is shown at the end of this chapter.

## Testing Pyramid

Martin Fowler wrote about the testing pyramid, an example of which is shown in Figure 9-1.

![C:\Users\steve_000\Dropbox\MicrosoftAuthoring\eBook2017\TestingPyramid.png](images/image-9.png)

Figure 9-1. *The Testing Pyramid*

The different layers of the pyramid, and their relative sizes, represent different kinds of tests and how many you should write for your application. As you can see, the recommendation is to have a large base of unit tests, supported by a smaller layer of integration tests, with an even smaller layer of functional tests. Each layer should ideally only have tests in it that cannot be performed adequately at a lower layer. Keep the testing pyramid in mind when you are trying to decide which kind of test you need for a particular scenario.

## What to Test

A common problem for developers who are inexperienced with writing automated tests is coming up with what to test. A good starting point is to test conditional logic. Anywhere you have a method with behavior that changes based on a conditional statement (if-else, switch, etc.), you should be able to come up at least a couple of tests that confirm the correct behavior for certain conditions. If your code has error conditions, it’s good to write at least one test for the “happy path” through the code (with no errors), and at least one test for the “sad path” (with errors or atypical results) to confirm your application behaves as expected in the face of errors. Finally, try to focus on testing things that can fail, rather than focusing on metrics like code coverage. More code coverage is better than less, generally. However, writing a few more tests of a very complex and business-critical method is usually a better use of time than writing tests for auto-properties just to improve test code coverage metrics.

# Organizing Test Projects

Test projects can be organized however works best for you. It’s a good idea to separate tests by type (unit test, integration test) and by what they are testing (by project, by namespace). Whether this separation consists of folders within a single test project, or multiple test projects, is a design decision. One project is simplest, but for large projects with many tests, or in order to more easily run different sets of tests, you might want to have several different test projects. Many teams organize test projects based on the project they are testing, which for applications with more than a few projects can result in a large number of test projects, especially if you still break these down according to what kind of tests are in each project. A compromise approach is to have one project per kind of test, per application, with folders inside the test projects to indicate the project (and class) being tested.

A common approach is to organize the application projects under a ‘src’ folder, and the application’s test projects under a parallel ‘tests’ folder. You can create matching solution folders in Visual Studio, if you find this organization useful.

![Image](images/image54.png)

Figure 9-2. *Test organization in your solution*

You can use whichever test framework you prefer. The xUnit framework works well and is what all of the ASP.NET Core and EF Core tests are written in. You can add an xUnit test project in Visual Studio using the template shown in Figure 9-3, or from the CLI using dotnet new xunit.

![Image](images/image55.png)

Figure 9-3. *Add an xUnit Test Project in Visual Studio*

## Test Naming

You should [name your tests in a consistent fashion](https://ardalis.com/unit-test-naming-convention), with names that indicate what each test does. One approach I’ve had great success with is to name test classes according to the class and method they are testing. This results in many small test classes, but it makes it extremely clear what each test is responsible for. With the test class name set up to identify the class and method to be tested, the test method name can be used to specify the behavior being tested. This should include the expected behavior and any inputs or assumptions that should yield this behavior. Some example test names:

* CatalogControllerGetImage.CallsImageServiceWithId
* CatalogControllerGetImage.LogsWarningGivenImageMissingException
* CatalogControllerGetImage.ReturnsFileResultWithBytesGivenSuccess
* CatalogControllerGetImage.ReturnsNotFoundResultGivenImageMissingException

A variation of this approach ends each test class name with “Should” and modifies the tense slightly:

* CatalogControllerGetImage**Should**.**Call**ImageServiceWithId
* CatalogControllerGetImage**Should**.**Log**WarningGivenImageMissingException

Some teams find the second naming approach clearer, though slightly more verbose. In any case, try to use a naming convention that provides insight into test behavior, so that when one or more tests fail, it’s obvious from their names what cases have failed. Avoid naming your tests vaguely, such as ControllerTests.Test1, as these offer no value when you see them in test results.

If you follow a naming convention like the one above that produces many small test classes, it’s a good idea to further organize your tests using folders and namespaces. Figure 9-4 shows one approach to organizing tests by folder within several test projects.

![Image](images/image56.png)

Figure 9-4. *Organizing test classes by folder based on class being tested.*

Of course, if a particular application class has many methods being tested (and thus many test classes), it may make sense to place these in a folder corresponding to the application class. This organization is no different than how you might organize files into folders elsewhere. If you have more than three or four related files in a folder containing many other files, it’s often helpful to move them into their own subfolder.

# Unit Testing ASP.NET Core Apps

In a well-designed ASP.NET Core application, most of the complexity and business logic will be encapsulated in business entities and a variety of services. The ASP.NET Core MVC app itself, with its controllers, filters, viewmodels, and views, should require very few unit tests. Much of the functionality of a given action method or handler lies outside the method itself. Testing whether routing works correctly, or global error handling, cannot be done effectively with a unit test. Likewise, any filters, including model validation and authentication and authorization filters, cannot be unit tested. Without these sources of behavior, most handlers and action methods should be trivially small, delegating the bulk of their work to services that can be tested independent of the controllers or pages that use them.

Sometimes you’ll need to refactor your code in order to unit test it. Frequently this involves identifying abstractions and using dependency injection to access the abstraction in the code you’d like to test, rather than coding directly against infrastructure. For example, consider this simple action method for displaying images:

[HttpGet("[controller]/pic/{id}")]

public IActionResult GetImage(int id)

{

var contentRoot = \_env.ContentRootPath + "//Pics";

var path = Path.Combine(contentRoot, id + ".png");

Byte[] b = System.IO.File.ReadAllBytes(path);

return File(b, "image/png");

}

Unit testing this method is made difficult by its direct dependency on System.IO.File, which it uses to read from the file system. You can test this behavior to ensure it works as expected but doing so with real files is an integration test. It’s worth noting you can’t unit test this method’s route – you’ll see how to do this with a functional test shortly.

If you can’t unit test the file system behavior directly, and you can’t test the route, what is there to test? Well, after refactoring to make unit testing possible, you may discover some test cases and missing behavior, such as error handling. What does the method do when a file isn’t found? What should it do? In this example, the refactored method looks like this:

[HttpGet("[controller]/pic/{id}")]

public IActionResult GetImage(int id)

{

byte[] imageBytes;

try

{

imageBytes = \_imageService.GetImageBytesById(id);

}

catch (CatalogImageMissingException ex)

{

\_logger.LogWarning($"No image found for id: {id}");

return NotFound();

}

return File(imageBytes, "image/png");

}

The \_logger and \_imageService are both injected as dependencies. Now you can test that the same id that is passed to the action method is passed to the \_imageService, and that the resulting bytes are returned as part of the FileResult. You can also test that error logging is happening as expected, and that a NotFound result is returned if the image is missing, assuming this is important application behavior (that is, not just temporary code the developer added to diagnose an issue). The actual file logic has moved into a separate implementation service and has been augmented to return an application-specific exception for the case of a missing file. You can test this implementation independently, using an integration test.

In most cases, you’ll want to use global exception handlers in your controllers, so the amount of logic in them should be minimal and probably not worth unit testing. You should do most of your testing of controller actions using functional tests and the TestServer class described below.

# Integration Testing ASP.NET Core Apps

Most of the integration tests in your ASP.NET Core apps should be testing services and other implementation types defined in your Infrastructure project. The best way to test that your ASP.NET Core MVC project is behaving correctly is with functional tests that run against your app running in a test host. An example of an integration test of a data access class is shown in the Integration Testing section earlier in this chapter.

# Functional Testing ASP.NET Core Apps

For ASP.NET Core applications, the TestServer class makes functional tests fairly easy to write. You configure a TestServer using a WebHostBuilder, directly (just as you normally do for your application), or with the WebApplicationFactory type (available since version 2.1). You should try to match your test host to your production host as closely as possible, so your tests will exercise behavior similar to what the app will do in production. The WebApplicationFactory class is helpful for configuring the TestServer’s ContentRoot, which is used by ASP.NET Core to locate static resources like Views.

You can create simple functional tests by creating a test class that implements IClassFixture<WebApplicationFactory<TEntry>>, where TEntry is your application’s Startup class. With this in place, your test fixture can create a client using the factory’s CreateClient method:

public class BasicWebTests : IClassFixture<WebApplicationFactory<Startup>>

{

protected readonly HttpClient \_client;

public BaseWebTest(WebApplicationFactory<Startup> factory)

{

\_client = factory.CreateClient();

}

// write tests that use \_client

}

Frequently, you'll want to perform some additional configuration of your site before each test runs, such as configuring the application to use an in memory data store and then seeding the application with test data. To do this, you should create your own subclass of WebApplicationFactory<TEntry> and override its ConfigureWebHost method. The example below is from the eShopOnWeb FunctionalTests project and is used as part of the tests on the main web application.

using Microsoft.AspNetCore.Hosting;

using Microsoft.AspNetCore.Mvc.Testing;

using Microsoft.EntityFrameworkCore;

using Microsoft.eShopWeb.Infrastructure.Data;

using Microsoft.eShopWeb.Infrastructure.Identity;

using Microsoft.eShopWeb.Web;

using Microsoft.Extensions.DependencyInjection;

using Microsoft.Extensions.Logging;

using System;

namespace Microsoft.eShopWeb.FunctionalTests.Web.Controllers

{

public class CustomWebApplicationFactory<TStartup>

: WebApplicationFactory<Startup>

{

protected override void ConfigureWebHost(IWebHostBuilder builder)

{

builder.ConfigureServices(services =>

{

// Create a new service provider.

var serviceProvider = new ServiceCollection()

.AddEntityFrameworkInMemoryDatabase()

.BuildServiceProvider();

// Add a database context (ApplicationDbContext) using an in-memory

// database for testing.

services.AddDbContext<CatalogContext>(options =>

{

options.UseInMemoryDatabase("InMemoryDbForTesting");

options.UseInternalServiceProvider(serviceProvider);

});

services.AddDbContext<AppIdentityDbContext>(options =>

{

options.UseInMemoryDatabase("Identity");

options.UseInternalServiceProvider(serviceProvider);

});

// Build the service provider.

var sp = services.BuildServiceProvider();

// Create a scope to obtain a reference to the database

// context (ApplicationDbContext).

using (var scope = sp.CreateScope())

{

var scopedServices = scope.ServiceProvider;

var db = scopedServices.GetRequiredService<CatalogContext>();

var loggerFactory = scopedServices.GetRequiredService<ILoggerFactory>();

var logger = scopedServices

.GetRequiredService<ILogger<CustomWebApplicationFactory<TStartup>>>();

// Ensure the database is created.

db.Database.EnsureCreated();

try

{

// Seed the database with test data.

CatalogContextSeed.SeedAsync(db, loggerFactory).Wait();

}

catch (Exception ex)

{

logger.LogError(ex, $"An error occurred seeding the " +

"database with test messages. Error: {ex.Message}");

}

}

});

}

}

}

Tests can make use of this custom WebApplicationFactory by using it to create a client and then making requests to the application using this client instance. The application will have data seeded that can be used as part of the test's assertions. The following test verifies that the home page of the eShopOnWeb application loads correctly and includes a product listing that was added to the application as part of the seed data.

using Microsoft.eShopWeb.FunctionalTests.Web.Controllers;

using Microsoft.eShopWeb.Web;

using System.Net.Http;

using System.Threading.Tasks;

using Xunit;

namespace Microsoft.eShopWeb.FunctionalTests.WebRazorPages

{

public class HomePageOnGet : IClassFixture<CustomWebApplicationFactory<Startup>>

{

public HomePageOnGet(CustomWebApplicationFactory<Startup> factory)

{

Client = factory.CreateClient();

}

public HttpClient Client { get; }

[Fact]

public async Task ReturnsHomePageWithProductListing()

{

// Arrange & Act

var response = await Client.GetAsync("/");

response.EnsureSuccessStatusCode();

var stringResponse = await response.Content.ReadAsStringAsync();

// Assert

Assert.Contains(".NET Bot Black Sweatshirt", stringResponse);

}

}

}

This functional test exercises the full ASP.NET Core MVC / Razor Pages application stack, including all middleware, filters, binders, etc. that may be in place. It verifies that a given route ("/") returns the expected success status code and HTML output. It does so without setting up a real web server, and so avoids much of the brittleness that using a real web server for testing can experience (for example, problems with firewall settings or availability of ports). Functional tests that run against TestServer are usually slower than integration and unit tests, but are much faster than tests that would run over the network to a test web server. You should use functional tests to ensure your application's front-end stack is working as expected. These tests are especially useful when you find duplication in your controllers or pages and you address the duplication by adding filters. Ideally, such a refactoring should not change the behavior of the application, and a suite of functional tests would be able to verify this is the case.

Development process for Azure-hosted ASP.NET Core applications

“With the cloud, individuals and small businesses can snap their fingers and instantly set up enterprise-class services.”

Roy Stephan

# Vision

Develop well-designed ASP .NET Core applications the way you like, using Visual Studio or the dotnet CLI and Visual Studio Code or your editor of choice.

# Development environment for ASP.NET Core apps

## Development tools choices: IDE or editor

Whether you prefer a full and powerful IDE or a lightweight and agile editor, Microsoft has you covered when developing ASP.NET Core applications.

**Visual Studio.** If you’re using *Visual Studio 2017* (or later) you can build ASP.NET Core applications as long as you have the *.NET Core cross-platform development* workload installed. Figure 10-1 shows the required workload in the Visual Studio setup dialog.

![VS2017Workload](images/image57.png)Figure 10-1. *Installing the .NET Core workload in Visual Studio.*

[Download Visual Studio](https://www.visualstudio.com/downloads/)

Visual Studio Code and dotnet CLI (Cross-Platform Tools for Mac, Linux and Windows). If you prefer a lightweight and cross-platform editor supporting any development language, you can use Microsoft Visual Studio Code and the dotnet CLI. These products provide a simple yet robust experience that streamlines the developer workflow. Additionally, Visual Studio Code supports extensions for C# and web development, providing intellisense and shortcut-tasks within the editor.

[Download the .NET Core SDK](https://www.microsoft.com/net/download/core)

[Download Visual Studio Code](https://code.visualstudio.com/download)

# Development workflow for Azure-hosted ASP.NET Core apps

The application development lifecycle starts from each developer’s machine, coding the app using their preferred language and testing it locally. Developers may choose their preferred source control system and can configure Continuous Integration (CI) and/or Continuous Delivery/Deployment (CD) using a build server or based on built-in Azure features.

To get started with developing an ASP.NET Core application using CI/CD, you can use Visual Studio Team Services or your organization’s own Team Foundation Server (TFS).

## Initial Setup

To create a release pipeline for your app, you need to have your application code in source control. Set up a local repository and connect it to a remote repository in a team project. Follow these instructions:

* [Share your code with Git and Visual Studio](https://www.visualstudio.com/en-us/docs/git/share-your-code-in-git-vs) or
* [Share your code with TFVC and Visual Studio](https://www.visualstudio.com/en-us/docs/tfvc/share-your-code-in-tfvc-vs)

Create an Azure App Service where you’ll deploy your application. Create a Web App by going to the App Services blade on the Azure portal. Click +Add, select the Web App template, click Create, and provide a name and other details. The web app will be accessible from {name}.azurewebsites.net.

![AzureWebApp](images/image-10.png)

Figure 10-2. *Creating a new Azure App Service Web App in the Azure Portal.*

Your CI build process will perform an automated build whenever new code is committed to the project’s source control repository. This gives you immediate feedback that the code builds (and, ideally, passes automated tests) and can potentially be deployed. This CI build will produce a web deploy package artifact and publish it for consumption by your CD process.

[Define your CI build process](https://www.visualstudio.com/en-us/docs/build/apps/aspnet/aspnetcore-to-azure)

Be sure to enable continuous integration so the system will queue a build whenever someone on your team commits new code. Test the build and verify that it is producing a web deploy package as one of its artifacts.

When a build succeeds, your CD process will deploy the results of your CI build to your Azure web app. To configure this, you create and configure a *Release*, which will deploy to your Azure App Service.

[Define your CD release process](https://www.visualstudio.com/en-us/docs/build/apps/aspnet/aspnetcore-to-azure)

Once your CI/CD pipeline is configured, you can simply make updates to your web app and commit them to source control to have them deployed.

## Workflow for developing Azure-hosted ASP.NET Core applications

Once you have configured your Azure account and your CI/CD process, developing Azure-hosted ASP.NET Core applications is simple. The following are the basic steps you usually take when building an ASP.NET Core app, hosted in Azure App Service as a Web App, as illustrated in Figure 10-3.

![EndToEndDevDeployWorkflow](images/image-11.png)

Figure 10-3. *Step-by-step workflow for building ASP.NET Core apps and hosting them in Azure.*

###

### Step 1. Local Dev Environment Inner Loop

Developing your ASP.NET Core application for deployment to Azure is no different from developing your application otherwise. Use the local development environment you’re comfortable with, whether that’s Visual Studio or the dotnet CLI and Visual Studio Code or your preferred editor. You can write code, run and debug your changes, run automated tests, and make local commits to source control until you’re ready to push your changes to your shared source control repository.

### Step 2. Application Code Repository

Whenever you’re ready to share your code with your team, you should push your changes from your local source repository to your team’s shared source repository. If you’ve been working in a custom branch, this step usually involves merging your code into a shared branch (perhaps by means of a [pull request](https://www.visualstudio.com/en-us/docs/git/pull-requests)).

### Step 3. Build Server: Continuous Integration. Build, Test, Package

A new build is triggered on the build server whenever a new commit is made to the shared application code repository. As part of the CI process, this build should fully compile the application and run automated tests to confirm everything is working as expected. The end result of the CI process should be a packaged version of the web app, ready for deployment.

### Step 4. Build Server: Continuous Delivery

Once a build as succeeded, the CD process will pick up the build artifacts produced. This will include a web deploy package. The build server will deploy this package to Azure App Service, replacing any existing service with the newly created one. Typically this step targets a staging environment, but some applications deploy directly to production through a CD process.

### Step 5. Azure App Service. Web App.

Once deployed, the ASP.NET Core application runs within the context of an Azure App Service Web App. This Web App can be monitored and further configured using the Azure Portal.

### Step 6. Production Monitoring and Diagnostics

While the Web App is running, you can monitor the health of the application and collect diagnostics and user behavior data. Application Insights is included in Visual Studio, and offers automatic instrumentation for ASP.NET apps. It can provide you with information on usage, exceptions, requests, performance, and logs.

## References

Build and Deploy Your ASP.NET Core App to Azure
<https://www.visualstudio.com/en-us/docs/build/apps/aspnet/aspnetcore-to-azure>

Azure Hosting Recommendations for ASP.NET Core Web Apps

“Line-of-business leaders everywhere are bypassing IT departments to get applications from the cloud (aka SaaS) and paying for them like they would a magazine subscription. And when the service is no longer required, they can cancel the subscription with no equipment left unused in the corner.”

Daryl Plummer, Gartner analyst

# Summary

Whatever your application’s needs and architecture, Microsoft Azure can support it. Your hosting needs can be as simple as a static web site to an extremely sophisticated application made up of dozens of services. For ASP.NET Core monolithic web applications and supporting services, there are several well-known configurations that are recommended. The recommendations below are grouped according to the kind of resource to be hosted, whether full applications, individual processes, or data.

# Web Applications

Web applications can be hosted with:

* App Service Web Apps
* Containers (several options)
* Virtual Machines (VMs)

## Of these, App Service Web Apps is the recommended approach for most scenarios, including simple container-based apps. For microservice architectures, consider a container-based approach. If you need more control over the machines running your application, consider Azure Virtual Machines.

## App Service Web Apps

App Service Web Apps offers a fully managed platform optimized for hosting web applications. It’s a platform as a service(PaaS) offering that lets you focus on your business logic, while Azure takes care of the infrastructure needed to run and scale the app. Some key features of App Service Web Apps:

* DevOps optimization (continuous integration and delivery, multiple environments, A/B testing, scripting support)
* Global scale and high availability
* Connections to SaaS platforms and your on-premises data
* Security and compliance
* Visual Studio integration

Azure App Service is the best choice for most web apps. Deployment and management are integrated into the platform, sites can scale quickly to handle high traffic loads, and the built-in load balancing and traffic manager provide high availability. You can move existing sites to Azure App Service easily with an online migration tool, use an open-source app from the Web Application Gallery, or create a new site using the framework and tools of your choice. The WebJobs feature makes it easy to add background job processing to your App Service web app. If you have an existing ASP.NET application hosted on-premises using a local database, there's a clear path to migrate the app to an App Service Web App with an Azure SQL Database (or secure access to your on-premises database server, if preferred).

![Recommended migration strategy for on-premises .NET apps to Azure App Service](images/image-12.png)

In most cases, moving from a locally hosted ASP.NET app to an App Service Web App is a straightforward process. Little or no modification should be required of the app itself, and it can quickly start to take advantage of the many features that Azure App Service Web Apps offer.

In addition to apps that are not optimized for the cloud, Azure App Service Web Apps are an excellent solution for many simple monolithic (non-distributed) applications, such as many ASP.NET Core apps. In this approach, the architecture is basic and simple to understand and manage:

![Basic Azure architecture](images/image-13.png)

A small number of resources in a single resource group is typically sufficient to manage such an app. Apps that are typically deployed as a single unit, rather than those apps that are made up of many separate processes, are good candidates for this [basic architectural approach](https://docs.microsoft.com/azure/architecture/reference-architectures/app-service-web-app/basic-web-app). Though architecturally simple, this approach still allows the hosted app to scale both up (more resources per node) and out (more hosted nodes) to meet any increase in demand. With autoscale, the app can be configured to automatically adjust the number of nodes hosting the app based on demand and average load across nodes.

## App Service Web Apps for Containers

In addition to support for hosting web apps directly, [App Service Web Apps for Containers](https://azure.microsoft.com/services/app-service/containers/) can be used to run containerized applications on Windows and Linux. Using this service, you can easily deploy and run containerized applications that can scale with your business. The apps have all of the features of App Service Web Apps listed above. In addition, Web Apps for Containers support streamlined CI/CD with Docker Hub, Azure Container Registry, and GitHub. You can use Azure DevOps to define build and deployment pipelines that publish changes to a registry. These changes can then be tested in a staging environment and automatically deployed to production using deployment slots, allowing zero-downtime upgrades. Rolling back to previous versions can be done just as easily.

There are a few scenarios where Web Apps for Containers make the most sense. If you have existing apps that you can containerize, whether in Windows or Linux containers, you can host these easily using this toolset. Simply publish your container and then configure Web Apps for Containers to pull the latest version of that image from your registry of choice. This is a "lift and shift" approach to migrating from classic app hosting models to a cloud-optimized model.

![Migrate containerized on-premises .NET application to Azure Web Apps for Containers](images/image-14.png)

This approach also works well if your development team is able to move to a container-based development process. The "inner loop" of developing apps with containers includes building the app with containers. Changes made to the code as well as to container configuration are pushed to source control, and an automated build is responsible for publishing new container images to a registry like Docker Hub or Azure Container Registry. These images are then used as the basis for additional development, as well as for deployments to production, as shown in the following diagram:

![End to End Docker DevOps Lifecycle Workflow](images/image-15.png)

Developing with containers offers many advantages, especially when containers are used in production. The same container configuration is used to host the app in each environment in which it runs, from local development machine to build and test systems to production. This greatly reduces the likelihood of defects resulting from differences in machine configuration or software versions. Developers can also use whatever tools they're most productive with, including operating system, since containers can run on any OS. In some cases, distributed applications involving many containers may be very resource-intensive to run on a single development machine. In this scenario, it may make sense to upgrade to using Kubernetes and Azure Dev Spaces, covered in the next section.

As portions of larger applications are broken up into their own smaller, independent *microservices*, additional design patterns can be used to improve app behavior. Instead of working directly with individual services, an *API gateway* can simplify access and decouple the client from its back end. Having separate service back ends for different front ends also allows services to evolve in concert with their consumers. Common services can be accessed via a separate *sidecar*container, which might include common client connectivity libraries using the *ambassador* pattern.

![Microservices sample architecture with several common design patterns noted.](images/image-16.png)

[Learn more about design patterns to consider when building microservice-based systems.](https://docs.microsoft.com/azure/architecture/microservices/design/patterns)

## Azure Kubernetes Service

Azure Kubernetes Service (AKS) manages your hosted Kubernetes environment, making it quick and easy to deploy and manage containerized applications without container orchestration expertise. It also eliminates the burden of ongoing operations and maintenance by provisioning, upgrading, and scaling resources on demand, without taking your applications offline.

AKS reduces the complexity and operational overhead of managing a Kubernetes cluster by offloading much of that responsibility to Azure. As a hosted Kubernetes service, Azure handles critical tasks like health monitoring and maintenance for you. Also, you pay only for the agent nodes within your clusters, not for the masters. As a managed Kubernetes service, AKS provides:

* Automated Kubernetes version upgrades and patching.
* Easy cluster scaling.
* Self-healing hosted control plane (masters).
* Cost savings - pay only for running agent pool nodes.

With Azure handling the management of the nodes in your AKS cluster, you no longer need to perform many tasks manually, like cluster upgrades. Because Azure handles these critical maintenance tasks for you, AKS doesn't provide direct access (such as with SSH) to the cluster.

Teams who are leveraging AKS can also take advantage of Azure Dev Spaces. Azure Dev Spaces helps teams to focus on the development and rapid iteration of their microservice application by allowing teams to work directly with their entire microservices architecture or application running in AKS. Azure Dev Spaces also provides a way to independently update portions of your microservices architecture in isolation without affecting the rest of the AKS cluster or other developers.

![Azure Dev Spaces workflow example](images/image.gif)

Azure Dev Spaces:

* Minimize local machine setup time and resource requirements
* Allow teams to iterate more rapidly
* Reduce number of integration environments required by team
* Remove need to mock certain services in distributed system when developing/testing

[Learn more about Azure Dev Spaces](https://docs.microsoft.com/azure/dev-spaces/about)

## Azure Virtual Machines

If you have an existing application that would require substantial modifications to run in App Service, you could choose Virtual Machines in order to simplify migrating to the cloud. However, correctly configuring, securing, and maintaining VMs requires much more time and IT expertise compared to Azure App Service. If you’re considering Azure Virtual Machines, make sure you take into account the ongoing maintenance effort required to patch, update, and manage your VM environment. Azure Virtual Machines is Infrastructure-as-a-Service (IaaS), while App Service is a Platform-as-a-Service (PaaS).

# Logical Processes

Individual logical processes that can be decoupled from the rest of the application may be deployed independently to Azure Functions in a “serverless” manner. Azure Functions lets you just write the code you need for a given problem, without worrying about the application or infrastructure to run it. You can choose from a variety of programming languages, including C#, F#, Node.js, Python, and PHP, allowing you to pick the most productive language for the task at hand. Like most cloud-based solutions, you pay only for the amount of time your use, and you can trust Azure Functions to scale up as needed.

# Data

Azure offers a wide variety of data storage options, so that your application can use the appropriate data provider for the data in question.

For transactional, relational data, Azure SQL Databases are the best option. For high performance read-mostly data, a Redis cache backed by an Azure SQL Database is a good solution.

Unstructured JSON data can be stored in a variety of ways, from SQL Database columns to Blobs or Tables in Azure Storage, to DocumentDB. Of these, DocumentDB offers the best querying functionality, and is the recommended option for large numbers of JSON-based documents that must support querying.

Transient command- or event-based data used to orchestrate application behavior can use Azure Service Bus or Azure Storage Queues. Azure Storage Bus offers more flexibility and is the recommended service for non-trivial messaging within and between applications.

# Architecture Recommendations

Your application’s requirements should dictate its architecture. There are many different Azure services available. Choosing the right one is an important decision. Microsoft offers a gallery of reference architectures to help identify typical architectures optimized for common scenarios. You may find a reference architecture that maps closely to your application’s requirements, or at least offers a starting point.

Figure 11-1 shows an example reference architecture. This diagram describes a recommended architecture approach for a Sitecore content management system website optimized for marketing.

![Image](images/image66.png)

Figure 11-1. *Sitecore marketing website reference architecture.*

References – Azure Hosting Recommendations

* Azure Solution Architectures
  <https://azure.microsoft.com/en-us/solutions/architecture/>
* Azure Basic Web Application Architecture
  <https://docs.microsoft.com/azure/architecture/reference-architectures/app-service-web-app/basic-web-app>
* Design Patterns for Microservices
  <https://docs.microsoft.com/azure/architecture/microservices/design/patterns>
* Azure Developer Guide
  <https://azure.microsoft.com/en-us/campaigns/developer-guide/>
* Web Apps Overview
  <https://docs.microsoft.com/azure/app-service/app-service-web-overview>
* Web Apps for Containers
  <https://azure.microsoft.com/services/app-service/containers/>
* Introduction to Azure Kubernetes Service (AKS)
  <https://docs.microsoft.com/azure/aks/intro-kubernetes>