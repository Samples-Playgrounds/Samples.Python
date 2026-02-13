CSCI0330

Intro Computer Systems

Doeppner

gdb Cheatsheet
Fall 2018

1 Introduction

2 Program Execution

3 TUI (Text User Interface) Mode

4 Viewing Variables, Registers and Memory

5 More Information

5.1 Official Documentation
5.2 Tutorials

6 Tips

1

1

4

4

5
6
6

6

1 Introduction
This document contains several
and C-programming career.

gdb

 commands which you will find useful throughout your x86-

The commands contained within this document are by no means exhaustive;
features which are not documented here. Consult the man pages
(man gdb)
you require further information.

 contains many

gdb
 or the internet if

Throughout this document, commands shall be listed in the form

[c]ommand

 <required arg> (optional arg)

    This is what the command does.
    This is an example use of this command.

where the character(s) in [brackets] are the abbreviated version of the command.

2 Program Execution
[b]reak
Sets a breakpoint on either a function, a line given by a line number, or the instruction located at
a particular address.

 <function name or filename:line# or *memory address>

If you do not have access to the source code of a function and wish to set a breakpoint on a
 is the name of
particular instruction, call
the procedure); this command will allow you to see the memory address of each instruction. See
section 4 for further information.

disassemble function_name

function_name

 (where

1

​
​

​
​
​
​

​
​

​

​
​
​
​
CSCI0330

gdb Cheatsheet

Fall 2017

(gdb) break main
Breakpoint 1 at 0x80488f6: file main.c, line 67.

[d]elete
Removes the indicated breakpoint. To see breakpoint numbers, run

 <breakpoint #>

info break

, or

i b

.

(gdb) delete 4

 <breakpoint #>

[condition]
Updates the breakpoint indicated by the given number so that execution of the program stops at
that point only if
variables and functions that are available in the scope of the breakpoint location

 is expressed in C syntax, and can only use

condition

condition

<condition>

 is true.

(gdb) break main
Breakpoint 1 at 0x80488f6: file main.c, line 48
(gdb) condition 1 argc <= 2 || !strcmp(argv[1], "jasmine")

 (about)

[i]nfo
Lists information about the argument (
provided.
about

1
​:
 can be one of the following

about

), or lists what possible arguments are if none are

● [f]rame

 – list information about the current stack frame, including the address of the

current frame, the address of the previous frame, locations of saved registers, function
arguments, and local variables.

● [s]tack

– list the stack backtrace, showing what function calls have been made, and

their arguments. You can also use the commands
–lists the contents of each register.

backtrace
[all-r]egisters

 or

where

 to do the same.

 lists even more

● [r]egisters
registers.
● [b]reak

breakpoint is in.

● [fu]nctions
 flag

gcc

-g

– lists the number and address of each breakpoint, and what function the

- lists all of the function signatures, if the program was compiled with the

. This is useful for setting breakpoints in functions.

 <filename of executable>

[file]
Loads the specified file into

 gdb.

 (arg1 arg2 ... argn)

[r]un
Runs the loaded executable program with program arguments

arg1 ... argn

.

[c]ontinue
Resumes execution of a stopped program, stopping again at the next breakpoint.

2

​
​
​
​
​

​
​
​
​
​
​

​
​
​
​
​
​
​
​
​
​
​
​
​
​
​
​
​
​
​

​
​

​
​
​

CSCI0330

gdb Cheatsheet

Fall 2017

[s]tep
Steps through a single line of code. Steps into function calls.

(gdb) break main
Breakpoint 1 at 0x8049377: file main.c, line 34.
(gdb) r

Breakpoint 1, main (argc=2, argv=0xbffff704) at main.c:34
35    int val = foo(argv[1]);
(gdb) s
foo (word=0xbffff8b3) at main.c:11
12    char bar = word[0];

[s]tep[i]
Steps through a single x86 instruction. Steps into calls.

(gdb) 0x080484d5 in main()
1: x/i $pc
=> 0x80484d5 <main + 113>:
(gdb) si
0x080484ec in do_something()
1: x/i $pc
=> 0x80484ec <main + 113>:

call

0x80484ec<do_something>

push

%ebp

[n]ext
Steps through a single line of code. Steps over function calls.

(gdb) break main
Breakpoint 1 at 0x8049377: file main.c, line 34.
(gdb) r
Breakpoint 1, main (argc=2, argv=0xbffff704) at main.c:34
35    int val = foo(argv[1]);
(gdb) n
36    bar(val);

[n]ext[i]
Steps through a single x86 instruction. Steps over calls
(gdb)
0x080484d5 in main ()
​ ​
1: x/i $pc
=> 0x80484d5 <main + 113>:     call
(gdb) ni
0x080484da in main ()
1: x/i $pc
=> 0x80484da <main + 113>:     mov

.

0x80484ec<do_something>

$0x0,%eax

[k]ill
Kills the current debugging session.

[b]ack[t]race

3

​

CSCI0330

gdb Cheatsheet

Fall 2017

Prints a stack trace, listing each function and its arguments. This does the same thing as the
commands

info stack

where

 and

.

    (gdb) bt
    #0 fibonacci (n=1) at main.c:45
    #1 fibonacci (n=2) at main.c:45
    #3 main (argc=2, argv=0xbffff6e4) at main.c:34

[where]
Prints a stack trace, listing each function and its arguments. This is the same as the commands
info stack

backtrace

 and

.

[q]uit
Quits

 gdb.

3 TUI (Text User Interface) Mode

layout
TUI
out of
enable
the
TUI

 is a terminal interface which allows the user to view the source file while debugging. The
gdb
TUI

 as
 commands and key bindings, such as

. You can also switch in and

gdb tui

tui

 mode is enabled by default when you invoke
 runs by using various
TUI
 or
. To disable
 becomes unreadable, pressing

 mode while
gdb
Ctrl-x Ctrl-a

TUI
Ctrl-l

 mode, you can type
 will reload it.

tui disable

. If the layout of

Once you are running TUI mode, there are several commands you can use to change the
display. One of them is layout name. The name parameter controls which additional windows
are displayed, and can be any of the following:

 will display the next layout.
 will display the previous layout.

 will display the source and command windows.
 will display the assembly and command windows.

 will display the source, assembly, and command windows.

● next
● prev
● src
● asm
● split
● regs

 will display the register, source, and command windows when in src layout. When

in asm or split layout, will display the register, assembler, and command windows.

When you have multiple windows open, you can then use the command
focus between windows. The
any of the following:

 parameter controls which window is focused, and can be
name
​

 to switch
name
​

focus

● next
● prev
● src
● asm
● regs

 will make the next window active for scrolling.
 will make the previous window active for scrolling.

 will make the source window active for scrolling.
 will make the assembly window active for scrolling.
 will make the register window active for scrolling.

4

​
​
​
​

​
​
​

​
​
​
​
​
​
​
​
​
​
​
​
​
​
​
​
​
​
​
​
​
​
​
​
​

​
​
​
​
​
​

​
​

​
​
​
​
​
​
​
CSCI0330

gdb Cheatsheet

Fall 2017

● cmd

 will make the command window active for scrolling.

When the command window is active for scrolling, for example, using the arrow keys allows you
to scroll through

 commands instead of moving the text window.

gdb

4 Viewing Variables, Registers and Memory

[p]rint
 <expression>
Prints the value which the indicated
names (from the current scope), memory addresses, registers, and constants as its operands to
various operators. It is written in C syntax, which means that in addition to arithmetic operations,
you can also use casting operations and dereferencing operations.

 evaluates to. expression can contain variable

expression

To access the value contained in a register, replace the
instead of

%eax

.

%

 character prefix with

$

, e.g.

$eax

(gdb) print *(char *)($esp + $eax + my_ptr_array[13])
‘e’

 <expression>

[p]rint/x
Prints the value which the indicated expression evaluates to as a hexadecimal number.
expression

 is evaluated the same way as it is in

print

.

(gdb) p/x my_var
$1 = 0x1b

[x]/(number)(format)(unit_size)
Examines the data located in memory at address.

 <address>

● number

 optionally indicates that several contiguous elements, beginning at
address
should be examined. This is very useful for examining the contents of an array. By
default, this argument is 1.

,

● format

 indicates how data should be printed. In most cases, this is the same character
. One exception is the format i, which prints an

that you would use in a call to
instruction rather than a decimal integer.

printf()

● unit_size
(2 bytes),
examining instructions.

[w]ords

, or

 indicates the size of the data to examine. It can be

[b]ytes

,

[h]alfwords

[g]iant

words. By default, this is bytes, which is perfect for

A variation of this command is the
arguments, but repeats execution every time

display

 command. This command takes the same
 waits for input. For example,

gdb

display/I $pc

would display the next instruction after each step.

(gdb) x/4x argv

5

​
​
​
​
​
​

​
​
​
​
​
​
​

​
​
​
​

​

​
​
​
​
​
​
​
​
​
​
​
​
​
​

​

​
​
​
​
CSCI0330

gdb Cheatsheet

Fall 2017

0xbffff86b    0xbffff8b3    0xbffff8b6    0x00000000

0xbffff6e4:
(gdb) x/2c argv[1]
0xbffff86b:
(gdb) x/3i foo
0x80485e6 <foo>:
0x80485e7 <foo+1>:
0x80485e9 <foo+3>:

104 ‘h’       105 ‘i’

push %ebp
mov  %esp, %ebp
push %ebx

[disassemble] <function name>
Disassembles a function into assembly instructions, displaying the address, name, and
operands of each instruction.

5 More Information

Below are some additional resources for all of your
links).

gdb

 needs (the bullet points are clickable

5.1 Official Documentation

● Viewing the stack
● Running programs
● Stopping execution
● Viewing program source
● Viewing program data

5.2 Tutorials

● Using GNU’s GDB Debugger
● Beej’s Quick Guide to GDB

6 Tips

● If you edit your program while it is being run in

gdb

, open another terminal, recompile

your program, and restart it in
gdb
of the program while maintaining all of your previous breakpoints.

run (args)

 by typing

gdb

.

 will load the new version

● To view the next assembly instruction that will be executed, use the command

● Type

display/I %pc
CTRL-Z
execution with the

[c]ontinue

 command.

 to suspend execution of your program within

gdb

. You can then resume

6

​
​

​
​
​
​
​
​
​
​
​
​
​
​
​
​
