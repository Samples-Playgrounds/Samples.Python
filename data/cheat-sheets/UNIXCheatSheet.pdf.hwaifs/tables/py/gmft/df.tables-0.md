|    | Command       | Description                          | Examples and Options                    |
|---:|:--------------|:-------------------------------------|:----------------------------------------|
|  0 | <tab>         | Attempt to autocomplete              | Use this to speed up typing/avoid typos |
|  1 | Navigating    | Directories                          | nan                                     |
|  2 | ls            | List the contents of the directory.  | ls -larth /home/mcuser/science/code     |
|  3 | cd            | Change directory.                    | cd /home/mcuser/science                 |
|  4 | pwd           | present working directory.           | pwd                                     |
|  5 | *             | Wild card, any number of chars.      | ls *.txt                                |
|  6 | ?             | Wild card, 0 or 1 characters.        | ls foo?.txt                             |
|  7 | .             | Current directory.                   | cd .                                    |
|  8 | ..            | Directory one level up.              | cd ..                                   |
|  9 | ~             | Home directory.                      | cd ~                                    |
| 10 | -             | Previous directory.                  | cd -                                    |
| 11 | Modifying     | Directories and Files                | nan                                     |
| 12 | mkdir         | Make new empty directory.            | mkdir MyNewDirectory                    |
| 13 | rmdir         | Remove empty directory.              | rmdir MyNewDirectory                    |
| 14 | mv            | Move files (overwrites destination). | mv -i foo.txt foo2.txt                  |
| 15 | cp            | Copy files (overwrites destination). | cp -i ../foo.txt .                      |
| 16 | rm            | Remove files. CANNOT UNDO!           | rm -i foo.txt                           |
| 17 | nan           | Change file permissions.             | chmod a+rwx badger.txt                  |
| 18 | chmod         | rwx = read, write, execute.          | chmod o-wx badger.txt                   |
| 19 | nan           | ugoa = user, group, other, all.      | chmod u+x myscript.sh                   |
| 20 | Viewing Files | in Terminal                          | nan                                     |
| 21 | less          | View files in terminal window.       | less foo.txt                            |
| 22 | cat           | Concatenate files.                   | cat foo1.txt foo2.txt                   |
| 23 | head          | Display first 10 lines.              | head -20 foo.txt                        |
| 24 | tail          | Display last 10 lines.               | tail -f logfile.txt                     |
| 25 | Searching     | nan                                  | nan                                     |
| 26 | nan           | nan                                  | grep myvarname *.txt                    |
| 27 | grep          | Search for word(s) in a file.        | grep rodent *.txt                       |
| 28 | nan           | nan                                  | grep "Hello World" *.txt                |
| 29 | nan           | nan                                  | find playground -name "*.txt"           |
| 30 | find          | Search a path for files/directories  | find playground -type d                 |
| 31 | nan           | that match some specification.       | find playground -not -name "*.txt"      |
| 32 | Environment   | Variables                            | nan                                     |
| 33 | $HOME         | Home directory.                      | workpath=$HOME/playground               |
| 34 | $SHELL        | Shell name.                          | echo $SHELL                             |
| 35 | $USER         | User name.                           | echo $USER                              |
| 36 | $PATH         | Paths to look in for executables.    | PATH=${PATH}:/my/new/program/path/bin   |
| 37 | env           | List environment vars and values.    | env | less                              |