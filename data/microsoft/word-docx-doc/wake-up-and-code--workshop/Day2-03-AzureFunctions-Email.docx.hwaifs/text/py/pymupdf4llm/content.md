Azure Functions Intro + Email

Sources:

Portal: https://docs.microsoft.com/en-us/azure/azure-functions/functions-create-first-azure-function

VS: https://docs.microsoft.com/en-us/azure/azure-functions/functions-create-your-first-function-visual-studio

SendGrid V3 API Sample: https://sendgrid.com/docs/for-developers/sending-email/v3-csharp-code-example/

Email with SendGrid: https://docs.microsoft.com/en-us/azure/azure-functions/functions-bindings-sendgrid


Create your first function in the Azure portal

Azure Functions lets you execute your code in a serverless environment without having to first create a VM or
publish a web application. In this topic, learn how to use Functions to create a "hello world" function in the
Azure portal.


If you don't have an Azure subscription, create a free account before you begin.

Note

C# developers should consider creating your first function in Visual Studio 2017 instead of in the portal.

Log in to Azure

Sign in to the Azure portal at https://portal.azure.com with your Azure account.

Create a function app

You must have a function app to host the execution of your functions. A function app lets you group functions
as a logic unit for easier management, deployment, and sharing of resources.

Select the New button found on the upper left-hand corner of the Azure portal, then
select Compute > Function App.


Use the function app settings as specified in the table below the image.


Setting

Suggested value

Description

App name

Globally unique name

Name that identifies your new function app. Valid characters are a-z, 0-9, and -.

Subscription

Your subscription

The subscription under which this new function app is created.

Resource Group

myResourceGroup

Name for the new resource group in which to create your function app.

OS

Windows

Serverless hosting is currently only available when running on Windows. For Linux hosting, see Create your
first function running on Linux using the Azure CLI.

Hosting plan

Consumption plan

Hosting plan that defines how resources are allocated to your function app. In the default Consumption Plan,
resources are added dynamically as required by your functions. In this serverless hosting, you only pay for the
time your functions run. When you run in an App Service plan, you must manage the scaling of your function
app.

Location

West Europe

Choose a region near you or near other services your functions access.

Runtime stack

Preferred language

Choose a runtime that supports your favorite function programming language. Choose .NET for C# and F#
functions.

Storage

Globally unique name

Create a storage account used by your function app. Storage account names must be between 3 and 24
characters in length and may contain numbers and lowercase letters only. You can also use an existing account,
which must meets the storage account requirements.

Application Insights

Default

Application Insights is enabled by default. Choose a location near your function app.


Select Create to provision and deploy the function app.

Select the Notification icon in the upper-right corner of the portal and watch for the Deployment
succeeded message.


Select Go to resource to view your new function app.

Tip

Having trouble finding your function apps in the portal, try adding Function Apps to your favorites in the
Azure portal.

Next, you create a function in the new function app.

Create an HTTP triggered function

Expand your new function app, then select the + button next to Functions, choose In-portal, and
select Continue.


Choose WebHook + API and then select Create.


A function is created using a language-specific template for an HTTP triggered function.

Now, you can run the new function by sending an HTTP request.

Test the function

In your new function, click </> Get function URL at the top right, select default (Function key), and then
click Copy.


Paste the function URL into your browser's address bar. Add the query string value &name=<yourname> to
the end of this URL and press the Enter key on your keyboard to execute the request. You should see the
response returned by the function displayed in the browser.

The following example shows the response in the browser:


The request URL includes a key that is required, by default, to access your function over HTTP.

When your function runs, trace information is written to the logs. To see the trace output from the previous
execution, return to your function in the portal and click the arrow at the bottom of the screen to expand
the Logs.


Clean up resources

Other quick starts in this collection build upon this quick start. If you plan to work with subsequent quick
starts, tutorials, or with any of the services you have created in this quick start, do not clean up the resources.

Resources in Azure refers to function apps, functions, storage accounts, and so forth. They are grouped
into resource groups, and you can delete everything in a group by deleting the group.

You created resources to complete these quickstarts. You may be billed for these resources, depending on
your account status and service pricing. If you don't need the resources anymore, here's how to delete them:

In the Azure portal, go to the Resource group page.

To get to that page from the function app page, select the Overview tab and then select the link under Resource
group.


To get to that page from the dashboard, select Resource groups, and then select the resource group that you
used for this quickstart.

In the Resource group page, review the list of included resources, and verify that they are the ones you want to
delete.

Select Delete resource group, and follow the instructions.

Deletion may take a couple of minutes. When it's done, a notification appears for a few seconds. You can also
select the bell icon at the top of the page to view the notification.

Next steps

You have created a function app with a simple HTTP triggered function.

Learn how to create functions with other kinds of triggers or how to integrate functions with other Azure
services.

Create a function that runs on a schedule

Add messages to an Azure Storage queue using Functions

For more information, see Azure Functions HTTP bindings.


Create your first function using Visual Studio

Azure Functions lets you execute your code in a serverless environment without having to first create a VM or
publish a web application.

In this article, you learn how to use the Visual Studio 2017 tools for Azure Functions to locally create and test a
"hello world" function. You then publish the function code to Azure. These tools are available as part of the
Azure development workload in Visual Studio 2017.


This topic includes a video that demonstrates the same basic steps.

# **Prerequisites**


To complete this tutorial:

Install Visual Studio 2017 and ensure that the Azure development workload is also installed.

Make sure you have the latest Azure Functions tools.

If you don't have an Azure subscription, create a free account before you begin.

# **Create a function app project**


The Azure Functions project template in Visual Studio creates a project that can be published to a function app
in Azure. A function app lets you group functions as a logical unit for management, deployment, and sharing of
resources.

In Visual Studio, select New > Project from the File menu.

In the New Project dialog, select Installed, expand Visual C# > Cloud, select Azure Functions, type a Name for
your project, and click OK. The function app name must be valid as a C# namespace, so don't use underscores,
hyphens, or any other nonalphanumeric characters.


Use the settings specified in the table that follows the image.


Setting

Suggested value

Description

Version

Azure Functions 2.x (.NET Core)

This creates a function project that uses the version 2.x runtime of Azure Functions which supports .NET Core.
Azure Functions 1.x supports the .NET Framework. For more information, see How to target Azure Functions
runtime version.

Template

HTTP trigger

This creates a function triggered by an HTTP request.

Storage account

Storage Emulator

An HTTP trigger doesn't use the Storage account connection. All other trigger types require a valid Storage
account connection string.

Access rights

Anonymous

The created function can be triggered by any client without providing a key. This authorization setting makes it
easy to test your new function. For more information about keys and authorization, see Authorization keys in
the HTTP and webhook bindings.

Click OK to create the function project and HTTP triggered function.

Visual Studio creates a project and in it a class that contains boilerplate code for the chosen function type.
The FunctionName attribute on the method sets the name of the function. The HttpTrigger attribute specifies
that the function is triggered by an HTTP request. The boilerplate code sends an HTTP response that includes a
value from the request body or query string. You can add input and output bindings to a function by applying
the appropriate attributes to the method. For more information, see the Triggers and bindings section of
the Azure Functions C# developer reference.

Now that you've created your function project and an HTTP-triggered function, you can test it on your local
computer.

# **Test the function locally**


Azure Functions Core Tools lets you run an Azure Functions project on your local development computer. You
are prompted to install these tools the first time you start a function from Visual Studio.

To test your function, press F5. If prompted, accept the request from Visual Studio to download and install
Azure Functions Core (CLI) tools. You may also need to enable a firewall exception so that the tools can handle
HTTP requests.

Copy the URL of your function from the Azure Functions runtime output.


Paste the URL for the HTTP request into your browser's address bar. Append the query string ?
name=<YOUR_NAME> to this URL and execute the request. The following shows the response in the browser
to the local GET request returned by the function:


To stop debugging, press Shift + F5.

After you have verified that the function runs correctly on your local computer, it's time to publish the project
to Azure.

# **Publish the project to Azure**


You must have a function app in your Azure subscription before you can publish your project. You can create a
function app right from Visual Studio.

In Solution Explorer, right-click the project and select Publish.

Select Azure Function App, choose Create New, and then select Publish.


When you enable Run from Zip, your function app in Azure is run directly from the deployment package. For
more information, see Run your Azure Functions from a package file.

Caution

When you choose Select Existing, all files in the existing function app in Azure are overwritten by files from the
local project. Only use this option when republishing updates to an existing function app.

If you haven't already connected Visual Studio to your Azure account, select Add an account....


In the Create App Service dialog, use the Hosting settings as specified in the table below the image:


Setting

Suggested value

Description

App Name

Globally unique name

Name that uniquely identifies your new function app.

Subscription

Choose your subscription

The Azure subscription to use.

Resource Group

myResourceGroup

Name of the resource group in which to create your function app. Choose New to create a new resource group.

App Service Plan

Consumption plan

Make sure to choose the Consumption under Size after you click New to create a serverless plan. Also, choose
a Location in a region near you or near other services your functions access. When you run in a plan other
than Consumption, you must manage the scaling of your function app.

Storage Account

General purpose storage account

An Azure storage account is required by the Functions runtime. Click New to create a general purpose storage
account. You can also use an existing account that meets the storage account requirements.

Click Create to create a function app and related resources in Azure with these settings and deploy your
function project code.

After the deployment is complete, make a note of the Site URL value, which is the address of your function app
in Azure.

# **Test your function in Azure**


Copy the base URL of the function app from the Publish profile page. Replace the localhost:portportion of the
URL you used when testing the function locally

with the new base URL. As before, make sure to append the query string ?name=<YOUR_NAME> to this URL
and execute the request.

The URL that calls your HTTP triggered function should be in the following format:

Copy

http://<APP_NAME>.azurewebsites.net/api/<FUNCTION_NAME>?name=<YOUR_NAME>

Paste this new URL for the HTTP request into your browser's address bar. The following shows the response in
the browser to the remote GET request returned by the function:

# **Watch the video** **Next steps**


You have used Visual Studio to create and publish a C# function app with a simple HTTP triggered function.

Learn how to add input and output bindings that integrate with other services.

Learn more about developing functions as .NET class libraries.


v3 API C# Code Example

We recommend using SendGrid C#, our client library, available on GitHub, with full documentation.

Do you have an API Key yet? If not, go get one. You're going to need it to integrate!

# **Using SendGrid's C# Library**


// using SendGrid's C# Library

// https://github.com/sendgrid/sendgrid-csharp

using SendGrid;

using SendGrid.Helpers.Mail;

using System;

using System.Threading.Tasks;


namespace Example

{

internal class Example

{

private static void Main()

{

Execute().Wait();

}


static async Task Execute()

{

var apiKey =
Environment.GetEnvironmentVariable("NAME_OF_THE_ENVIRONMENT_VARIABLE_FOR_YOUR_SENDGRID_KEY");

var client = new SendGridClient(apiKey);

var from = new EmailAddress("test@example.com", "Example User");

var subject = "Sending with SendGrid is Fun";

var to = new EmailAddress("test@example.com", "Example User");

var plainTextContent = "and easy to do anywhere, even with C#";

var htmlContent = "<strong>and easy to do anywhere, even with C#</strong>";

var msg = MailHelper.CreateSingleEmail(from, to, subject, plainTextContent, htmlContent);

var response = await client.SendEmailAsync(msg);

}

}

}


Azure Functions SendGrid bindings

This article explains how to send email by using SendGrid bindings in Azure Functions. Azure Functions
supports an output binding for SendGrid.

This is reference information for Azure Functions developers. If you're new to Azure Functions, start with the
following resources:

Create your first function

Azure Functions developer reference

Language-specific reference for C#, C# script, F#, Java, JavaScript, or Python

Azure Functions triggers and bindings concepts

Code and test Azure Functions locally

# **Packages - Functions 1.x**


The SendGrid bindings are provided in the Microsoft.Azure.WebJobs.Extensions.SendGrid NuGet package,
version 2.x. Source code for the package is in the azure-webjobs-sdk-extensions GitHub repository.

The following table tells how to add support for this binding in each development environment.

Development environment

To add support in Functions 1.x

Local development - C# class library

Install the package

Local development - C# script, JavaScript, F#

Automatic

Portal development

Automatic

# **Packages - Functions 2.x**


The SendGrid bindings are provided in the Microsoft.Azure.WebJobs.Extensions.SendGrid NuGet package,
version 3.x. Source code for the package is in the azure-webjobs-sdk-extensions GitHub repository.


The following table tells how to add support for this binding in each development environment.

Development environment

To add support in Functions 2.x

Local development - C# class library

Install the package

Local development - C# script, JavaScript, F#, Java and Python

Register the extension

Portal development

Install when adding output binding

To learn how to update existing binding extensions in the portal without having to republish your function app
project, see Update your extensions.

# **Example**


See the language-specific example:

C#

C# script (.csx)

JavaScript

## **C# example**


The following example shows a C# function that uses a Service Bus queue trigger and a SendGrid output
binding.

C#Copy

[FunctionName("SendEmail")]

public static void Run(

[ServiceBusTrigger("myqueue", Connection = "ServiceBusConnection")] OutgoingEmail email,

[SendGrid(ApiKey = "CustomSendGridKeyAppSettingName")] out SendGridMessage message)

{

message = new SendGridMessage();

message.AddTo(email.To);

message.AddContent("text/html", email.Body);


message.SetFrom(new EmailAddress(email.From));

message.SetSubject(email.Subject);

}


public class OutgoingEmail

{

public string To { get; set; }

public string From { get; set; }

public string Subject { get; set; }

public string Body { get; set; }

}

You can omit setting the attribute's ApiKey property if you have your API key in an app setting named
"AzureWebJobsSendGridApiKey".

## **C# script example**


The following example shows a SendGrid output binding in a function.json file and a C# script function that
uses the binding.

Here's the binding data in the function.json file:

JSONCopy

{

"bindings": [

{

"type": "queueTrigger",

"name": "mymsg",

"queueName": "myqueue",

"connection": "AzureWebJobsStorage",

"direction": "in"

},

{

"type": "sendGrid",

"name": "$return",

"direction": "out",

"apiKey": "SendGridAPIKeyAsAppSetting",

"from": "{FromEmail}",

"to": "{ToEmail}"

}

]

}

The configuration section explains these properties.


Here's the C# script code:

C#Copy

#r "SendGrid"


using System;

using SendGrid.Helpers.Mail;

using Microsoft.Azure.WebJobs.Host;


public static SendGridMessage Run(Message mymsg, ILogger log)

{

SendGridMessage message = new SendGridMessage()

{

Subject = $"{mymsg.Subject}"

};


message.AddContent("text/plain", $"{mymsg.Content}");


return message;

}

public class Message

{

public string ToEmail { get; set; }

public string FromEmail { get; set; }

public string Subject { get; set; }

public string Content { get; set; }

}

## **JavaScript example**


The following example shows a SendGrid output binding in a function.json file and a JavaScript function that
uses the binding.

Here's the binding data in the function.json file:

JSONCopy

{

"bindings": [

{

"name": "$return",

"type": "sendGrid",

"direction": "out",

"apiKey" : "MySendGridKey",

"to": "{ToEmail}",

"from": "{FromEmail}",

"subject": "SendGrid output bindings"


}

]

}

The configuration section explains these properties.

Here's the JavaScript code:

JavaScriptCopy

module.exports = function (context, input) {

var message = {

"personalizations": [ { "to": [ { "email": "sample@sample.com" } ] } ],

from: { email: "sender@contoso.com" },

subject: "Azure news",

content: [{

type: 'text/plain',

value: input

}]

};


context.done(null, message);

};

# **Attributes**


In C# class libraries, use the SendGrid attribute.

For information about attribute properties that you can configure, see Configuration. Here's
a SendGridattribute example in a method signature:

C#Copy

[FunctionName("SendEmail")]

public static void Run(

[ServiceBusTrigger("myqueue", Connection = "ServiceBusConnection")] OutgoingEmail email,

[SendGrid(ApiKey = "CustomSendGridKeyAppSettingName")] out SendGridMessage message)

{

...

}

For a complete example, see C# example.

# **Configuration**


The following table explains the binding configuration properties that you set in the function.json file and
the SendGrid attribute.

function.json property

Attribute property

Description

type


Required - must be set to sendGrid.

direction


Required - must be set to out.

name


Required - the variable name used in function code for the request or request body. This value is $return when
there is only one return value.

apiKey

ApiKey

The name of an app setting that contains your API key. If not set, the default app setting name is
"AzureWebJobsSendGridApiKey".

to

To

the recipient's email address.

from

From

the sender's email address.

subject

Subject

the subject of the email.

text

Text

the email content.

When you're developing locally, app settings go into the local.settings.json file.

# **host.json settings**


This section describes the global configuration settings available for this binding in version 2.x. The example
host.json file below contains only the version 2.x settings for this binding. For more information about global
configuration settings in version 2.x, see host.json reference for Azure Functions version 2.x.

Note


For a reference of host.json in Functions 1.x, see host.json reference for Azure Functions 1.x.

JSONCopy

{

"version": "2.0",

"extensions": {

"sendGrid": {

"from": "Azure Functions <samples@functions.com>"

}

}

}

Property

Default

Description

from

n/a

The sender's email address across all functions.


