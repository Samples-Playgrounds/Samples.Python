# UNIX Command Cheat Sheet

Carnegie Observatories Summer Research Program
Every command and filename is CaSe sEnSiTiVe!














|Command|Description|Examples and Options|
|---|---|---|
|`<tab>`|Attempt to autocomplete|Use this to speed up typing/avoid typos|
|_Navigating Directories_|_Navigating Directories_|_Navigating Directories_|
|`ls`|List the contents of the directory.|`ls -larth /home/mcuser/science/code`|
|`cd`|Change directory.|`cd /home/mcuser/science`|
|`pwd`|_p_resent _w_orking _d_irectory.|`pwd`|
|`*`|Wild card, any number of chars.|`ls *.txt`|
|`?`|Wild card, 0 or 1 characters.|`ls foo?.txt`|
|`.`|Current directory.|`cd .`|
|`..`|Directory one level up.|`cd ..`|
|`~`|Home directory.|`cd ~`|
|`-`|Previous directory.|`cd -`|
|_Modifying Directories and Files_|_Modifying Directories and Files_|_Modifying Directories and Files_|
|`mkdir`|Make new empty directory.|`mkdir MyNewDirectory`|
|`rmdir`|Remove empty directory.|`rmdir MyNewDirectory`|
|`mv`|Move ﬁles (overwrites destination).|`mv -i foo.txt foo2.txt`|
|`cp`|Copy ﬁles (overwrites destination).|`cp -i ../foo.txt .`|
|`rm`|Remove ﬁles. **CANNOT UNDO!**|`rm -i foo.txt`|
|`chmod`|Change ﬁle permissions.<br>`rwx` = read, write, execute.<br>`ugoa` = user, group, other, all.|`chmod a+rwx badger.txt`<br>`chmod o-wx badger.txt`<br>`chmod u+x myscript.sh`|
|_Viewing Files in Terminal_|_Viewing Files in Terminal_|_Viewing Files in Terminal_|
|`less`|View ﬁles in terminal window.|`less foo.txt`|
|`cat`|Con_cat_enate ﬁles.|`cat foo1.txt foo2.txt`|
|`head`|Display ﬁrst 10 lines.|`head -20 foo.txt`|
|`tail`|Display last 10 lines.|`tail -f logfile.txt`|
|_Searching_|_Searching_|_Searching_|
|`grep`|Search for word(s) in a ﬁle.|`grep myvarname *.txt`<br>`grep rodent *.txt`<br>`grep "Hello World" *.txt`|
|`find`|Search a path for ﬁles/directories<br>that match some speciﬁcation.|`find playground -name "*.txt"`<br>`find playground -type d`<br>`find playground -not -name "*.txt"`|
|_Environment Variables_|_Environment Variables_|_Environment Variables_|
|`$HOME`|Home directory.|`workpath=$HOME/playground`|
|`$SHELL`|Shell name.|`echo $SHELL`|
|`$USER`|User name.|`echo $USER`|
|`$PATH`|Paths to look in for executables.|`PATH=${PATH}:/my/new/program/path/bin`|
|`env`<br>|List environment vars and values.<br>|`env | less`|


|Command|Description|Examples and Options|
|---|---|---|
|_File Manipulation_|_File Manipulation_|_File Manipulation_|
|`wc`|Word count.|`wc -l mycode.py`|
|`sort`|Sort input alphanumerically.||
|`|`|Pipe/ﬁlter output through another<br>program.|`cat foo.txt | less`<br>`sort myfile.txt | grep mykeyword`|
|`>`|Redirect standard output to. Over-<br>writes existing ﬁle.|`cat foo.txt > foo2.txt`|
|`>>`|Redirect standard output and con-<br>catenate to.|`cat foo.txt >> foo2.txt`|
|`<`|Redirect standard input from.|`less < foo.txt`|
|`awk`|Advanced operations by column.||
|`sed`|Advanced operations by row.||
|_Job/process Manipulation_|_Job/process Manipulation_|_Job/process Manipulation_|
|`&`|Run process in background.|`./run_job.sh &`|
|`jobs`|Show your current processes|`jobs`|
|`ps`|Show processes (more ﬂexible)|`ps -u username`|
|`top`|Show top active processes|`top -u username`|
|`kill`|Stop a job|`kill processid`|
|`Ctrl-z`|Pause current job|`./run_job.sh; Ctrl-z`|
|`Ctrl-c`|Cancel current job|`./run_job.sh; Ctrl-c`|
|`bg`|Resume process in background|`./run_job.sh; Ctrl-z; bg %1`|
|`fg`|Bring process to foreground|`fg %2`|
|_Remote Connections_|_Remote Connections_|_Remote Connections_|
|`ssh`|Secure shell login.|`ssh -Y user@host.edu`|
|`scp`|Secure copy.|`scp user@host.edu:path/to/file.txt .`|
|`wget`|Download ﬁle from remote URL.|`wget www.google.com -O google.html`|
|`Ctrl-d`|Exit login. Sometimes disabled.|Can also use `exit`, `logout`|
|_Miscellaneous_|_Miscellaneous_|_Miscellaneous_|
|`man`|_Man_ual for other commands.|`man cat`|
|`sleep`|Do nothing|`sleep 30`|
|`touch`|Create empty ﬁle/update timestamp|`touch newfile.txt`|
|`whoami`|Print current user.|`whoami`|
|`du`|Disk usage.|`du -shc mydirectory/*`|
|`df`|Disk free.|`df -h`|
|`diff`|Shows diﬀerences between two ﬁles.|`diff -w file1.txt file2.txt`|
|`echo`|Write text to screen.|`echo "Hello? Can you hear me?"`|
|`which`|Find path for command.|`which gcc`|
|`tar`|Compress/uncompress ﬁles.|`tar -zcvf files.tar.gz a.txt b.fits`<br>`tar -zxvf downloadedstuff.tar.gz`|
|`history`|See command history.|`history | grep myscript.py`|
|`alias`|Create command shortcut.|`alias lrt='ls -lhrt'`|
|`source`|Execute ﬁle in shell.|`source ˜/.bash_profile`|


