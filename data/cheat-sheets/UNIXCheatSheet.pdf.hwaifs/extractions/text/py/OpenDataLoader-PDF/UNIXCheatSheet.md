# UNIX Command Cheat Sheet

Carnegie Observatories Summer Research Program Every command and ﬁlename is CaSe sEnSiTiVe!

<table>
  <tr>
    <th>Command<br><br></th>
    <th>Description</th>
    <th>Examples and Options</th>
  </tr>
  <tr>
    <td><tab><br><br></td>
    <td>Attempt to autocomplete</td>
    <td>Use this to speed up typing/avoid typos</td>
  </tr>
  <tr>
    <td colspan="3">Navigating Directories</td>
  </tr>
  <tr>
    <td>ls</td>
    <td>List the contents of the directory.<br><br></td>
    <td>ls -larth /home/mcuser/science/code</td>
  </tr>
  <tr>
    <td>cd</td>
    <td>Change directory.<br><br></td>
    <td>cd /home/mcuser/science</td>
  </tr>
  <tr>
    <td>pwd<br><br></td>
    <td>present working directory.<br><br></td>
    <td>pwd</td>
  </tr>
  <tr>
    <td>*</td>
    <td>Wild card, any number of chars.</td>
    <td>ls *.txt</td>
  </tr>
  <tr>
    <td>?<br><br></td>
    <td>Wild card, 0 or 1 characters.</td>
    <td>ls foo?.txt</td>
  </tr>
  <tr>
    <td>.</td>
    <td>Current directory.<br><br></td>
    <td>cd .</td>
  </tr>
  <tr>
    <td>..</td>
    <td>Directory one level up.</td>
    <td>cd ..</td>
  </tr>
  <tr>
    <td> </td>
    <td>Home directory.</td>
    <td>cd</td>
  </tr>
  <tr>
    <td>-</td>
    <td>Previous directory.</td>
    <td>cd -</td>
  </tr>
  <tr>
    <td colspan="3">Modifying Directories and Files</td>
  </tr>
  <tr>
    <td>mkdir</td>
    <td>Make new empty directory.<br><br></td>
    <td>mkdir MyNewDirectory</td>
  </tr>
  <tr>
    <td>rmdir</td>
    <td>Remove empty directory.<br><br></td>
    <td>rmdir MyNewDirectory</td>
  </tr>
  <tr>
    <td>mv</td>
    <td>Move ﬁles (overwrites destination).</td>
    <td>mv -i foo.txt foo2.txt</td>
  </tr>
  <tr>
    <td>cp<br><br></td>
    <td>Copy ﬁles (overwrites destination).</td>
    <td>cp -i ../foo.txt .</td>
  </tr>
  <tr>
    <td>rm<br><br></td>
    <td>Remove ﬁles. CANNOT UNDO!<br><br></td>
    <td>rm -i foo.txt</td>
  </tr>
  <tr>
    <td>chmod<br><br></td>
    <td>Change ﬁle permissions. rwx = read, write, execute. ugoa = user, group, other, all.</td>
    <td>chmod a+rwx badger.txt chmod o-wx badger.txt chmod u+x myscript.sh</td>
  </tr>
  <tr>
    <td colspan="3">Viewing Files in Terminal</td>
  </tr>
  <tr>
    <td>less<br><br></td>
    <td>View ﬁles in terminal window.<br><br></td>
    <td>less foo.txt</td>
  </tr>
  <tr>
    <td>cat<br><br></td>
    <td>Concatenate ﬁles.</td>
    <td>cat foo1.txt foo2.txt</td>
  </tr>
  <tr>
    <td>head<br><br></td>
    <td>Display ﬁrst 10 lines.</td>
    <td>head -20 foo.txt</td>
  </tr>
  <tr>
    <td>tail<br><br></td>
    <td>Display last 10 lines.</td>
    <td>tail -f logfile.txt</td>
  </tr>
  <tr>
    <td colspan="3">Searching</td>
  </tr>
  <tr>
    <td>grep</td>
    <td>Search for word(s) in a ﬁle.<br><br></td>
    <td>grep myvarname *.txt grep rodent *.txt grep "Hello World" *.txt</td>
  </tr>
  <tr>
    <td>find</td>
    <td>Search a path for ﬁles/directories that match some speciﬁcation.</td>
    <td>find playground -name "*.txt" find playground -type d find playground -not -name "*.txt"</td>
  </tr>
  <tr>
    <td colspan="3">Environment Variables</td>
  </tr>
  <tr>
    <td>$HOME<br><br></td>
    <td>Home directory.</td>
    <td>workpath=$HOME/playground</td>
  </tr>
  <tr>
    <td>$SHELL<br><br></td>
    <td>Shell name.</td>
    <td>echo $SHELL</td>
  </tr>
  <tr>
    <td>$USER<br><br></td>
    <td>User name.<br><br></td>
    <td>echo $USER</td>
  </tr>
  <tr>
    <td>$PATH</td>
    <td>Paths to look in for executables.<br><br></td>
    <td>PATH=${PATH}:/my/new/program/path/bin</td>
  </tr>
  <tr>
    <td>env</td>
    <td>List environment vars and values.</td>
    <td>env | less</td>
  </tr>
</table>


## Common text editors: emacs, vim, vi, pico, nano

<table>
  <tr>
    <th>Command</th>
    <th>Description<br><br></th>
    <th>Examples and Options</th>
  </tr>
  <tr>
    <td colspan="3">File Manipulation</td>
  </tr>
  <tr>
    <td>wc<br><br></td>
    <td>Word count.</td>
    <td>wc -l mycode.py</td>
  </tr>
  <tr>
    <td>sort<br><br></td>
    <td>Sort input alphanumerically.</td>
    <td> </td>
  </tr>
  <tr>
    <td>|<br><br></td>
    <td>Pipe/ﬁlter output through another program.<br><br></td>
    <td>cat foo.txt | less sort myfile.txt | grep mykeyword</td>
  </tr>
  <tr>
    <td>><br><br></td>
    <td>Redirect standard output to. Overwrites existing ﬁle.</td>
    <td>cat foo.txt > foo2.txt</td>
  </tr>
  <tr>
    <td>>><br><br></td>
    <td>Redirect standard output and concatenate to.</td>
    <td>cat foo.txt >> foo2.txt</td>
  </tr>
  <tr>
    <td><<br><br></td>
    <td>Redirect standard input from.</td>
    <td>less < foo.txt</td>
  </tr>
  <tr>
    <td>awk</td>
    <td>Advanced operations by column.</td>
    <td> </td>
  </tr>
  <tr>
    <td>sed<br><br></td>
    <td>Advanced operations by row.</td>
    <td> </td>
  </tr>
  <tr>
    <td colspan="3">Job/process Manipulation</td>
  </tr>
  <tr>
    <td>&</td>
    <td>Run process in background.<br><br></td>
    <td>./run_job.sh &</td>
  </tr>
  <tr>
    <td>jobs<br><br></td>
    <td>Show your current processes</td>
    <td>jobs</td>
  </tr>
  <tr>
    <td>ps</td>
    <td>Show processes (more ﬂexible)<br><br></td>
    <td>ps -u username</td>
  </tr>
  <tr>
    <td>top<br><br></td>
    <td>Show top active processes</td>
    <td>top -u username</td>
  </tr>
  <tr>
    <td>kill</td>
    <td>Stop a job<br><br></td>
    <td>kill processid</td>
  </tr>
  <tr>
    <td>Ctrl-z<br><br></td>
    <td>Pause current job</td>
    <td>./run_job.sh; Ctrl-z</td>
  </tr>
  <tr>
    <td>Ctrl-c<br><br></td>
    <td>Cancel current job</td>
    <td>./run_job.sh; Ctrl-c</td>
  </tr>
  <tr>
    <td>bg<br><br></td>
    <td>Resume process in background<br><br></td>
    <td>./run_job.sh; Ctrl-z; bg %1</td>
  </tr>
  <tr>
    <td>fg<br><br></td>
    <td>Bring process to foreground</td>
    <td>fg %2</td>
  </tr>
  <tr>
    <td colspan="3">Remote Connections</td>
  </tr>
  <tr>
    <td>ssh</td>
    <td>Secure shell login.<br><br></td>
    <td>ssh -Y user@host.edu</td>
  </tr>
  <tr>
    <td>scp<br><br></td>
    <td>Secure copy.<br><br></td>
    <td>scp user@host.edu:path/to/file.txt .</td>
  </tr>
  <tr>
    <td>wget<br><br></td>
    <td>Download ﬁle from remote URL.</td>
    <td>wget www.google.com -O google.html</td>
  </tr>
  <tr>
    <td>Ctrl-d</td>
    <td>Exit login. Sometimes disabled.<br><br></td>
    <td>Can also use exit, logout</td>
  </tr>
  <tr>
    <td colspan="3">Miscellaneous</td>
  </tr>
  <tr>
    <td>man<br><br></td>
    <td>Manual for other commands.<br><br></td>
    <td>man cat</td>
  </tr>
  <tr>
    <td>sleep<br><br></td>
    <td>Do nothing</td>
    <td>sleep 30</td>
  </tr>
  <tr>
    <td>touch<br><br></td>
    <td>Create empty ﬁle/update timestamp<br><br></td>
    <td>touch newfile.txt</td>
  </tr>
  <tr>
    <td>whoami<br><br></td>
    <td>Print current user.<br><br></td>
    <td>whoami</td>
  </tr>
  <tr>
    <td>du<br><br></td>
    <td>Disk usage.<br><br></td>
    <td>du -shc mydirectory/*</td>
  </tr>
  <tr>
    <td>df<br><br></td>
    <td>Disk free.</td>
    <td>df -h</td>
  </tr>
  <tr>
    <td>diff<br><br></td>
    <td>Shows diﬀerences between two ﬁles.</td>
    <td>diff -w file1.txt file2.txt</td>
  </tr>
  <tr>
    <td>echo<br><br></td>
    <td>Write text to screen.</td>
    <td>echo "Hello? Can you hear me?"</td>
  </tr>
  <tr>
    <td>which<br><br></td>
    <td>Find path for command.</td>
    <td>which gcc</td>
  </tr>
  <tr>
    <td>tar</td>
    <td>Compress/uncompress ﬁles.<br><br></td>
    <td>tar -zcvf files.tar.gz a.txt b.fits tar -zxvf downloadedstuff.tar.gz</td>
  </tr>
  <tr>
    <td>history<br><br></td>
    <td>See command history.<br><br></td>
    <td>history | grep myscript.py</td>
  </tr>
  <tr>
    <td>alias<br><br></td>
    <td>Create command shortcut.</td>
    <td>alias lrt='ls -lhrt'</td>
  </tr>
  <tr>
    <td>source</td>
    <td>Execute ﬁle in shell.</td>
    <td>source ˜/.bash_profile</td>
  </tr>
</table>


