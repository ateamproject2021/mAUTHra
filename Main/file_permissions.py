#!/usr/bin/env python3
import sys

def main():
    #collector result string
    result = ""

    #this code allows for file's contents to be used as input in our function
    with open(sys.argv[1], 'r') as f:
        contents = f.readlines()
    #the "meat" of the test case module
    for line in contents:
    #insert specific test case criteria here
        if "chmod" in line:
            if "+r" in line:
                new_line = line.replace("+r", "user added readability to this file >>>")
                result += new_line
            else: result += line
    if len(result) < 5:
        print("No applicable log entries found.")
    else: print(result)

#no touchy
if __name__ == "__main__":
    main()
