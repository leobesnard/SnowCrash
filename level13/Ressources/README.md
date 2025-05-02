For this level we see the file level13.

	level13@SnowCrash:~$ ls
	level13

	level13@SnowCrash:~$ ./level13
	UID 2013 started us but we we expect 4242

We look in the file with strings and we see that it use the getuid function

Then we use gdb to look at the program step by step the file
Using layout regs and layout asm we are able to determine where the value of the UID is put in comparison.
So we have to change it to 4242 just before the comparison

	(gdb) break getuid
	Breakpoint 1 at 0x8048380
	(gdb) run
	Starting program: /home/user/level13/level13 

	Breakpoint 1, 0xb7ee4cc0 in getuid () from /lib/i386-linux-gnu/libc.so.6
	(gdb) print $eax
	$1 = 1
	(gdb) step
	Single stepping until exit from function getuid,
	which has no line number information.
	0x0804859a in main ()
	(gdb) print $eax
	$2 = 2013
	(gdb) set $eax=4242
	(gdb) print $eax
	$3 = 4242
	(gdb) step
	Single stepping until exit from function main,
	which has no line number information.
	your token is 2A31L79asukciNyi8uppkEuSx
	0xb7e454d3 in __libc_start_main () from /lib/i386-linux-gnu/libc.so.6

