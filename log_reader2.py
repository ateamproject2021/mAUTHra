#!/usr/bin/env python3
import sys

with open(sys.argv[1], 'r') as f:
	contents = f.readlines()
result_new_group = ""
result_incorrect_password = ""

for line in contents:
    if "new group: " in line:
        result_new_group += line + "\n"
        
    if "incorrect password" in line:
        result_incorrect_password += line + "\n"

print("Log entries pertaining to new users:\n"
        + result_new_group
        + "Log entries pertaining to failed passwords:\n"
        + result_incorrect_password)
	
