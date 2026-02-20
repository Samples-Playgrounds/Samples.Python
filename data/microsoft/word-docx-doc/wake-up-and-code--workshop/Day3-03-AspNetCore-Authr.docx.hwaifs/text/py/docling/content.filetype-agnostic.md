# Authorization for MVC &amp; Razor Pages

Sources:

- Simple MVC (from docs): [https://docs.microsoft.com/en-us/aspnet/core/security/authorization/simple](https:/docs.microsoft.com/en-us/aspnet/core/security/authorization/simple)
- Simple Razor Pages (from blog post): [https://wakeupandcode.com/authentication-authorization-in-asp-net-core-razor-pages/#authrpages](https:/wakeupandcode.com/authentication-authorization-in-asp-net-core-razor-pages/#authrpages)

## Simple authorization in ASP.NET Core

Authorization in MVC is controlled through the AuthorizeAttribute attribute and its various parameters. At its simplest, applying the AuthorizeAttribute attribute to a controller or action limits access to the controller or action to any authenticated user.

For example, the following code limits access to the AccountController to any authenticated user.

C#Copy

[Authorize]

public class AccountController : Controller

{

public ActionResult Login()

{

}

public ActionResult Logout()

{

}

}

If you want to apply authorization to an action rather than the controller, apply the AuthorizeAttributeattribute to the action itself:

C#Copy

public class AccountController : Controller

{

public ActionResult Login()

{

}

[Authorize]

public ActionResult Logout()

{

}

}

Now only authenticated users can access the Logout function.

You can also use the AllowAnonymous attribute to allow access by non-authenticated users to individual actions. For example:

C#Copy

[Authorize]

public class AccountController : Controller

{

[AllowAnonymous]

public ActionResult Login()

{

}

public ActionResult Logout()

{

}

}

This would allow only authenticated users to the AccountController, except for the Login action, which is accessible by everyone, regardless of their authenticated or unauthenticated / anonymous status.

**Warning**

[AllowAnonymous] bypasses all authorization statements. If you combine [AllowAnonymous] and any [Authorize] attribute, the [Authorize] attributes are ignored. For example if you apply [AllowAnonymous] at the controller level, any [Authorize] attributes on the same controller (or on any action within it) is ignored.

## Authorization in ASP.NET Core (Razor Pages)

From: [https://wakeupandcode.com/authentication-authorization-in-asp-net-core-razor-pages/#authrpages](https:/wakeupandcode.com/authentication-authorization-in-asp-net-core-razor-pages/#authrpages)

For Razor Pages, the quickest way to add Authorization for your pages (or entire folders of pages) is to update your ConfigureServices() method in your Startup.cs class, by calling AddRazorPagesOptions() after AddMvc(). The NetLearner configuration includes the following code:

services.AddMvc()

.AddRazorPagesOptions(options =&gt;

{

options.Conventions.AuthorizePage("/LearningResources/Create");

options.Conventions.AuthorizePage("/LearningResources/Edit");

options.Conventions.AuthorizePage("/LearningResources/Delete");

options.Conventions.AllowAnonymousToPage("/Index");

})

.SetCompatibilityVersion(CompatibilityVersion.Version\_2\_2);

The above code ensures that the CRUD pages for Creating, Editing and Deleting any of the LearningResources are only accessible to someone who is currently logged in. Each call to AuthorizePage() includes a specific page name identified by a known route. In this case, the LearningResources folder exists within the Pages folder of the application.

Finally, the call to AllowAnonymousPage() ensures that the app’s [index](https:/github.com/shahedc/NetLearner/blob/master/web/Pages/Index.cshtml) page (at the root of the Pages folder) is accessible to any user without requiring any login.

If you still wish to use the [Authorize] attribute for Razor Pages, you may apply this attribute in your PageModel classes for each Razor Page, as needed. If I were to add it to one of my Razor Pages in the LearningResources folder, it could look like this:

[Authorize]

public class CreateModel : PageModel

{

...

}

### Testing Authorization in NetLearner

When I run my application, I can register and log in as a user to create new Learning Resources. On first launch, I have to apply migrations to create the database from scratch. Please refer to my previous post on [EF Core Migrations](https:/wakeupandcode.com/ef-core-migrations-in-asp-net-core) to learn how you can do the same in your environment.

Here’s a screenshot of the Create page for a user who is logged in:

<!-- image -->

Here’s a screenshot of the page that an “anonymous” user sees when no one is logged in, indicating that the user has been redirected to the Login page:

<!-- image -->

Here’s a screenshot of a list of Learning Resources, visible to anyone whether they’re logged in or not:

<!-- image -->

### Other Authorization Options

Razor Pages have multiple ways of restricting access to pages and folders, including the following methods (as described in the official docs):

- AuthorizePage: Require authorization to access a page
- AuthorizeFolder: Require authorization to access a folder of pages
- AuthorizeAreaPage: Require authorization to access an area page
- AuthorizeAreaFolder: Require authorization to access a folder of areas
- AllowAnonymousToPage: Allow anonymous access to a page
- AllowAnonymousToFolder: Allow anonymous access to a folder of pages

You can get more information on all of the above methods at the following URL:

- Razor Pages authorization conventions in ASP.NET Core: [https://docs.microsoft.com/en-us/aspnet/core/security/authorization/razor-pages-authorization](https:/docs.microsoft.com/en-us/aspnet/core/security/authorization/razor-pages-authorization)
- Detailed Tutorial: [https://docs.microsoft.com/en-us/aspnet/core/security/authorization/secure-data](https:/docs.microsoft.com/en-us/aspnet/core/security/authorization/secure-data)