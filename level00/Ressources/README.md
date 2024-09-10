We trying to see what files are owned by the flag00 user.

level00@SnowCrash:~$ find / -user flag00 2>/dev/null
/usr/sbin/john
/rofs/usr/sbin/john

level00@SnowCrash:~$ cat /usr/sbin/john
cdiiddwpgswtgt

When we try it as password we get a failure

level00@SnowCrash:~$ su flag00
Password:
su: Authentication failure

We use the decode.fr site given by the 42 video
And we find that the passphrase is a rot15 to the phrase "nottoohardhere"

This time it works

level00@SnowCrash:~$ su flag00
Password:
Don't forget to launch getflag !
flag00@SnowCrash:~$ getflag
Check flag.Here is your token : x24ti5gi3x0ol2eh4esiuxias

With that token we can log to the level01 account
