On the level03 we do a basic "ls" command and we see this pcap file.

	level02@SnowCrash:~$ ls
	level02.pcap

We are going to copy it to our machine and analyse it with cloudshark. (web site given in the video)

	scp -P 4242 level02@192.168.1.11:/home/user/level02/level02.pcap . 

With the tools given by cloudshark we can see the stream and find something.
	
	Password: ft_wandr...NDRel.L0L

We try it but it's not working.

Then on cloudshark we switch from ASCII to Hex Dump to see which characters are used.
We seeing that the dots are 7f which is not a dot but a "DEL" character and the o is a 0.

Then we try to put the "DEL" at the right places and we got "ft_waNDReL0L"
This time it works.

	level02@SnowCrash:~$ su flag02
	Password:
	Don't forget to launch getflag !
	flag02@SnowCrash:~$ getflag
	Check flag.Here is your token : kooda2puivaav1idi4f57q8iq
