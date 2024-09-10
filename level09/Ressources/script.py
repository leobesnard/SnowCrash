import sys

if ((len(sys.argv) == 2) and (sys.argv[1]) and (isinstance(sys.argv[1], str))):
	s = list(sys.argv[1])
	for i in range(0, len(s)):
		value = ord(s[i]) - i
		s[i] = chr(value)

	ret = "".join(s)
	print(ret)

else:
	print('This script need one argument')
