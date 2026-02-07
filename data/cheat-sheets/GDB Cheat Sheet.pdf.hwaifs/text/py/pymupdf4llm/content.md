Go to next instruction (source line) but
donʻt dive into functions.


Continue until the current function returns.


Continue normal execution.


# **Running**

# gdb _<program> [core dump]_

Start GDB (with optional core dump).


# gdb --args _<program> <args…>_

Start GDB and pass arguments


# gdb --pid _<pid>_

Start GDB and attach to process.


set args _<args...>_

Set arguments to pass to program to
be debugged.


run

Run the program to be debugged.


kill

Kill the running program.

# **Breakpoints**

break _<where>_

Set a new breakpoint.


delete _<breakpoint#>_

Remove a breakpoint.


clear

Delete all breakpoints.


enable _<breakpoint#>_

Enable a disabled breakpoint.


disable _<breakpoint#>_

Disable a breakpoint.

# **Watchpoints**

watch _<where>_

Set a new watchpoint.


delete/enable/disable _<watchpoint#>_

Like breakpoints.


## **GDB cheatsheet - page 1**

# **_<where>_**

_function_name_

Break/watch the named function.


_line_number_

Break/watch the line number in the current source file.


_file:line_number_

Break/watch the line number in the
named source file.

# **Conditions**

break/watch _<where>_ if _<condition>_

Break/watch at the given location if the
condition is met.
Conditions may be almost any C expression that evaluate to true or false.


condition _<breakpoint#> <condition>_

Set/change the condition of an existing
break- or watchpoint.

# **Examining the stack**

backtrace
where

Show call stack.


backtrace full
where full

Show call stack, also print the local variables in each frame.


frame _<frame#>_

Select the stack frame to operate on.

# **Stepping**

step

Go to next instruction (source line), diving into function.


[© 2007 Marc Haisenko <marc@darkdust.net>](mailto:marc@darkdust.net)



next


finish


continue


# **Variables and memory**

print _/format <what>_

Print content of variable/memory location/register.


display _/format <what>_

Like „print“, but print the information
after each stepping instruction.


undisplay _<display#>_

Remove the „display“ with the given
number.


enable display _<display#>_
disable display _<display#>_

En- or disable the „display“ with the given number.


x _/nfu <address>_

Print memory.
_n_ : How many units to print (default 1).
f _:_ Format character (like „print“).
_u_ : Unit.


Unit is one of:


_b_ : Byte,
_h_ : Half-word (two bytes)
_w_ : Word (four bytes)
_g_ : Giant word (eight bytes)).


# **Format**

_a_ Pointer.
_c_ Read as integer, print as character.
_d_ Integer, signed decimal.
_f_ Floating point number.

_o_ Integer, print as octal.
_s_ Try to treat as C string.
_t_ Integer, print as binary ( _t_ = „two“).
_u_ Integer, unsigned decimal.
_x_ Integer, print as hexadecimal.
# **<what>**

_expression_

Almost any C expression, including
function calls (must be prefixed with a
cast to tell GDB the return value type).


_file_name_ :: _variable_name_

Content of the variable defined in the
named file (static variables).


_function_ :: _variable_name_

Content of the variable defined in the
named function (if on the stack).


_{type}address_

Content at _address_, interpreted as
being of the C type _type_ .


$ _register_

Content of named register. Interesting
registers are $esp (stack pointer), $ebp
(frame pointer) and $eip (instruction
pointer).

# **Threads**

thread _<thread#>_

Chose thread to operate on.


## **GDB cheatsheet - page 2**

# **Manipulating the program**

set var _<variable_name>_ = _<value>_

Change the content of a variable to the
given value.


return _<expression>_

Force the current function to return immediately, passing the given value.

# **Sources**

directory _<directory>_

Add _directory_ to the list of directories
that is searched for sources.


list
list _<filename>_ :<function>
list _<filename>_ : _<line_number>_
list _<first>,<last>_

Shows the current or given source context. The _filename_ may be omitted. If
_last_ is omitted the context starting at
_start_ is printed instead of centered around it.


set listsize _<count>_

Set how many lines to show in „list“.

# **Signals**

handle _<signal> <options>_

Set how to handle signles. Options are:


_(no)print_ : (Donʻt) print a message when
signals occurs.


_(no)stop_ : (Donʻt) stop the program
when signals occurs.


_(no)pass_ : (Donʻt) pass the signal to the
program.


[© 2007 Marc Haisenko <marc@darkdust.net>](mailto:marc@darkdust.net)


# **Informations**

disassemble
disassemble _<where>_

Disassemble the current function or
given location.


info args

Print the arguments to the function of
the current stack frame.


info breakpoints

Print informations about the break- and
watchpoints.


info display

Print informations about the „displays“.


info locals

Print the local variables in the currently
selected stack frame.


info sharedlibrary

List loaded shared libraries.


info signals

List all signals and how they are currently handled.


info threads

List all threads.


show directories

Print all directories in which GDB searches for source files.


show listsize

Print how many are shown in the „list“
command.


whatis _variable_name_

Print type of named variable.


