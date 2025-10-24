<!-- image -->

## DevOps for ASP.NET Core Developers

<!-- image -->

Cam Soper Scott Addie Colin Dembovsky

## EDITION v1.1.0

Refer changelog for the book updates and community contributions.

This guide is available as a downloadable PDF e-book .

PUBLISHED BY

Microsoft Developer Division, .NET, and Visual Studio product teams

A division of Microsoft Corporation

One Microsoft Way

Redmond, Washington 98052-6399

Copyright © 2022 by Microsoft Corporation

All rights reserved. No part of the contents of this book may be reproduced or transmitted in any form or by any means without the written permission of the publisher.

This book is provided "as-is" and expresses the author's views and opinions. The views, opinions, and information expressed in this book, including URL and other Internet website references, may change without notice.

Some examples depicted herein are provided for illustration only and are fictitious. No real association or connection is intended or should be inferred.

Microsoft and the trademarks listed at https://www.microsoft.com on the "Trademarks" webpage are trademarks of the Microsoft group of companies.

Mac and macOS are trademarks of Apple Inc.

The Docker whale logo is a registered trademark of Docker, Inc. Used by permission.

All other marks and logos are property of their respective owners.

## Credits

Authors:

Cam Soper

Scott Addie

Colin Dembovsky

## Welcome

Welcome to the Azure Development Lifecycle guide for .NET! This guide introduces the basic concepts of building a development lifecycle around Azure using .NET tools and processes. After finishing this guide, you'll reap the benefits of a mature DevOps toolchain.

## Who this guide is for

<!-- image -->

<!-- image -->

You should be an experienced ASP.NET Core developer (200-300 level). You don't need to know anything about Azure, as we'll cover that in this introduction. This guide may also be useful for DevOps engineers who are more focused on operations than development.

This guide targets Windows developers. However, Linux and macOS are fully supported by .NET Core. To adapt this guide for Linux/macOS, watch for callouts for Linux/macOS differences.

## What this guide doesn’t cover

This guide is focused on an end-to-end continuous deployment experience for .NET developers. It's not an exhaustive guide to all things Azure, and it doesn't focus extensively on .NET APIs for Azure services. The emphasis is all around continuous integration, deployment, monitoring, and debugging. Near the end of the guide, recommendations for next steps are offered. Included in the suggestions are Azure platform services that are useful to ASP.NET Core developers.

## What’s in this guide

## Tools and downloads

Learn where to acquire the tools used in this guide.

## Deploy to App Service

Learn the various methods for deploying an ASP.NET Core app to Azure App Service.

## Continuous integration and deployment with Azure DevOps

Build an end -to -end continuous integration and deployment solution for your ASP.NET Core app with GitHub, Azure DevOps Services, and Azure.

## Continuous integration and deployment with GitHub Actions

Build an end -to -end continuous integration and deployment solution for your ASP.NET Core app with GitHub, GitHub Actions, and Azure, including code scanning for security and quality using CodeQL.

## Monitor and debug

Use Azure’s tools to monitor, troubleshoot, and tune your application.

## Next steps

Other learning paths for the ASP.NET Core developer learning Azure.

## Additional introductory reading

If this is your first exposure to cloud computing, these articles explain the basics.

- What is Cloud Computing?
- Examples of Cloud Computing
- What is IaaS?
- What is PaaS?

<!-- image -->

## Contents

| Tools and downloads  ..............................................................................................................  1                                                             |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Prerequisites  ................................ ................................................................ ................................................................ .............. 1 |
| Recommended tools (Windows only) ................................ ................................................................ .............................. 1                                |
| Deploy an app to App Service ................................................................................................  3                                                                   |
| Download and test the app ................................................................ ................................................................ ................. 3                    |
| Create the Azure App Service Web App ................................ ................................................................ ......................... 5                                 |
| Deployment with Visual Studio ................................................................ ................................................................ .......... 6                       |
| Deployment slots  ................................ ................................................................ ................................................................ ..... 8       |
| Summary  ................................ ................................................................ ................................................................ ..................  10 |
| Additional reading ................................ ................................................................ ................................ ................................  10         |
| Continuous integration and deployment with Azure DevOps  .........................................  11                                                                                             |
| Publish the app’s code to GitHub  ................................................................ ................................................................ ..  12                         |
| Disconnect local Git deployment  ................................................................ ................................................................ ...  12                         |
| Create an Azure DevOps organization ................................ ................................................................ .........................  13                                |
| Create a team project in Azure DevOps organization  ................................................................ ...........................  13                                               |
| Configure a self-hosted agent if necessary ................................ ................................................................ ................  13                                  |
| Configure the Azure Pipelines pipeline ................................ ................................................................ ........................  14                              |
| Grant Azure DevOps access to the GitHub repository ................................................................ ......................  14                                                     |
| Create the build definition  ................................................................ ................................................................ ...........  16                     |
| Create the release pipeline ................................................................ ................................................................ ...........  18                      |
| Commit changes to GitHub and automatically deploy to Azure ................................................................ .......  22                                                            |
| Examine the Azure Pipelines pipeline ................................ ................................................................ ...........................  23                             |
| Build definition ................................ ................................................................ ................................................................ ..  23         |
| Release pipeline ................................ ................................................................ ................................ ................................  26           |
| Additional reading ................................ ................................................................ ................................ ................................  29         |
| Publish the app’s code to GitHub ................................................................ ................................ ..............................  30                              |
| Disconnect local Git deployment ................................................................ ................................ ...............................  31                              |

| Create an Azure DevOps organization  ................................ ................................................................ ....................  31                            |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Create a team project in Azure DevOps organization ................................................................ .......................  32                                            |
| Configure a self-hosted agent if necessary  ................................ ................................................................ ...........  32                              |
| Configure the Azure Pipelines pipeline ................................ ................................................................ ...................  32                           |
| Commit changes to GitHub and automatically deploy to Azure ................................................................ ..  40                                                         |
| Examine the Azure Pipelines pipeline  ................................ ................................................................ ......................  41                         |
| Additional reading ................................ ................................ ................................................................ ...........................  47      |
| Continuous integration and deployment with GitHub Actions ................................................................ ..........  48                                                  |
| GitHub Actions  ................................ ................................................................ ................................................................ ..  48  |
| Secure code with CodeQL  ................................................................ ................................................................ ............  48                |
| Compare and contrast GitHub Actions and Azure Pipelines  ................................................................ ..........  49                                                   |
| Continuous integration and deployment with GitHub Actions ................................................................ ..........  49                                                  |
| GitHub Actions  ................................ ................................................................ ................................................................ ..  49  |
| Secure code with CodeQL  ................................................................ ................................................................ ............  50                |
| Compare and contrast GitHub Actions and Azure Pipelines  ................................................................ ..........  50                                                   |
| Compare and contrast GitHub Actions and Azure Pipelines ................................................................ ...............  50                                               |
| Pipelines as code ................................ ................................................................ ................................ ..............................  50    |
| Agents and runners ................................ ................................ ................................................................ .........................  51        |
| Comparison of GitHub Actions and Azure Pipelines  ................................................................ .........................  52                                           |
| Build a .NET web app using GitHub Actions  ................................ ................................................................ ..............  55                            |
| Workflow structure ................................ ................................ ................................................................ ..........................  55       |
| Create a basic build workflow ................................................................ ................................................................ .....  56                  |
| Dissect the workflow file  ................................................................ ................................................................ ...............  58           |
| Publish the output ................................ ................................ ................................................................ ...........................  59      |
| Deploy a .NET web app using GitHub Actions ................................ ................................................................ ..........  61                                |
| Environments  ................................ ................................................................ ................................................................ .....  61 |
| Azure authentication ................................................................ ................................................................ .......................  62         |
| Add environments  ................................ ................................ ................................................................ ...........................  63       |
| Deploy to staging ................................ ................................................................ ................................ .............................  65     |
| Deploy to production  ................................................................ ................................................................ .....................  68          |
| ................................ ................................................................ ...........................                                                              |
| Handle environment configuration 71                                                                                                                                                        |

| Final workflow file  ................................ ................................................................ ................................ ............................  73                  |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Secure .NET Code with CodeQL and GitHub Actions ................................ ................................ .............................  75                                                       |
| Create the code scanning workflow  ................................ ................................................................ .........................  76                                        |
| Customize CodeQL settings ................................................................ ................................................................ .........  79                                 |
| Review the security alerts  ................................................................ ................................................................ .............  80                           |
| Monitor and debug ...............................................................................................................  83                                                                     |
| Basic monitoring and troubleshooting  ................................ ................................................................ ........................  83                                      |
| Advanced monitoring  ................................ ................................ ................................................................ .........................  84                     |
| Profile with Application Insights  ................................................................ ................................................................ .....  84                            |
| Logging ................................ ................................................................ ................................................................ .....................  87      |
| Log streaming  ................................ ................................................................ ................................................................ ........  87            |
| Alerts  ................................................................ ................................ ................................................................ ..........................  88 |
| Live debugging ................................ ................................................................ ................................................................ ......  88              |
| Conclusion  ................................ ................................................................ ................................................................ ...............  89        |
| Additional reading ................................ ................................................................ ................................ ................................  89                |
| Next steps  ..............................................................................................................................  90                                                            |
| Storage and databases  ................................................................ ................................................................ .......................  90                      |
| Identity  ................................ ................................................................ ................................................................ ......................  90   |
| Mobile  ................................ ................................................................ ................................................................ .......................  90    |
| Web infrastructure ................................ ................................................................ ................................ ................................  91                |

## Tools and downloads

Azure has several interfaces for provisioning and managing resources, such as the Azure portal , Azure CLI , Azure PowerShell , Azure Cloud Shell, and Visual Studio. This guide takes a minimalist approach and uses the Azure Cloud Shell whenever possible to reduce the steps required. However, the Azure portal must be used for some portions.

## Prerequisites

The following subscriptions are required:

- Azure — If you don't have an account, get a free trial .
- Azure DevOps Services — your Azure DevOps subscription and organization is created in Chapter 4.
- GitHub — If you don't have an account, sign up for free .

The following tools are required:

- Git — A fundamental understanding of Git is recommended for this guide. Review the Git documentation, specifically git remote and git push .
- .NET Core SDK — Version 2.1.300 or later is required to build and run the sample app. If Visual Studio is installed with the .NET Core cross -platform development workload, the .NET Core SDK is already installed.

Verify your .NET Core SDK installation. Open a command shell, and run the following command:

:::{custom-style=CodeBox} dotnetcli dotnet --version :::

## Recommended tools (Windows only)

- Visual Studio's robust Azure tools provide a GUI for most of the functionality described in this guide. Any edition of Visual Studio will work, including the free Visual Studio Community Edition. The tutorials are written to demonstrate development, deployment, and DevOps both with and without Visual Studio.

Confirm that Visual Studio has the following workloads installed:

- – ASP.NET and web development
- – Azure development

- – .NET Core cross -platform development

## Deploy an app to App Service

Azure App Service is Azure's web hosting platform. Deploying a web app to Azure App Service can be done manually or by an automated process. This section of the guide discusses deployment methods that can be triggered manually or by script using the command line, or triggered manually using Visual Studio.

In this section, you’ll accomplish the following tasks:

[!div class=“checklist”]

- Download and build the sample app.
- Create an Azure App Service Web App using the Azure Cloud Shell.
- Deploy the sample app to Azure using Git.
- Deploy a change to the app using Visual Studio.
- Add a staging slot to the web app.
- Deploy an update to the staging slot.
- Swap the staging and production slots.

## Download and test the app

The app used in this guide is a pre-built ASP.NET Core app, Simple Feed Reader. It's an ASP.NET Core Razor Pages app that uses the Microsoft.SyndicationFeed.ReaderWriter API to retrieve an RSS/Atom feed and display the news items in a list.

Feel free to review the code, but it's important to understand that there's nothing special about this app. It's just a simple ASP.NET Core app for illustrative purposes.

From a command shell, download the code, build the project, and run it as follows.

## Note

Linux and macOS users should make appropriate changes for paths, for example, using forward slash (/) rather than back slash (\).*

1. Clone the code to a folder on your local machine.

Home page - SimpleFee X

Gi. Command Prompt - dotnet run

→

localhost:5000/?FeedUrl=http%3A%2F%2F1

- • ×

* 2 ..

C: \5rc\simple-feed-reader\SimpleFeedReader&gt;dotnet run

Hosting environment: Production

- :::{custom-style=CodeBox} console git clone https://github.com/dotnet-architecture/simplefeed -reader/ :::
2. Change your working folder to the simple-feed-reader folder that was created.

SimpleFeedReader

Enter a feed URL:

http://feeds.hanselman.c

- :::{custom-style=CodeBox} console cd .\simple-feed-reader\SimpleFeedReader :::

Retrieve Feed

Title

3. Restore the packages, and build the solution.
2. :::{custom-style=CodeBox} dotnetcli dotnet build :::
4. Run the app.

6/15/2018 11:50:21 PM

+00:00

:::{custom-style=CodeBox} dotnetcli dotnet run :::

ASP.NET Core Architect David Fowler's hidden gems in 2.1

Carriage Returns and Line Feeds will ultimately bite you - Some Git Tips

<!-- image -->

5. Open a browser and navigate to http://localhost:5000. The app allows you to type or paste a syndication feed URL and view a list of news items.

<!-- image -->

6. Once you're satisfied the app is working correctly, shut it down by pressing Ctrl+C in the command shell.

## Create the Azure App Service Web App

To deploy the app, you'll need to create an App Service Web App. After creation of the Web App, you'll deploy to it from your local machine using Git.

1. Sign in to the Azure Cloud Shell. Note: When you sign in for the first time, Cloud Shell prompts to create a storage account for configuration files. Accept the defaults or provide a unique name.
2. Use the Cloud Shell for the following steps.
- a. Declare a variable to store your web app's name. The name must be unique to be used in the default URL. Using the $RANDOM Bash function to construct the name guarantees uniqueness and results in the format webappname99999.

:::{custom-style=CodeBox} console webappname=mywebapp$RANDOM :::

- b. Create a resource group. Resource groups provide a means to aggregate Azure resources to be managed as a group.
2. :::{custom-style=CodeBox} azurecli az group create --location centralus --name AzureTutorial :::

The az command invokes the Azure CLI. The CLI can be run locally, but using it in the Cloud Shell saves time and configuration.

- c. Create an App Service plan in the S1 tier. An App Service plan is a grouping of web apps that share the same pricing tier. The S1 tier isn't free, but it's required for the staging slots feature.

:::{custom-style=CodeBox} azurecli az appservice plan create --name $webappname -resource-group AzureTutorial --sku S1 :::

- d. Create the web app resource using the App Service plan in the same resource group.

:::{custom-style=CodeBox} azurecli az webapp create --name $webappname --resourcegroup AzureTutorial --plan $webappname :::

- e. Set the deployment branch to main in the appsettings configuration.

:::{custom-style=CodeBox} azurecli az webapp config appsettings set --name $webappname --resource-group AzureTutorial --settings DEPLOYMENT\_BRANCH=main :::

- f. Set the deployment credentials. These deployment credentials apply to all the web apps in your subscription. Don't use special characters in the user name.

:::{custom-style=CodeBox} azurecli az webapp deployment user set --user-name REPLACE\_WITH\_USER\_NAME --password REPLACE\_WITH\_PASSWORD :::

- g. Configure the web app to accept deployments from local Git and display the Git deployment URL . Note this URL for reference later .

:::{custom-style=CodeBox} azurecli echo Git deployment URL: $(az webapp deployment source config-local-git --name $webappname --resource-group AzureTutorial --query url -output tsv) :::

- h. Display the web app URL. Browse to this URL to see the blank web app. Note this URL for reference later .
2. :::{custom-style=CodeBox} console echo Web app URL:

http://$webappname.azurewebsites.net :::

3. Using a command shell on your local machine, navigate to the web app's project folder (for example, *.-feed-reader). Execute the following commands to set up Git to push to the deployment URL:
- a. Add the remote URL to the local repository.
3. :::{custom-style=CodeBox} console git remote add azure-prod GIT\_DEPLOYMENT\_URL :::
- b. Push the local default branch (main) to the azure-prod remote's deployment branch (main).

:::{custom-style=CodeBox} console git push azure-prod main :::

You'll be prompted for the deployment credentials you created earlier. Observe the output in the command shell. Azure builds the ASP.NET Core app remotely.

4. In a browser, navigate to the Web app URL and note the app has been built and deployed. Additional changes can be committed to the local Git repository with git commit. These changes are pushed to Azure with the preceding git push command.

## Deployment with Visual Studio

## Note

This section applies to Windows only. Linux and macOS users should make the change described in step 2 below. Save the file, and commit the change to the local repository with git commit. Finally, push the change with git push, as in the first section.*

The app has already been deployed from the command shell. Let's use Visual Studio's integrated tools to deploy an update to the app. Behind the scenes, Visual Studio accomplishes the same thing as the command line tooling, but within Visual Studio's familiar UI.

1. Open SimpleFeedReader.sln in Visual Studio.
2. In Solution Explorer, open Pages.cshtml. Change &lt;h2&gt;Simple Feed Reader&lt;/h2&gt; to &lt;h2&gt;Simple Feed Reader - V2&lt;/h2&gt;.
3. Press Ctrl+Shift+B to build the app.
4. In Solution Explorer, right-click on the project and click Publish .

App Service

Host your web and mobile applications, REST APls, and more in Azure

Subscription

Solution Explorer

Microsoft casoper@microsoft.com

Search Solution Explorer (Ctri+:)

1 Solution SimpleFeedReader' (1 project)

Im SimpleFeedReadi

Build vs-beta

View

Resource Group

Search

4

Rebuild

Clean

View

Pack

Publish...

Overview

Scope to This

New Solution Explorer View

Show on Code Map

File Nesting

AzureTutorial

Edit SimpleFeedReader.csproj

Add mywebapp14483

casoper-blog

Manage NuGet Packages...

Manage User Secrets

Set as StartUp Project

Debug

Source Control

Cut

Remove

Rename

Unload Project

Open Folder in File Explorer

Properties

Connected Services

Dependencies

•Properties

Pages

Repositories appsettings.json

<!-- image -->

5. Visual Studio can create a new App Service resource, but this update will be published over the existing deployment. In the Pick a publish target dialog, select App Service from the list on the left, and then select Select Existing. Click Publish .
6. In the App Service dialog, confirm that the Microsoft or Organizational account used to create your Azure subscription is displayed in the upper right. If it's not, click the drop-down and add it.
7. Confirm that the correct Azure Subscription is selected. For View, select Resource Group . Expand the AzureTutorial resource group and then select the existing web app. Click OK .

<!-- image -->

Visual Studio builds and deploys the app to Azure. Browse to the web app URL. Validate that the &lt;h2&gt; element modification is live.

XX

X

• = 1] Home page - SimpleFer X + v

→

mywebapp14483.azurewebsites.net/

SimpleFeedReader

Simple Feed Reader - V2

Enter a feed URL:

Retrieve Feed

© 2017 - SimpleFeedReader

- • x

# R

<!-- image -->

## Deployment slots

Deployment slots support the staging of changes without impacting the app running in production. Once the staged version of the app is validated by a quality assurance team, the production and staging slots can be swapped. The app in staging is promoted to production in this manner. The following steps create a staging slot, deploy some changes to it, and swap the staging slot with production after verification.

1. Sign in to the Azure Cloud Shell, if not already signed in.
2. Create the staging slot.
- a. Create a deployment slot with the name staging .
4. :::{custom-style=CodeBox} azurecli az webapp deployment slot create --name $webappname --resource-group AzureTutorial --slot staging :::
- b. Set the deployment branch to main in the appsettings configuration.
6. :::{custom-style=CodeBox} azurecli az webapp config appsettings set --name $webappname --resource-group AzureTutorial --slot staging --settings DEPLOYMENT\_BRANCH=main :::
- c. Configure the staging slot to use deployment from local Git and get the staging deployment URL. Note this URL for reference later .
8. :::{custom-style=CodeBox} azurecli echo Git deployment URL for staging: $(az webapp deployment source config-local-git --name $webappname --resource-group AzureTutorial -slot staging --query url --output tsv) :::
- d. Display the staging slot's URL. Browse to the URL to see the empty staging slot. Note this URL for reference later .

9 • 1] Home page - SimpleFer × + ~

© mywebapp14483.azurewebsites.net/

SimpleFeedReader

Simple Feed Reader - V2

Enter a feed URL:

Retrieve Feed

© 2017 - SimpleFeedReader

3. In a text editor or Visual Studio, modify Pages/Index.cshtml again so that the &lt;h2&gt; element reads &lt;h2&gt;Simple Feed Reader - V3&lt;/h2&gt; and save the file.

SimpleFeedReader

Enter a feed URL:

4. Commit the file to the local Git repository, using either the Changes page in Visual Studio's Team Explorer tab, or by entering the following using the local machine's command shell:

Retrieve Feed

:::{custom-style=CodeBox} console git commit -a -m "upgraded to V3" :::

© 2017 - SimpleFeedReader

5. Using the local machine's command shell, add the staging deployment URL as a Git remote and push the committed changes:
- a. Add the remote URL for staging to the local Git repository.

:::{custom-style=CodeBox} console git remote add azure-staging

&lt;Git\_staging\_deployment\_URL&gt; :::

- b. Push the local default branch (main) to the azure-staging remote's deployment branch (main).

:::{custom-style=CodeBox} console git push azure-staging main :::

Wait while Azure builds and deploys the app.

6. To verify that V3 has been deployed to the staging slot, open two browser windows. In one window, navigate to the original web app URL. In the other window, navigate to the staging web app URL. The production URL serves V2 of the app. The staging URL serves V3 of the app.
7. In the Cloud Shell, swap the verified/warmed-up staging slot into production.

<!-- image -->

-0 ×

- :::{custom-style=CodeBox} console echo Staging web app URL: http://$webappnamestaging.azurewebsites.net :::

0 11 Home page- Simplefee × + v

O mywebapp14483.azurewebsites.net/

SimpleFeedReader

Simple Feed Reader - V3

Enter a feed URL:

Retrieve Feed

-

2 ...

:::{custom-style=CodeBox} azurecli az webapp deployment slot swap --name $webappname --resource-group AzureTutorial --slot staging :::

8. Verify that the swap occurred by refreshing the two browser windows.

4 5 1 Home page-Simplefet X

&lt;&gt; O

Omywebapp14483-staging.azurewebsites.net/

SimpleFeedReader

Simple Feed Reader - V2

Enter a feed URL:

Retrieve Feed

© 2017 - SimpleFeedReader

-

0 ×

<!-- image -->

## Summary

In this section, the following tasks were completed:

- Downloaded and built the sample app.
- Created an Azure App Service Web App using the Azure Cloud Shell.
- Deployed the sample app to Azure using Git.
- Deployed a change to the app using Visual Studio.
- Added a staging slot to the web app.
- Deployed an update to the staging slot.
- Swapped the staging and production slots.

In the next section, you’ll learn how to build a DevOps pipeline with Azure Pipelines.

## Additional reading

- Web Apps overview
- Build a .NET Core and SQL Database web app in Azure App Service
- Configure deployment credentials for Azure App Service
- Set up staging environments in Azure App Service

## Continuous integration and deployment with Azure DevOps

## Note

This section details continuous integration and deployment with Azure DevOps. You can achieve that with GitHub Actions as well. GitHub Actions is a workflow engine built into GitHub that can also be used for continuous integration and deployment. To follow the guide for building and deploying to Azure using GitHub, complete the Publish the app's code to GitHub and Disconnect local Git deployment sections below and then proceed to the GitHub Actions section .

In the previous chapter, you created a local Git repository for the Simple Feed Reader app. In this chapter, you'll publish that code to a GitHub repository and construct an Azure DevOps Services pipeline using Azure Pipelines. The pipeline enables continuous builds and deployments of the app. Any commit to the GitHub repository triggers a build and a deployment to the Azure Web App's staging slot.

In this section, you’ll complete the following tasks:

[!div class=“checklist”]

- Publish the app's code to GitHub
- Disconnect local Git deployment
- Create an Azure DevOps organization
- Create a team project in Azure DevOps organization
- Configure a self-hosted agent if necessary
- Create a build definition
- Create a release pipeline
- Commit changes to GitHub and automatically deploy to Azure
- Examine the Azure Pipelines pipeline

## Publish the app’s code to GitHub

1. Open a browser window, and navigate to https://github.com.
2. Click the + drop-down in the header, and select New repository:
1. Select your account in the Owner drop-down, and enter simple-feed-reader in the Repository name textbox.
2. Click the Create repository button.
3. Open your local machine's command shell. Navigate to the directory in which the simple-feedreader Git repository is stored.
4. Rename the existing origin remote to upstream. Execute the following command:
7. :::{custom-style=CodeBox} console git remote rename origin upstream :::
5. Add a new origin remote pointing to your copy of the repository on GitHub. Execute the following command:
6. Publish your local Git repository to the newly created GitHub repository. Execute the following command:
10. :::{custom-style=CodeBox} console git push -u origin main :::
7. Open a browser window, and navigate to https://github.com/&lt;GitHub\_username&gt;/simplefeed -reader/. Validate that your code appears in the GitHub repository.

<!-- image -->

```
:::{custom-style=CodeBox} console git remote add origin https://github.com/<GitHub_username>/simple-feed-reader/ :::
```

## Disconnect local Git deployment

Remove the local Git deployment with the following steps. Azure Pipelines (an Azure DevOps service) both replaces and augments that functionality.

1. Open the Azure portal, and navigate to the staging (mywebapp&lt;unique\_number&gt;/staging) Web App. The Web App can be quickly located by entering staging in the portal's search box:

<!-- image -->

Click Deployment Center. A new panel appears. Click Disconnect to remove the local Git source control configuration that was added in the previous chapter. Confirm the removal operation by clicking the Yes button.

1. Navigate to the mywebapp App Service. As a reminder, the portal's search box can be used to quickly locate the App Service.
2. Click Deployment Center. A new panel appears. Click Disconnect to remove the local Git source control configuration that was added in the previous chapter. Confirm the removal operation by clicking the Yes button.

## Create an Azure DevOps organization

1. Open a browser, and navigate to the Azure DevOps organization creation page .
2. Select New organization
3. Confirm the information, and then select Continue .
4. Sign in to your organization at any time, https://dev.azure.com/{yourorganization}

## Create a team project in Azure DevOps organization

1. Choose the organization, and then select New project .
2. Enter the project name as MyFirstProject and select the Visibility as Private
3. Select Create project .

For more information, see Create a project

## Configure a self -hosted agent if necessary

To build your code or deploy your software using Azure Pipelines, you need at least one agent. In Azure Pipelines, you can run parallel jobs on either Microsoft-hosted or self-hosted agent. But with the recent change in Azure Pipelines free grant of parallel jobs is temporarily disable for the public projects.For more details, refer Configure and pay for parallel jobs .

Go to Organization Settings and then Pipelines &gt; Parallel jobs. If you see value 0 under Microsofthosted that means you need a Self-hosted agent to run your pipeline.

Jobs Agents Details Security Settings Maintenance History

Public projects

Free

Last run l

Yesterday

Microsoft-hosted O

Current status

Idle

Agent version

2.185.1

<!-- image -->

You can create that by following details mentioned in Self-hosted agents. After successful configuration, you'll be able to see available agent under Organization Settings &gt; Agent pools &gt; {youragentname}

<!-- image -->

## Configure the Azure Pipelines pipeline

There are three distinct steps to complete. Completing the steps in the following three sections results in an operational DevOps pipeline.

## Grant Azure DevOps access to the GitHub repository

1. In your project, navigate to the Pipelines page. Then choose the action to create a new pipeline:

<!-- image -->

use use the classic ealtor to create the pipeline.

Connect

Select

Configure

Review

• We need your authorization to access your repositories

New pipeline

Where is your code?

Connection name *

Azure Repos Git

1. Use Use the classic editor to create the pipeline.

• Bitbucket Cloud YAML

Authorize using Auth

Hosted by Atlassian

YAML

Home to the world's largest community of developers

• Goreto

GitHub Enterprise Server

YAML

Are sul Enterprise sever u enterprise

Other Git

Any generic Git repository

= Subversion

Centralized version control by Apache

Use the classic editor to create a pipeline without YAML.

Select the GitHub option from the Select a source section::

Select a source

<!-- image -->

VSTS Git

1. Select the GitHub option from the Select a source section::

External Git

<!-- image -->

1. Authorization is required before Azure DevOps can access your GitHub repository. Enter GitHub connection in the Connection name textbox. For example:
1. If two -factor authentication is enabled on your GitHub account, a personal access token is required. In that case, click the Authorize with a GitHub personal access token link. See the official GitHub personal access token creation instructions for help. Only the repo scope of permissions is needed. Otherwise, click the Authorize using OAuth button.

<!-- image -->

Tasks Variables Triggers Options Retention History

Pipeline

Select a template

Buld pipeine

Name

MyFirstProject-ASP.NET Core (.NET Framework)-Cl

Or start with an at Empty pipeline y Get sources

© sughoreo/simple-feed-resder 2 main

Agent job 1

3 Run on agent

Use NuGet 4.4.1

Others

NuGet restore

Visual Studio buld

* But solution

Visual Studio Test dotnet

A Test sembles

Publish symbols path

Publish build artifacts

1 Push out stact

+

Agent pool * @ | Pool information | Manage E

Default

ASP.NET Corel

" U

2. When prompted, sign in to your GitHub account. Then select Authorize to grant access to your Azure DevOps organization. If successful, a new service endpoint is created.
3. Click the ellipsis button next to the Repository button. Select the /simple-feed-reader repository from the list. Click the Select button.
4. Select the default branch (main) from the Default branch for manual and scheduled builds drop-down. Click the Continue button. The template selection page appears.

## Create the build definition

1. From the template selection page, enter ASP.NET Core in the search box:
1. The template search results appear. Hover over the ASP.NET Core template, and click the Apply button.
2. The Tasks tab of the build definition appears. Select the self-hosted Agent pool if you have created that in the earlier step.
4. &gt; [!NOTE]
5. &gt; If you are using MS-hosted agent then select the *Hosted &gt; Azure Pipelines* from drop down.

<!-- image -->

<!-- image -->

• Save &amp; queue v &gt; Discard

= Summary &gt; Queue ...

X

inal the type arop-aown is set to include. sel tne branch spectication arop-aown to main.

Save build definition

• Enable continuous integration l

Save &amp; queue V

Select folder *

\

I Batch changes while a build is in progress

H

Save &amp; queue

Comment

Branch filters

1. Click the Triggers tab.

Save

Type

Save as draft

Include

+ Add

Path filters

+ Add

2. Check the Enable continuous integration box. Under the Branch filters section, confirm that the Type drop-down is set to Include. Set the Branch specification drop-down to main .

Save

<!-- image -->

Cancel

These settings cause a build to trigger when any change is pushed to the default branch (*main*) of the GitHub repository. Continuous integration is tested in the [Commit changes to GitHub and automatically deploy to Azure](#commit-changes-togithub-and-automatical) section.

1. Click the Save &amp; queue button, and select the Save option:
1. The following modal dialog appears:

<!-- image -->

<!-- image -->

Use the default folder of *\\*, and click the **Save** button.

...

bicke keleases la lyour team project. Click ne new pipenne Dulton.

rrom the template selection page, enter ApP service Deployment In the search Dox.

- Overview

E Boards

Select a template

Or start with an la Empty job

Repos

Pipelines

Featured a Pipelines

di Environments

* Releases

001 Library

## Create the release pipeline

Deploy your application to Azure App Service. Choose from

WebJobs.

1. Click the Releases tab of your team project. Click the New pipeline button.

• Task groups

Others

*** Deployment groups

• Test Plans

Artifacts

Azure App Service deployment with continuous monitoring

Deploy your Web applications to Azure App Service and enable continuous monitoring using Application Insights.

Azure App Service deployment with slot

Deploy your Azure Web App to a staging slot and swap slots tol deploy to production.

Azure App Service deployment with tests and performance tests

Deploy your Azure Web App and run tests or cloud-based web performance tests.

Azure Service Fabric Compose deployment

Deploy a Docker Compose application to a Service Fabric cluster.

Azure Service Fabric deployment

<!-- image -->

The template selection pane appears.

1. From the template selection page, enter App Service Deployment in the search box:
1. The template search results appear. Hover over the Azure App Service Deployment with Slot template, and click the Apply button. The Pipeline tab of the release pipeline appears.

<!-- image -->

Azure App Service Deplo! X

click tre ada Dulton in che Artitacts Dox. ne Ada artitact panel appedis.

All pipelines › ** New release pipeline

Add artifact

Pipeline

• Tasks v

Variables

Source type

Artifacts | + Add

V Build artifact

+ Add an

3 more artifact types V

Schedule

Project *

not set

MyFirstProject

Source (Build definition) *

This setting is required.

Add

1. Click the Add button in the Artifacts box. The Add artifact panel appears:
1. Select the Build tile from the Source type section. This type allows for the linking of the release pipeline to the build definition.
2. Select MyFirstProject from the Project drop-down.
3. Select the build definition name, MyFirstProject-ASP.NET Core-CI, from the Source (Build definition) drop-down.
4. Select Latest from the Default version drop-down. This option builds the artifacts produced by the latest run of the build definition.

<!-- image -->

Retention Options

History

Stages | + Add v

<!-- image -->

LAUN

Stages | + Add v

R

+ Add

Stage

Production

5. Replace the text in the Source alias textbox with Drop .
6. Click the Add button. The Artifacts section updates to display the changes.
7. Click the lightning bolt icon to enable continuous deployments:

Drop

Schedule not set

<!-- image -->

With this option enabled, a deployment occurs each time a new build is available.

1. A Continuous deployment trigger panel appears to the right. Click the toggle button to enable the feature. It isn't necessary to enable the Pull request trigger .
2. Click the Add drop-down in the Build branch filters section. Choose the Build Definition's default branch option. This filter causes the release to trigger only for a build from the GitHub repository's default branch (main).
3. Click the Save button. Click the OK button in the resulting Save modal dialog.
4. Click the Stage 1 box. An Stage panel appears to the right. Change the Stage 1 text in the Stage name textbox to Production .
1. Click the 1 phase, 2 tasks link in the Production box:

<!-- image -->

Artifacts

W Delete ^ Move V ...

belect the sell-mosted get poor you have created Inal In the earler step.

Production

Deployment process

Run on agent

Stages | + Add v

# Run on agent

Azure App Service deploy

Deploy Azure App Service to Slot

Azure Ano Service manage

* Manage Azure App Service - Slot Swap

Agent job O

Display name*

Run on agent

Agent selection ^

Agent pool • | Pool information | Manage C

Default

<!-- image -->

Production

• 1 job, 2 tasks

The **Tasks** tab of the environment appears.

1. Click the Deploy Azure App Service to Slot task. Its settings appear in a panel to the right.
2. Select the Azure subscription associated with the App Service from the Azure subscription drop-down. Once selected, click the Authorize button.
3. Select Web App from the App type drop-down.
4. Select mywebapp/ from the App service name drop-down.
5. Select AzureTutorial from the Resource group drop-down.
6. Select staging from the Slot drop-down.
7. Select Run on agent* under Tasks. On the right pane, you'll see Agent Job .
8. Select the self -hosted Agent pool if you have created that in the earlier step.
9. &gt; [!NOTE]
10. &gt; If you are using MS-hosted agent then select the *Hosted &gt; Azure Pipelines* from drop down.
1. Click the Save button.
2. Hover over the default release pipeline name. Click the pencil icon to edit it. Use MyFirstProject-ASP.NET Core-CD as the name.

<!-- image -->

• Remove

Tasks

• MyFirstProject / MyFirst... V

Dashboards Code Work

Triggers

-

Continuous integration

Builds

Releases

Library

Options

Retention

History

Task Groups Deployment Groups scottaddie/simple-feed-reader

Enabled

All definitions ›

Build an

Save &amp; queue V

• scottaddie/simple-feed-reader

<!-- image -->

1. Click the Save button.

## Commit changes to GitHub and automatically deploy to Azure

1. Open SimpleFeedReader.sln in Visual Studio.
2. In Solution Explorer, open Pages.cshtml. Change &lt;h2&gt;Simple Feed Reader - V3&lt;/h2&gt; to &lt;h2&gt;Simple Feed Reader - V4&lt;/h2&gt;.
3. Press Ctrl+Shift+B to build the app.
4. Commit the file to the GitHub repository. Use either the Changes page in Visual Studio's Team Explorer tab, or execute the following using the local machine's command shell:
5. :::{custom-style=CodeBox} console git commit -a -m "upgraded to V4" :::
5. Push the change in the default branch (main) to the origin remote of your GitHub repository. In the following command, replace the placeholder {BRANCH} with the default branch (use main):

:::{custom-style=CodeBox} console git push origin {BRANCH} :::

The commit appears in the GitHub repository's default branch (main). You'll be able to see the commit history in https://github.com/&lt;GitHub\_username&gt;/simple-feedreader/commits/main.

The build is triggered, since continuous integration is enabled in the build definition's Triggers tab:

<!-- image -->

Variables

aown sous delalls.

butter to see more delals or each step.

Notice Inal te v4 text appears In the neaaing.

O Search all pipelines

Pipelines

Recent All Runs

+ New v

MyFirstProject-ASP.NET Core-..

Recently run pipelines

@ Production

Pipeline

Enter a feed URL:

Retrieve Feed

MyFirstProject-ASP.NET Core-CD

SimpleFeedReader

Releases

Deployments

Analytics

Releases

Release-3

Last run sia 20210420.... ¿ main

#20210420.5 • Update Index cshtml

New pipeline

Edit

* Create release

T Filter pipelines

# All releases v

(Just now

Simple Feed Reader - V4

1. Navigate to the Pipelines. You'll see the CI pipeline details and monitor each steps if you drill down Jobs details.
1. Similarly, go to the Releases tab to see the details of CD pipeline. You can always drill down further to see more details of each step.
1. Once the build succeeds, a deployment to Azure occurs. Navigate to the app in the browser. Notice that the "V4" text appears in the heading:

<!-- image -->

<!-- image -->

<!-- image -->

## Examine the Azure Pipelines pipeline

## Build definition

A build definition was created with the name MyFirstProject-ASP.NET Core-CI. Upon completion, the build produces a .zip file including the assets to be published. The release pipeline deploys those assets to Azure.

The build definition’s Tasks tab lists the individual steps being used. There are five build tasks.

Created

4/20/2021, 12:58:08 PM

Stages

© Production

• ... › MyFirstProject-ASP.NET Core (NET Framework)-C|

Options Retention History

Tasks Variables Triggers m

Pipeline

Build pipeline

= Get sources

• sughosneo/simple-feed-reader

Agent job 1

= Run on agent

Use NuGet 4.4.1

#• NuGet tool installer

NuGet restore

NuGet

• Build solution

Visual Studio build

Test Assemblies

Visual Studio Test

Publish Artifact

Publish build artifacts

<!-- image -->

1. Restore — Executes the dotnet restore command to restore the app's NuGet packages. The default package feed used is nuget.org.
2. Build — Executes the dotnet build --configuration release command to compile the app's code. This --configuration option is used to produce an optimized version of the code, which is suitable for deployment to a production environment. Modify the BuildConfiguration variable on the build definition's Variables tab if, for example, a debug configuration is needed.
3. Test — Executes the dotnet test --configuration release --logger trx --results-directory &lt;local\_path\_on\_build\_agent&gt; command to run the app's unit tests. Unit tests are executed within any C# project matching the **/Tests/.csproj glob pattern. Test results are saved in a .trx file at the location specified by the --results-directory option. If any tests fail, the build fails and isn't deployed.

H Save &amp; queue y

Tasks

Variables

&lt; MyFirstProject-ASP.NET Core (.NET Framework)-Cl

Runs Branches Analytics

Description

#20210420.5 Update Index.cshtml

• Individual Cl for (* 3º main $ 97c0a2b *

#20210420.4 Update Index.cshtml

• Individual Cl for * 3º main 4 d1077bb *

#20210420.3 Update Index.cshtml

• Individual Cl for ( 8º main $ 58b2b8e *

#20210420.2 Update Index.cshtml

• Individual Cl for * 8° main ° cb034f7|

• Queue

Edit

Run pipeline ts 19m ago

© 41s

[!NOTE] To verify the unit tests work, modify SimpleFeedReader.Tests.cs to purposefully break one of the tests. For example, change Assert.True(result.Count &gt; 0); to Assert.False(result.Count &gt; 0); in the Returns\_News\_Stories\_Given\_Valid\_Uri method. Commit and push the change to GitHub. The build is triggered and fails. The build pipeline status changes to failed. Revert the change, commit, and push again. The build succeeds.

4. Publish — Executes the dotnet publish --configuration release --output &lt;local\_path\_on\_build\_agent&gt; command to produce a .zip file with the artifacts to be deployed. The --output option specifies the publish location of the .zip file. That location is specified by passing a predefined variable named $(build.artifactstagingdirectory). That variable expands to a local path, such as *c:\_work\1, on the build agent.
5. Publish Artifact — Publishes the .zip file produced by the Publish task. The task accepts the .zip file location as a parameter, which is the predefined variable $(build.artifactstagingdirectory). The .zip file is published as a folder named drop .

Click the build definition’s Summary link to view a history of builds with the definition:

<!-- image -->

On the resulting page, click the individual build for more details.

<!-- image -->

A summary of this specific build is displayed. Click the published link, and notice the drop folder produced by the build is listed:

Triggers

Options

Retention

History

• Save &amp; queue v

Stages

7 Discard

= Summary

...

Pipeline

Tasks v

Variables

Retention on MyFirstProject-ASP.NET Core (.NET Framework)-Cl * Retained by release

• #20210420.5 Update Index.cshtml

Summary Releases

Triggered by

# sughosneo

Repository and version

•sughosneo/simple-feed-reader

Artifacts | + Add

8 main $ 97c0a2b

&lt; Artifacts

Published Consumed

Name

Drop

&gt; • drop

Run new

View change

<!-- image -->

Schedule not set

Use the ellipsis and click on Downloads artifacts links to inspect the published artifacts.

## Release pipeline

A release pipeline was created with the name MyFirstProject-ASP.NET Core-CD:

<!-- image -->

The two major components of the release pipeline are the Artifacts and the Stages. Clicking the box in the Artifacts section reveals the following panel:

Options

History

Pipeline

Tasks v

Variables

Pipeline

Tasks V

Production

Artifacts | † Add

Deployment process

Phase 1

Run on agent

Drop

Fo Azure App Service Deploy

Schedule not set

Azure App Senice Manage

Retention Options

History

Variables

Retention

Options

Artifact

Stages | + Add v

...

Build - Drop

<!-- image -->

The Source (Build definition) value represents the build definition to which this release pipeline is linked. The .zip file produced by a successful run of the build definition is provided to the Production environment for deployment to Azure. Click the 1 phase, 2 tasks link in the Production environment box to view the release pipeline tasks:

<!-- image -->

The release pipeline consists of two tasks: Deploy Azure App Service to Slot and Manage Azure App Service -Slot Swap. Clicking the first task reveals the following task configuration:

[I Delete

X

Pipeline

Tasks V

Production

Deployment process

Phase1

Run on agent

<!-- image -->

The Azure subscription, service type, web app name, resource group, and deployment slot are defined in the deployment task. The Package or folder textbox holds the .zip file path to be extracted and deployed to the staging slot of the mywebapp&lt;unique\_number&gt; web app.

Clicking the slot swap task reveals the following task configuration:

Variables

Retention /

Options

Azure App Service Manage

Version

0.=

Display name *

Manage Azure App Service - Slot Swap

Azure subscription * @ | Manage E

Visual Studio Enterprise

Action 0

Swap Slots

App Service name *

mywebapp11857

Resource group *

AzureTutorial

Source Slot *

staging

Swap with Production 0

Preserve Vnet

<!-- image -->

The subscription, resource group, service type, web app name, and deployment slot details are provided. The Swap with Production check box is checked. Consequently, the bits deployed to the staging slot are swapped into the production environment.

## Additional reading

- Create your first pipeline with Azure Pipelines
- Build and .NET Core project
- Deploy a web app with Azure Pipelines

click the + arop-aown in the ned

+

New repository

New gist

## Continuous integration and deployment with Azure DevOps

## Note

This section details continuous integration and deployment with Azure DevOps. You can achieve that with GitHub Actions as well. GitHub Actions is a workflow engine built into GitHub that can also be used for continuous integration and deployment. To follow the guide for building and deploying to Azure using GitHub, complete the Publish the app's code to GitHub and Disconnect local Git deployment sections below and then proceed to the GitHub Actions section .

In the previous chapter, you created a local Git repository for the Simple Feed Reader app. In this chapter, you'll publish that code to a GitHub repository and construct an Azure DevOps Services pipeline using Azure Pipelines. The pipeline enables continuous builds and deployments of the app. Any commit to the GitHub repository triggers a build and a deployment to the Azure Web App's staging slot.

In this section, you’ll complete the following tasks:

[!div class=“checklist”]

- Publish the app's code to GitHub
- Disconnect local Git deployment
- Create an Azure DevOps organization
- Create a team project in Azure DevOps organization
- Configure a self-hosted agent if necessary
- Create a build definition
- Create a release pipeline
- Commit changes to GitHub and automatically deploy to Azure
- Examine the Azure Pipelines pipeline

## Publish the app’s code to GitHub

1. Open a browser window, and navigate to https://github.com.
2. Click the + drop-down in the header, and select New repository:

<!-- image -->

1. Select your account in the Owner drop-down, and enter simple-feed-reader in the Repository name textbox.
2. Click the Create repository button.
3. Open your local machine's command shell. Navigate to the directory in which the simple-feedreader Git repository is stored.
4. Rename the existing origin remote to upstream. Execute the following command:
5. :::{custom-style=CodeBox} console git remote rename origin upstream :::
5. Add a new origin remote pointing to your copy of the repository on GitHub. Execute the following command:
7. :::{custom-style=CodeBox} console git remote add origin https://github.com/&lt;GitHub\_username&gt;/simple-feed-reader/ :::
6. Publish your local Git repository to the newly created GitHub repository. Execute the following command:
9. :::{custom-style=CodeBox} console git push -u origin main :::
7. Open a browser window, and navigate to https://github.com/&lt;GitHub\_username&gt;/simplefeed -reader/. Validate that your code appears in the GitHub repository.

## Disconnect local Git deployment

Remove the local Git deployment with the following steps. Azure Pipelines (an Azure DevOps service) both replaces and augments that functionality.

1. Open the Azure portal, and navigate to the staging (mywebapp&lt;unique\_number&gt;/staging) Web App. The Web App can be quickly located by entering staging in the portal's search box:
1. Click Deployment Center. A new panel appears. Click Disconnect to remove the local Git source control configuration that was added in the previous chapter. Confirm the removal operation by clicking the Yes button.
2. Navigate to the mywebapp App Service. As a reminder, the portal's search box can be used to quickly locate the App Service.
3. Click Deployment Center. A new panel appears. Click Disconnect to remove the local Git source control configuration that was added in the previous chapter. Confirm the removal operation by clicking the Yes button.

<!-- image -->

## Create an Azure DevOps organization

1. Open a browser, and navigate to the Azure DevOps organization creation page .
2. Select New organization
3. Confirm the information, and then select Continue .

Jobs Agents Details Security Settings Maintenance History

Public projects

Free

Last run

Yesterday

Current status

Idle

Agent version

2.185.1

4. Sign in to your organization at any time, https://dev.azure.com/{yourorganization}

Parallel jobs

## Create a team project in Azure DevOps organization

1. Choose the organization, and then select New project .
2. Enter the project name as MyFirstProject and select the Visibility as Private
3. Select Create project .

For more information, see Create a project

## Configure a self-hosted agent if necessary

To build your code or deploy your software using Azure Pipelines, you need at least one agent. In Azure Pipelines, you can run parallel jobs on either Microsoft-hosted or self-hosted agent. But with the recent change in Azure Pipelines free grant of parallel jobs is temporarily disable for the public projects.For more details, refer Configure and pay for parallel jobs .

Go to Organization Settings and then Pipelines &gt; Parallel jobs. If you see value 0 under Microsofthosted that means you need a Self-hosted agent to run your pipeline.

<!-- image -->

You can create that by following details mentioned in Self-hosted agents. After successful configuration, you'll be able to see available agent under Organization Settings &gt; Agent pools &gt;

## {youragentname}

<!-- image -->

## Configure the Azure Pipelines pipeline

There are three distinct steps to complete. Completing the steps in the following three sections results in an operational DevOps pipeline.

pipeline.

select the Gitrub option trom the select a source section..

Select a source

VSTS Git

## Grant Azure DevOps access to the GitHub repository

External Git

1. In your project, navigate to the Pipelines page. Then choose the action to create a new pipeline:

Create your first Pipeline

Automate your build and release processes using our wizard, and go from code to cloud-hosted within minutes.

Create Pipeline

Use Use the classic editor to create the pipeline.

Connect

Select

New pipeline

Where is your code?

Azure Repos Git YAML

Free private Git repositories, pull requests, and code search

Bitbucket Cloud YAML

<!-- image -->

Hosted by Atlassian

1. Use Use the classic editor to create the pipeline.

YAML

The self-hosted version of GitHub Enterprise

The sel-hosted vere an or er

→ Other ei

Any generic Git repository

S subversion

Centralized version control by Apache

Use the classic editor to create a pipeline without YAML.

<!-- image -->

1. Select the GitHub option from the Select a source section::
1. Authorization is required before Azure DevOps can access your GitHub repository. Enter GitHub connection in the Connection name textbox. For example:

<!-- image -->

Configure

rom the temple selection page, enter Asr.NEI Core In the searen Dox.

Select a template

Or start with an e Empty pipeline

ASP.NET Core

• We need your authorization to access your repositories

Connection name *

Others scottaddie GitHub connection

dotnet

ASP.NET Core

Build and test an ASPINET Core web application.

Authorize using OAuth aN ASP.NET Core (NET Framework)

Build an ASPINET Core web application that targets the full .NET Framework.

<!-- image -->

1. If two -factor authentication is enabled on your GitHub account, a personal access token is required. In that case, click the Authorize with a GitHub personal access token link. See the official GitHub personal access token creation instructions for help. Only the repo scope of permissions is needed. Otherwise, click the Authorize using OAuth button.
2. When prompted, sign in to your GitHub account. Then select Authorize to grant access to your Azure DevOps organization. If successful, a new service endpoint is created.
3. Click the ellipsis button next to the Repository button. Select the /simple-feed-reader repository from the list. Click the Select button.
4. Select the default branch (main) from the Default branch for manual and scheduled builds drop-down. Click the Continue button. The template selection page appears.

## Create the build definition

1. From the template selection page, enter ASP.NET Core in the search box:

<!-- image -->

The template search results appear. Hover over the ASP.NET Core template, and click the Apply button.

1. The Tasks tab of the build definition appears. Select the self-hosted Agent pool if you have created that in the earlier step.

X

Tasks

Variables Triggers Options

Retention History

Pipeline

Culld poeine y Get sources

B Save &amp; queue Y Discard

• Enable continuous integration

• sughosnea/simple-feed-reader

= Summary

• Queue ...

Name*

P main

Agent job 1

O Batch changes while a build is in progress

3 Run on agent

Use NuGet 4.4.1

Branch filters

Po NuGet too rosier

NuGet restore

Visual Studio build

0) Paul sou tion

Type

Test Assemblies

Visual Studio Test

Include

Publish symbols path

+ Publish Artifact

Pubish buld artifacts

+ Add

Path filters

+ Add

+

MyFirstProject-ASP.NET Core (NET Framework)-Cl

Agent pool • © | Pool information | Manage E

Default

~ O

<!-- image -->

## &gt; [!NOTE]

- &gt; If you are using MS-hosted agent then select the *Hosted &gt; Azure Pipelines* from drop down.
1. Click the Triggers tab.
2. Check the Enable continuous integration box. Under the Branch filters section, confirm that the Type drop-down is set to Include. Set the Branch specification drop-down to main .

<!-- image -->

These settings cause a build to trigger when any change is pushed to the default branch (*main*) of the GitHub repository. Continuous integration is tested in the [Commit changes to GitHub and automatically deploy to Azure](#commit-changes-togithub-and-automatical) section.

1. Click the Save &amp; queue button, and select the Save option:

Ine tollowing modd aldog appears.

click the keleases lab or your team project. Click tne ew pipeline button.

Overview

Boards

Save build definition

Repos

E Save &amp; queue V

LI!

* Pipelines

Select folder *

1 Save &amp; queue a Pipelines

di Environments

• Releases

H Save

0% Library

Comment

• Task groups

1 Save as draft

*** Deployment groups

• Test Plans

Artifacts

<!-- image -->

1. The following modal dialog appears:

<!-- image -->

Use the default folder of *\\*, and click the **Save** button.

## Create the release pipeline

1. Click the Releases tab of your team project. Click the New pipeline button.

<!-- image -->

X

No release pipelines found

Automate your release process in a few easy steps with a new pipeline

New pipeline

Cancel

slot template, ana click ne Apply Dutton. Ine pipeline lao Or the release pipell rrom the template selection page, enter ApP service Deployment in the search box.

All pipelines › * New release pipeline

Select a template

Pipeline

Or start with an ku Empty job

• Tasks v

Variables

Retention Options

History

Featured

Artifacts | + Add

WebJobs.

Others artifact

1. From the template selection page, enter App Service Deployment in the search box:

Azure App Service deployment with continuous

+ Add an monitoring

• 1 job, 2 tasks

Deploy your Web applications to Azure App Service and enable continuous monitoring using Application Insights.

Schedule not set

Azure App Service deployment with slot

Deploy your Azure Web App to a staging slot and swap slots to deploy to production.

Azure App Service deployment with tests and performance tests

Deploy your Azure Web App and run tests or cloud-based web performance tests.

Click the Add button in the Artifacts box. The Add artifact panel appears:

Azure Service Fabric Compose deployment

Add artifact

Deploy a Docker Compose application to a Service Fabric cluster.

Source type

Azure Service Fabric deployment

Deploy an Azure Service Fabric application.

/ Build

Git

3 more artifact types v

Project*

MyFirstProject

Source (Build definition) *

O This setting is required.

Add

<!-- image -->

1. The template search results appear. Hover over the Azure App Service Deployment with Slot template, and click the Apply button. The Pipeline tab of the release pipeline appears.
1. Click the Add button in the Artifacts box. The Add artifact panel appears:

<!-- image -->

<!-- image -->

Stages | + Add v

Azure App Service deployment

The template selection pane appears.

Azure App Service Deploy X

click the lignining polt icon to enable continuous a

Artifacts

+ Add

1. Select the Build tile from the Source type section. This type allows for the linking of the release pipeline to the build definition.
2. Select MyFirstProject from the Project drop-down.
3. Select the build definition name, MyFirstProject-ASP.NET Core-CI, from the Source (Build definition) drop-down.

Drop

4. Select Latest from the Default version drop-down. This option builds the artifacts produced by the latest run of the build definition.
5. Replace the text in the Source alias textbox with Drop .
6. Click the Add button. The Artifacts section updates to display the changes.
7. Click the lightning bolt icon to enable continuous deployments:

<!-- image -->

With this option enabled, a deployment occurs each time a new build is available.

1. A Continuous deployment trigger panel appears to the right. Click the toggle button to enable the feature. It isn't necessary to enable the Pull request trigger .
2. Click the Add drop-down in the Build branch filters section. Choose the Build Definition's default branch option. This filter causes the release to trigger only for a build from the GitHub repository's default branch (main).
3. Click the Save button. Click the OK button in the resulting Save modal dialog.
4. Click the Stage 1 box. An Stage panel appears to the right. Change the Stage 1 text in the Stage name textbox to Production .

lick he phase, &amp; tasks link in the Production Dox.

select the sell-nosted Agent poor l you nave createa Inal In tne earler step.

Production

Deployment process

Run on agent

= Run on agent

Stages | + Add v

Stages | † Add v

Deploy Azure App Service to Slot

Azure App Service deploy

, Manage Azure App Service - Slot Swap

Azure ADD service mandaci

Production

• 1 job, 2 tasks

R

Agent job O

Display name*

Run on agent

Stage

Production

Agent selection ^

Agent pool © | Pool information | Manage C

E Properties ^

Default

Name and owners of the stage

<!-- image -->

1. Click the 1 phase, 2 tasks link in the Production box:

<!-- image -->

The **Tasks** tab of the environment appears.

1. Click the Deploy Azure App Service to Slot task. Its settings appear in a panel to the right.
2. Select the Azure subscription associated with the App Service from the Azure subscription drop-down. Once selected, click the Authorize button.
3. Select Web App from the App type drop-down.
4. Select mywebapp/ from the App service name drop-down.
5. Select AzureTutorial from the Resource group drop-down.
6. Select staging from the Slot drop-down.
7. Select Run on agent* under Tasks. On the right pane, you'll see Agent Job .
8. Select the self -hosted Agent pool if you have created that in the earlier step.

<!-- image -->

...

I| Delete = Move V ...

• Remove

" o

Myrustrioject-Asr.NEl Core-co as the name.

Tasks

• MyFirstProject / MyFirst... V

Triggers

-

Continuous integration

Releases

Library

- &gt; [!NOTE]
- &gt; If you are using MS-hosted agent then select the *Hosted &gt; Azure Pipelines* from drop down.
1. Click the Save button.
2. Hover over the default release pipeline name. Click the pencil icon to edit it. Use MyFirstProject-ASP.NET Core-CD as the name.
1. Click the Save button.

<!-- image -->

## Commit changes to GitHub and automatically deploy to Azure

1. Open SimpleFeedReader.sln in Visual Studio.
2. In Solution Explorer, open Pages.cshtml. Change &lt;h2&gt;Simple Feed Reader - V3&lt;/h2&gt; to &lt;h2&gt;Simple Feed Reader - V4&lt;/h2&gt;.
3. Press Ctrl+Shift+B to build the app.
4. Commit the file to the GitHub repository. Use either the Changes page in Visual Studio's Team Explorer tab, or execute the following using the local machine's command shell:

:::{custom-style=CodeBox} console git commit -a -m "upgraded to V4" :::

5. Push the change in the default branch (main) to the origin remote of your GitHub repository. In the following command, replace the placeholder {BRANCH} with the default branch (use main):

:::{custom-style=CodeBox} console git push origin {BRANCH} :::

The commit appears in the GitHub repository's default branch (main). You'll be able to see the commit history in https://github.com/&lt;GitHub\_username&gt;/simple-feedreader/commits/main.

The build is triggered, since continuous integration is enabled in the build definition's Triggers tab:

<!-- image -->

Builds

Dashboards Code Work

Options

Retention

History

Task Groups Deployment Groups

Build an

Save &amp; queue V

• scottaddie/simple-feed-reader

Variables

aown sous delalls.

butter to see more delals or each step.

Notice Inal Ine v4 text appears In the nedding.

O Search all pipelines

Pipelines

Recent All Runs

+ New v

SimpleFeedReader

MyFirstProject-ASP.NET Core-..

Recently run pipelines

@ Production

Pipeline

MyFirstProject-ASP.NET Core-CD

Releases Denloyments Analvtics

Releases

Release-3

Last run sia 20210420.... 8º main

#20210420.5 • Update Index cshtml

New pipeline

Edit

• Create release

T Filter pipelines

# All releases v

(Just now

1. Navigate to the Pipelines. You'll see the CI pipeline details and monitor each steps if you drill down Jobs details.

Enter a feed URL:

Retrieve Feed

<!-- image -->

1. Similarly, go to the Releases tab to see the details of CD pipeline. You can always drill down further to see more details of each step.

© 2017 - SimpleFeedReader

<!-- image -->

1. Once the build succeeds, a deployment to Azure occurs. Navigate to the app in the browser. Notice that the "V4" text appears in the heading:

<!-- image -->

## Examine the Azure Pipelines pipeline

## Build definition

A build definition was created with the name MyFirstProject-ASP.NET Core-CI. Upon completion, the build produces a .zip file including the assets to be published. The release pipeline deploys those assets to Azure.

The build definition’s Tasks tab lists the individual steps being used. There are five build tasks.

Created

4/20/2021,12:58:08 PM

Stages

© Production

• ... › MyFirstProject-ASP.NET Core (NET Framework)-C|

Options Retention History

Tasks Variables Triggers m

Pipeline

Build pipeline

= Get sources

• sughosneo/simple-feed-reader

Agent job 1

= Run on agent

Use NuGet 4.4.1

#• NuGet tool installer

NuGet restore

NuGet

• Build solution

Visual Studio build

Test Assemblies

Visual Studio Test

Publish Artifact

Publish build artifacts

<!-- image -->

1. Restore — Executes the dotnet restore command to restore the app's NuGet packages. The default package feed used is nuget.org.
2. Build — Executes the dotnet build --configuration release command to compile the app's code. This --configuration option is used to produce an optimized version of the code, which is suitable for deployment to a production environment. Modify the BuildConfiguration variable on the build definition's Variables tab if, for example, a debug configuration is needed.
3. Test — Executes the dotnet test --configuration release --logger trx --results-directory &lt;local\_path\_on\_build\_agent&gt; command to run the app's unit tests. Unit tests are executed within any C# project matching the **/Tests/.csproj glob pattern. Test results are saved in a .trx file at the location specified by the --results-directory option. If any tests fail, the build fails and isn't deployed.

H Save &amp; queue y

Tasks

Variables

&lt; MyFirstProject-ASP.NET Core (.NET Framework)-Cl

Runs Branches Analytics

Description

#20210420.5 Update Index.cshtml

• Individual Cl for (* 3º main $ 97c0a2b *

#20210420.4 Update Index.cshtml

• Individual Cl for * 3º main 4 d1077bb *

#20210420.3 Update Index.cshtml

• Individual Cl for ( 8º main $ 58b2b8e *

#20210420.2 Update Index.cshtml

• Individual Cl for * 8° main ° cb034f7|

• Queue

Edit

Run pipeline ts 19m ago

© 41s

[!NOTE] To verify the unit tests work, modify SimpleFeedReader.Tests.cs to purposefully break one of the tests. For example, change Assert.True(result.Count &gt; 0); to Assert.False(result.Count &gt; 0); in the Returns\_News\_Stories\_Given\_Valid\_Uri method. Commit and push the change to GitHub. The build is triggered and fails. The build pipeline status changes to failed. Revert the change, commit, and push again. The build succeeds.

4. Publish — Executes the dotnet publish --configuration release --output &lt;local\_path\_on\_build\_agent&gt; command to produce a .zip file with the artifacts to be deployed. The --output option specifies the publish location of the .zip file. That location is specified by passing a predefined variable named $(build.artifactstagingdirectory). That variable expands to a local path, such as *c:\_work\1, on the build agent.
5. Publish Artifact — Publishes the .zip file produced by the Publish task. The task accepts the .zip file location as a parameter, which is the predefined variable $(build.artifactstagingdirectory). The .zip file is published as a folder named drop .

Click the build definition’s Summary link to view a history of builds with the definition:

<!-- image -->

On the resulting page, click the individual build for more details.

<!-- image -->

A summary of this specific build is displayed. Click the published link, and notice the drop folder produced by the build is listed:

Triggers

Options

Retention

History

• Save &amp; queue v

Stages

7 Discard

= Summary

...

Pipeline

Tasks V

Variables

Retention on MyFirstProject-ASP.NET Core (.NET Framework)-Cl * Retained by release

• #20210420.5 Update Index.cshtml

Summary Releases

Triggered by

# sughosneo

Repository and version

•sughosneo/simple-feed-reader

Artifacts | + Add

8 main $ 97c0a2b

&lt; Artifacts

Published Consumed

Name

Drop

&gt; • drop

Run new

View change

<!-- image -->

Schedule not set

Use the ellipsis and click on Downloads artifacts links to inspect the published artifacts.

## Release pipeline

A release pipeline was created with the name MyFirstProject-ASP.NET Core-CD:

<!-- image -->

The two major components of the release pipeline are the Artifacts and the Stages. Clicking the box in the Artifacts section reveals the following panel:

Options

History

Pipeline

Tasks v

Variables

Pipeline

Tasks V

Production

Artifacts | † Add

Deployment process

Phase 1

Run on agent

Drop

Fo Azure App Service Deploy

Schedule not set

Azure App Senice Manage

Retention Options

History

Variables

Retention

Options

Artifact

Stages | + Add v

...

Build - Drop

<!-- image -->

The Source (Build definition) value represents the build definition to which this release pipeline is linked. The .zip file produced by a successful run of the build definition is provided to the Production environment for deployment to Azure. Click the 1 phase, 2 tasks link in the Production environment box to view the release pipeline tasks:

<!-- image -->

The release pipeline consists of two tasks: Deploy Azure App Service to Slot and Manage Azure App Service -Slot Swap. Clicking the first task reveals the following task configuration:

[I Delete

X

Pipeline

Tasks V

Production

Deployment process

Phase1

Run on agent

<!-- image -->

The Azure subscription, service type, web app name, resource group, and deployment slot are defined in the deployment task. The Package or folder textbox holds the .zip file path to be extracted and deployed to the staging slot of the mywebapp&lt;unique\_number&gt; web app.

Clicking the slot swap task reveals the following task configuration:

Variables

Retention /

Options

Azure App Service Manage

Version

0.=

Display name *

Manage Azure App Service - Slot Swap

Azure subscription * @ | Manage E

Visual Studio Enterprise

Action 0

Swap Slots

App Service name *

mywebapp11857

Resource group *

AzureTutorial

Source Slot *

staging

Swap with Production 0

Preserve Vnet

<!-- image -->

The subscription, resource group, service type, web app name, and deployment slot details are provided. The Swap with Production check box is checked. Consequently, the bits deployed to the staging slot are swapped into the production environment.

## Additional reading

- Create your first pipeline with Azure Pipelines
- Build and .NET Core project
- Deploy a web app with Azure Pipelines

## Continuous integration and deployment with GitHub Actions

GitHub has long been the home for millions of open-source developers around the globe. Most developers associate source control with GitHub. However, GitHub is an evolving platform that can be used for more than just synchronizing Git repositories.

## GitHub Actions

GitHub Actions is a workflow engine that can automate workflows for nearly all events that occur on GitHub. Actions is a great solution for Continuous Integration/Continuous Deployment (CI/CD) pipelines.

In this section of articles, you'll learn how to create an Actions workflow. The workflow will build, test, and deploy a .NET web app to Azure Web Apps.

## Note

Before you begin, complete the Publish the app's code to GitHub and Disconnect local Git deployment sections of the Continuous integration and deployment with Azure DevOps section to publish your code to GitHub. Then proceed to the Build article.

In the Build article, you'll create the initial workflow to build and test the .NET app. You'll: [!div class="checklist"]

- Learn the basic structure of a GitHub Action workflow YAML file.
- Use a template to create a basic build workflow that builds a .NET app and executes unit tests.
- Publish the compiled app so that it's ready for deployment.

In the Deploy article, you’ll:

[!div class=“checklist”]

- Learn about environments in GitHub Actions.
- Create two environments and specify environment protection rules.
- Create environment secrets for managing environment-specific configuration.
- Extend the workflow YAML file to add deployment steps.
- Add a manual dispatch trigger.

## Secure code with CodeQL

In addition to building and deploying code, GitHub Advanced Security offers tools for "shifting left" with security. That is, integrating security early on in the software delivery lifecycle. CodeQL is a code scanning language that runs queries to find potential vulnerabilities or quality issues in your code. CodeQL is run using an Actions workflow.

In the CodeQL article, you’ll:

[!div class=“checklist”]

- Create a Code Scanning Action.
- Edit the workflow file to include custom scan settings.
- See scanning results.

## Compare and contrast GitHub Actions and Azure Pipelines

GitHub Actions and Azure Pipelines have a common lineage and are similar in many respects. However, you should understand the differences before selecting a platform for building, testing, and deploying apps. In the Comparison article, you'll deep dive into these platforms and compare and contrast them. You'll also learn how to select the correct platform for your CI/CD needs.

## Continuous integration and deployment with GitHub Actions

GitHub has long been the home for millions of open-source developers around the globe. Most developers associate source control with GitHub. However, GitHub is an evolving platform that can be used for more than just synchronizing Git repositories.

## GitHub Actions

GitHub Actions is a workflow engine that can automate workflows for nearly all events that occur on GitHub. Actions is a great solution for Continuous Integration/Continuous Deployment (CI/CD) pipelines.

In this section of articles, you'll learn how to create an Actions workflow. The workflow will build, test, and deploy a .NET web app to Azure Web Apps.

| Note                                                                                                                                                                                                                                                     |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Before you begin, complete the Publish the app’s code to GitHub and Disconnect local Git  deployment sections of the Continuous integration and deployment with Azure DevOps section to  publish your code to GitHub. Then proceed to the Build article. |

In the Build article, you’ll create the initial workflow to build and test the .NET app. You’ll:

[!div class=“checklist”]

- Learn the basic structure of a GitHub Action workflow YAML file.
- Use a template to create a basic build workflow that builds a .NET app and executes unit tests.
- Publish the compiled app so that it's ready for deployment.

In the Deploy article, you’ll:

[!div class=“checklist”]

- Learn about environments in GitHub Actions.

- Create two environments and specify environment protection rules.
- Create environment secrets for managing environment-specific configuration.
- Extend the workflow YAML file to add deployment steps.
- Add a manual dispatch trigger.

## Secure code with CodeQL

In addition to building and deploying code, GitHub Advanced Security offers tools for "shifting left" with security. That is, integrating security early on in the software delivery lifecycle. CodeQL is a code scanning language that runs queries to find potential vulnerabilities or quality issues in your code. CodeQL is run using an Actions workflow.

In the CodeQL article, you’ll:

[!div class=“checklist”]

- Create a Code Scanning Action.
- Edit the workflow file to include custom scan settings.
- See scanning results.

## Compare and contrast GitHub Actions and Azure Pipelines

GitHub Actions and Azure Pipelines have a common lineage and are similar in many respects. However, you should understand the differences before selecting a platform for building, testing, and deploying apps. In the Comparison article, you'll deep dive into these platforms and compare and contrast them. You'll also learn how to select the correct platform for your CI/CD needs.

## Compare and contrast GitHub Actions and Azure Pipelines

GitHub Actions and Azure Pipelines have a common history. In fact, the Actions agent is a fork of the Pipelines agent. There are many similarities between GitHub Actions and Azure Pipelines and it's worth comparing and contrasting them.

## Pipelines as code

Before you compare GitHub Actions and Azure Pipelines, you should consider the benefits of pipelines as code. Pipelines as code:

[!div class=“checklist”]

- Benefit from standard source control practices (such as code reviews via pull request and versioning).
- Can be audited for changes just like any other files in the repository.
- Don't require accessing a separate system or UI to edit.
- Can fully codify the build, test, and deploy process for code.

- Can usually be templatized to empower teams to create standard processes across multiple repositories.

## Note

The term "pipelines" can also be referred to by several different interchangeable words: pipeline , workflow, and build are common terms. In this article, references to Azure Pipelines are referring to YAML Pipelines, and not the older UI-based Classic Pipelines .

## Agents and runners

Before you examine pipelines themselves, you should consider how these pipelines execute. Both GitHub Actions and Azure Pipelines are really orchestration engines. When a pipeline is triggered, the system finds an "agent" and tells the agent to execute the jobs defined in the pipeline file.

Azure Pipelines run on agents. The agent is written in .NET, so it will run wherever .NET can run: Windows, macOS, and Linux. Agents can even run in containers. Agents are registered to a pool in Azure Pipelines or to a repository or organization in GitHub. Agents can be hosted or private .

GitHub Workflows execute on runners. The runner code is essentially a fork of the Azure Pipelines code, so it's very similar. It's also cross-platform and you can also use hosted or self-hosted runners.

## Hosted agents and runners

Hosted agents (Azure Pipelines) and hosted runners (GitHub) are agents that are spun up and managed by Azure DevOps or GitHub respectively. You don't need to maintain any build infrastructure. When a pipeline triggers that targets a hosted agent, an instance of the specified agent image is created. The job is run by the agent on the instance, and once the job completes, the instance is destroyed. The same applies for hosted runners running GitHub workflows.

## Note

The list of software installed on Azure Pipelines images is listed in this repository. You can select the platform folder and examine the README.md files. You can find information on GitHub hosted runners .

## Private agents and self-hosted runners

There are times when you can’t use hosted images. For example, when you:

- Require SDKs or other software that isn't installed on the images.
- Need to access resources that aren't public (such as an internal SonarQube server or an internal Artifactory instance).
- Need to deploy to private networks.
- Need to install licenses for third -party software required for building your code.
- Need more storage or memory than is provided to the hosted agent images.
- Need more time than the maximum build time limit for hosted agents.

## Important

It's possible to install tools and SDKs when running pipelines on hosted agents. If the install steps don't take long, this is viable. However, if the tools/software take a long time to install, then you may be better off with a private agent or self-hosted runner, since the install steps will need to execute for every run of the workflow.

## Azure DevOps agents

Every Azure DevOps account has a hosted pool with a single agent that can run one job at a time. Also included is a set number of free build minutes. You may purchase additional "hosted pipelines" in Azure DevOps. When you purchase an additional hosted pipeline, you're really removing the build minutes limit and adding concurrency. One pipeline can run one job at a time. Two pipelines can run two jobs simultaneously, and so on.

## Comparison of agents

| Feature                                    | GitHub                                                                                                                                                       | Azure Pipelines                                                                                                                                                                                                                                                                                      | Links                                     |
|--------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------|
| Hosted agents for  public  repos/projects  | Free                                                                                                                                                         | Up to 10 free Microsoft-hosted parallel jobs  that can run for up to 360 minutes (6 hours)  each time with no overall time limit per  month. You aren’t given this free grant by  default, you have to submit a request                                                                              | Azure  Pipelines GitHub                   |
| Hosted agents for  private  repos/projects | 2,000 minutes  free per month,  3,000 minutes  for Pro and  Team licenses,  50,000 minutes  for Enterprise  license.  Additional  minutes may be  purchased. | One free parallel job that can run for up to  60 minutes each time, until you’ve used  1,800 minutes (30 hours) per month. You  can pay for additional capacity per parallel  job. Paid parallel jobs remove the monthly  time limit and allow you to run each job for  up to 360 minutes (6 hours). |                                           |
| Cross - platform                           | Yes                                                                                                                                                          | Yes                                                                                                                                                                                                                                                                                                  |                                           |
| Scale set agents                           | No                                                                                                                                                           | Yes                                                                                                                                                                                                                                                                                                  | Azure virtual  machine  scale set  agents |

## Comparison of GitHub Actions and Azure Pipelines

Azure Pipelines (YAML pipelines) provide a mature set of features. Some of the features include:

- Approvals
- Artifact storage

- Deployment jobs
- Environments
- Gates
- Stages
- Templates
- Triggers
- Variable groups

For a full list of Azure Pipelines features, refer to the Feature availability table.

GitHub Actions are evolving rapidly and provide features such as triggers for almost all GitHub events, artifact storage, environments and environment rules, starter templates, and matrices. Read more about the entire feature set refer GitHub Actions .

## Feature comparison

The following table is current as of January 2023 and is not an exhaustive list of features.

| Feature            | Description                                                         | GitHub Actions   | Azure Pipelines   |
|--------------------|---------------------------------------------------------------------|------------------|-------------------|
| Approvals          | Define approval  conditions before  moving further in the  pipeline | Yes              | Yes               |
| Artifacts          | Upload, store, and  download artifacts  from jobs                   | Yes              | Yes               |
| Caching            | Cache folders or files  for subsequent runs                         | Yes              | Yes               |
| Conditions         | Specify conditions  for steps or jobs                               | Yes              | Yes               |
| Container  Jobs    | Run jobs inside a  container                                        | Yes              | Yes               |
| Demands            | Specify demands  that must be met to  match jobs to agents          | Yes              | Yes               |
| Dependenci es      | Specify  dependencies  between jobs or  stages                      | Yes              | Yes               |
| Deployment  Groups | A logical set of target  machines for  deployments                  | No               | Yes               |
| Deployment  Jobs   | Job that targets a  deployment group                                | No               | Yes               |

| Feature                                         | Description                                                                                                | GitHub Actions   | Azure Pipelines   |
|-------------------------------------------------|------------------------------------------------------------------------------------------------------------|------------------|-------------------|
| Environment s                                   | A collection of  resources to target  or a logical  environment                                            | Yes              | Yes               |
| Gates/Check s                                   | Automatic collection  and evaluation of  signals to control  continuation                                  | Yes              | Yes               |
| Jobs                                            | Sequence of steps  that are executed on  an agent                                                          | Yes              | Yes               |
| Service  Containers                             | Manage the lifecycle  of a containerized  service instance  available during a  job                        | Yes              | Yes               |
| Service  Connections                            | Abstract credentials  to external systems                                                                  | No               | Yes               |
| Passwordles s  connections  to cloud  providers | Provide technologies  and support use  cases that reduce  and potentially  eliminate the use of  passwords | Yes              | No                |
| Stages                                          | Group jobs in a  pipeline                                                                                  | No               | Yes               |
| Templates                                       | Define reusable,  parameterized  building blocks for  steps, jobs, or  variables                           | Yes              | Yes               |
| Starter  Templates                              | Defines a starter  workflow based on  the type of code  detected in a  repository                          | Yes              | No                |
| Triggers                                        | Set of events that  cause the pipeline to  trigger                                                         | Yes              | Yes               |

| Feature          | Description                                                           | GitHub Actions   | Azure Pipelines   |
|------------------|-----------------------------------------------------------------------|------------------|-------------------|
| Variables        | Variables that can be  passed in, statically  or dynamically  defined | Yes              | Yes               |
| Variable  Groups | Store values for use  across multiple  pipelines                      | No               | Yes               |

## Important

GitHub Actions is rapidly evolving. Be sure to check documentation carefully before deciding which platform is right for you.

## Build a .NET web app using GitHub Actions

GitHub Actions allow you to automate workflows in response to events that are triggered in GitHub. A common workflow is Continuous Integration (CI), but Actions can automate other processes. For example, sending welcome emails when people join a repository.

To explore moving code to the cloud, you'll build a GitHub Actions workflow file. The workflow file will be used for the Simple Feed Reader app you've already deployed to Azure App Service.

In this article, you will: &gt; [!div class="checklist"] &gt; &gt; * Learn the basic structure of a GitHub Action workflow YAML file. &gt; * Use a template to create a basic build workflow that builds the .NET app and executes unit tests. &gt; * Publish the compiled app so that it's ready for deployment.

## Workflow structure

Workflows are defined in YAML files, and contain several common nodes:

- a name
- a trigger, defined by an on section
- one or more job sections composed of one or more steps
- optional attributes such as environment variables

Jobs are run on runners. You can use hosted runners, which are spun up by GitHub during the workflow and then thrown away. Hosted runners are great because you don't have to maintain your own build infrastructure. For workflows that require a specific build environment, or for running workflows on a private network, you can also use private runners. To create a private runner, install the runner on any machine that supports .NET.

Each job will specify what runner GitHub should use to execute the steps. You can also specify dependencies between jobs using the needs attribute. Deployment jobs can also specify an environment to target.

template. select set up this worknow lo creale d

Search or jump to

[Pull requests Issues Codespaces Marketplace Explore

Y colindembovsky / simple-feed-reader

(&gt; Code

I Ail requests

(• Action

E Projects

Ф wal O Securty

Le bights lit Setings

Get started with GitHub Actions

Buld test and deploy you

Waging work the wry you want Select a workflow template to get started skip is and set up a worknew yoursel

NET

By Gerto Actem

Set up this work for dobrat restore

## Tip

Deploy Nodejs to Azure Web

App

The steps node can be as easy as inline commands, or they can be actions. Most CI workflows will have a combination of run steps (for executing scripts) and actions. Individual actions are pulled into the workflow by referencing the GitHub Action repository (and optionally a tag or commit hash for specific versions) and specifying any parameters using the with keyword.

CH O

Deploy to Alibaba Cloud ACK

Deploy to Amazon ECS

For more information, see GitHub Actions YAML syntax .

From a workflow file, you're able to run any of the available .NET CLI commands. For example, if you're required to build, test, and deploy an ASP.NET Core Blazor WebAssembly app with Ahead-of-Time (AoT) compilation, you'd use the following commands:

- dotnet workload install
- dotnet restore
- dotnet build
- dotnet test
- dotnet publish

## The .NET SDK is a workflow necessity

All .NET workflows require the .NET SDK, and this can be set up by the actions/setup-dotnet GitHub Action. This action sets up a .NET CLI environment for use in actions. Some GitHub hosted runners have the .NET SDK preinstalled, but that's subject to change. As a best practice, use the actions/setupdotnet action to ensure the proper version is available.

## Create a basic build workflow

A primary principle of effective DevOps is to "build once, and deploy many times". You'll start by creating a workflow to build a basic .NET app. In the next step, you'll publish the output to prepare for deployment.

1. Navigate to your GitHub repository and select the Actions tab.
2. GitHub detects that there's .NET code in the repository and suggests a .NET workflow template. Select Set up this workflow to create a new YAML workflow file:

**Figure 1**: Creating a new workflow.

<!-- image -->

© Watch -

pening te logs, you alsee athe dE Dullas man, ns commit soul trigger the workhow to ru

completed, you should see a successiul run.

( Summary

Search or jump to....

Pull requests Issues Codespaces Marketplace Explore coocked 9 menuat ago in tane

У colindembovsky / simple-feed-reader forked from Azure-Samples/simple-feed-reader

Copyrter (C) Micronett Corpiration, alt-lehet patarves.

&lt;&gt; Code

O Actions

No wrap

CD Wiki

Marketplac

I Pull requests

Update dotnet.yml.NET #2

A Summary

Jobs

• build

W Projects

• Security

Le Insights @ Settings

Puste succeeces.

Commit changes

•barning(o)

•trear(e)

Update dotnet.yml

Tine elipsed 03:00:00.19

Featured Acti

1. Commit the file onto the main branch. Since you've defined a trigger condition for commits to main, this commit should trigger the workflow to run. dotnet.yml

on push

Uplo

Telt ren for /hoes/rumter/work/t/hple-feed-rester/stxpie-teed-reeder/STxpIefendiesder.Tests/bsn/Detug/netcorespp2.1/StapLe/

By act

Uplo work

Setu

By ac

Setu

Closi

By actions ter

**Figure 2**: Commit the YAML file.

<!-- image -->

1. Select the Actions tab again. You should see a running workflow. Once the workflow has completed, you should see a successful run.
1. Opening the logs, you can see that the .NET build succeeded and the tests ran and passed.

**Figure 3**: Successful build view.

<!-- image -->

**Figure 4**: Checking the logs.

<!-- image -->

Start commit -

© Watch = 0

## Note

If any of the tests fail, the workflow will fail.

## Dissect the workflow file

Let’s examine the workflow YAML file you have so far:

```
name: .NET on: push: branches: [ main ] pull_request: branches: [ main ] jobs: build: runs-on: ubuntu -latest steps: -uses: actions/checkout@v3 -name: Setup .NET uses: actions/setup-dotnet@v3 with: dotnet -version: 6.0.x -name: Restore dependencies run: dotnet restore -name: Build run: dotnet build --no-restore -name: Test run: dotnet test --no-build --verbosity normal
```

## Notice the following things:

1. There's a name that names the workflow.
2. The on object specifies when this workflow should run. This workflow has two events that trigger it: push to main and pull\_request to main. Each time someone commits to main or creates a pull request (PR) to main, this workflow will execute.
3. There's a single job called build. This build should run on a hosted agent. ubuntu\_latest specifies the most recent Ubuntu hosted agent.
4. There are five steps:
1. actions/checkout@v3 is an action that checks out the code in the repository onto the runner.
2. actions/setup-dotnet@v3 is an action that sets up the .NET CLI. This step also specifies a name attribute for the logs and the dotnet-version parameter within the with object.
3. Three run steps that execute dotnet restore, dotnet build, and dotnet test. name attributes are also specified for these run steps to make the logs look pretty.

1.

18

11

12

13

14

15

Navigale done guaywork tows come yo me dna select the penel icon to eall

Search or jump to...

У colindembovsky / simple-feed-reader

Pull requests Issues Codespaces Marketplace Explore forked from Azure-Samples/simple-feed-reader

Y colindembovsky / simple-feed-reader

‹&gt; Code

I1 Pull requests

Actions forked from Azure-Samples/simple-feed-reader

‹&gt; Code

12 Pull requests

• Actions

P master - simple-feed-reader / github / workflows /

L Projects

Projects

Ц Wiki

• Security

L Insights

10 Wiki

© Security

Insights

฿ Settings simple-feed-reader / github / workflows / dotnet.yml

dotnet.yml

Cancel

‹&gt; Edit file nane: -NET

on:

push:

branches: [ master ]

pul1 request:

branches: [ master 1

jobs:

build:

runs-on: ubuntu-latest steps:

- uses: actions/checkoutiv2

name: NET

## Publish the output

• Watch - 0

+ -

• Star

P Fork

79

Go to file

Start commit -

Latest commit 103eala 4 minutes ago

• History

Spaces

03 Settings

No wrap

Marketplace

Documentation

Now that you've successfully built and tested the code, add steps that publish the output so you can deploy the web app. Raw Blame Marketplace / Search results

Upload a Build Artifact

By actions O

1. Navigate to the .github/workflows/dotnet.yml file and select the pencil icon to edit
1. Add the following Publish step below the Test step. The step runs the dotnet publish command to publish the web app:
3. :::{custom-style=CodeBox} ```yml
4. – name: Test run: dotnet test – no-build – verbosity normal # &lt;– this is the current bottom line
5. – name: Publish run: dotnet publish SimpleFeedReader/SimpleFeedReader.csproj -c Release -o website ``` :::
2. This publishes the web app to a folder on the hosted agent. Now you'll want to upload the site as a build artifact that can be deployed to Azure. To complete this activity, you'll use an existing action.
3. On the list of actions in the Actions Helper pane on the right, search for artifact. Select on the Upload a Build Artifact (By actions) action.

**Figure 5**: Edit the YAML file.

<!-- image -->

**Figure 6**: Accessing the snippet helper.

<!-- image -->

12 803

• Watch -

# Star

slipped dna paste i tre worklow below the publish step.

· colindembovsky / simple-feed-reader forked from Azure-Samples/simple-feed-reader

‹&gt; Code

Marketplace / Search results / Upload a Build Artifact

I1 Pull requests

• Actions

• Update dotnet.yml NET #5

( Summary

Upload a Build Artifact

JODH

• build

By actions v2

* 803

W Projects

CO Wiki

© Security

Le Insights

Triggered via push 2 minutes ago

@ colindembovsky pushed -o e2daste waster

฿ Settings

Status

Success

Total duration

1m 30s

Anitacte

1. Edit the version to v2.2.2 to display a sample snippet. Select the clipboard icon to copy the snippet and paste it into the workflow below the publish step.

build

1m 15s

<!-- image -->

Installation

Copy and paste the following snippet into your • yml file.

Version: v2.2.2 -

- name: Upload a Build Artifact uses: actions/upload-artifact@v2.2.2

with:

# Artifact name path:

Available Options:

error: Fail the action with an error message

**Figure 7**: Copying a snippet.

1. Edit the YAML for this step to look as follows:
2. :::{custom-style=CodeBox} ```yml
3. – name: Upload a Build Artifact uses: actions/upload-artifact@v3 with: name: website path: SimpleFeedReader/website/** if-no-files-found: error ``` :::
2. Commit the file.
3. Once the workflow completes, you'll see the artifact from the Home tab:

**Figure 8**: Viewing artifacts in the summary page.

<!-- image -->

## Final workflow file

The final workflow file should look something like this:

```
name: .NET on: push: branches: [ main ] pull_request: branches: [ main ] jobs: build: runs-on: ubuntu -latest steps: -uses: actions/checkout@v3 -name: Setup .NET uses: actions/setup-dotnet@v3 with: dotnet -version: 6.0.x -name: Restore dependencies run: dotnet restore -name: Build run: dotnet build --no-restore -name: Test run: dotnet test --no-build --verbosity normal -name: Publish run: dotnet publish SimpleFeedReader/SimpleFeedReader.csproj -c Release -o website -name: Upload a Build Artifact uses: actions/upload-artifact@v3 with: name: website path: SimpleFeedReader/website/** if -no-files -found: error
```

## Deploy a .NET web app using GitHub Actions

## Warning

Please complete the Build tutorial before starting this lab.

In this article, you'll: &gt; [!div class="checklist"] &gt; &gt; * Learn about Environments in GitHub Actions. &gt; * Create two environments and specify environment protection rules. &gt; * Create environment secrets for managing environment-specific configuration. &gt; * Extend the workflow YAML file to add deployment steps. &gt; * Add a manual dispatch trigger.

## Environments

Now that you've published an artifact that's potentially deployable, you'll add deployment jobs to the workflow. There's nothing special about a deployment job, other than the fact that it references an

environment. Environments are logical constructs that allow you to specify environment protection rules, such as approvals, on any group of resources that you're targeting.

In this walkthrough, you'll be deploying to two environments: PRE-PROD and PROD. In a typical development lifecycle, you'll want to deploy the latest code to a soft environment (typically DEV) that is expected to be a bit unstable. You'll use PRE-PROD as this soft environment. The "higher" environments (like UAT and PROD) are harder environments that are expected to be more stable. To enforce this, you can build protection rules into higher environments. You'll configure an approval protection rule on the PROD environment: whenever a deployment job targets an environment with an approval rule, it will pause until approval is granted before executing.

GitHub environments are logical. They represent the physical (or virtual) resources that you're deploying to. In this case, the PRE-PROD is just a deployment slot on the Azure Web App. PROD is the production slot. The PRE-PROD deployment job will deploy the published .NET app to the staging slot. The PROD deployment job will swap the slots.

Once you have these steps in place, you'll update the workflow to handle environment-specific configuration using environment secrets.

## Note

For more information, see GitHub Actions -Environments .

## Azure authentication

To perform actions such as deploying code to an Azure resource, you need the correct permissions. For deployment to Azure Web Apps, you can use a publishing profile. If you want to deploy to a staging slot, then you'll need the publishing profile for the slot too. Instead, you can use a service principal (SPN) and assign permission to this service principal. You can then authenticate using credentials for the SPN before using any commands that the SPN has permissions to perform.

Once you have an SPN, you'll create a repository secret to securely store the credentials. You can then refer to the secret whenever you need to authenticate. The secret is encrypted and once it has been saved, can never be viewed or edited (only deleted or re-created).

## Create an SPN

1. In your terminal or Cloud Shell, run the following command to create a service principal with contributor permissions to the web app you created earlier:

:::{custom-style=CodeBox} azurecli az ad sp create-for-rbac --name "{sp-name}" --sdk-auth --role contributor \ --scopes /subscriptions/{subscription-id}/resourceGroups/{resourcegroup}/providers/Microsoft.Web/sites/{webappname} :::

2. The command should output JSON that has credentials embedded:

```
:::{custom-style=CodeBox} json { "clientId": "<GUID>", "clientSecret": "<GUID>", "subscriptionId": "<GUID>", "tenantId": "<GUID>", ... } :::
```

Search or jump to.

Pull roquests Issues Codespaces Marketplace

Actions secrets / New secret y colindembovsky / simple-feed-reader

torked from Azurs Sempestlerole 19nd reeds

• Conle

12 Pull imposts

© Actiona

Name

Options

Manage access

AZURE\_CREDENTIALS

Security de analysis

Branches

Value

Webhooks

"clientld". "9

"clientSecret": ""

Deploy kaya

"tenantld":

"subscriptionld": "

Actions

Codernsies

**fione

"**.

Add secret

**.

• Noject

CD Wiki

© Curry

- Inighis

Actions secrets

© Watch

* Star

New repository secret

Socrets are environmant variables that are encrypted. Anyone with collaborator acces to this repository can use these secrets for Actions.

Secrets are nat passed to woridows that are triggered by a pull request from a fork. Learn more.

3. Make sure to record the clientId, clientSecret, subscription, and tenantId. You can also leave the terminal open for copy/paste later.

## Create a repository secret

There are no secrets for this repository.

1. Now you're going to create an encrypted secret to store the credentials. You'll create this secret at the repository level.

Chaste a carnot

2. Navigate to GitHub and select your repository Settings tab. Then select Secrets. Select New repository secret:
1. Copy and paste the JSON from the az ad sp create-for-rbac command into the body of the secret. You can create this JSON by hand too if you have the relevant fields for your SPN. The secret should be named AZURE\_CREDENTIALS. Select Add secret to save the new secret:
1. You'll consume this secret in a workflow in later steps. To access it, use the variable notation ${{}}. In this case, ${{ AZURE\_CREDENTIAL }} will be populated with the JSON you saved.

**Figure 1**: Create a secret.

<!-- image -->

**Figure 2**: Add Azure credentials.

<!-- image -->

## Add environments

Environments are used as a logical boundary. You can add approvals to environments to ensure quality. You can also track deployments to environments and specify environment-specific values (secrets) for configuration.

Explore let Settings

l.

select bettings dna ben drones an your reposi enter PRe-PRop ana select contigure environment.

Search or jump to..

7 All requests issues Codespaces Markutplace Explore

Y colindembovsky / simple-feed-reader forked from Anure-Sampleshingle-feed-reader

(&gt; Code

I) Pull requests

© Actiora

Environments / Add

Options

Manage access

Security &amp; analysis

Name

Notifications

Integrations

Deploy keys

1 wiki

© Securty

Environments a Projects

We haights

@ Setting

There are no environments for this repository

For this example, you're going to split the actual Azure environment into two logical environments called PRE -PROD and PROD. When you deploy the web app, you'll deploy to the staging slot of the Azure web app, represented by the PRE-PROD environment. When you're ready to deploy to PROD, you'll just perform a slot swap.

In this case, the only difference between the environments is the slot that you're deploying to. In real life, there would typically be different web apps (and separate web app plans), separate resource groups, and even separate subscriptions. Typically, there's an SPN per environment. You may want to override the AZURE\_CREDENTIAL value that you saved as a repository secret by creating it as an environment secret .

## Note

Precedence works from Environment to repository. If a targeted environment has a secret called MY\_SECRET, then that value is used. If not, the repository value of MY\_SECRET (if any) is used.

1. Select Settings and then Environments in your repository. Select New Environment:
1. Enter PRE -PROD and select Configure environment:

**Figure 3**: Create an environment.

<!-- image -->

**Figure 4**: Name the environment.

<!-- image -->

© Watch = e t2 sta

New environment

Search or jump to....

Pull requests Issues Codespaces Marketplace Explore

Y colindembovsky / simple-feed-reader forked from Azure-Samples/simple-feed-reader

‹&gt; Code

I2 Pull requests

© Actions

Options

Manage access

Security &amp; analysis

Branches

Webhooks

Notifications

Integrations

Deploy keys

Autolink references

Actions

Environments

Secrets

Moderation settings

LD Wiki

© Security

L Insights

@ Settings

Environments / Configure PROD

1. Since deploying to a staging slot doesn't affect the web app, you can safely deploy to the slot without requiring an approval first. A reviewer could be added if desired. For this example, leave the Environment protection rules empty.

Search for people ce teams

[!NOTE] If you target an environment in a workflow and it does not exist, an "empty" environment is created automatically. The environment would look exactly the same as the PRE -PROD environment -it would exist, but would not have any protection rules enabled.

2. Select Environments again and again select New Environment. Now enter PROD as the name and select Configure environment .

5**•

nantection aulec

3. Check the Required reviewers rule and add yourself as a reviewer. Don't forget to select Save protection rules:

**Figure 5**: Add protection rules.

<!-- image -->

## Deploy to staging

You can now add additional jobs to the workflow to deploy to the environments! You'll start by adding a deployment to the PRE-PROD environment, which in this case is the web app staging slot.

1. Navigate to the .github/workflows/dotnet.yml file and select the pencil icon to edit the file.
2. You're going to use the web app name a few times in this workflow, and will need the name of the resource group too. You'll define the app and resource group names as variables. With the variables, you can maintain the values in one place in the workflow file.
3. Add this snippet below the on block and above the jobs block:
4. :::{custom-style=CodeBox} ```yml env: app-name: "" rg-name: "" jobs: # &lt;– this is the existing jobs line ``` :::

[!WARNING] You'll need to replace &lt;name of your web app&gt; with the actual name of your web app, and &lt;name of your resource group&gt; with the actual name of your resource group.

4. Add a new job below the build job as follows:

Projects

**fioune

:::{custom-style=CodeBox} ```yml if-no-files-found: error # &lt;– last line of build job: insert below this line deploy\_staging: needs: build runs-on: ubuntu-latest

```
environment: name: PRE -PROD url: ${{ steps.deploywebapp.outputs.webapp-url }} steps: -name: Download a Build Artifact uses: actions/download-artifact@v3 with: name: website path: website -name: Login via Azure CLI uses: azure/login@v1 with: creds: ${{ secrets.AZURE_CREDENTIALS }} -name: Deploy web app id: deploywebapp uses: azure/webapps-deploy@v2 with: app -name: ${{ env.app-name }} slot -name: staging package: website -name: az cli logout run: az logout
```

``` :::

The preceding workflow defines several steps:

1. You're creating a new job called deploy\_staging.
2. You specify a dependency using needs. This job needs the build job to complete successfully before it starts.
3. This job also runs on the latest Ubuntu hosted agent, as specified with the runs-on attribute.
4. You specify that this job is targeting the PRE-PROD environment using the environment object. You also specify the url property. This URL will be displayed in the workflow diagram, giving users an easy way to navigate to the environment. The value of this property is set as the output of the step with id deploywebapp, which is defined below.
5. You're executing a download-artifact step to download the artifact (compiled web app) from the build job.
6. You then login to Azure using the AZURE\_CREDENTIALS secret you saved earlier. Note the ${{ }} notation for dereferencing variables.
7. You then perform a webapp-deploy, specifying the app-name, slot-name, and path to the downloaded artifact (package). This action also defines an output parameter that you use to set the url of the environment above.

&lt; →

→ G A Not secure | cd-simplefeedreader-staging azurewebsites.net

AZ Exams

AZ Exams

A Not secure | cd-simplefeedreader-staging azurewebsites.net

Learning

Learning

.NET on Actions

NET on Actions

SimpleFeedReader

SimpleFeedReader

8. Finally, you execute a logout to log out of the Azure context.
5. Commit the file.

Enter a feed URL:

6. When the run completes, you should see two successful jobs. The URL for the PRE-PROD stage has been set and selecting it will navigate you to your web app staging slot:

**iono 7** Tha chaoino clot nunnino

**Figure 6**: Deployment to PRE-PROD is successful.

<!-- image -->

1. Notice how the staging slot's direct URL contains -staging:
1. You can also now see deployments. Navigate to https://{your repository url}/deployments to view your deployments:

**Figure 7**: The staging slot running.

<!-- image -->

Search or jump to....

Pull requests Issues Codespaces Marketplace Explore

° colindembovsky / simple-feed-reader forked from Azure-Samples/simple-feed-reader

‹&gt; Code

11 Pull requests

• Actions

" Projects

Ц Wiki

Deployed to PRE-PROD

**figune 9**. View denlovmente..

• Security

~ Insights

13 Settings

**Figure 8**: View deployments.

<!-- image -->

## Deploy to production

Now that you've deployed successfully to PRE-PROD, you'll want to deploy to PROD. Deployment to PROD will be slightly different since you don't need to copy the website again - you just need to swap the staging slot with the production slot. You'll do this using an Azure CLI (az) command.

1. Navigate to the .github/workflows/dotnet.yml file and select the pencil icon to edit the file.
2. Add a new job below the deploy\_staging job as follows:
3. :::{custom-style=CodeBox} ```yml run: az logout # &lt;– last line of previous job: insert below this line

deploy\_prod: needs: deploy\_staging runs-on: ubuntu-latest

```
environment: name: PROD url: ${{ steps.slot_swap.outputs.url }} steps: -name: Login via Azure CLI uses: azure/login@v1 with: creds: ${{ secrets.AZURE_CREDENTIALS }} -name: Swap staging slot into production id: slot_swap run: | az webapp deployment slot swap -g ${{ env.rg-name }} -n ${{ env.app-name }} -s staging url=$(az webapp show -g ${{ env.rg-name }} -n ${{ env.app-name }} --query "defaultHostName" -o tsv) echo "::set -output name=url::http://$url" -name: az cli logout run: az logout ``` :::
```

The deployment to the PROD environment workflow specifies several steps:

1. Once again, you specify a new job deploy\_prod that needs deploy\_staging to complete before starting.
2. You're targeting the PROD environment this time. Also, the url value is different from before.

© Watch -

$ Star

select Approve ana deploy to start Ine PROD JOD.

• Watch r

• Watch +

Search or jump to....

Pull requests Issues Codespaces Marketplace Explore

Review pending deployments requested by colindembovsky in NET #9

Y colindembovsky / simple-feed-reader forked from Anure-Samples/imple-feed-render

&lt;&gt; Code

I7 Pull requests

• Actions a Projects

• Update dotnet.yml NET #9

PROD

Review needed from colindembovsky

• Summary

Jobs

Leave a comment

• build

• deploy staging

© deploy\_prod

** igno

• Wiki dotnet.ymi

on: push build

let Insights

© Security

Reject

• Star

0

&amp; Fork

# sur

Y Fork

79

Cancel workflow

Cancel workflow

3. For the steps, you don't need to download the artifact since you're just going to perform a slot swap. You start by executing a login to the Azure context.
4. The Swap staging slot into production step is a multi-line run command (note the use of the pipe symbol |). You also specify an id for this step so that you can refer to it (you refer to it in the url property of the environment). The first line executes the slot swap using the variables you defined above in the workflow. The second line uses an az webapp show command to extract the URL of the target web app. This final line uses ::set -output in an echo to create an output variable for this task, setting the value to the web app URL.

[!NOTE] The URL must start with http:// or https:// or it won’t render.

3. Commit the file.
4. Let the workflow run for a couple minutes until it has deployed to PRE-PROD. At this point, the workflow will pause and wait for the required approval since you're targeting the PROD environment, which requires an approval as defined earlier:
1. Select Review deployments, select the PROD checkbox, optionally add a comment, and then select Approve and deploy to start the PROD job.
1. The deployment should only take a few seconds. Once it has completed, the URL for the PROD environment will update.

**Figure 9**: Waiting for an approval.

<!-- image -->

**Figure 10**: Approve the PROD deployment.

<!-- image -->

• Settings

79

Search or jump to...

G

The deployments have been approved.

AZ Exams

Learning

Pull requests Issues Codespaces Marketplace Explore

A Not secure | cd-simplefeedreader.azurewebsites.net

.NET on Actions

У colindembovsky / simple-feed-reader forked from Azure-Samples/simple-feed-reader

‹&gt; Code

I2 Pull requests

O Actions

Update dotnet.yml .NET #10

G Summary

Jobs

© build

© deploy\_staging

© deploy\_prod

**fioune 11**. PROD denloyment comnleted

**fioune 12**. The DRON cite

" Projects

M Wiki

© Security

L Insights

@ Settings

SimpleFeedReader

**Figure 11**: PROD deployment completed.

<!-- image -->

1. Selecting the PROD URL will navigate you to the PROD site.

**Figure 12**: The PROD site.

<!-- image -->

## Add a manual queue option

You now have an end -to -end build and deploy workflow, including approvals. One more change you can make is to add a manual trigger to the workflow so that the workflow can be triggered from within the Actions tab of the repository.

1. Navigate to the .github/workflows/dotnet.yml file and select the pencil icon to edit the file.
2. Add a new trigger between on and push on lines 3 and 4:
3. :::{custom-style=CodeBox} yml on: workflow\_dispatch: # &lt;-- this is the new line push: :::
3. The workflow\_dispatch trigger displays a Run workflow button in the Actions tab of the repository—but only if the trigger is defined in the default branch. However, once this trigger is defined in the workflow, you can select the branch for the run.
4. Commit the file.

© Watch - 0

Search or jump to....

Pull requests

Y colindembovsky / simple-feed-reader forked from Azure-Samples/simple-feed-reader

• Code

I? Pull requests

• Actions

Workflows

All workflows lo NET

• Projects

New workflow

Issues Codespaces Marketplace Explore

Щ Wiki

© Security

Le Insights

NET

5. To see the Run workflow button, select the Actions tab. Select the .NET workflow in the list of workflows. At the top of the list of runs, you'll see the Run workflow button. If you select it, you can choose the branch to run the workflow against and queue it:

• Update dotnet.ymi

**fioune 13**. Manual dicnatch..

Use workflow from

**Figure 13**: Manual dispatch.

<!-- image -->

## Handle environment configuration

Your workflow is deploying the same binary to each environment. This concept is important to ensure that the binaries you test in one environment are the same that you deploy to the next. However, environments typically have different settings like database connection strings. You want to ensure that the DEV app is using DEV settings and the PROD app is using PROD settings.

For this simple app, there's no database connection string. However, there's an example configuration setting that you can modify for each environment. If you open the simple-feed- reader/SimpleFeedReader/appsettings.json file, you'll see that the configuration includes a setting for the Header text on the Index page:

```
"UI": { "Index": { "Header": "Simple News Reader" } } ,
```

To show how environment configuration can be handled, you're going to add a secret to each environment and then substitute that value into the settings as you deploy.

## Add environment secrets

1. On your repository, select Settings &gt; Environments &gt; PRE-PROD .
2. Select Add secret and add a secret called index\_header with the value PRE PROD News Reader. Select Add secret .

@ Settings master

© Watch -

62 Star

Actions secrets

Add secret

X

New repository secret

Secrets are environment variables that are encrypted. Anyone with collaborator access to this repository can use these secrets for Actions.

Name

Secrets are not passed to workflows that are triggered by a pull request from a fork. Learn more.

index\_header

Value

Environment secrets

PRE PROD News Reader

INDEX\_HEADER

PROD

INDEX\_HEADER

PRE-PROD

Set an amount of time to wait before allowing deployments to proceed.

Repository secrets

Save protection rules

&amp; AZURE\_CREDENTIALS

Environment secrets

Secrets are encrypted environment variables. They are accessible only by GitHub Actions in the contex

1

Add Secret

**fioune 15**. View cernetc.

**fioune 14**• Add an envisaament coset

**Figure 14**: Add an environment secret.

<!-- image -->

1. Repeat these steps to add a secret called index\_header with the value PROD News Reader for the PROD environment.
2. If you select Settings &gt; Secrets in the repository, you'll see the changes. They should look something like this:

**Figure 15**: View secrets.

<!-- image -->

## Update the workflow to handle configuration

1. Navigate to the .github/workflows/dotnet.yml file and select the pencil icon to edit the file.
2. Add the following step before the az cli logout step in the deploy\_staging job:

```
:::{custom-style=CodeBox} ```yml - name: Update config uses: Azure/appservice-settings@v1 with: app-name: ${{ env.app-name }} slot-name: staging app-settings-json: | [ { "name": "UI:Index:Header", "value": "${{ secrets.INDEX_HEADER }}","slotSetting": true } ]
```

```
-name: az cli logout # <-this exists already ``` :::
```

8

→

A Not secure cd-simplefeedreader-staging.azureweb...

AZ Exams i Learning

• NET on Actions

SimpleFeedReader

PRE PROD News Reader

Enter a feed URL:

- →

G A Not secure | cd-simplefeedreader. azurewebsites.net i AZ Exams

i Learning ) NET on Actions

SimpleFeedReader

PROD News Reader

3. Add almost the same code to the deploy\_prod job above its az cli logout step. The only difference is that you don't specify a slot-name, since you're targeting the production slot:

Retrieve Feed

© 2017 - SimpleFeedReader

Retrieve Feed

- :::{custom-style=CodeBox} ```yml - name: Update config uses: Azure/appservice-settings@v1 with: app-name: ${{ env.app-name }} app-settings-json: | [ { "name": "UI:Index:Header", "value": "${{ secrets.INDEX\_HEADER }}","slotSetting": true } ]
4. Commit the file.
5. Let the workflow run and approve the deployment to PROD once the approval is reached.
6. You should see the following headers on the index page for both sites:
- **Figure 16**: Settings changed in the environments.

```
-name: az cli logout # <-this exists already ``` :::
```

<!-- image -->

## Final workflow file

The final workflow file should look like this:

```
name: .NET on: workflow_dispatch: inputs: reason: description: 'The reason for running the workflow' required: true default: 'Manual build from GitHub UI' push: branches: [ main ] pull_request: branches: [ main ] env: app -name: "cd -simplefeedreader" rg -name: "cd -dotnetactions" jobs: build:
```

•..

10

```
runs-on: ubuntu -latest steps: -uses: actions/checkout@v3 -name: 'Print manual run reason' if: ${{ github.event_name == 'workflow_dispatch' }} run: | echo 'Reason: ${{ github.event.inputs.reason }}' -name: Setup .NET uses: actions/setup-dotnet@v3 with: dotnet -version: 6.0.x -name: Restore dependencies run: dotnet restore -name: Build run: dotnet build --no-restore -name: Test run: dotnet test --no-build --verbosity normal -name: Publish run: dotnet publish SimpleFeedReader/SimpleFeedReader.csproj -c Release -o website -name: Upload a Build Artifact uses: actions/upload-artifact@v3 with: name: website path: SimpleFeedReader/website/** if -no-files -found: error deploy_staging: needs: build runs-on: ubuntu -latest environment: name: STAGING url: ${{ steps.deploywebapp.outputs.webapp-url }} steps: -name: Download a Build Artifact uses: actions/download-artifact@v3 with: name: website path: website -name: Login via Azure CLI uses: azure/login@v1 with: creds: ${{ secrets.AZURE_CREDENTIALS }} -name: Deploy web app id: deploywebapp uses: azure/webapps-deploy@v2 with: app -name: ${{ env.app-name }} slot -name: staging package: website -name: Update config uses: Azure/appservice-settings@v1 with: app -name: ${{ env.app-name }} slot -name: staging app -settings-json: |
```

```
[ { "name": "UI:Index:Header", "value": "${{ secrets.INDEX_HEADER }}", "slotSetting": true } ] -name: az cli logout run: az logout deploy_prod: needs: deploy_staging runs-on: ubuntu -latest environment: name: PROD url: ${{ steps.slot_swap.outputs.url }} steps: -name: Login via Azure CLI uses: azure/login@v1 with: creds: ${{ secrets.AZURE_CREDENTIALS }} -name: Swap staging slot into production id: slot_swap run: | az webapp deployment slot swap -g ${{ env.rg-name }} -n ${{ env.app-name }} -s staging url=$(az webapp show -g ${{ env.rg-name }} -n ${{ env.app-name }} --query "defaultHostName" -o tsv) echo "::set -output name=url::http://$url" -name: Update config uses: Azure/appservice-settings@v1 with: app -name: ${{ env.app-name }} app -settings-json: | [ { "name": "UI:Index:Header", "value": "${{ secrets.INDEX_HEADER }}", "slotSetting": true } ] -name: az cli logout run: az logout
```

## Secure .NET Code with CodeQL and GitHub Actions

CodeQL is a static code analysis engine that can automate security and quality checks. With CodeQL, you can perform variant analysis, which uses known vulnerabilities as seeds to find similar issues. CodeQL is part of GitHub Advanced Security that includes:

[!div class=“checklist”]

Search or jump to....

Pull requests Issues Marketplace Explore

Y colindembovsky / simple-feed-reader forked from Azure-Samples/simple-feed-reader

&lt;&gt; Code

12 Pull requests

• Actions

WE Projects

1 Wiki

© Security w Insights

© Settings

- Code scanning—find potential security vulnerabilities in your code. Overview
- Secret scanning—detect secrets and tokens that are committed.
- Dependency scanning—detect vulnerabilities in packages that you consume.

Code scanning alerts

CodeQL supports some of the most popular programming languages and compilers:

Croate a new code cranning wonkflow.

- C/C++
- Java
- C#
- Python
- Go
- JavaScript
- TypeScript

CodeQL is a powerful language and security professionals can create custom queries using CodeQL. However, teams can benefit immensely from the large open-source collection of queries that the security community has created without having to write any custom CodeQL.

In this article, you'll set up a GitHub workflow that will scan code in your repository using CodeQL. You will:

[!div class=“checklist”]

- Create a code scanning action.
- Edit the workflow file to include custom scan settings.
- See scanning results.

## Note

To see security alerts for your repository, you must be a repository owner.

## Create the code scanning workflow

You can use a starter workflow for code scanning by navigating to the Security tab of your repository.

1. Navigate to your GitHub repository and select the Security &gt; Code Scanning Alerts. The top recommended workflow should be CodeQL Analysis. Select Set up this workflow .

**Figure 1:** Create a new code scanning workflow.

<!-- image -->

**ioune 1.**

4

10

11

Search or jump to....

Pull requests Issues Marketplace Explore

Search or jump to...

Pull requests Issues Marketplace Explore

Y colindembovsky / simple-feed-reader

Y colindembovsky / simple-feed-reader forked from Azure-Samples/simple-feed-reader

forked from Azure-Samples/simple-feed-reader

‹&gt; Code

I7 Pull requests

&lt;&gt; Code

17 Pull requests

Workflows

‹&gt; Edit new file

• Preview

All workflows

NET

• to conmit it to your repository-

• Actions

Projects

MO Wiki

Security

L Insights

@ Settings

• Actions

Projects

M Wiki

• Security

L Insights

@ Settings

1. A new workflow file is created in your .github/workflows folder.

codeql-analysisymi

2. Select Start Commit on the upper right to save the default workflow. You can commit to the main branch. Search Marketplace for Actions

CodeQL

• You may wish to alter this file to override the set of languages analyzed,

1 workflow run

• or to provide custom queries or build logic.

* ******** NOTE ********

# Ne have attempted to detect the languages in your repository. Please check

• the "Language" matrix defined below to confirm you have the correct set of

# supported CodeQL languages.

#

12

name: "CodeoL-

**iome 3** Wiew the Coded workflow nune.

**fioune ?.**

Commit the file

Event -

Status ~

Branch -

Actor -

**Figure 2:** Commit the file.

<!-- image -->

1. Select the Actions tab. In the left -hand tree, you'll see a CodeQL node. Select this node to filter for CodeQL workflow runs.

**Figure 3:** View the CodeQL workflow runs.

<!-- image -->

Take a look at the workflow file while it runs. If you remove the comments from the file, you'll see the following YAML:

```
name: "CodeQL" on: push: branches: [ main ] pull_request: branches: [ main ] schedule: -cron: '40 14 * * 6' jobs: analyze: name: Analyze runs-on: ubuntu -latest strategy: fail -fast: false
```

• Watch -

• Watch -

* Star

Star

+-

+ -

Y Fork

Y Fork

92

92

```
matrix: language: [ 'csharp' ] steps: -name: Checkout repository uses: actions/checkout@v3 -name: Initialize CodeQL uses: github/codeql-action/init@v1 with: languages: ${{ matrix.language }} -name: Autobuild uses: github/codeql-action/autobuild@v1 -name: Perform CodeQL Analysis uses: github/codeql-action/analyze@v1
```

Notice the following things:

1. The workflow name is CodeQL.
2. This workflow triggers on push and pull\_request events to the main branch. There's also a cron trigger. The cron trigger lets you define a schedule for triggering this workflow and is randomly generated for you. In this case, this workflow will run at 14:40 UTC every Saturday.

[!TIP] If you edit the workflow file and hover over the cron expression, a tooltip will show you the English text for the cron expression.

3. There's a single job called analyze that runs on the ubuntu-latest hosted agent.
4. This workflow defines a strategy with a matrix on the array of language. In this case, there's only csharp. If the repository contained other languages, you could add them to this array. This causes the job to "fan out" and create an instance per value of the matrix.
5. There are four steps, starting with checkout.
6. The second step initializes the CodeQL scanner for the language this job is going to scan. CodeQL intercepts calls to the compiler to build a database of the code while the code is being built.
7. The Autobuild step will attempt to automatically build the source code using common conventions. If this step fails, you can replace it with your own custom build steps.
8. After building, the CodeQL analysis is performed, where suites of queries are run against the code database.
9. The run should complete successfully. However, there appear to be no issues.

Search or jump to...

Overview

Security policy

Code scanning

Pull requests Issues Marketplace Explore

Y colindembovsky / simple-feed-reader forked from Azure-Samples/simple-feed-reader

Security advisories

‹&gt; Code

Il Pull requests

Dependabot alerts

P master -

Code scanning alerts simple-feed-reader / github /

CodeQL

This branch is 20 commits ahead of Azure-Samples:master.

colindembovsky Create codeql-analysis.yml workflows

ISSUE TEMPLATE.md

**iono 5**

**figune 4.** No neculte to the initial ecan.

Filters -

Q tool:CodeQL is:open

Projects

• v 0Open x 0 Closed

Set up more code scanning tools

4 +- g-

© Watch -

0

• Star 0

Y Fork

92

Branch - Severity - Rule - Tag - Sort-

Actions

Щ Wiki

• Security

L Insights

฿ Settings

**Figure 4:** No results to the initial scan.

<!-- image -->

## Customize CodeQL settings

The CodeQL scan isn't reporting any security issues. That's expected with this basic sample. CodeQL can also scan for quality issues. The current workflow is using the default security-extended suite. You can add quality scanning in by adding a configuration file to customize the scanning suites. In this step, you'll configure CodeQL to use the security-and-quality suites.

[!INFORMATION] For other CodeQL configuration options, see Configuring CodeQL code scanning in your CI system .

1. Navigate to the .github folder in the Code tab and select Add File:
1. Enter codeql/codeql-config.yml as the name. This creates the file in a folder. Paste in the following code:
3. :::{custom-style=CodeBox} ```yml name: “Security and Quality”

**Figure 5:** Create a new file.

<!-- image -->

queries:

- – uses: security-and-quality ``` :::

Search or jump to...

• Pull requests Issues Marketplace Explore y colindembovsky / simple-feed-reader

forked from Azure-Samples/simple-feed-reader

‹&gt; Code

13 Pull requests simple-feed-reader / github / codeql / codeql-config.yml

‹&gt; Edit new file

1

name: "Security and Quality"

2

<!-- image -->

queries:

- uses: security-and-quality

**Fioune 6.**

**Figure 6:** Create the CodeQL configuration file.

1. Select Commit to main at bottom of the editor to commit the file.
2. Edit the CodeQL workflow to use the new configuration file. Navigate to .github/workflows/codeql-analysis.yml and select the pencil icon. Add a new property to the with section as shown below:
3. :::{custom-style=CodeBox} yml - name: Initialize CodeQL uses: github/codeql-action/init@v1 with: languages: ${{ matrix.language }} config-file: ./.github/codeql/codeql-config.yml # &lt;-add this line :::
1. Select Start Commit and commit to the main branch.

## Review the security alerts

<!-- image -->

When the last CodeQL workflow run completes, you should see two issues in the Security tab:

Search or jump to...

Pull requests Issues Marketplace Explore

Missed 'readonly' opportunity

A private field where all assignments occur as part of the declaration or in a constructor in the same class can be 'readonly.

Open

Y colindembovsky / simple-feed-reader

E Note language features

maintainability forked from Azure-Samples/simple-feed-reader

Branch: master -

&lt;&gt; Code

17 Pull requests

© Actions

SimpleFeedReader/obj/Debug/netcoreapp2.1/Razor/Pages/Index.cshtml.g.cs ®

Overview

Field \_tagHelperRunner" can be readonly'.

CodeQL

Security policy

Security advisories

Tool

Rule ID

CodeQL

Dependabot alerts cs/missed-readonly-modifier

A private field where all assignments occur as part of the declaration or in a constructor in the same class can be readonly. Making a field readonly prevents unintended assignments after object initialization.

Code scanning alerts

CodeQL

• First appeared in commit 824b301 8 minutes ago

-O-

Update codeql-analysis.ym1

SimpleFeedReader/obj/Debug/netcoreapp2.1/Razor/Pages/Index.cshtml.g.cs#L31 on branch master

**figune 8.** Onen an alent.

W Projects

M Wiki

© Security 2

L Insights

@ Settings

Generated

Figure 7: View security alerts.

<!-- image -->

1. Select the first alert to open it.
2. In this case, the alert is for a generated file that isn't committed to the repository. For that reason, the preview is unavailable.
3. Notice the tags that are applied. These tags can be used for filtering issues.
4. Select Show more under the rule information to show help and recommendations.
1. Selecting Dismiss will open options for dismissing this issue:

**Figure 8:** Open an alert.

<!-- image -->

Dismiss -

© Watch -

0

Star

0

+-

Y Fork

92

Dismiss reason

False positive

This alert is not valid

Used in tests

This alert is not in production code

Won't fix

This alert is not relevant

Nicmice an alant

**igno o.**

Dismiss

**Figure 9:** Dismiss an alert.

<!-- image -->

mywebapp21816

App Service

2 Scarch (Chrl*/

werniew

Activity log

Access control (LAM)

• Tags

% Diagnose and solve problems de Quickstart

ment recentals homenisios

i@ Deployment options

66 Continuous Delivery (Preview)

SETTING

-Applcation setling"

Chuthenucabon Authonzabon

Application Insights

Managed service identity (Pr...

Custom domains

SSL settings

+ Networking

2 Scale up (App Service plan)

Ka Scale out (App Service plan)

Weblobs

PuST

MysQL In App

Properties

LOCKE

4 Browse

4 Stop

Resource group (change)

REUrCIUCOT

Status

Running

Loraton

Centr

Subscription (change)

VUch

Subscription ID

df118062-9277-4081-a559-888e4c82c4db

Diagnose and solve problems

Dur sell-service diagnostic and troubleshooting experience sepsyou isentry ana teiche ile wid yowed aps

Http Sxx

8

243.52 m

Having deployed the app and built a DevOps pipeline, it's important to understand how to monitor and troubleshoot the app.

In this section, you’ll complete the following tasks:

[!div class=“checklist”]

- Find basic monitoring and troubleshooting data in the Azure portal
- Learn how Azure Monitor provides a deeper look at metrics across all Azure services
- Connect the web app with Application Insights for app profiling
- Turn on logging and learn where to download logs
- Stream logs in real time
- Learn where to set up alerts
- Learn about remote debugging Azure App Service web apps.

## Basic monitoring and troubleshooting

App Service web apps are easily monitored in real time. The Azure portal renders metrics in easy-tounderstand charts and graphs.

1. Open the Azure portal, and then navigate to the mywebapp&lt;unique\_number&gt; App Service.
2. The Overview tab displays useful "at-a-glance" information, including graphs displaying recent metrics.

<!-- image -->

4 Swap O Restart aDelate

*Get publich profile () Reus publich profile

URL

https://mywebapp21816.azurewebsites.net

Ap Sempa ier Pingi 1 Smat camsoper

Git/Deployment username

Git clone url https://camsoper@mywebapp21816.scm.azurewebsites.net443/mywebapp21816.git

ttp://waws-prod-dm1-089.ftp.azurewebsites.windows.net

*

Data Out (

1к0

## Monitor and debug

SOPM

Application Insights

Data In

*

<!-- image -->

page.

nywebapp2181

O Search (Ctri-s

Overview ectvity log

Access control AM

Diagnose and solve problems

DEPLOTMETET

Quickstart

Deployment credentials

Deployment slots

• Deployment options.

( Continuous Delivery (Preview)

SETTINO

appucation setting

Authentication / Authorization

Application Insights

Managed service identity (Pr....

Custom domains

SSL settings

Networking

Scale up (App Service plan)

scale out (App service plan, wehiche

Push

MySQL In App

Properties

0*9

4 Browse

• Stor

Resource group Ghanad

AzureTutorial

Status

Running

Location

Central US

Subscription (change)

Subscription ID

* Swap

C Restart

• Delete &amp; Get publish profile C2 Reset publish profile https://mywebapp21816.azurewebsites.net

App Service plan/pricing tier mywebapp21816 (Standard: 1 Small)

Git/Deployment username

Git clone uri https://camsoper@mywebapp21816.scm.azurewebsites.net:443/mywebapp21816.git

FTP hostname htp:/waws-prod-dm1-0bs.ntp.azurewebsites.windows.net

* **Http 5xx**: Count of server-side errors, usually exceptions in ASP.NET Core code. Diaanose and solve problems.
* **Data In**: Data ingress coming into your web app.
* **Data Out**: Data egress from your web app to clients.
* **Requests**: Count of HTTP requests.

460.

360.

* **Average Response Time**: Average time for the web app to respond to HTTP requests.

5:30 PM

5:45 PM

5:15 PM

21.19 kE

DATA OUT

17.57 k

Several self -service tools for troubleshooting and optimization are also found on this page. Requests Average Response Time

<!-- image -->

* **Diagnose and solve problems** is a self-service troubleshooter.
* **Application Insights** is for profiling performance and app behavior, and is discussed later in this section.
* **App Service Advisor** makes recommendations to tune your app experience.

## Advanced monitoring

Azure Monitor is the centralized service for monitoring all metrics and setting alerts across Azure services. Within Azure Monitor, administrators can granularly track performance and identify trends. Each Azure service offers its own set of metrics to Azure Monitor.

## Profile with Application Insights

Application Insights is an Azure service for analyzing the performance and stability of web apps and how users use them. The data from Application Insights is broader and deeper than that of Azure Monitor. The data can provide developers and administrators with key information for improving apps. Application Insights can be added to an Azure App Service resource without code changes.

1. Open the Azure portal, and then navigate to the mywebapp&lt;unique\_number&gt; App Service.
2. From the Overview tab, click the Application Insights tile.

5:30 PM

6 PM

5:30 PM

5:45 PM

6 PM

Application Insights

Application Insights

Application Insights helps you detect and diagnose quality mywebapp21816 Application Insights resource is connected Change

Application Insights helps you detect and diagnose quality issues in your web apps and web services, and helps yo tually do with it.

issues in your apps, and helps you understand what your

Troubleshooting information

Getting started with Application Insights monitoring users actually do with it.

Link your application to Application Insights

• Select existing resource

Search....

• my-blog

• Create new resource

* New resource name mywebapp21816

Instrument your application

* Runtime/Framework

ASP.NET Core

Code level diagnostics

Identify code that slowed down your web app and debug runtime exceptions with local variables v Advanced Settings

<!-- image -->

* Location

East US

1. Select the Create new resource radio button. Use the default resource name, and select the location for the Application Insights resource. The location doesn't need to match that of your web app.
1. For Runtime/Framework, select ASP.NET Core. Accept the default settings.
2. Select OK. If prompted to confirm, select Continue .
3. After the resource has been created, click the name of Application Insights resource to navigate directly to the Application Insights page.

<!-- image -->

<!-- image -->

As the app is used, data accumulates. Select Refresh to reload the blade with new data.

mywebapp21816

Application Insights - Last 24 hours (30 minute granularity) - ASP.NET web application

• Search (Ctrl+/)

Overview

Activity log iM Access control (IAM)

Tags

% Diagnose and solve problems

INVESTIGATE

• Application map

Smart Detection

1- Live Metrics Stream

Metrics Explorer

Metrics (preview)

Search

Availability

Failures

Performance

Servers

Browser

Workbooks (preview)

USAGE (PREVIEW)

M Users

Sessions

Events

= Funnels

Beg User Flows

Retention

Impact

Cohorts

«

~ Search ith Metrics Explorer

Time range

# Analytics

© Refresh

Please try new Overview before it becomes the default experience. →

<!-- image -->

Application Insights provides useful server-side information with no additional configuration. To get the most value from Application Insights, instrument your app with the Application Insights SDK . When properly configured, the service provides end-to-end monitoring across the web server and

Ils

*

X

••• More

MONITORING

• Alerts (Classic)

+

browser, including client-side performance. For more information, see the Application Insights documentation .

Log stream

## Logging

Web server and app logs are disabled by default in Azure App Service. Enable the logs with the following steps:

1. Open the Azure portal, and navigate to the mywebapp&lt;unique\_number&gt; App Service.
2. In the menu to the left, scroll down to the Monitoring section. Select Diagnostics logs .
1. Turn on Application Logging (Filesystem). If prompted, click the box to install the extensions to enable app logging in the web app.
2. Set Web server logging to File System .
3. Enter the Retention Period in days. For example, 30.
4. Click Save .

<!-- image -->

ASP.NET Core and web server (App Service) logs are generated for the web app. They can be downloaded using the FTP/FTPS information displayed. The password is the same as the deployment credentials created earlier in this guide. The logs can be streamed directly to your local machine with PowerShell or Azure CLI. Logs can also be viewed in Application Insights .

## Log streaming

App and web server logs can be streamed in real time through the portal.

1. Open the Azure portal, and navigate to the mywebapp&lt;unique\_number&gt; App Service.
2. In the menu to the left, scroll down to the Monitoring section and select Log stream .

MONITORING

MONITORING

V Alerts (Classic)

V Alerts (Classic)

Diagnostics logs

Diagnostics logs

Log stream

Log stream

Process explorer

Process explorer

<!-- image -->

Logs can also be streamed via Azure CLI or Azure PowerShell, including through the Cloud Shell.

## Alerts

Azure Monitor also provides real time alerts based on metrics, administrative events, and other criteria.

<!-- image -->

The Alerts (classic) service can be found in Azure Monitor or under the Monitoring section of the App Service settings.

<!-- image -->

## Live debugging

Azure App Service can be debugged remotely with Visual Studio when logs don't provide enough information. However, remote debugging requires the app to be compiled with debug symbols. Debugging shouldn't be done in production, except as a last resort.

## Conclusion

In this section, you completed the following tasks:

[!div class=“checklist”]

- Find basic monitoring and troubleshooting data in the Azure portal
- Learn how Azure Monitor provides a deeper look at metrics across all Azure services
- Connect the web app with Application Insights for app profiling
- Turn on logging and learn where to download logs
- Stream logs in real time
- Learn where to set up alerts
- Learn about remote debugging Azure App Service web apps.

## Additional reading

| •   | Troubleshooting ASP.NET Core on Azure App Service and IIS                         |
|-----|-----------------------------------------------------------------------------------|
| •   | Common errors reference for Azure App Service and IIS with ASP.NET Core           |
| •   | Monitor Azure web app performance with Application Insights                       |
| •   | Enable diagnostics logging for web apps in Azure App Service                      |
| •   | Troubleshoot a web app in Azure App Service using Visual Studio                   |
| •   | Create classic metric alerts in Azure Monitor for Azure services  -  Azure portal |

## Next steps

In this guide, you created a DevOps pipeline for an ASP.NET Core sample app. Congratulations! We hope you enjoyed learning to publish ASP.NET Core web apps to Azure App Service and automate the continuous integration of changes.

Beyond web hosting and DevOps, Azure has a wide array of Platform-as-a-Service (PaaS) services useful to ASP.NET Core developers. This section gives a brief overview of some of the most commonly used services.

## Storage and databases

Redis Cache is high-throughput, low-latency data caching available as a service. It can be used for caching page output, reducing database requests, and providing ASP.NET Core session state across multiple instances of an app.

Azure Storage is Azure's massively scalable cloud storage. Developers can take advantage of Queue Storage for reliable message queuing, and Table Storage is a NoSQL key-value store designed for rapid development using massive, semi-structured data sets.

Azure SQL Database provides familiar relational database functionality as a service using the Microsoft SQL Server Engine.

Cosmos DB globally distributed, multi-model NoSQL database service. Multiple APIs are available, including SQL API (formerly called DocumentDB), Cassandra, and MongoDB.

## Identity

Azure Active Directory and Azure Active Directory B2C are both identity services. Azure Active Directory is designed for enterprise scenarios and enables Azure AD B2B (business-to-business) collaboration, while Azure Active Directory B2C is intended business-to-customer scenarios, including social network sign-in.

## Mobile

Notification Hubs is a multi -platform, scalable push-notification engine to quickly send millions of messages to apps running on various types of devices.

## Web infrastructure

Azure Container Service manages your hosted Kubernetes environment, making it quick and easy to deploy and manage containerized apps without container orchestration expertise. Azure Search is used to create an enterprise search solution over private, heterogenous content. Service Fabric is a distributed systems platform that makes it easy to package, deploy, and manage scalable and reliable microservices and containers.