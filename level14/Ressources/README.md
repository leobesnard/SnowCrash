For this level we tried to list all the files, we see nothing, no interesting files owned by flag14 or level14.

After more research we find out that we will need to use gdb, like on the level13 but on /bin/getflag

	level14@SnowCrash:~$ gdb /bin/getflag
	GNU gdb (Ubuntu/Linaro 7.4-2012.04-0ubuntu2.1) 7.4-2012.04
	Copyright (C) 2012 Free Software Foundation, Inc.
	License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
	This is free software: you are free to change and redistribute it.
	There is NO WARRANTY, to the extent permitted by law.  Type "show copying"
	and "show warranty" for details.
	This GDB was configured as "i686-linux-gnu".
	For bug reporting instructions, please see:
	<http://bugs.launchpad.net/gdb-linaro/>...
	Reading symbols from /bin/getflag...(no debugging symbols found)...done.
	(gdb) run
	Starting program: /bin/getflag 
	You should not reverse this
	[Inferior 1 (process 3007) exited with code 01]

We see that we it is protected from using gdb.
So we try to disasemble the main to understand better what is happening.

Here is the first part we need to see.
	Dump of assembler code for function main:
	   0x08048946 <+0>:	push   %ebp
	   0x08048947 <+1>:	mov    %esp,%ebp
	   0x08048949 <+3>:	push   %ebx
	   0x0804894a <+4>:	and    $0xfffffff0,%esp
	   0x0804894d <+7>:	sub    $0x120,%esp
	   0x08048953 <+13>:	mov    %gs:0x14,%eax
	   0x08048959 <+19>:	mov    %eax,0x11c(%esp)
	   0x08048960 <+26>:	xor    %eax,%eax
	   0x08048962 <+28>:	movl   $0x0,0x10(%esp)
	   0x0804896a <+36>:	movl   $0x0,0xc(%esp)
	   0x08048972 <+44>:	movl   $0x1,0x8(%esp)
	   0x0804897a <+52>:	movl   $0x0,0x4(%esp)
	   0x08048982 <+60>:	movl   $0x0,(%esp)
	   0x08048989 <+67>:	call   0x8048540 <ptrace@plt>
	   0x0804898e <+72>:	test   %eax,%eax
	   0x08048990 <+74>:	jns    0x80489a8 <main+98>

We see that it use ptrace to protect the script from debugging. (it check if there is only one process tracing it so when we try to debug there the gdb process and himself)

We need to put a breakpoint on ptrace and then we need to change the value of $eax just before it test it.

	(gdb) break ptrace
	Breakpoint 1 at 0xb7f146d0
	(gdb) run
	Starting program: /bin/getflag 

	Breakpoint 1, 0xb7f146d0 in ptrace () from /lib/i386-linux-gnu/libc.so.6
	(gdb) print $eax
	$1 = 0
	(gdb) step
	Single stepping until exit from function ptrace,
	which has no line number information.
	0x0804898e in main ()
	(gdb) print $eax
	$2 = -1
	(gdb) set $eax = 0
	(gdb) print $eax
	$3 = 0

Now when it test the value we are going to jump to the success case. 
We will need the UID of level14 and flag14 users.

	level14@SnowCrash:~$ id level14
	uid=2014(level14) gid=2014(level14) groups=2014(level14),100(users)
	level14@SnowCrash:~$ id flag14
	uid=3014(flag14) gid=3014(flag14) groups=3014(flag14),1001(flag)



We can now break on the getuid function then moove step by step printing the $eax value and when we see 2014 we replace it by 3014.
It will make us appear to be flag14 user.

	(gdb) break getuid
	Breakpoint 2 at 0xb7ee4cc0
	(gdb) step
	Single stepping until exit from function main,
	which has no line number information.

	Breakpoint 2, 0xb7ee4cc0 in getuid () from /lib/i386-linux-gnu/libc.so.6
	(gdb) print $eax
	$4 = 32
	(gdb) step
	Single stepping until exit from function getuid,
	which has no line number information.
	0x08048b02 in main ()
	(gdb) print $eax
	$5 = 2014
	(gdb) set $eax = 3014
	(gdb) print $eax
	$6 = 3014
	(gdb) step
	Single stepping until exit from function main,
	which has no line number information.
	Check flag.Here is your token : 7QiHafiNa3HVozsaXkawuYrTstxbpABHD8CPnHJ
	0xb7e454d3 in __libc_start_main () from /lib/i386-linux-gnu/libc.so.6

So we get the flag for flag14 user and when we connect we see this

	level14@SnowCrash:~$ su flag14
	Password: 
	Congratulation. Type getflag to get the key and send it to me the owner of this livecd :)
	flag14@SnowCrash:~$ getflag
	Check flag.Here is your token : 7QiHafiNa3HVozsaXkawuYrTstxbpABHD8CPnHJ






