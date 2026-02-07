## Haskell Cheat Sheet

This cheat sheet lays out the fundamental elements of the Haskell language: syntax, keywords and other elements. It is presented as both an executable Haskell file and a printable document. Load the source into your favorite interpreter to play with code samples shown.

## Basic Syntax

## Comments

A single line comment starts with ' ✲✲ ' and extends to the end of the line. Multi-line comments start with ' ④✲ ' and extend to ' ✲⑥ '. Comments can be nested.

Comments above function definitions should start with ' ④✲ ⑤ ' and those next to parameter types with ' ✲✲ ❫ ' for compatibility with Haddock 1 , a system for documenting Haskell code.

## Reserved Words

The following words are reserved in Haskell. It is a syntax error to give a variable or a function one of these names.

1 ❤/a116/a116♣✿✴✴❤❛/a115❦❡❧❧✳♦/a114❣✴❤❛❞❞♦❝❦✴

<!-- image -->

## Strings

- ✧❛❜❝✧ -Unicode string, sugar for ❬✬❛✬✱✬❜✬✱✬❝✬❪ .
- ✬❛✬ - Single character.

Multi-line Strings Normally, it is a syntax error if a string has any actual newline characters. That is, this is a syntax error:

```
/a115/a116/a114✐♥❣✶ ❂ ✧▼② ❧♦♥❣ /a115/a116/a114✐♥❣✳✧
```

Backslashes (' ❭ ') can 'escape' a newline:

```
/a115/a116/a114✐♥❣✶ ❂ ✧▼② ❧♦♥❣ ✧ ✧/a115/a116/a114✐♥❣✳✧
```

The area between the backslashes is ignored. Newlines in the string must be represented explicitly:

```
/a115/a116/a114✐♥❣✷ ❂ ✧▼② ❧♦♥❣ ❭♥✧ ✧/a115/a116/a114✐♥❣✳✧
```

That is, /a115/a116/a114✐♥❣✶ evaluates to:

▼② ❧♦♥❣ /a115/a116/a114✐♥❣/a0

While /a115/a116/a114✐♥❣✷ evaluates to:

▼② ❧♦♥❣ /a115/a116/a114✐♥❣/a0

## Numbers

- ✶ - Integer or Floating point
- ✶✳✵✱ ✶❡✶✵ - Floating point
- ✶✳ - syntax error
- ✲✶ - sugar for ✭♥❡❣❛/a116❡ ✶✮
- ✷✲✶ - sugar for ✭✭✲✮ ✷ ✶✮

## Enumerations

- ❬✶✳✳✶✵❪ - List of numbers -✶✱ ✷✱ . . . ✱ ✶✵ .
- ❬✶✵✵✳✳❪ - Infinite list of numbers -✶✵✵✱ ✶✵✶✱ ✶✵✷✱ . . . .
- ❬✶✶✵✳✳✶✵✵❪ - Empty list; ranges only go forwards.
- ❬✵✱ ✲✶ ✳✳❪ - Negative integers.
- ❬✲✶✵✵✳✳✲✶✶✵❪ -Syntax error; need ❬✲✶✵✵✳✳ ✲✶✶✵❪ for negatives.
- ❬✶✱✸✳✳✶✵✵❪✱ ❬✲✶✱✸✳✳✶✵✵❪ -List from 1 to 100 by 2, -1 to 100 by 4.

In fact, any value which is in the ❊♥✉♠ class can be used:

- ❬✬❛✬ ✳✳ ✬③✬❪ -List of characters -❛✱ ❜✱ . . . ✱ ③ .
- ❬✶✳✵✱ ✶✳✺ ✳✳ ✷❪ -❬✶✳✵✱✶✳✺✱✷✳✵❪ .
- ❬❯♣♣❡/a114❝❛/a115❡▲❡/a116/a116❡/a114 ✳✳❪ -List of ●❡♥❡/a114❛❧❈❛/a116❡❣♦/a114② values (from ❉❛/a116❛✳❈❤❛/a114 ).

## Lists &amp; Tuples

- ❬❪ - Empty list.
- ❬✶✱✷✱✸❪ - List of three numbers.
- ✶ ✿ ✷ ✿ ✸ ✿ ❬❪ - Alternate way to write lists using 'cons' ( ✿ ) and 'nil' ( ❬❪ ).
- ✧❛❜❝✧ - List of three characters (strings are lists).
- ✬❛✬ ✿ ✬❜✬ ✿ ✬❝✬ ✿ ❬❪ -List of characters (same as ✧❛❜❝✧ ).
- ✭✶✱✧❛✧✮ - 2-element tuple of a number and a string.
- ✭❤❡❛❞✱ /a116❛✐❧✱ ✸✱ ✬❛✬✮ - 4-element tuple of two functions, a number and a character.

## 'Layout' rule, braces and semi-colons.

Haskell can be written using braces and semicolons, just like C. However, no one does. Instead, the 'layout' rule is used, where spaces represent scope. The general rule is: always indent. When the compiler complains, indent more.

Braces and semi-colons Semi-colons terminate an expression, and braces represent scope. They can be used after several keywords: ✇❤❡/a114❡ , ❧❡/a116 , ❞♦ and ♦❢ . They cannot be used when defining a function body. For example, the below will not compile.

```
/a115/a113✉❛/a114❡✷ ① ❂ ④ ① ✯ ①❀ ⑥
```

However, this will work fine:

```
/a115/a113✉❛/a114❡✷ ① ❂ /a114❡/a115✉❧/a116 ✇❤❡/a114❡ ④ /a114❡/a115✉❧/a116 ❂ ① ✯ ①❀ ⑥
```

Function Definition Indent the body at least one space from the function name:

```
/a115/a113✉❛/a114❡ ① ❂ ① ✯ ①
```

Unless a ✇❤❡/a114❡ clause is present. In that case, indent the where clause at least one space from the function name and any function bodies at least one space from the ✇❤❡/a114❡ keyword:

```
/a115/a113✉❛/a114❡ ① ❂ ①✷ ✇❤❡/a114❡ ①✷ ❂ ① ✯ ①
```

Let Indent the body of the let at least one space from the first definition in the ❧❡/a116 . If ❧❡/a116 appears on its own line, the body of any definition must appear in the column after the let:

```
/a115/a113✉❛/a114❡ ① ❂ ❧❡/a116 ①✷ ❂ ① ✯ ① ✐♥ ①✷
```

As can be seen above, the ✐♥ keyword must also be in the same column as ❧❡/a116 . Finally, when multiple definitions are given, all identifiers must appear in the same column.

## Keywords

Haskell keywords are listed below, in alphabetical order.

## Case

❝❛/a115❡ is similar to a /a115✇✐/a116❝❤ statement in C# or Java, but can match a pattern: the shape of the value being inspected. Consider a simple data type:

```
❞❛/a116❛ ❈❤♦✐❝❡/a115 ❂ ❋✐/a114/a115/a116 ❙/a116/a114✐♥❣ ⑤ ❙❡❝♦♥❞ ⑤ ❚❤✐/a114❞ ⑤ ❋♦✉/a114/a116❤
```

❝❛/a115❡ can be used to determine which choice was given:

```
✇❤✐❝❤❈❤♦✐❝❡ ❝❤ ❂ ❝❛/a115❡ ❝❤ ♦❢ ❋✐/a114/a115/a116 ❴ ✙ ✧✶/a115/a116✦✧ ❙❡❝♦♥❞ ✙ ✧✷♥❞✦✧ ❴ ✙ ✧❙♦♠❡/a116❤✐♥❣ ❡❧/a115❡✳✧
```

As with pattern-matching in function definitions, the ' ❴ ' token is a 'wildcard' matching any value.

Nesting &amp; Capture ing are also allowed.

Nested matching and bind-

```
❞❛/a116❛ ▼❛②❜❡ ❛ ❂ ❏✉/a115/a116 ❛ ⑤ ◆♦/a116❤✐♥❣
```

Figure 1: The definition of ▼❛②❜❡

Using ▼❛②❜❡ we can determine if any choice was given using a nested match:

```
❛♥②❈❤♦✐❝❡✶ ❝❤ ❂ ❴✮ ✙ ✧❋✐/a114/a115/a116✦✧ ❏✉/a115/a116 ❙❡❝♦♥❞ ✙ ✧❙❡❝♦♥❞✦✧
```

```
❝❛/a115❡ ❝❤ ♦❢ ◆♦/a116❤✐♥❣ ✙ ✧◆♦ ❝❤♦✐❝❡✦✧ ❏✉/a115/a116 ✭❋✐/a114/a115/a116 ❴ ✙ ✧❙♦♠❡/a116❤✐♥❣ ❡❧/a115❡✳✧
```

Binding can be used to manipulate the value matched:

```
❛♥②❈❤♦✐❝❡✷ ❝❤ ❂ ❝❛/a115❡ ❝❤ ♦❢ ◆♦/a116❤✐♥❣ ✙ ✧◆♦ ❝❤♦✐❝❡✦✧ ❏✉/a115/a116 /a115❝♦/a114❡❅✭❋✐/a114/a115/a116 ✧❣♦❧❞✧✮ ✙ ✧❋✐/a114/a115/a116 ✇✐/a116❤ ❣♦❧❞✦✧ ❏✉/a115/a116 /a115❝♦/a114❡❅✭❋✐/a114/a115/a116 ❴✮ ✙ ✧❋✐/a114/a115/a116 ✇✐/a116❤ /a115♦♠❡/a116❤✐♥❣ ❡❧/a115❡✿ ✧ ✰✰ /a115❤♦✇ /a115❝♦/a114❡ ❴ ✙ ✧◆♦/a116 ✜/a114/a115/a116✳✧
```

Matching Order Matching proceeds from top to bottom. If ❛♥②❈❤♦✐❝❡✶ is reordered as follows, the first pattern will always succeed:

```
❛♥②❈❤♦✐❝❡✸ ❝❤ ❂ ❝❛/a115❡ ❝❤ ♦❢ ❴ ✙ ✧❙♦♠❡/a116❤✐♥❣ ❡❧/a115❡✳✧ ◆♦/a116❤✐♥❣ ✙ ✧◆♦ ❝❤♦✐❝❡✦✧
```

```
❏✉/a115/a116 ✭❋✐/a114/a115/a116 ❴✮ ✙ ✧❋✐/a114/a115/a116✦✧ ❏✉/a115/a116 ❙❡❝♦♥❞ ✙ ✧❙❡❝♦♥❞✦✧
```

Guards Guards, or conditional matches, can be used in cases just like function definitions. The only difference is the use of the ✲❃ instead of ❂ . Here is a simple function which does a case-insensitive string match:

```
/a115/a116/a114❝♠♣ /a115✶ /a115✷ ❂ ❝❛/a115❡ ✭/a115✶✱ /a115✷✮ ♦❢ ✭❬❪✱ ❬❪✮ ✙ ❚/a114✉❡ ✭/a115✶✿/a115/a115✶✱ /a115✷✿/a115/a115✷✮ ⑤ /a116♦❯♣♣❡/a114 /a115✶ ✣ /a116♦❯♣♣❡/a114 /a115✷ ✙ /a115/a116/a114❝♠♣ /a115/a115✶ /a115/a115✷ ⑤ ♦/a116❤❡/a114✇✐/a115❡ ✙ ❋❛❧/a115❡ ❴ ✙ ❋❛❧/a115❡
```

## Class

A Haskell function is defined to work on a certain type or set of types and cannot be defined more than once. Most languages support the idea of 'overloading', where a function can have different behavior depending on the type of its arguments. Haskell accomplishes overloading through ❝❧❛/a115/a115 and ✐♥/a115/a116❛♥❝❡ declarations. A ❝❧❛/a115/a115 defines one or more functions that can be applied to any types which are members (i.e., instances) of that class. A class is analogous to an interface in Java or C#, and instances to a concrete implementation of the interface.

A class must be declared with one or more type variables. Technically, Haskell 98 only allows one type variable, but most implementations of Haskell support so-called multi-parameter type classes , which allow more than one type variable.

We can define a class which supplies a flavor for a given type:

```
❝❧❛/a115/a115 ❋❧❛✈♦/a114 ❛ ✇❤❡/a114❡ ✢❛✈♦/a114 ✿✿ ❛ ✙ ❙/a116/a114✐♥❣
```

Notice that the declaration only gives the type signature of the function-no implementation is given here (with some exceptions, see 'Defaults' on page 3). Continuing, we can define several instances:

✐♥/a115/a116❛♥❝❡ ❋❧❛✈♦/a114 ❇♦♦❧ ✇❤❡/a114❡ ✢❛✈♦/a114 ❴ ❂ ✧/a115✇❡❡/a116✧ ✐♥/a115/a116❛♥❝❡ ❋❧❛✈♦/a114 ❈❤❛/a114 ✇❤❡/a114❡ ✢❛✈♦/a114 ❴ ❂ ✧/a115♦✉/a114✧ Evaluating ❢❧❛✈♦/a114 ❚/a114✉❡ gives: ❃ ✢❛✈♦/a114 ❚/a114✉❡ ✧/a115✇❡❡/a116✧ While ❢❧❛✈♦/a114 ✬①✬ gives: ❃ ✢❛✈♦/a114 ✬①✬ ✧/a115♦✉/a114✧

Defaults Default implementations can be given for functions in a class. These are useful when certain functions can be defined in terms of others in the class. A default is defined by giving a body to one of the member functions. The canonical example is ❊/a113 , which defines ✴❂ (not equal) in terms of ❂❂ . :

```
❝❧❛/a115/a115 ❊/a113 ❛ ✇❤❡/a114❡ ✭✣✮ ✿✿ ❛ ✙ ❛ ✙ ❇♦♦❧ ✭✚✮ ✿✿ ❛ ✙ ❛ ✙ ❇♦♦❧ ✭✚✮ ❛ ❜ ❂ ✆ ✭❛ ✣ ❜✮
```

Recursive definitions can be created, but an ✐♥/a115/a116❛♥❝❡ declaration must always implement at least one class member.

## Data

So-called algebraic data types can be declared as follows:

```
❞❛/a116❛ ▼②❚②♣❡ ❂ ▼②❱❛❧✉❡✶ ⑤ ▼②❱❛❧✉❡✷
```

▼②❚②♣❡ is the type's name . ▼②❱❛❧✉❡✶ and ▼②❱❛❧✉❡ are values of the type and are called constructors . Multiple constructors are separated with the ' ⑤ ' character. Note that type and constructor names must start with a capital letter. It is a syntax error otherwise.

Constructors with Arguments The type above is not very interesting except as an enumeration. Constructors that take arguments can be declared, allowing more information to be stored:

```
❞❛/a116❛ /a80♦✐♥/a116 ❂ ❚✇♦❉ ■♥/a116 ■♥/a116 ⑤ ❚❤/a114❡❡❉ ■♥/a116 ■♥/a116 ■♥/a116
```

Notice that the arguments for each constructor are type names, not constructors. That means this kind of declaration is illegal:

❞❛/a116❛ /a80♦❧② ❂ ❚/a114✐❛♥❣❧❡ ❚✇♦❉ ❚✇♦❉ ❚✇♦❉ instead, the /a80♦✐♥/a116 type must be used: ❞❛/a116❛ /a80♦❧② ❂ ❚/a114✐❛♥❣❧❡ /a80♦✐♥/a116 /a80♦✐♥/a116 /a80♦✐♥/a116

Type and Constructor Names Type and constructor names can be the same, because they will never be used in a place that would cause confusion. For example:

```
❞❛/a116❛ ❯/a115❡/a114 ❂ ❯/a115❡/a114 ❙/a116/a114✐♥❣ ⑤ ❆❞♠✐♥ ❙/a116/a114✐♥❣
```

which declares a type named ❯/a115❡/a114 with two constructors, ❯/a115❡/a114 and ❆❞♠✐♥ . Using this type in a function makes the difference clear:

```
✇❤❛/a116❯/a115❡/a114 ✭❯/a115❡/a114 ❴✮ ❂ ✧♥♦/a114♠❛❧ ✉/a115❡/a114✳✧ ✇❤❛/a116❯/a115❡/a114 ✭❆❞♠✐♥ ❴✮ ❂ ✧❛❞♠✐♥ ✉/a115❡/a114✳✧
```

Some literature refers to this practice as type punning .

Type Variables Declaring so-called polymorphic data types is as easy as adding type variables in the declaration:

```
❞❛/a116❛ ❙❧♦/a116✶ ❛ ❂ ❙❧♦/a116✶ ❛ ⑤ ❊♠♣/a116②✶
```

This declares a type ❙❧♦/a116✶ with two constructors, ❙❧♦/a116✶ and ❊♠♣/a116②✶ . The ❙❧♦/a116✶ constructor can take an argument of any type, which is represented by the type variable ❛ above.

We can also mix type variables and specific types in constructors:

```
❞❛/a116❛ ❙❧♦/a116✷ ❛ ❂ ❙❧♦/a116✷ ❛ ■♥/a116 ⑤ ❊♠♣/a116②✷
```

Above, the ❙❧♦/a116✷ constructor can take a value of any type and an ■♥/a116 value.

Record Syntax Constructor arguments can be declared either positionally, as above, or using record syntax, which gives a name to each argument. For example, here we declare a ❈♦♥/a116❛❝/a116 type with names for appropriate arguments:

```
❞❛/a116❛ ❈♦♥/a116❛❝/a116 ❂ ❈♦♥/a116❛❝/a116 ④ ❝/a116◆❛♠❡ ✿✿ ❙/a116/a114✐♥❣ ✱ ❝/a116❊♠❛✐❧ ✿✿ ❙/a116/a114✐♥❣ ✱ ❝/a116/a80❤♦♥❡ ✿✿ ❙/a116/a114✐♥❣ ⑥
```

These names are referred to as selector or accessor functions and are just that, functions. They must start with a lowercase letter or underscore and cannot have the same name as another function in scope. Thus the ' ❝/a116 ' prefix on each above. Multiple constructors (of the same type) can use the same accessor function for values of the same type, but that can be dangerous if the accessor is not used by all constructors. Consider this rather contrived example:

```
❞❛/a116❛ ❈♦♥ ❂ ❈♦♥ ④ ❝♦♥❱❛❧✉❡ ✿✿ ❙/a116/a114✐♥❣ ⑥
```

```
⑤ ❯♥❝♦♥ ④ ❝♦♥❱❛❧✉❡ ✿✿ ❙/a116/a114✐♥❣ ⑥ ⑤ ◆♦♥❝♦♥ ✇❤✐❝❤❈♦♥ ❝♦♥ ❂ ✧❝♦♥✈❛❧✉❡ ✐/a115 ✧ ✰✰ ❝♦♥❱❛❧✉❡ ❝♦♥
```

If ✇❤✐❝❤❈♦♥ is called with a ◆♦♥❝♦♥ value, a runtime error will occur.

Finally, as explained elsewhere, these names can be used for pattern matching, argument capture and 'updating.'

Class Constraints Data types can be declared with class constraints on the type variables, but this practice is generally discouraged. It is generally better to hide the 'raw' data constructors using the module system and instead export 'smart' constructors which apply appropriate constraints. In any case, the syntax used is:

```
❞❛/a116❛ ✭◆✉♠ ❛✮ ❂❃ ❙♦♠❡◆✉♠❜❡/a114 ❛ ❂ ❚✇♦ ❛ ❛ ⑤ ❚❤/a114❡❡ ❛ ❛ ❛
```

This declares a type ❙♦♠❡◆✉♠❜❡/a114 which has one type variable argument. Valid types are those in the ◆✉♠ class.

Deriving Many types have common operations which are tedious to define yet necessary, such as the ability to convert to and from strings, compare for equality, or order in a sequence. These capabilities are defined as typeclasses in Haskell.

Because seven of these operations are so common, Haskell provides the ❞❡/a114✐✈✐♥❣ keyword which will automatically implement the typeclass on the associated type. The seven supported typeclasses are: ❊/a113 , ❘❡❛❞ , ❙❤♦✇ , ❖/a114❞ , ❊♥✉♠ , ■① , and ❇♦✉♥❞❡❞ .

Two forms of ❞❡/a114✐✈✐♥❣ are possible. The first is used when a type only derives one class:

```
❞❛/a116❛ /a80/a114✐♦/a114✐/a116② ❂ ▲♦✇ ⑤ ▼❡❞✐✉♠ ⑤ ❍✐❣❤ ❞❡/a114✐✈✐♥❣ ❙❤♦✇
```

The second is used when multiple classes are derived:

```
❞❛/a116❛ ❆❧❛/a114♠ ❂ ❙♦❢/a116 ⑤ ▲♦✉❞ ⑤ ❉❡❛❢❡♥✐♥❣ ❞❡/a114✐✈✐♥❣ ✭❘❡❛❞✱ ❙❤♦✇✮
```

It is a syntax error to specify ❞❡/a114✐✈✐♥❣ for any other classes besides the six given above.

## Deriving

See the section on ❞❡/a114✐✈✐♥❣ under the ❞❛/a116❛ keyword on page 4.

Do

The ❞♦ keyword indicates that the code to follow will be in a monadic context. Statements are separated by newlines, assignment is indicated by ❁✲ , and a ❧❡/a116 form is introduce which does not require the ✐♥ keyword.

If and IO ✐❢ can be tricky when used with IO. Conceptually it is no different from an ✐❢ in any other context, but intuitively it is hard to develop. Consider the function ❞♦❡/a115❋✐❧❡❊①✐/a115/a116/a115 from ❙②/a115/a116❡♠✳❉✐/a114❡❝/a116♦/a114② :

```
❞♦❡/a115❋✐❧❡❊①✐/a115/a116 ✿✿ ❋✐❧❡/a80❛/a116❤ ✙ ■❖ ❇♦♦❧
```

The ✐❢ statement has this 'signature':

```
✐❢✲/a116❤❡♥✲❡❧/a115❡ ✿✿ ❇♦♦❧ ✙ ❛ ✙ ❛ ✙ ❛
```

That is, it takes a ❇♦♦❧ value and evaluates to some other value based on the condition. From the type signatures it is clear that ❞♦❡/a115❋✐❧❡❊①✐/a115/a116 cannot be used directly by ✐❢ :

```
✇/a114♦♥❣ ✜❧❡◆❛♠❡ ❂ ✐❢ ❞♦❡/a115❋✐❧❡❊①✐/a115/a116 ✜❧❡◆❛♠❡ /a116❤❡♥ ✳✳✳ ❡❧/a115❡ ✳✳✳
```

That is, ❞♦❡/a115❋✐❧❡❊①✐/a115/a116 results in an ■❖ ❇♦♦❧ value, while ✐❢ wants a ❇♦♦❧ value. Instead, the correct value must be 'extracted' by running the IO action:

```
/a114✐❣❤/a116✶ ✜❧❡◆❛♠❡ ❂ ❞♦ ✕ ✝ ❞♦❡/a115❋✐❧❡❊①✐/a115/a116 ✜❧❡◆❛♠❡ ✐❢ ✕ /a116❤❡♥ /a114❡/a116✉/a114♥ ✶ ❡❧/a115❡ /a114❡/a116✉/a114♥ ✵
```

Notice the use of /a114❡/a116✉/a114♥ . Because ❞♦ puts us 'inside' the ■❖ monad, we can't 'get out' except through /a114❡/a116✉/a114♥ . Note that we don't have to use ✐❢ inline here-we can also use ❧❡/a116 to evaluate the condition and get a value first:

```
/a114✐❣❤/a116✷ ✜❧❡◆❛♠❡ ❂ ❞♦ ✕ ✝ ❞♦❡/a115❋✐❧❡❊①✐/a115/a116 ✜❧❡◆❛♠❡
```

```
❧❡/a116 /a114❡/a115✉❧/a116 ❂ ✐❢ ✕ /a116❤❡♥ ✶ ❡❧/a115❡ ✵ /a114❡/a116✉/a114♥ /a114❡/a115✉❧/a116
```

Again, notice where /a114❡/a116✉/a114♥ is. We don't put it in the ❧❡/a116 statement. Instead we use it once at the end of the function.

Multiple ❞♦ 's When using ❞♦ with ✐❢ or ❝❛/a115❡ , another ❞♦ is required if either branch has multiple statements. An example with ✐❢ :

```
❝♦✉♥/a116❇②/a116❡/a115✶ ❢ ❂ ❞♦ ♣✉/a116❙/a116/a114▲♥ ✧❊♥/a116❡/a114 ❛ ✜❧❡♥❛♠❡✳✧ ❛/a114❣/a115 ✝ ❣❡/a116▲✐♥❡ ✐❢ ❧❡♥❣/a116❤ ❛/a114❣/a115 ✣ ✵ -- no 'do'. /a116❤❡♥ ♣✉/a116❙/a116/a114▲♥ ✧◆♦ ✜❧❡♥❛♠❡ ❣✐✈❡♥✳✧ ❡❧/a115❡ -- multiple statements require -- a new 'do'. ❞♦ ❢ ✝ /a114❡❛❞❋✐❧❡ ❛/a114❣/a115 ♣✉/a116❙/a116/a114▲♥ ✭✧❚❤❡ ✜❧❡ ✐/a115 ✧ ✰✰ /a115❤♦✇ ✭❧❡♥❣/a116❤ ❢✮ ✰✰ ✧ ❜②/a116❡/a115 ❧♦♥❣✳✧✮
```

And one with ❝❛/a115❡ :

```
❝♦✉♥/a116❇②/a116❡/a115✷ ❂ ❞♦ ♣✉/a116❙/a116/a114▲♥ ✧❊♥/a116❡/a114 ❛ ✜❧❡♥❛♠❡✳✧ ❛/a114❣/a115 ✝ ❣❡/a116▲✐♥❡ ❝❛/a115❡ ❛/a114❣/a115 ♦❢ ❬❪ ✙ ♣✉/a116❙/a116/a114▲♥ ✧◆♦ ❛/a114❣/a115 ❣✐✈❡♥✳✧
```

```
✜❧❡ ✙ ❞♦ ❢ ✝ /a114❡❛❞❋✐❧❡ ✜❧❡ ♣✉/a116❙/a116/a114▲♥ ✭✧❚❤❡ ✜❧❡ ✐/a115 ✧ ✰✰ /a115❤♦✇ ✭❧❡♥❣/a116❤ ❢✮ ✰✰ ✧ ❜②/a116❡/a115 ❧♦♥❣✳✧✮
```

An alternative syntax uses semi-colons and braces. A ❞♦ is still required, but indention is unnecessary. This code shows a ❝❛/a115❡ example, but the principle applies to ✐❢ as well:

```
❝♦✉♥/a116❇②/a116❡/a115✸ ❂ ❞♦ ♣✉/a116❙/a116/a114▲♥ ✧❊♥/a116❡/a114 ❛ ✜❧❡♥❛♠❡✳✧ ❛/a114❣/a115 ✝ ❣❡/a116▲✐♥❡ ❝❛/a115❡ ❛/a114❣/a115 ♦❢ ❬❪ ✙ ♣✉/a116❙/a116/a114▲♥ ✧◆♦ ❛/a114❣/a115 ❣✐✈❡♥✳✧ ✜❧❡ ✙ ❞♦ ④ ❢ ✝ /a114❡❛❞❋✐❧❡ ✜❧❡❀ ♣✉/a116❙/a116/a114▲♥ ✭✧❚❤❡ ✜❧❡ ✐/a115 ✧ ✰✰ /a115❤♦✇ ✭❧❡♥❣/a116❤ ❢✮ ✰✰ ✧ ❜②/a116❡/a115 ❧♦♥❣✳✧✮❀ ⑥
```

## Export

See the section on ♠♦❞✉❧❡ on page 6.

## If, Then, Else

Remember, ✐❢ always 'returns' a value. It is an expression, not just a control flow statement. This function tests if the string given starts with a lower case letter and, if so, converts it to upper case:

```
-- Use pattern-matching to -- get first character /a115❡♥/a116❡♥❝❡❈❛/a115❡ ✭/a115✿/a114❡/a115/a116✮ ❂ ✐❢ ✐/a115▲♦✇❡/a114 /a115 /a116❤❡♥ /a116♦❯♣♣❡/a114 /a115 ✿ /a114❡/a115/a116
```

```
❡❧/a115❡ /a115 ✿ /a114❡/a115/a116
```

- -- Anything else is empty string /a115❡♥/a116❡♥❝❡❈❛/a115❡ ❴ ❂ ❬❪

## Import

See the section on ♠♦❞✉❧❡ on page 6.

## In

```
See ❧❡/a116 on page 6.
```

## Infix, infixl and infixr

See the section on operators on page 11.

## Instance

See the section on ❝❧❛/a115/a115 on page 3.

## Let

Local functions can be defined within a function using ❧❡/a116 . The ❧❡/a116 keyword must always be followed by ✐♥ . The ✐♥ must appear in the same column as the ❧❡/a116 keyword. Functions defined have access to all other functions and variables within the same scope (including those defined by ❧❡/a116 ). In this example, ♠✉❧/a116 multiplies its argument ♥ by ① , which was passed to the original ♠✉❧/a116✐♣❧❡/a115 . ♠✉❧/a116 is used by map to give the multiples of x up to 10:

```
♠✉❧/a116✐♣❧❡/a115 ① ❂ ❧❡/a116 ♠✉❧/a116 ♥ ❂ ♥ ✯ ① ✐♥ ♠❛♣ ♠✉❧/a116 ❬✶✳✳✶✵❪
```

❧❡/a116 'functions' with no arguments are actually constants and, once evaluated, will not evaluate again. This is useful for capturing common portions of your function and re-using them. Here is a silly example which gives the sum of a list of numbers, their average, and their median:

```
❧✐/a115/a116❙/a116❛/a116/a115 ♠ ❂ ❧❡/a116 ♥✉♠❜❡/a114/a115 ❂ ❬✶✱✸ ✳✳ ♠❪ /a116♦/a116❛❧ ❂ /a115✉♠ ♥✉♠❜❡/a114/a115 ♠✐❞ ❂ ❤❡❛❞ ✭/a116❛❦❡ ✭♠ ❵❞✐✈❵ ✷✮ ♥✉♠❜❡/a114/a115✮ ✐♥ ✧/a116♦/a116❛❧✿ ✧ ✰✰ /a115❤♦✇ /a116♦/a116❛❧ ✰✰ ✧✱ ♠✐❞✿ ✧ ✰✰ /a115❤♦✇ ♠✐❞
```

Deconstruction The left-hand side of a ❧❡/a116 definition can also destructure its argument, in case sub-components are to be accessed. This definition would extract the first three characters from a string

```
✜/a114/a115/a116❚❤/a114❡❡ /a115/a116/a114 ❂ ❧❡/a116 ✭❛✿❜✿❝✿❴✮ ❂ /a115/a116/a114 ✐♥ ✧■♥✐/a116✐❛❧ /a116❤/a114❡❡ ❝❤❛/a114❛❝/a116❡/a114/a115 ❛/a114❡✿ ✧ ✰✰ /a115❤♦✇ ❛ ✰✰ ✧✱ ✧ ✰✰ /a115❤♦✇ ❜ ✰✰ ✧✱ ❛♥❞ ✧ ✰✰ /a115❤♦✇ ❝
```

Note that this is different than the following, which only works if the string has three characters:

```
♦♥❧②❚❤/a114❡❡ /a115/a116/a114 ❂ ❧❡/a116 ✭❛✿❜✿❝✿❬❪✮ ❂ /a115/a116/a114 ✐♥ ✧❚❤❡ ❝❤❛/a114❛❝/a116❡/a114/a115 ❣✐✈❡♥ ❛/a114❡✿ ✧ ✰✰ /a115❤♦✇ ❛ ✰✰ ✧✱ ✧ ✰✰ /a115❤♦✇ ❜ ✰✰ ✧✱ ❛♥❞ ✧ ✰✰ /a115❤♦✇ ❝
```

## Of

See the section on ❝❛/a115❡ on page 2.

## Module

Amodule is a compilation unit which exports functions, types, classes, instances, and other modules.

A module can only be defined in one file, though its exports may come from multiple sources. To make a Haskell file a module, just add a module declaration at the top:

```
♠♦❞✉❧❡ ▼②▼♦❞✉❧❡ ✇❤❡/a114❡
```

Module names must start with a capital letter but otherwise can include periods, numbers and underscores. Periods are used to give sense of structure, and Haskell compilers will use them as indications of the directory a particular source file is, but otherwise they have no meaning.

The Haskell community has standardized a set of top-level module names such as ❉❛/a116❛ , ❙②/a115/a116❡♠ , ◆❡/a116✇♦/a114❦ , etc. Be sure to consult them for an appropriate place for your own module if you plan on releasing it to the public.

Imports The Haskell standard libraries are divided into a number of modules. The functionality provided by those libraries is accessed by importing into your source file. To import all everything exported by a library, just use the module name:

✐♠♣♦/a114/a116 ❚❡①/a116✳❘❡❛❞

Everything means everything : functions, data types and constructors, class declarations, and even other modules imported and then exported by the that module. Importing selectively is accomplished by giving a list of names to import. For example, here we import some functions from ❚❡①/a116✳❘❡❛❞ :

```
✐♠♣♦/a114/a116 ❚❡①/a116✳❘❡❛❞ ✭/a114❡❛❞/a80❛/a114❡♥✱ ❧❡①✮
```

Data types can imported in a number of ways. We can just import the type and no constructors:

✐♠♣♦/a114/a116 ❚❡①/a116✳❘❡❛❞ ✭▲❡①❡♠❡✮

Of course, this prevents our module from patternmatching on the values of type ▲❡①❡♠❡ . We can import one or more constructors explicitly:

```
✐♠♣♦/a114/a116 ❚❡①/a116✳❘❡❛❞ ✭▲❡①❡♠❡✭■❞❡♥/a116✱ ❙②♠❜♦❧✮✮
```

All constructors for a given type can also be imported:

```
✐♠♣♦/a114/a116 ❚❡①/a116✳❘❡❛❞ ✭▲❡①❡♠❡✭✳✳✮✮
```

We can also import types and classes defined in the module:

```
✐♠♣♦/a114/a116 ❚❡①/a116✳❘❡❛❞ ✭❘❡❛❞✱ ❘❡❛❞❙✮
```

In the case of classes, we can import the functions defined for a class using syntax similar to importing constructors for data types:

```
✐♠♣♦/a114/a116 ❚❡①/a116✳❘❡❛❞ ✭❘❡❛❞✭/a114❡❛❞/a115/a80/a114❡❝ ✱ /a114❡❛❞▲✐/a115/a116✮✮
```

Note that, unlike data types, all class functions are imported unless explicitly excluded. To only import the class, we use this syntax:

```
✐♠♣♦/a114/a116 ❚❡①/a116✳❘❡❛❞ ✭❘❡❛❞✭✮✮
```

Exclusions If most, but not all, names are to be imported from a module, it would be tedious to list them all. For that reason, imports can also be specified via the ❤✐❞✐♥❣ keyword:

```
✐♠♣♦/a114/a116 ❉❛/a116❛✳❈❤❛/a114 ❤✐❞✐♥❣ ✭✐/a115❈♦♥/a116/a114♦❧ ✱ ✐/a115▼❛/a114❦✮
```

Except for instance declarations, any type, function, constructor or class can be hidden.

Instance Declarations It must be noted that ✐♥/a115/a116❛♥❝❡ declarations cannot be excluded from import: all ✐♥/a115/a116❛♥❝❡ declarations in a module will be imported when the module is imported.

Qualified Imports The names exported by a module (i.e., functions, types, operators, etc.) can have a prefix attached through qualified imports. This is particularly useful for modules which have a large number of functions having the same name as /a80/a114❡❧✉❞❡ functions. ❉❛/a116❛✳❙❡/a116 is a good example:

```
✐♠♣♦/a114/a116 /a113✉❛❧✐✜❡❞ ❉❛/a116❛✳❙❡/a116 ❛/a115 ❙❡/a116
```

This form requires any function, type, constructor or other name exported by ❉❛/a116❛✳❙❡/a116 to now be prefixed with the alias (i.e., ❙❡/a116 ) given. Here is one way to remove all duplicates from a list:

```
/a114❡♠♦✈❡❉✉♣/a115 ❛ ❂ ❙❡/a116✳/a116♦▲✐/a115/a116 ✭❙❡/a116✳❢/a114♦♠▲✐/a115/a116 ❛✮
```

A second form does not create an alias. Instead, the prefix becomes the module name. We can write a simple function to check if a string is all upper case:

```
✐♠♣♦/a114/a116 /a113✉❛❧✐✜❡❞ ❈❤❛/a114 ❛❧❧❯♣♣❡/a114 /a115/a116/a114 ❂ ❛❧❧ ❈❤❛/a114✳✐/a115❯♣♣❡/a114 /a115/a116/a114
```

Except for the prefix specified, qualified imports support the same syntax as normal imports. The name imported can be limited in the same ways as described above.

Exports If an export list is not provided, then all functions, types, constructors, etc. will be available to anyone importing the module. Note that any imported modules are not exported in this case. Limiting the names exported is accomplished by adding a parenthesized list of names before the ✇❤❡/a114❡ keyword:

```
♠♦❞✉❧❡ ▼②▼♦❞✉❧❡ ✭▼②❚②♣❡ ✱ ▼②❈❧❛/a115/a115 ✱ ♠②❋✉♥❝✶ ✳✳✳✮ ✇❤❡/a114❡
```

The same syntax as used for importing can be used here to specify which functions, types, constructors, and classes are exported, with a few differences. If a module imports another module, it can also export that module:

```
♠♦❞✉❧❡ ▼②❇✐❣▼♦❞✉❧❡ ✭♠♦❞✉❧❡ ❉❛/a116❛✳❙❡/a116 ✱ ♠♦❞✉❧❡ ❉❛/a116❛✳❈❤❛/a114✮ ✇❤❡/a114❡ ✐♠♣♦/a114/a116 ❉❛/a116❛✳❙❡/a116 ✐♠♣♦/a114/a116 ❉❛/a116❛✳❈❤❛/a114
```

A module can even re-export itself, which can be useful when all local definitions and a given imported module are to be exported. Below we export ourselves and ❉❛/a116❛✳❙❡/a116 , but not ❉❛/a116❛✳❈❤❛/a114 :

```
♠♦❞✉❧❡ ❆♥♦/a116❤❡/a114❇✐❣▼♦❞✉❧❡ ✭♠♦❞✉❧❡ ❉❛/a116❛✳❙❡/a116 ✱ ♠♦❞✉❧❡ ❆♥♦/a116❤❡/a114❇✐❣▼♦❞✉❧❡✮ ✇❤❡/a114❡ ✐♠♣♦/a114/a116 ❉❛/a116❛✳❙❡/a116 ✐♠♣♦/a114/a116 ❉❛/a116❛✳❈❤❛/a114
```

## Newtype

While ❞❛/a116❛ introduces new values and /a116②♣❡ just creates synonyms, ♥❡✇/a116②♣❡ falls somewhere between. The syntax for ♥❡✇/a116②♣❡ is quite restrictedonly one constructor can be defined, and that constructor can only take one argument. Continuing the above example, we can define a /a80❤♦♥❡ type as follows:

```
♥❡✇/a116②♣❡ ❍♦♠❡ ❂ ❍ ❙/a116/a114✐♥❣ ♥❡✇/a116②♣❡ ❲♦/a114❦ ❂ ❲ ❙/a116/a114✐♥❣ ❞❛/a116❛ /a80❤♦♥❡ ❂ /a80❤♦♥❡ ❍♦♠❡ ❲♦/a114❦
```

As opposed to /a116②♣❡ , the ❍ and ❲ 'values' on /a80❤♦♥❡ are not just ❙/a116/a114✐♥❣ values. The typechecker treats them as entirely new types. That means our ❧♦✇❡/a114◆❛♠❡ function from above would not compile. The following produces a type error:

```
❧/a80❤♦♥❡ ✭/a80❤♦♥❡ ❤♠ ✇❦✮ ❂ /a80❤♦♥❡ ✭❧♦✇❡/a114 ❤♠✮ ✭❧♦✇❡/a114 ✇❦✮
```

Instead, we must use pattern-matching to get to the 'values' to which we apply ❧♦✇❡/a114 :

```
❧/a80❤♦♥❡ ✭/a80❤♦♥❡ ✭❍ ❤♠✮ ✭❲ ✇❦✮✮ ❂ /a80❤♦♥❡ ✭❍ ✭❧♦✇❡/a114 ❤♠✮✮ ✭❲ ✭❧♦✇❡/a114 ✇❦✮✮
```

The key observation is that this keyword does not introduce a new value; instead it introduces a new type. This gives us two very useful properties:

- No runtime cost is associated with the new type, since it does not actually produce new values. In other words, newtypes are absolutely free!
- The type-checker is able to enforce that common types such as ■♥/a116 or ❙/a116/a114✐♥❣ are used in restricted ways, specified by the programmer.

Finally, it should be noted that any ❞❡/a114✐✈✐♥❣ clause which can be attached to a ❞❛/a116❛ declaration can also be used when declaring a ♥❡✇/a116②♣❡ .

## Return

See ❞♦ on page 4.

## Type

This keyword defines a type synonym (i.e., alias). This keyword does not define a new type, like ❞❛/a116❛ or ♥❡✇/a116②♣❡ . It is useful for documenting code but otherwise has no effect on the actual type of a given function or value. For example, a /a80❡/a114/a115♦♥ data type could be defined as:

```
❞❛/a116❛ /a80❡/a114/a115♦♥ ❂ /a80❡/a114/a115♦♥ ❙/a116/a114✐♥❣ ❙/a116/a114✐♥❣
```

where the first constructor argument represents their first name and the second their last. However, the order and meaning of the two arguments is not very clear. A /a116②♣❡ declaration can help:

```
/a116 ②♣❡ ❋✐/a114/a115/a116◆❛♠❡ ❂ ❙/a116/a114✐♥❣ /a116 ②♣❡ ▲❛/a115/a116◆❛♠❡ ❂ ❙/a116/a114✐♥❣ ❞❛/a116❛ /a80❡/a114/a115♦♥ ❂ /a80❡/a114/a115♦♥ ❋✐/a114/a115/a116◆❛♠❡ ▲❛/a115/a116◆❛♠❡
```

Because /a116②♣❡ introduces a synonym, type checking is not affected in any way. The function ❧♦✇❡/a114 , defined as:

❧♦✇❡/a114 /a115 ❂ ♠❛♣ /a116♦▲♦✇❡/a114 /a115

which has the type

```
❧♦✇❡/a114 ✿✿ ❙/a116/a114✐♥❣ ✙ ❙/a116/a114✐♥❣
```

can be used on values with the type ❋✐/a114/a115/a116◆❛♠❡ or ▲❛/a115/a116◆❛♠❡ just as easily:

```
❧◆❛♠❡ ✭/a80❡/a114/a115♦♥ ❢ ❧ ✮ ❂ /a80❡/a114/a115♦♥ ✭❧♦✇❡/a114 ❢✮ ✭❧♦✇❡/a114 ❧✮
```

Because /a116②♣❡ is just a synonym, it cannot declare multiple constructors the way ❞❛/a116❛ can. Type variables can be used, but there cannot be more than the type variables declared with the original type. That means a synonym like the following is possible:

```
/a116 ②♣❡ ◆♦/a116❙✉/a114❡ ❛ ❂ ▼❛②❜❡ ❛ but this not:
```

/a116 ②♣❡ ◆♦/a116❙✉/a114❡ ❛ ❜ ❂ ▼❛②❜❡ ❛

Note that fewer type variables can be used, which useful in certain instances.

## Where

Similar to ❧❡/a116 , ✇❤❡/a114❡ defines local functions and constants. The scope of a ✇❤❡/a114❡ definition is the current function. If a function is broken into multiple definitions through pattern-matching, then the scope of a particular ✇❤❡/a114❡ clause only applies to that definition. For example, the function /a114❡/a115✉❧/a116 below has a different meaning depending on the arguments given to the function /a115/a116/a114❧❡♥ :

```
/a115/a116/a114❧❡♥ ❬❪ ❂ /a114❡/a115✉❧/a116 ✇❤❡/a114❡ /a114❡/a115✉❧/a116 ❂ ✧◆♦ /a115/a116/a114✐♥❣ ❣✐✈❡♥✦✧ /a115/a116/a114❧❡♥ ❢ ❂ /a114❡/a115✉❧/a116 ✰✰ ✧ ❝❤❛/a114❛❝/a116❡/a114/a115 ❧♦♥❣✦✧ ✇❤❡/a114❡ /a114❡/a115✉❧/a116 ❂ /a115❤♦✇ ✭❧❡♥❣/a116❤ ❢✮
```

Where vs. Let A ✇❤❡/a114❡ clause can only be defined at the level of a function definition. Usually, that is identical to the scope of ❧❡/a116 definition. The only difference is when guards are being used. The

scope of the ✇❤❡/a114❡ clause extends over all guards. In contrast, the scope of a ❧❡/a116 expression is only the current function clause and guard, if any.

## Declarations, Etc.

The following section details rules on function declarations, list comprehensions, and other areas of the language.

## Function Definition

Functions are defined by declaring their name, any arguments, and an equals sign:

```
/a115/a113✉❛/a114❡ ① ❂ ① ✯ ①
```

All functions names must start with a lowercase letter or ' ❴ '. It is a syntax error otherwise.

Pattern Matching Multiple 'clauses' of a function can be defined by 'pattern-matching' on the values of arguments. Here, the the ❛❣/a114❡❡ function has four separate cases:

- -- Matches when the string "y" is given. ❛❣/a114❡❡✶ ✧②✧ ❂ ✧●/a114❡❛/a116✦✧ -- Matches when the string "n" is given. ❛❣/a114❡❡✶ ✧♥✧ ❂ ✧❚♦♦ ❜❛❞✳✧ -- Matches when string beginning -- with 'y' given. ❛❣/a114❡❡✶ ✭✬②✬✿❴✮ ❂ ✧❨❆❍❖❖✦✧ -- Matches for any other value given.
- ❛❣/a114❡❡✶ ❴ ❂ ✧❙❖ ❙❆❉✳✧

Note that the ' ❴ ' character is a wildcard and matches any value.

Pattern matching can extend to nested values. Assuming this data declaration:

```
❞❛/a116❛ ❇❛/a114 ❂ ❇✐❧ ✭▼❛②❜❡ ■♥/a116✮ ⑤ ❇❛③
```

and recalling the definition of ▼❛②❜❡ from page 2 we can match on nested ▼❛②❜❡ values when ❇✐❧ is present:

```
❢ ✭❇✐❧ ✭❏✉/a115/a116 ❴✮✮ ❂ ✳✳✳ ❢ ✭❇✐❧ ◆♦/a116❤✐♥❣✮ ❂ ✳✳✳ ❢ ❇❛③ ❂ ✳✳✳
```

Pattern-matching also allows values to be assigned to variables. For example, this function determines if the string given is empty or not. If not, the value bound to /a115/a116/a114 is converted to lower case:

```
/a116♦▲♦✇❡/a114❙/a116/a114 ❬❪ ❂ ❬❪ /a116♦▲♦✇❡/a114❙/a116/a114 /a115/a116/a114 ❂ ♠❛♣ /a116♦▲♦✇❡/a114 /a115/a116/a114
```

Note that /a115/a116/a114 above is similer to ❴ in that it will match anything; the only difference is that the value matched is also given a name.

n + k Patterns This (sometimes controversial) pattern-matching facility makes it easy to match certain kinds of numeric expressions. The idea is to define a base case (the ' n ' portion) with a constant number for matching, and then to define other matches (the ' k ' portion) as additives to the base case. Here is a rather inefficient way of testing if a number is even or not:

```
✐/a115❊✈❡♥ ✵ ❂ ❚/a114✉❡ ✐/a115❊✈❡♥ ✶ ❂ ❋❛❧/a115❡ ✐/a115❊✈❡♥ ✭♥ ✰ ✷✮ ❂ ✐/a115❊✈❡♥ ♥
```

Argument Capture Argument capture is useful for pattern-matching a value and using it, without declaring an extra variable. Use an ' ❅ ' symbol in between the pattern to match and the variable to bind the value to. This facility is used below to bind the head of the list in ❧ for display, while also binding the entire list to ❧/a115 in order to compute its length:

```
❧❡♥ ❧/a115❅✭❧✿❴✮ ❂ ✧▲✐/a115/a116 /a115/a116❛/a114/a116/a115 ✇✐/a116❤ ✧ ✰✰ /a115❤♦✇ ❧ ✰✰ ✧ ❛♥❞ ✐/a115 ✧ ✰✰ /a115❤♦✇ ✭❧❡♥❣/a116❤ ❧/a115✮ ✰✰ ✧ ✐/a116❡♠/a115 ❧♦♥❣✳✧ ❧❡♥ ❬❪ ❂ ✧▲✐/a115/a116 ✐/a115 ❡♠♣/a116②✦✧
```

Guards Boolean functions can be used as 'guards' in function definitions along with pattern matching. An example without pattern matching:

```
✇❤✐❝❤ ♥ ⑤ ♥ ✣ ✵ ❂ ✧③❡/a114♦✦✧ ⑤ ❡✈❡♥ ♥ ❂ ✧❡✈❡♥✦✧ ⑤ ♦/a116❤❡/a114✇✐/a115❡ ❂ ✧♦❞❞✦✧
```

Notice ♦/a116❤❡/a114✇✐/a115❡ - it always evaluates to true and can be used to specify a 'default' branch.

Guards can be used with patterns. Here is a function that determines if the first character in a string is upper or lower case:

```
✇❤❛/a116 ❬❪ ❂ ✧❡♠♣/a116② /a115/a116/a114✐♥❣✦✧ ✇❤❛/a116 ✭❝✿❴✮ ⑤ ✐/a115❯♣♣❡/a114 ❝ ❂ ✧✉♣♣❡/a114 ❝❛/a115❡✦✧ ⑤ ✐/a115▲♦✇❡/a114 ❝ ❂ ✧❧♦✇❡/a114 ❝❛/a115❡✧ ⑤ ♦/a116❤❡/a114✇✐/a115❡ ❂ ✧♥♦/a116 ❛ ❧❡/a116/a116❡/a114✦✧
```

Matching &amp; Guard Order Pattern-matching proceeds in top to bottom order. Similarly, guard expressions are tested from top to bottom. For example, neither of these functions would be very interesting:

```
❛❧❧❊♠♣/a116② ❴ ❂ ❋❛❧/a115❡ ❛❧❧❊♠♣/a116② ❬❪ ❂ ❚/a114✉❡
```

```
❛❧✇❛②/a115❊✈❡♥ ♥ ⑤ ♦/a116❤❡/a114✇✐/a115❡ ❂ ❋❛❧/a115❡ ⑤ ♥ ❵❞✐✈❵ ✷ ✣ ✵ ❂ ❚/a114✉❡
```

Record Syntax Normally pattern matching occurs based on the position of arguments in the value being matched. Types declared with record syntax, however, can match based on those record names. Given this data type:

```
❞❛/a116❛ ❈♦❧♦/a114 ❂ ❈ ④ /a114❡❞ ✱ ❣/a114❡❡♥ ✱ ❜❧✉❡ ✿✿ ■♥/a116 ⑥
```

we can match on ❣/a114❡❡♥ only:

```
✐/a115●/a114❡❡♥❩❡/a114♦ ✭❈ ④ ❣/a114❡❡♥ ❂ ✵ ⑥✮ ❂ ❚/a114✉❡ ✐/a115●/a114❡❡♥❩❡/a114♦ ❴ ❂ ❋❛❧/a115❡
```

Argument capture is possible with this syntax, although it gets clunky. Continuing the above, we now define a /a80✐①❡❧ type and a function to replace values with non-zero ❣/a114❡❡♥ components with all black:

```
❞❛/a116❛ /a80✐①❡❧ ❂ /a80 ❈♦❧♦/a114
```

```
-- Color value untouched if green is 0
```

```
/a115❡/a116●/a114❡❡♥ ✭/a80 ❝♦❧❅✭❈ ④ ❣/a114❡❡♥ ❂ ✵ ⑥✮✮ ❂ /a80 ❝♦❧ /a115❡/a116●/a114❡❡♥ ❴ ❂ /a80 ✭❈ ✵ ✵ ✵✮
```

Lazy Patterns This syntax, also known as irrefutable patterns, allows pattern matches which always succeed. That means any clause using the pattern will succeed, but if it tries to actually use the matched value an error may occur. This is generally useful when an action should be taken on the type of a particular value, even if the value isn't present.

For example, define a class for default values:

```
❝❧❛/a115/a115 ❉❡❢ ❛ ✇❤❡/a114❡ ❞❡❢❱❛❧✉❡ ✿✿ ❛ ✙ ❛
```

The idea is you give ❞❡❢❱❛❧✉❡ a value of the right type and it gives you back a default value for that type. Defining instances for basic types is easy:

```
✐♥/a115/a116❛♥❝❡ ❉❡❢ ❇♦♦❧ ✇❤❡/a114❡ ❞❡❢❱❛❧✉❡ ❴ ❂ ❋❛❧/a115❡
```

```
✐♥/a115/a116❛♥❝❡ ❉❡❢ ❈❤❛/a114 ✇❤❡/a114❡ ❞❡❢❱❛❧✉❡ ❴ ❂ ✬ ✬
```

▼❛②❜❡ is a littler trickier, because we want to get a default value for the type, but the constructor might be ◆♦/a116❤✐♥❣ . The following definition would work, but it's not optimal since we get ◆♦/a116❤✐♥❣ when ◆♦/a116❤✐♥❣ is passed in.

```
✐♥/a115/a116❛♥❝❡ ❉❡❢ ❛ ❂❃ ❉❡❢ ✭▼❛②❜❡ ❛✮ ✇❤❡/a114❡ ❞❡❢❱❛❧✉❡ ✭❏✉/a115/a116 ①✮ ❂ ❏✉/a115/a116 ✭❞❡❢❱❛❧✉❡ ①✮ ❞❡❢❱❛❧✉❡ ◆♦/a116❤✐♥❣ ❂ ◆♦/a116❤✐♥❣
```

We'd rather get a ❏✉/a115/a116 ✭ default value ✮ back instead. Here is where a lazy pattern saves us - we can pretend that we've matched ❏✉/a115/a116 ① and use that to get a default value, even if ◆♦/a116❤✐♥❣ is given:

```
✐♥/a115/a116❛♥❝❡ ❉❡❢ ❛ ❂❃ ❉❡❢ ✭▼❛②❜❡ ❛✮ ✇❤❡/a114❡ ❞❡❢❱❛❧✉❡ ⑦✭❏✉/a115/a116 ①✮ ❂ ❏✉/a115/a116 ✭❞❡❢❱❛❧✉❡ ①✮
```

As long as the value ① is not actually evaluated, we're safe. None of the base types need to look at ① (see the ' ❴ ' matches they use), so things will work just fine.

One wrinkle with the above is that we must provide type annotations in the interpreter or the code when using a ◆♦/a116❤✐♥❣ constructor. ◆♦/a116❤✐♥❣ has type ▼❛②❜❡ ❛ but, if not enough other information is available, Haskell must be told what ❛ is. Some example default values:

```
-- Return "Just False" ❞❡❢▼❇ ❂ ❞❡❢❱❛❧✉❡ ✭◆♦/a116❤✐♥❣ ✿✿ ▼❛②❜❡ ❇♦♦❧✮ -- Return "Just ' '" ❞❡❢▼❈ ❂ ❞❡❢❱❛❧✉❡ ✭◆♦/a116❤✐♥❣ ✿✿ ▼❛②❜❡ ❈❤❛/a114✮
```

## List Comprehensions

A list comprehension consists of four types of elements: generators , guards , local bindings , and targets . A list comprehension creates a list of target values based on the generators and guards given. This comprehension generates all squares:

<!-- formula-not-decoded -->

① ❁✲ ❬✶✳✳❪ generates a list of all ■♥/a116❡❣❡/a114 values and puts them in ① , one by one. ① ✯ ① creates each element of the list by multiplying ① by itself.

Guards allow certain elements to be excluded. The following shows how divisors for a given number (excluding itself) can be calculated. Notice how ❞ is used in both the guard and target expression.

```
❞✐✈✐/a115♦/a114/a115 ♥ ❂ ❬❞ ⑤ ❞ ✝ ❬✶✳✳✭♥ ❵❞✐✈❵ ✷✮❪ ✱ ♥ ❵♠♦❞❵ ❞ ✣ ✵❪
```

Local bindings provide new definitions for use in the generated expression or subsequent generators and guards. Below, ③ is used to represent the minimum of ❛ and ❜ :

```
/a115/a116/a114❛♥❣❡ ❂ ❬✭❛✱③✮ ⑤ ❛ ✝❬✶✳✳✸❪ ✱ ❜ ✝❬✶✳✳✸❪ ✱ ❝ ✝ ❬✶✳✳✸❪
```

<!-- formula-not-decoded -->

Comprehensions are not limited to numbers. Any list will do. All upper case letters can be generated:

```
✉♣/a115 ❂ ❬❝ ⑤ ❝ ✝ ❬♠✐♥❇♦✉♥❞ ✳✳ ♠❛①❇♦✉♥❞❪ ✱ ✐/a115❯♣♣❡/a114 ❝❪
```

Or, to find all occurrences of a particular break value ❜/a114 in a list ✇♦/a114❞ (indexing from 0):

```
✐❞①/a115 ✇♦/a114❞ ❜/a114 ❂ ❬✐ ⑤ ✭✐✱ ❝✮ ✝ ③✐♣ ❬✵✳✳❪ ✇♦/a114❞ ✱ ❝ ✣ ❜/a114❪
```

Aunique feature of list comprehensions is that pattern matching failures do not cause an error; they are just excluded from the resulting list.

## Operators

There are very few predefined 'operators' in Haskell-most that appear predefined are actually syntax (e.g., ' ❂ '). Instead, operators are simply functions that take two arguments and have special syntactic support. Any so-called operator can be applied as a prefix function using parentheses:

```
✸ ✰ ✹ ✣ ✭✰✮ ✸ ✹
```

To define a new operator, simply define it as a normal function, except the operator appears between the two arguments. Here's one which takes inserts a comma between two strings and ensures no extra spaces appear:

```
✜/a114/a115/a116 ★★ ❧❛/a115/a116 ❂ ❧❡/a116 /a116/a114✐♠ /a115 ❂ ❞/a114♦♣❲❤✐❧❡ ✐/a115❙♣❛❝❡
```

```
✭/a114❡✈❡/a114/a115❡ ✭❞/a114♦♣❲❤✐❧❡ ✐/a115❙♣❛❝❡ ✭/a114❡✈❡/a114/a115❡ /a115✮✮✮ ✐♥ /a116/a114✐♠ ❧❛/a115/a116 ✰✰ ✧✱ ✧ ✰✰ /a116/a114✐♠ ✜/a114/a115/a116 ❃ ✧ ❍❛/a115❦❡❧❧ ✧ ★★ ✧ ❈✉/a114/a114② ✧ ❈✉/a114/a114②✱ ❍❛/a115❦❡❧❧
```

Of course, full pattern matching, guards, etc. are available in this form. Type signatures are a bit different, though. The operator 'name' must appear in parentheses:

```
✭★★✮ ✿✿ ❙/a116/a114✐♥❣ ✙ ❙/a116/a114✐♥❣ ✙ ❙/a116/a114✐♥❣
```

Allowable symbols which can be used to define operators are:

```
★ ✩ ✪ ✫ ✯ ✰ /a0 ✴ ❁ ❂ ❃ ❄ ❅ ✟ ❫ ⑤ ✲ ⑦
```

However, there are several 'operators' which cannot be redefined. They are: ❁✲ , ✲❃ and ❂ . The last, ❂ , cannot be redefined by itself, but can be used as part of multi-character operator. The 'bind' function, ❃❃❂ , is one example.

Precedence &amp; Associativity The precedence and associativity, collectively called fixity , of any operator can be set through the ✐♥❢✐① , ✐♥❢✐①/a114 and ✐♥❢✐①❧ keywords. These can be applied both to top-level functions and to local definitions. The syntax is:

```
✐♥❢✐① | ✐♥❢✐①/a114 | ✐♥❢✐①❧ precedence op
```

where precedence varies from 0 to 9. Op can actually be any function which takes two arguments (i.e., any binary operation). Whether the operator is left or right associative is specified by ✐♥❢✐①❧ or ✐♥❢✐①/a114 , respectively. Such ✐♥❢✐① declarations have no associativity.

Precedence and associativity make many of the rules of arithmetic work 'as expected.' For example, consider these minor updates to the precedence of addition and multiplication:

```
✐♥✜①❧ ✽ ❵♣❧✉/a115✶❵ ♣❧✉/a115✶ ❛ ❜ ❂ ❛ ✰ ❜ ✐♥✜①❧ ✼ ❵♠✉❧/a116✶❵ ♠✉❧/a116✶ ❛ ❜ ❂ ❛ ✯ ❜
```

The results are surprising:

```
❃ ✷ ✰ ✸ ✯ ✺ ✶✼ ❃ ✷ ❵♣❧✉/a115✶❵ ✸ ❵♠✉❧/a116✶❵ ✺ ✷✺
```

Reversing associativity also has interesting effects. Redefining division as right associative:

```
✐♥✜①/a114 ✼ ❵❞✐✈✶❵ ❞✐✈✶ ❛ ❜ ❂ ❛ ✴ ❜
```

We get interesting results:

```
❃ ✷✵ ✴ ✷ ✴ ✷ ✺✳✵ ❃ ✷✵ ❵❞✐✈✶❵ ✷ ❵❞✐✈✶❵ ✷ ✷✵✳✵
```

## Currying

In Haskell, functions do not have to get all of their arguments at once. For example, consider the ❝♦♥✈❡/a114/a116❖♥❧② function, which only converts certain elements of string depending on a test:

```
❝♦♥✈❡/a114/a116❖♥❧② /a116❡/a115/a116 ❝❤❛♥❣❡ /a115/a116/a114 ❂ ♠❛♣ ✭✟❝ ✙ ✐❢ /a116❡/a115/a116 ❝ /a116❤❡♥ ❝❤❛♥❣❡ ❝ ❡❧/a115❡ ❝✮ /a115/a116/a114
```

Using ❝♦♥✈❡/a114/a116❖♥❧② , we can write the ❧✸✸/a116 function which converts certain letters to numbers:

```
❧✸✸/a116 ❂ ❝♦♥✈❡/a114/a116❖♥❧② ✐/a115▲✸✸/a116 /a116♦▲✸✸/a116 ✇❤❡/a114❡ ✐/a115▲✸✸/a116 ✬♦✬ ❂ ❚/a114✉❡ ✐/a115▲✸✸/a116 ✬❛✬ ❂ ❚/a114✉❡ -- etc. ✐/a115▲✸✸/a116 ❴ ❂ ❋❛❧/a115❡ /a116♦▲✸✸/a116 ✬♦✬ ❂ ✬✵✬ /a116♦▲✸✸/a116 ✬❛✬ ❂ ✬✹✬ -- etc. /a116♦▲✸✸/a116 ❝ ❂ ❝
```

Notice that ❧✸✸/a116 has no arguments specified. Also, the final argument to ❝♦♥✈❡/a114/a116❖♥❧② is not given. However, the type signature of ❧✸✸/a116 tells the whole story:

```
❧✸✸/a116 ✿✿ ❙/a116/a114✐♥❣ ✙ ❙/a116/a114✐♥❣
```

That is, ❧✸✸/a116 takes a string and produces a string. It is a 'constant', in the sense that ❧✸✸/a116 always returns a value that is a function which takes a string and produces a string. ❧✸✸/a116 returns a 'curried' form of ❝♦♥✈❡/a114/a116❖♥❧② , where only two of its three arguments have been supplied.

This can be taken further. Say we want to write a function which only changes upper case letters. We know the test to apply, ✐/a115❯♣♣❡/a114 , but we don't want to specify the conversion. That function can be written as:

```
❝♦♥✈❡/a114/a116❯♣♣❡/a114 ❂ ❝♦♥✈❡/a114/a116❖♥❧② ✐/a115❯♣♣❡/a114
```

which has the type signature:

```
❝♦♥✈❡/a114/a116❯♣♣❡/a114 ✿✿ ✭❈❤❛/a114 ✙ ❈❤❛/a114✮ ✙ ❙/a116/a114✐♥❣ ✙ ❙/a116/a114✐♥❣
```

That is, ❝♦♥✈❡/a114/a116❯♣♣❡/a114 can take two arguments. The first is the conversion function which converts individual characters and the second is the string to be converted.

A curried form of any function which takes multiple arguments can be created. One way to think of this is that each 'arrow' in the function's signature represents a new function which can be created by supplying one more argument.

Sections Operators are functions, and they can be curried like any other. For example, a curried version of ' ✰ ' can be written as:

<!-- formula-not-decoded -->

However, this can be unwieldy and hard to read. 'Sections' are curried operators, using parentheses. Here is ❛❞❞✶✵ using sections:

```
❛❞❞✶✵ ❂ ✭✶✵ ✰✮
```

The supplied argument can be on the right or left, which indicates what position it should take. This is important for operations such as concatenation:

<!-- formula-not-decoded -->

Which produces quite different results:

```
❃ ♦♥▲❡❢/a116 ✧❢♦♦✧ ✧❜❛/a114✧ ✧❜❛/a114❢♦♦✧ ❃ ♦♥❘✐❣❤/a116 ✧❢♦♦✧ ✧❜❛/a114✧ ✧❢♦♦❜❛/a114✧
```

## 'Updating' values and record syntax

Haskell is a pure language and, as such, has no mutable state. That is, once a value is set it never changes. 'Updating' is really a copy operation, with new values in the fields that 'changed.' For example, using the ❈♦❧♦/a114 type defined earlier, we can write a function that sets the ❣/a114❡❡♥ field to zero easily:

<!-- formula-not-decoded -->

The above is a bit verbose and can be rewriten using record syntax. This kind of 'update' only sets values for the field(s) specified and copies the rest:

<!-- formula-not-decoded -->

Here we capture the ❈♦❧♦/a114 value in ❝ and return a new ❈♦❧♦/a114 value. That value happens to have the same value for /a114❡❞ and ❜❧✉❡ as ❝ and it's ❣/a114❡❡♥ component is 0. We can combine this with pattern matching to set the ❣/a114❡❡♥ and ❜❧✉❡ fields to equal the /a114❡❞ field:

<!-- formula-not-decoded -->

Notice we must use argument capture (' ❝❅ ') to get the ❈♦❧♦/a114 value and pattern matching with record syntax (' ❈ ④ /a114❡❞ ❂ /a114⑥ ') to get the inner /a114❡❞ field.

## Anonymous Functions

An anonymous function (i.e., a lambda expression or lambda for short), is a function without a name. They can be defined at any time like so:

<!-- formula-not-decoded -->

which defines a function which takes an argument and returns a tuple containing that argument in both positions. They are useful for simple functions which don't need a name. The following determines if a string has mixed case (or is all whitespace):

```
♠✐①❡❞❈❛/a115❡ /a115/a116/a114 ❂ ❛❧❧ ✭✟❝ ✙ ✐/a115❙♣❛❝❡ ❝ ✤ ✐/a115▲♦✇❡/a114 ❝ ✤ ✐/a115❯♣♣❡/a114 ❝✮ /a115/a116/a114
```

Of course, lambdas can be the returned from functions too. This classic returns a function which will then multiply its argument by the one originally given:

```
♠✉❧/a116❇② ♥ ❂ ✟♠ ✙ ♥ ✯ ♠
```

For example:

```
❃ ❧❡/a116 ♠✉❧/a116✶✵ ❂ ♠✉❧/a116❇② ✶✵ ❃ ♠✉❧/a116✶✵ ✶✵ ✶✵✵
```

## Type Signatures

Haskell supports full type inference, meaning in most cases no types have to be written down. Type signatures are still useful for at least two reasons.

Documentation -Even if the compiler can figure out the types of your functions, other programmers or even yourself might not be able to later. Writing the type signatures on all top-level functions is considered very good form.

Specialization -Typeclasses allow functions with overloading. For example, a function to negate any list of numbers has the signature:

```
♥❡❣❛/a116❡❆❧❧ ✿✿ ◆✉♠ ❛ ❂❃ ❬❛❪ ✙ ❬❛❪
```

2 ❤/a116/a116♣✿✴✴❣✐/a116❤✉❜✳❝♦♠✴♠✹❞❝✹♣✴❝❤❡❛/a116/a115❤❡❡/a116

3 ❤/a116/a116♣✿✴✴❤❛❝❦❛❣❡✳❤❛/a115❦❡❧❧✳♦/a114❣✴❝❣✐✲❜✐♥✴❤❛❝❦❛❣❡✲/a115❝/a114✐♣/a116/a115✴♣❛❝❦❛❣❡✴❈❤❡❛/a116❙❤❡❡/a116

4 ❤/a116/a116♣✿✴✴❜❧♦❣✳❝♦❞❡/a115❧♦✇❡/a114✳❝♦♠✴

However, for efficiency or other reasons you may only want to allow ■♥/a116 types. You would accomplish that with a type signature:

```
♥❡❣❛/a116❡❆❧❧ ✿✿ ❬■♥/a116❪ ✙ ❬■♥/a116❪
```

Type signatures can appear on top-level functions and nested ❧❡/a116 or ✇❤❡/a114❡ definitions. Generally this is useful for documentation, although in some cases they are needed to prevent polymorphism. A type signature is first the name of the item which will be typed, followed by a ✿✿ , followed by the types. An example of this has already been seen above.

Type signatures do not need to appear directly above their implementation. They can be specified anywhere in the containing module (yes, even below!). Multiple items with the same signature can also be defined together:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Type Annotations Sometimes Haskell cannot determine what type is meant. The classic demonstration of this is the so-called ' /a115❤♦✇ ✳ /a114❡❛❞ ' problem:

❝❛♥/a80❛/a114/a115❡■♥/a116 ① ❂ /a115❤♦✇ ✭/a114❡❛❞ ①✮

Haskell cannot compile that function because it does not know the type of ① . We must limit the type through an annotation:

```
❝❛♥/a80❛/a114/a115❡■♥/a116 ① ❂ /a115❤♦✇ ✭✭/a114❡❛❞ ①✮ ✿✿ ■♥/a116✮
```

Annotations have the same syntax as type signatures, but may adorn any expression.

## Unit

✭✮ - 'unit' type and 'unit' value. The value and type that represents no useful information.

## Contributors

My thanks to those who contributed patches and useful suggestions: Dave Bayer, Cale Gibbard, Stephen Hicks, Kurt Hutchinson, Johan Kiviniemi, Adrian Neumann, Barak Pearlmutter, Lanny Ripple, Markus Roberts, Holger Siegel, Leif Warner, and Jeff Zaroyko.

## Version

This is version 1.10. The source can be found at GitHub 2 . The latest released version of the PDF can be downloaded from Hackage 3 . Visit CodeSlower.com 4 for other projects and writings.