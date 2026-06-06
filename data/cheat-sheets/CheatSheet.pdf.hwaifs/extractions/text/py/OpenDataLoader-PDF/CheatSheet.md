# Haskell Cheat Sheet

This cheat sheet lays out the fundamental elements of the Haskell language: syntax, keywords and other elements. It is presented as both an executable Haskell ﬁle and a printable document. Load the source into your favorite interpreter to play with code samples shown.

## Basic Syntax Comments

A single line comment starts with ‘ ’ and extends to the end of the line. Multi-line comments start with ’ ’ and extend to ’ ’. Comments can be nested.

Comments above function deﬁnitions should start with ‘ ’ and those next to parameter types with ‘ ’ for compatibility with Haddock1, a system for documenting Haskell code.

### Reserved Words

The following words are reserved in Haskell. It is a syntax error to give a variable or a function one of these names.

• • • • • • •

• • • • • • •

1

• • • • • •

### Strings

- • – Unicode string, sugar for

.

- • – Single character.


Multi-line Strings Normally, it is a syntax error if a string has any actual newline characters. That is, this is a syntax error:

Backslashes (‘ ’) can “escape” a newline:

The area between the backslashes is ignored. Newlines in the string must be represented explicitly:

### Enumerations

- • – List of numbers – . . . .
- • – Inﬁnite list of numbers –

. . . .

- • – Empty list; ranges only go forwards.
- • – Negative integers.
- • – Syntax error; need for negatives.
- • – List from 1 to 100 by 2, -1 to 100 by 4.


In fact, any value which is in the class can be used:

- • – List of characters –

. . . .

- • – .
- • – List of values (from ).


That is, evaluates to:

While evaluates to:

### Numbers

- • – Integer or Floating point
- • – Floating point
- • – syntax error
- • – sugar for
- • – sugar for


### Lists & Tuples

- • – Empty list.
- • – List of three numbers.
- • – Alternate way to write lists using “cons” ( ) and “nil” ( ).
- • – List of three characters (strings are lists).
- • – List of characters (same as ).
- • – 2-element tuple of a number and a string.
- • – 4-element tuple of two functions, a number and a character.


### “Layout” rule, braces and semi-colons.

Haskell can be written using braces and semicolons, just like C. However, no one does. Instead, the “layout” rule is used, where spaces represent scope. The general rule is: always indent. When the compiler complains, indent more.

Let Indent the body of the let at least one space from the ﬁrst deﬁnition in the . If appears on its own line, the body of any deﬁnition must appear in the column after the let:

Nesting & Capture Nested matching and binding are also allowed.

Figure 1: The deﬁnition of

Braces and semi-colons Semi-colons terminate an expression, and braces represent scope. They can be used after several keywords: ,

, and . They cannot be used when deﬁning a function body. For example, the below will not compile.

As can be seen above, the keyword must also be in the same column as . Finally, when multiple deﬁnitions are given, all identiﬁers must appear in the same column.

## Keywords

Using we can determine if any choice was given using a nested match:

However, this will work ﬁne:

Haskell keywords are listed below, in alphabetical order.

Binding can be used to manipulate the value matched:

Function Deﬁnition Indent the body at least one space from the function name:

### Case

is similar to a statement in C# or Java, but can match a pattern: the shape of the value being inspected. Consider a simple data type:

Unless a clause is present. In that case, indent the where clause at least one space from the function name and any function bodies at least one space from the keyword:

can be used to determine which choice was given:

Matching Order Matching proceeds from top to bottom. If is reordered as follows, the ﬁrst pattern will always succeed:

As with pattern-matching in function deﬁnitions, the ‘ ’ token is a “wildcard” matching any value.

Guards Guards, or conditional matches, can be used in cases just like function deﬁnitions. The only difference is the use of the instead of . Here is a simple function which does a case-insensitive string match:

Notice that the declaration only gives the type signature of the function—no implementation is given here (with some exceptions, see “Defaults” on page 3). Continuing, we can deﬁne several instances:

### Data

So-called algebraic data types can be declared as follows:

is the type’s name. and

are values of the type and are called constructors. Multiple constructors are separated with the ‘ ’ character. Note that type and constructor names must start with a capital letter. It is a syntax error otherwise.

Evaluating gives:

### Class

A Haskell function is deﬁned to work on a certain type or set of types and cannot be deﬁned more than once. Most languages support the idea of “overloading”, where a function can have different behavior depending on the type of its arguments. Haskell accomplishes overloading through and declarations. A deﬁnes one or more functions that can be applied to any types which are members (i.e., instances) of that class. A class is analogous to an interface in Java or C#, and instances to a concrete implementation of the interface.

A class must be declared with one or more type variables. Technically, Haskell 98 only allows one type variable, but most implementations of Haskell support so-called multi-parameter type classes, which allow more than one type variable.

We can deﬁne a class which supplies a ﬂavor for a given type:

While gives:

Defaults Default implementations can be given for functions in a class. These are useful when certain functions can be deﬁned in terms of others in the class. A default is deﬁned by giving a body to one of the member functions. The canonical example is , which deﬁnes (not equal) in terms of

. :

Recursive deﬁnitions can be created, but an

declaration must always implement at least one class member.

Constructors with Arguments The type above is not very interesting except as an enumeration. Constructors that take arguments can be declared, allowing more information to be stored:

Notice that the arguments for each constructor are type names, not constructors. That means this kind of declaration is illegal:

instead, the type must be used:

Type and Constructor Names Type and constructor names can be the same, because they will never be used in a place that would cause confusion. For example:

which declares a type named with two constructors, and . Using this type in a function makes the difference clear:

Some literature refers to this practice as type punning.

same accessor function for values of the same type, but that can be dangerous if the accessor is not used by all constructors. Consider this rather contrived example:

Type Variables Declaring so-called polymorphic data types is as easy as adding type variables in the declaration:

Because seven of these operations are so common, Haskell provides the keyword which will automatically implement the typeclass on the associated type. The seven supported typeclasses are: , , , , , , and

.

Two forms of are possible. The ﬁrst is used when a type only derives one class:

This declares a type with two constructors,

and . The constructor can take an argument of any type, which is represented by the type variable above.

We can also mix type variables and speciﬁc types in constructors:

If is called with a value, a runtime error will occur.

Finally, as explained elsewhere, these names can be used for pattern matching, argument capture and “updating.”

The second is used when multiple classes are derived:

Above, the constructor can take a value of any type and an value.

Record Syntax Constructor arguments can be declared either positionally, as above, or using record syntax, which gives a name to each argument. For example, here we declare a type with names for appropriate arguments:

Class Constraints Data types can be declared with class constraints on the type variables, but this practice is generally discouraged. It is generally better to hide the “raw” data constructors using the module system and instead export “smart” constructors which apply appropriate constraints. In any case, the syntax used is:

These names are referred to as selector or accessor functions and are just that, functions. They must start with a lowercase letter or underscore and cannot have the same name as another function in scope. Thus the “ ” preﬁx on each above. Multiple constructors (of the same type) can use the

This declares a type which has one type variable argument. Valid types are those in the class.

Deriving Many types have common operations which are tedious to deﬁne yet necessary, such as the ability to convert to and from strings, compare for equality, or order in a sequence. These capabilities are deﬁned as typeclasses in Haskell.

It is a syntax error to specify for any other classes besides the six given above.

### Deriving

See the section on under the keyword on page 4.

### Do

The keyword indicates that the code to follow will be in a monadic context. Statements are separated by newlines, assignment is indicated by , and a form is introduce which does not require the keyword.

If and IO can be tricky when used with IO. Conceptually it is no different from an in any other context, but intuitively it is hard to develop. Consider the function from

:

The statement has this “signature”:

That is, it takes a value and evaluates to some other value based on the condition. From the type signatures it is clear that cannot be used directly by :

Again, notice where is. We don’t put it in the statement. Instead we use it once at the end of the function.

Multiple ’s When using with or , another is required if either branch has multiple statements. An example with :

An alternative syntax uses semi-colons and braces. A is still required, but indention is unnecessary. This code shows a example, but the principle applies to as well:

That is, results in an value, while wants a value. Instead, the correct value must be “extracted” by running the IO action:

-- no ’do’.

-- multiple statements require

-- a new ’do’.

Notice the use of . Because puts us “inside” the monad, we can’t “get out” except through . Note that we don’t have to use

inline here—we can also use to evaluate the condition and get a value ﬁrst:

And one with :

Export See the section on on page 6.

### If, Then, Else

Remember, always “returns” a value. It is an expression, not just a control ﬂow statement. This function tests if the string given starts with a lower case letter and, if so, converts it to upper case:

-- Use pattern-matching to

-- get ﬁrst character

-- Anything else is empty string

Import See the section on on page 6.

In See on page 6.

Inﬁx, inﬁxl and inﬁxr See the section on operators on page 11.

Instance See the section on on page 3.

silly example which gives the sum of a list of numbers, their average, and their median:

A module can only be deﬁned in one ﬁle, though its exports may come from multiple sources. To make a Haskell ﬁle a module, just add a module declaration at the top:

Deconstruction The left-hand side of a definition can also destructure its argument, in case sub-components are to be accessed. This deﬁnition would extract the ﬁrst three characters from a string

Module names must start with a capital letter but otherwise can include periods, numbers and underscores. Periods are used to give sense of structure, and Haskell compilers will use them as indications of the directory a particular source ﬁle is, but otherwise they have no meaning.

The Haskell community has standardized a set of top-level module names such as , ,

, etc. Be sure to consult them for an appropriate place for your own module if you plan on releasing it to the public.

### Let

Local functions can be deﬁned within a function using . The keyword must always be followed by . The must appear in the same column as the keyword. Functions deﬁned have access to all other functions and variables within the same scope (including those deﬁned by ). In this example, multiplies its argument by , which was passed to the original . is used by map to give the multiples of x up to 10:

Note that this is different than the following, which only works if the string has three characters:

Of See the section on on page 2.

Imports The Haskell standard libraries are divided into a number of modules. The functionality provided by those libraries is accessed by importing into your source ﬁle. To import all everything exported by a library, just use the module name:

Everything means everything: functions, data types and constructors, class declarations, and even other modules imported and then exported by the that module. Importing selectively is accomplished by giving a list of names to import. For example, here we import some functions from :

“functions” with no arguments are actually constants and, once evaluated, will not evaluate again. This is useful for capturing common portions of your function and re-using them. Here is a

### Module

A module is a compilation unit which exports functions, types, classes, instances, and other modules.

Data types can imported in a number of ways. We can just import the type and no constructors:

Of course, this prevents our module from patternmatching on the values of type . We can import one or more constructors explicitly:

All constructors for a given type can also be imported:

We can also import types and classes deﬁned in the module:

#### Instance Declarations It must be noted that

declarations cannot be excluded from import: all declarations in a module will be imported when the module is imported.

Qualiﬁed Imports The names exported by a module (i.e., functions, types, operators, etc.) can have a preﬁx attached through qualiﬁed imports. This is particularly useful for modules which have a large number of functions having the same name as functions. is a good example:

Exports If an export list is not provided, then all functions, types, constructors, etc. will be available to anyone importing the module. Note that any imported modules are not exported in this case. Limiting the names exported is accomplished by adding a parenthesized list of names before the keyword:

In the case of classes, we can import the functions deﬁned for a class using syntax similar to importing constructors for data types:

This form requires any function, type, constructor or other name exported by to now be preﬁxed with the alias (i.e., ) given. Here is one way to remove all duplicates from a list:

The same syntax as used for importing can be used here to specify which functions, types, constructors, and classes are exported, with a few differences. If a module imports another module, it can also export that module:

Note that, unlike data types, all class functions are imported unless explicitly excluded. To only import the class, we use this syntax:

A second form does not create an alias. Instead, the preﬁx becomes the module name. We can write a simple function to check if a string is all upper case:

Exclusions If most, but not all, names are to be imported from a module, it would be tedious to list them all. For that reason, imports can also be speciﬁed via the keyword:

A module can even re-export itself, which can be useful when all local deﬁnitions and a given imported module are to be exported. Below we export ourselves and , but not :

Except for instance declarations, any type, function, constructor or class can be hidden.

Except for the preﬁx speciﬁed, qualiﬁed imports support the same syntax as normal imports. The name imported can be limited in the same ways as described above.

### Newtype

While introduces new values and just creates synonyms, falls somewhere between. The syntax for is quite restrictedonly one constructor can be deﬁned, and that constructor can only take one argument. Continuing the above example, we can deﬁne a type as follows:

As opposed to , the and “values” on are not just values. The typechecker treats them as entirely new types. That means our

function from above would not compile. The following produces a type error:

Instead, we must use pattern-matching to get to the “values” to which we apply :

Finally, it should be noted that any clause which can be attached to a declaration can also be used when declaring a .

Return See on page 4.

### Type

This keyword deﬁnes a type synonym (i.e., alias). This keyword does not deﬁne a new type, like or . It is useful for documenting code but otherwise has no effect on the actual type of a given function or value. For example, a data type could be deﬁned as:

where the ﬁrst constructor argument represents their ﬁrst name and the second their last. However, the order and meaning of the two arguments is not very clear. A declaration can help:

The key observation is that this keyword does not introduce a new value; instead it introduces a new type. This gives us two very useful properties:

- • No runtime cost is associated with the new type, since it does not actually produce new values. In other words, newtypes are absolutely free!
- • The type-checker is able to enforce that common types such as or are used in restricted ways, speciﬁed by the programmer.


Because introduces a synonym, type checking is not affected in any way. The function , deﬁned as:

which has the type

can be used on values with the type or just as easily:

Because is just a synonym, it cannot declare multiple constructors the way can. Type variables can be used, but there cannot be more than the type variables declared with the original type. That means a synonym like the following is possible:

but this not:

Note that fewer type variables can be used, which useful in certain instances.

### Where

Similar to , deﬁnes local functions and constants. The scope of a deﬁnition is the current function. If a function is broken into multiple deﬁnitions through pattern-matching, then the scope of a particular clause only applies to that deﬁnition. For example, the function below has a different meaning depending on the arguments given to the function :

Where vs. Let A clause can only be deﬁned at the level of a function deﬁnition. Usually, that is identical to the scope of deﬁnition. The only difference is when guards are being used. The

scope of the clause extends over all guards. In contrast, the scope of a expression is only the current function clause and guard, if any.

## Declarations, Etc.

and recalling the deﬁnition of from page 2 we can match on nested values when is present:

bind the value to. This facility is used below to bind the head of the list in for display, while also binding the entire list to in order to compute its length:

The following section details rules on function declarations, list comprehensions, and other areas of the language.

### Function Deﬁnition

Functions are deﬁned by declaring their name, any arguments, and an equals sign:

Pattern-matching also allows values to be assigned to variables. For example, this function determines if the string given is empty or not. If not, the value bound to is converted to lower case:

Guards Boolean functions can be used as “guards” in function deﬁnitions along with pattern matching. An example without pattern matching:

All functions names must start with a lowercase letter or “ ”. It is a syntax error otherwise.

Pattern Matching Multiple “clauses” of a function can be deﬁned by “pattern-matching” on the values of arguments. Here, the the function has four separate cases:

-- Matches when the string "y" is given.

-- Matches when the string "n" is given.

-- Matches when string beginning

-- with ’y’ given.

-- Matches for any other value given.

Note that the ‘ ’ character is a wildcard and matches any value.

Pattern matching can extend to nested values. Assuming this data declaration:

Note that above is similer to in that it will match anything; the only difference is that the value matched is also given a name.

n + k Patterns This (sometimes controversial) pattern-matching facility makes it easy to match certain kinds of numeric expressions. The idea is to deﬁne a base case (the “n” portion) with a constant number for matching, and then to deﬁne other matches (the “k” portion) as additives to the base case. Here is a rather inefﬁcient way of testing if a number is even or not:

Notice – it always evaluates to true and can be used to specify a “default” branch.

Guards can be used with patterns. Here is a function that determines if the ﬁrst character in a string is upper or lower case:

Argument Capture Argument capture is useful for pattern-matching a value and using it, without declaring an extra variable. Use an ‘ ’ symbol in between the pattern to match and the variable to

Matching & Guard Order Pattern-matching proceeds in top to bottom order. Similarly, guard expressions are tested from top to bottom. For example, neither of these functions would be very interesting:

Record Syntax Normally pattern matching occurs based on the position of arguments in the value being matched. Types declared with record syntax, however, can match based on those record names. Given this data type:

we can match on only:

Argument capture is possible with this syntax, although it gets clunky. Continuing the above, we now deﬁne a type and a function to replace values with non-zero components with all black:

-- Color value untouched if green is 0

the type of a particular value, even if the value isn’t present.

For example, deﬁne a class for default values:

The idea is you give a value of the right type and it gives you back a default value for that type. Deﬁning instances for basic types is easy:

code when using a constructor. has type but, if not enough other information is available, Haskell must be told what is. Some example default values:

-- Return "Just False"

-- Return "Just ’ ’"

is a littler trickier, because we want to get a default value for the type, but the constructor might be . The following deﬁnition would work, but it’s not optimal since we get when is passed in.

We’d rather get a default value back instead. Here is where a lazy pattern saves us – we can pretend that we’ve matched and use that to get a default value, even if is given:

### List Comprehensions

A list comprehension consists of four types of elements: generators, guards, local bindings, and targets. A list comprehension creates a list of target values based on the generators and guards given. This comprehension generates all squares:

generates a list of all values and puts them in , one by one. creates each element of the list by multiplying by itself.

Guards allow certain elements to be excluded. The following shows how divisors for a given number (excluding itself) can be calculated. Notice how is used in both the guard and target expression.

Lazy Patterns This syntax, also known as irrefutable patterns, allows pattern matches which always succeed. That means any clause using the pattern will succeed, but if it tries to actually use the matched value an error may occur. This is generally useful when an action should be taken on

As long as the value is not actually evaluated, we’re safe. None of the base types need to look at (see the “ ” matches they use), so things will work just ﬁne.

One wrinkle with the above is that we must provide type annotations in the interpreter or the

Local bindings provide new deﬁnitions for use in the generated expression or subsequent generators and guards. Below, is used to represent the minimum of and :

Comprehensions are not limited to numbers. Any list will do. All upper case letters can be generated:

Precedence and associativity make many of the rules of arithmetic work “as expected.” For example, consider these minor updates to the precedence of addition and multiplication:

Or, to ﬁnd all occurrences of a particular break value in a list (indexing from 0):

Of course, full pattern matching, guards, etc. are available in this form. Type signatures are a bit different, though. The operator “name” must appear in parentheses:

The results are surprising:

Allowable symbols which can be used to deﬁne operators are:

A unique feature of list comprehensions is that pattern matching failures do not cause an error; they are just excluded from the resulting list.

### Operators

There are very few predeﬁned “operators” in Haskell—most that appear predeﬁned are actually syntax (e.g., “ ”). Instead, operators are simply functions that take two arguments and have special syntactic support. Any so-called operator can be applied as a preﬁx function using parentheses:

To deﬁne a new operator, simply deﬁne it as a normal function, except the operator appears between the two arguments. Here’s one which takes inserts a comma between two strings and ensures no extra spaces appear:

However, there are several “operators” which cannot be redeﬁned. They are: , and . The last,

, cannot be redeﬁned by itself, but can be used as part of multi-character operator. The “bind” function, , is one example.

Reversing associativity also has interesting effects. Redeﬁning division as right associative:

We get interesting results:

Precedence & Associativity The precedence and associativity, collectively called ﬁxity, of any operator can be set through the , and

keywords. These can be applied both to top-level functions and to local deﬁnitions. The syntax is:

| | precedence op

where precedence varies from 0 to 9. Op can actually be any function which takes two arguments (i.e., any binary operation). Whether the operator is left or right associative is speciﬁed by or

, respectively. Such declarations have no associativity.

### Currying

In Haskell, functions do not have to get all of their arguments at once. For example, consider the

function, which only converts certain elements of string depending on a test:

Using , we can write the function which converts certain letters to numbers:

-- etc.

That is, can take two arguments. The ﬁrst is the conversion function which converts individual characters and the second is the string to be converted.

A curried form of any function which takes multiple arguments can be created. One way to think of this is that each “arrow” in the function’s signature represents a new function which can be created by supplying one more argument.

-- etc.

Notice that has no arguments speciﬁed. Also, the ﬁnal argument to is not given. However, the type signature of tells the whole story:

Sections Operators are functions, and they can be curried like any other. For example, a curried version of “ ” can be written as:

However, this can be unwieldy and hard to read. “Sections” are curried operators, using parentheses. Here is using sections:

changes. “Updating” is really a copy operation, with new values in the ﬁelds that “changed.” For example, using the type deﬁned earlier, we can write a function that sets the ﬁeld to zero easily:

The above is a bit verbose and can be rewriten using record syntax. This kind of “update” only sets values for the ﬁeld(s) speciﬁed and copies the rest:

Here we capture the value in and return a new value. That value happens to have the same value for and as and it’s component is 0. We can combine this with pattern matching to set the and ﬁelds to equal the ﬁeld:

That is, takes a string and produces a string. It is a “constant”, in the sense that always returns a value that is a function which takes a string and produces a string. returns a “curried” form of , where only two of its three arguments have been supplied.

This can be taken further. Say we want to write a function which only changes upper case letters. We know the test to apply, , but we don’t want to specify the conversion. That function can be written as:

The supplied argument can be on the right or left, which indicates what position it should take. This is important for operations such as concatenation:

Which produces quite different results:

which has the type signature:

### “Updating” values and record syntax

Haskell is a pure language and, as such, has no mutable state. That is, once a value is set it never

Notice we must use argument capture (“ ”) to get the value and pattern matching with record syntax (“ ”) to get the inner ﬁeld.

### Anonymous Functions

An anonymous function (i.e., a lambda expression or lambda for short), is a function without a name. They can be deﬁned at any time like so:

which deﬁnes a function which takes an argument and returns a tuple containing that argument in both positions. They are useful for simple functions which don’t need a name. The following determines if a string has mixed case (or is all whitespace):

However, for efﬁciency or other reasons you may only want to allow types. You would accomplish that with a type signature:

Haskell cannot compile that function because it does not know the type of . We must limit the type through an annotation:

Of course, lambdas can be the returned from functions too. This classic returns a function which will then multiply its argument by the one originally given:

For example:

### Type Signatures

Haskell supports full type inference, meaning in most cases no types have to be written down. Type signatures are still useful for at least two reasons.

Type signatures can appear on top-level functions and nested or deﬁnitions. Generally this is useful for documentation, although in some cases they are needed to prevent polymorphism. A type signature is ﬁrst the name of the item which will be typed, followed by a , followed by the types. An example of this has already been seen above.

Type signatures do not need to appear directly above their implementation. They can be speciﬁed anywhere in the containing module (yes, even below!). Multiple items with the same signature can also be deﬁned together:

Annotations have the same syntax as type signatures, but may adorn any expression.

### Unit

– “unit” type and “unit” value. The value and type that represents no useful information.

## Contributors

My thanks to those who contributed patches and useful suggestions: Dave Bayer, Cale Gibbard, Stephen Hicks, Kurt Hutchinson, Johan Kiviniemi, Adrian Neumann, Barak Pearlmutter, Lanny Ripple, Markus Roberts, Holger Siegel, Leif Warner, and Jeff Zaroyko.

Documentation—Even if the compiler can ﬁgure out the types of your functions, other programmers or even yourself might not be able to later. Writing the type signatures on all top-level functions is considered very good form.

Specialization—Typeclasses allow functions with overloading. For example, a function to negate any list of numbers has the signature:

## Version

Type Annotations Sometimes Haskell cannot determine what type is meant. The classic demonstration of this is the so-called “ ” problem:

This is version 1.10. The source can be found at GitHub2. The latest released version of the PDF can be downloaded from Hackage3. Visit CodeSlower.com4 for other projects and writings.

- 2
- 3
- 4


