#!/usr/bin/env python3
import sys

with open(sys.argv[1], 'r') as f:
	contents = f.readlines()
result = ""
for line in contents:
	if "incorrect password attempts" in line:
		result+= line

print(result)
	
