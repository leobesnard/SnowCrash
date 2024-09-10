We tried the same thing on previous level but obviously it was not working

Then i got the idea to check every user account on the system.

	level01@SnowCrash:~$ cat /etc/passwd
	...
	level00:x:2000:2000::/home/user/level00:/bin/bash
	level01:x:2001:2001::/home/user/level01:/bin/bash
	level02:x:2002:2002::/home/user/level02:/bin/bash
	level03:x:2003:2003::/home/user/level03:/bin/bash
	level04:x:2004:2004::/home/user/level04:/bin/bash
	level05:x:2005:2005::/home/user/level05:/bin/bash
	level06:x:2006:2006::/home/user/level06:/bin/bash
	level07:x:2007:2007::/home/user/level07:/bin/bash
	level08:x:2008:2008::/home/user/level08:/bin/bash
	level09:x:2009:2009::/home/user/level09:/bin/bash
	level10:x:2010:2010::/home/user/level10:/bin/bash
	level11:x:2011:2011::/home/user/level11:/bin/bash
	level12:x:2012:2012::/home/user/level12:/bin/bash
	level13:x:2013:2013::/home/user/level13:/bin/bash
	level14:x:2014:2014::/home/user/level14:/bin/bash
	flag00:x:3000:3000::/home/flag/flag00:/bin/bash
	flag01:42hDRfypTqqnw:3001:3001::/home/flag/flag01:/bin/bash
	flag02:x:3002:3002::/home/flag/flag02:/bin/bash
	flag03:x:3003:3003::/home/flag/flag03:/bin/bash
	flag04:x:3004:3004::/home/flag/flag04:/bin/bash
	flag05:x:3005:3005::/home/flag/flag05:/bin/bash
	flag06:x:3006:3006::/home/flag/flag06:/bin/bash
	flag07:x:3007:3007::/home/flag/flag07:/bin/bash
	flag08:x:3008:3008::/home/flag/flag08:/bin/bash
	flag09:x:3009:3009::/home/flag/flag09:/bin/bash
	flag10:x:3010:3010::/home/flag/flag10:/bin/bash
	flag11:x:3011:3011::/home/flag/flag11:/bin/bash
	flag12:x:3012:3012::/home/flag/flag12:/bin/bash
	flag13:x:3013:3013::/home/flag/flag13:/bin/bash
	flag14:x:3014:3014::/home/flag/flag14:/bin/bash
	...

I clearly see that the flag01 have something like a password in it.

I tried as a flag but it was not working

level01@SnowCrash:~$ su flag01
Password:
su: Authentication failure

Then i needed to try to use the JohnTheRipper program

I used the scp command to copy the output of "cat /etc/passwd" to get the hash
Then i used JTR to test that hash

	run echo -n 42hDRfypTqqnw > passwd

	run ./john passwd
	Using default input encoding: UTF-8
	Loaded 1 password hash (descrypt, traditional crypt(3) [DES 512/512 AVX512F])
	Will run 16 OpenMP threads
	Note: Passwords longer than 8 truncated (property of the hash)
	Proceeding with single, rules:Single
	Press 'q' or Ctrl-C to abort, 'h' for help, almost any other key for status
	Almost done: Processing the remaining buffered candidate passwords, if any.
	Proceeding with wordlist:./password.lst
	Enabling duplicate candidate password suppressor
###	abcdefg          (?)
	1g 0:00:00:00 DONE 2/3 (2024-08-21 22:19) 11.11g/s 1001Kp/s 1001Kc/s 1001KC/s 123456..Popcorn
	Use the "--show" option to display all of the cracked passwords reliably
	Session completed.

I saw that the password could be "abcdefg" so i tried it, it worked and i got the flag.

	su flag01
	Password:
	Don't forget to launch getflag !
	flag01@SnowCrash:~$ getflag
	Check flag.Here is your token : f2av5il02puano7naaf6adaaf
