Running

GDB cheatsheet - page 1

<where>

# gdb <program> [core dump]

function_name

Start GDB (with optional core dump).

Break/watch the named function.

# gdb --args <program> <args…>
Start GDB and pass arguments

# gdb --pid <pid>

line_number

Break/watch the line number in the cur-
rent source ﬁle.

Start GDB and attach to process.

file:line_number

Break/watch the line number in the
named source ﬁle.

break/watch <where> if <condition>

Conditions

Break/watch at the given location if the
condition is met.
Conditions may be almost any C ex-
pression that evaluate to true or false.

set args <args...>

Set arguments to pass to program to
be debugged.

run

kill

Run the program to be debugged.

Kill the running program.

Breakpoints

break <where>

Set a new breakpoint.

delete <breakpoint#>

Remove a breakpoint.

clear

Examining the stack

backtrace
where

Delete all breakpoints.

Show call stack.

enable <breakpoint#>

Enable a disabled breakpoint.

backtrace full
where full

disable <breakpoint#>

Disable a breakpoint.

Watchpoints

watch <where>

Set a new watchpoint.

delete/enable/disable <watchpoint#>

Like breakpoints.

Show call stack, also print the local va-
riables in each frame.

frame <frame#>

Select the stack frame to operate on.

step

Stepping

Go to next instruction (source line), di-
ving into function.

© 2007 Marc Haisenko <marc@darkdust.net>

next

finish

continue

Go to next instruction (source line) but
donʻt dive into functions.

Continue until the current function re-
turns.

Continue normal execution.

Variables and memory

print/format <what>

Print content of variable/memory locati-
on/register.

display/format <what>

Like „print“, but print the information
after each stepping instruction.

enable display <display#>
disable display <display#>

En- or disable the „display“ with the gi-
ven number.

x/nfu <address>

Print memory.
n: How many units to print (default 1).
f: Format character (like „print“).
u: Unit.

Unit is one of:

b: Byte,
h: Half-word (two bytes)
w: Word (four bytes)
g: Giant word (eight bytes)).

condition <breakpoint#> <condition>

Set/change the condition of an existing
break- or watchpoint.

undisplay <display#>

Remove the „display“ with the given
number.

a
c
d
f
o
s
t
u
x

Format

Pointer.
Read as integer, print as character.
Integer, signed decimal.
Floating point number.
Integer, print as octal.
Try to treat as C string.
Integer, print as binary (t = „two“).
Integer, unsigned decimal.
Integer, print as hexadecimal.
<what>

expression

Almost any C expression, including
function calls (must be preﬁxed with a
cast to tell GDB the return value type).

file_name::variable_name

Content of the variable deﬁned in the
named ﬁle (static variables).

function::variable_name

Content of the variable deﬁned in the
named function (if on the stack).

{type}address

Content at address, interpreted as
being of the C type type.

$register

Content of named register. Interesting
registers are $esp (stack pointer), $ebp
(frame pointer) and $eip (instruction
pointer).

Threads

thread <thread#>

Chose thread to operate on.

GDB cheatsheet - page 2

Manipulating the program
set var <variable_name>=<value>

Change the content of a variable to the
given value.

return <expression>

Force the current function to return im-
mediately, passing the given value.

directory <directory>

Sources

Add directory to the list of directories
that is searched for sources.

list
list <filename>:<function>
list <filename>:<line_number>
list <first>,<last>

Shows the current or given source con-
text. The ﬁlename may be omitted. If
last is omitted the context starting at
start is printed instead of centered a-
round it.

set listsize <count>

Set how many lines to show in „list“.

handle <signal> <options>

Signals

Set how to handle signles. Options are:

(no)print: (Donʻt) print a message when
signals occurs.

(no)stop: (Donʻt) stop the program
when signals occurs.

(no)pass: (Donʻt) pass the signal to the
program.

Informations

disassemble
disassemble <where>

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

List all signals and how they are cur-
rently handled.

info threads

List all threads.

show directories

Print all directories in which GDB sear-
ches for source ﬁles.

show listsize

Print how many are shown in the „list“
command.

whatis variable_name

Print type of named variable.

© 2007 Marc Haisenko <marc@darkdust.net>

