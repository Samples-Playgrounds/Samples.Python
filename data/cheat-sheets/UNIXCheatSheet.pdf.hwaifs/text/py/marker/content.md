## UNIX Command Cheat Sheet

Carnegie Observatories Summer Research Program Every command and filename is CaSe sEnSiTiVe!

| Command                         | Description                                     | Examples and Options                           |  |
|---------------------------------|-------------------------------------------------|------------------------------------------------|--|
| <tab></tab>                     | Attempt to autocomplete                         | Use this to speed up typing/avoid typos        |  |
| Navigating Directories          |                                                 |                                                |  |
| ls                              | List the contents of the directory.             | ls<br>-larth<br>/home/mcuser/science/code      |  |
| cd                              | Change directory.                               | cd<br>/home/mcuser/science                     |  |
| pwd                             | present<br>working<br>directory.                | pwd                                            |  |
| *                               | Wild card, any number of chars.                 | ls<br>*.txt                                    |  |
| ?                               | Wild card, 0 or 1 characters.                   | ls<br>foo?.txt                                 |  |
|                                 | Current directory.                              | cd                                             |  |
|                                 | Directory one level up.                         | cd<br>                                         |  |
| ~                               | Home directory.                                 | cd<br>~                                        |  |
| -                               | Previous directory.                             | cd<br>-                                        |  |
| Modifying Directories and Files |                                                 |                                                |  |
| mkdir                           | Make new empty directory.                       | mkdir<br>MyNewDirectory                        |  |
| rmdir                           | Remove empty directory.                         | rmdir<br>MyNewDirectory                        |  |
| mv                              | Move files (overwrites destination).            | mv<br>-i<br>foo.txt<br>foo2.txt                |  |
| cp                              | Copy files (overwrites destination).            | cp<br>-i<br>/foo.txt                           |  |
| rm                              | Remove files.<br>CANNOT UNDO!                   | rm<br>-i<br>foo.txt                            |  |
|                                 | Change file permissions.                        | chmod<br>a+rwx<br>badger.txt                   |  |
| chmod                           | = read, write, execute.<br>rwx                  | chmod<br>o-wx<br>badger.txt                    |  |
|                                 | = user, group, other, all.<br>ugoa              | chmod<br>u+x<br>myscript.sh                    |  |
| Viewing Files in Terminal       |                                                 |                                                |  |
| less                            | View files in terminal window.                  | less<br>foo.txt                                |  |
| cat                             | Concatenate files.                              | cat<br>foo1.txt<br>foo2.txt                    |  |
| head                            | Display first 10 lines.                         | head<br>-20<br>foo.txt                         |  |
| tail                            | Display last 10 lines.                          | tail<br>-f<br>logfile.txt                      |  |
| Searching                       |                                                 |                                                |  |
| grep                            |                                                 | grep<br>myvarname<br>*.txt                     |  |
|                                 | Search for word(s) in a file.                   | grep<br>rodent<br>*.txt                        |  |
|                                 |                                                 | grep<br>"Hello<br>World"<br>*.txt              |  |
| find                            |                                                 | find<br>playground<br>-name<br>"*.txt"         |  |
|                                 | Search<br>a<br>path<br>for<br>files/directories | find<br>playground<br>-type<br>d               |  |
|                                 | that match some specification.                  | find<br>playground<br>-not<br>-name<br>"*.txt" |  |
| Environment Variables           |                                                 |                                                |  |
| \$HOME                          | Home directory.                                 | workpath=\$HOME/playground                     |  |
| \$SHELL                         | Shell name.                                     | echo<br>\$SHELL                                |  |
| \$USER                          | User name.                                      | echo<br>\$USER                                 |  |
| \$PATH                          | Paths to look in for executables.               | PATH=\${PATH}:/my/new/program/path/bin         |  |
| env                             | List environment vars and values.               | env<br> <br>less                               |  |
|                                 |                                                 |                                                |  |

Common text editors: emacs, vim, vi, pico, nano

| Command                  | Description                                                   | Examples and Options                                                                      |  |
|--------------------------|---------------------------------------------------------------|-------------------------------------------------------------------------------------------|--|
| File Manipulation        |                                                               |                                                                                           |  |
| wc                       | Word count.                                                   | wc<br>-l<br>mycode.py                                                                     |  |
| sort                     | Sort input alphanumerically.                                  |                                                                                           |  |
|                          | Pipe/filter output through another<br>program.                | cat<br>foo.txt<br> <br>less<br>sort<br>myfile.txt<br> <br>grep<br>mykeyword               |  |
| >                        | Redirect standard output to.<br>Over<br>writes existing file. | cat<br>foo.txt<br>><br>foo2.txt                                                           |  |
| >>                       | Redirect standard output and con<br>catenate to.              | cat<br>foo.txt<br>>><br>foo2.txt                                                          |  |
| <                        | Redirect standard input from.                                 | less<br><<br>foo.txt                                                                      |  |
| awk                      | Advanced operations by column.                                |                                                                                           |  |
| sed                      | Advanced operations by row.                                   |                                                                                           |  |
| Job/process Manipulation |                                                               |                                                                                           |  |
| &                        | Run process in background.                                    | ./run_job.sh<br>&                                                                         |  |
| jobs                     | Show your current processes                                   | jobs                                                                                      |  |
| ps                       | Show processes (more flexible)                                | ps<br>-u<br>username                                                                      |  |
| top                      | Show top active processes                                     | top<br>-u<br>username                                                                     |  |
| kill                     | Stop a job                                                    | kill<br>processid                                                                         |  |
| Ctrl-z                   | Pause current job                                             | ./run_job.sh;<br>Ctrl-z                                                                   |  |
| Ctrl-c                   | Cancel current job                                            | ./run_job.sh;<br>Ctrl-c                                                                   |  |
| bg                       | Resume process in background                                  | ./run_job.sh;<br>Ctrl-z;<br>bg<br>%1                                                      |  |
| fg                       | Bring process to foreground                                   | fg<br>%2                                                                                  |  |
| Remote Connections       |                                                               |                                                                                           |  |
| ssh                      | Secure shell login.                                           | ssh<br>-Y<br>user@host.edu                                                                |  |
| scp                      | Secure copy.                                                  | scp<br>user@host.edu:path/to/file.txt                                                     |  |
| wget                     | Download file from remote URL.                                | wget<br>www.google.com<br>-O<br>google.html                                               |  |
| Ctrl-d                   | Exit login. Sometimes disabled.                               | Can also use<br>exit,<br>logout                                                           |  |
| Miscellaneous            |                                                               |                                                                                           |  |
| man                      | Manual for other commands.                                    | man<br>cat                                                                                |  |
| sleep                    | Do nothing                                                    | sleep<br>30                                                                               |  |
| touch                    | Create empty file/update timestamp                            | touch<br>newfile.txt                                                                      |  |
| whoami                   | Print current user.                                           | whoami                                                                                    |  |
| du                       | Disk usage.                                                   | du<br>-shc<br>mydirectory/*                                                               |  |
| df                       | Disk free.                                                    | df<br>-h                                                                                  |  |
| diff                     | Shows differences between two files.                          | diff<br>-w<br>file1.txt<br>file2.txt                                                      |  |
| echo                     | Write text to screen.                                         | echo<br>"Hello?<br>Can<br>you<br>hear<br>me?"                                             |  |
| which                    | Find path for command.                                        | which<br>gcc                                                                              |  |
| tar                      | Compress/uncompress files.                                    | tar<br>-zcvf<br>files.tar.gz<br>a.txt<br>b.fits<br>tar<br>-zxvf<br>downloadedstuff.tar.gz |  |
| history                  | See command history.                                          | history<br> <br>grep<br>myscript.py                                                       |  |
| alias                    | Create command shortcut.                                      | alias<br>lrt='ls<br>-lhrt'                                                                |  |
| source                   | Execute file in shell.                                        | source<br>˜/.bash_profile                                                                 |  |
|                          |                                                               |                                                                                           |  |