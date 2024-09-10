For this level, we find a executable and a token file.

	level09@SnowCrash:~$ ls -l
	total 12
	-rwsr-sr-x 1 flag09 level09 7640 Mar  5  2016 level09
	----r--r-- 1 flag09 level09   26 Mar  5  2016 token

The token seems encrypted.

	level09@SnowCrash:~$ cat token
	f4kmm6p|=�p�n��DB�Du{��

We need to find out what does this program.
With a lot of research we finally get something.

	...
	...
	...
	level09@SnowCrash:~$ ./level09 token
	tpmhr
	level09@SnowCrash:~$ ./level09 a
	a
	level09@SnowCrash:~$ ./level09 aa
	ab
	level09@SnowCrash:~$ ./level09 aaa
	abc
	level09@SnowCrash:~$ ./level09 aaaaaaa
	abcdefg

It seems that the program add it index to each character of the string.
Now we need to create a script that does the opposite.

You can find it in the "/Ressources" folder.
We copy it in our VM and use it on the content of the token file.

	scp -P 4242 script.py level09@192.168.1.11:/tmp/.

	level09@SnowCrash:~$ python /tmp/script.py $(cat token)
	f3iji1ju5yuevaus41q1afiuq
	level09@SnowCrash:~$ su flag09
	Password: 
	Don't forget to launch getflag !
	flag09@SnowCrash:~$ getflag
	Check flag.Here is your token : s5cAJpM8ev6XHw998pRWG728z

