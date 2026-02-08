|    | Command           | Description                              | Examples and Options                |
|---:|:------------------|:-----------------------------------------|:------------------------------------|
|  0 | File Manipulation | nan                                      | nan                                 |
|  1 | wc                | Word count.                              | wc -l mycode.py                     |
|  2 | sort              | Sort input alphanumerically.             | nan                                 |
|  3 | nan               | nan                                      | cat foo.txt | less                  |
|  4 | |                 | Pipe/filter output through another       | nan                                 |
|  5 | nan               | nan                                      | sort myfile.txt | grep mykeyword    |
|  6 | nan               | program.                                 | nan                                 |
|  7 | >                 | Redirect standard output to. Over￾writes | cat foo.txt > foo2.txt              |
|  8 | nan               | existing file.                           | nan                                 |
|  9 | >>                | Redirect standard output and             | cat foo.txt >> foo2.txt             |
| 10 | nan               | con￾catenate                             | nan                                 |
| 11 | nan               | to.                                      | nan                                 |
| 12 | <                 | Redirect standard input from.            | less < foo.txt                      |
| 13 | awk               | Advanced operations by column.           | nan                                 |
| 14 | sed               | Advanced operations by row.              | nan                                 |
| 15 | Job/process       | Manipulation                             | nan                                 |
| 16 | &                 | Run process in background.               | ./run_job.sh &                      |
| 17 | jobs              | Show your current processes              | jobs                                |
| 18 | ps                | Show processes (more flexible)           | ps -u username                      |
| 19 | top               | Show top active processes                | top -u username                     |
| 20 | kill              | Stop a job                               | kill processid                      |
| 21 | Ctrl-z            | Pause current job                        | ./run_job.sh; Ctrl-z                |
| 22 | Ctrl-c            | Cancel current job                       | ./run_job.sh; Ctrl-c                |
| 23 | bg                | Resume process in background             | ./run_job.sh; Ctrl-z; bg %1         |
| 24 | fg                | Bring process to foreground              | fg %2                               |
| 25 | Remote            | Connections                              | nan                                 |
| 26 | ssh               | Secure shell login.                      | ssh -Y user@host.edu                |
| 27 | scp               | Secure copy.                             | scp user@host.edu:path/to/file.txt  |
| 28 | wget              | Download file from remote URL.           | wget www.google.com -O google.html  |
| 29 | Ctrl-d            | Exit login. Sometimes disabled.          | Can also use exit, logout           |
| 30 | Miscellaneous     | nan                                      | nan                                 |
| 31 | man               | Manual for other commands.               | man cat                             |
| 32 | sleep             | Do nothing                               | sleep 30                            |
| 33 | touch             | Create empty file/update timestamp       | touch newfile.txt                   |
| 34 | whoami            | Print current user.                      | whoami                              |
| 35 | du                | Disk usage.                              | du -shc mydirectory/*               |
| 36 | df                | Disk free.                               | df -h                               |
| 37 | diff              | Shows differences between two files.     | diff -w file1.txt file2.txt         |
| 38 | echo              | Write text to screen.                    | echo "Hello? Can you hear me?"      |
| 39 | which             | Find path for command.                   | which gcc                           |
| 40 | nan               | nan                                      | tar -zcvf files.tar.gz a.txt b.fits |
| 41 | tar               | Compress/uncompress files.               | nan                                 |
| 42 | nan               | nan                                      | tar -zxvf downloadedstuff.tar.gz    |
| 43 | history           | See command history.                     | history | grep myscript.py          |
| 44 | alias             | Create command shortcut.                 | alias lrt='ls -lhrt'                |
| 45 | source            | Execute file in shell.                   | source ˜/.bash_profile              |