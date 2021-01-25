#!/usr/bin/env python3
import sys

error = False
def main(error):
    #collector result string
    result = ""
    linecounter = 0
    #this code allows for file's contents to be used as input in our function
    with open(sys.argv[1], 'r') as f:
        contents = f.readlines()
    if error == True:
        print("Incorrect input, please try again\nFor command line output, enter (1), to write output to a file, enter (2), for both, enter (3)")
        user_input = input()
    else:
        print("For command line output, enter (1), to write output to a file, enter (2), for both, enter (3)")
        user_input = input()

    if user_input.isdigit() == False:
        return main(True)

    if int(user_input) not in range(1,4):
        main(True)
    #the "meat" of the test case module
    print("Enter your custom search parameter:")
    custom_input = input()

    if int(user_input) == 1:
        for line in contents:
    #insert specific test case criteria here
            if custom_input in line:
                result += line
                linecounter += 1
        if len(result) < 5:
            print("No applicable log entries found.")
        else: print((result) + "mAUTHra has found " +str(linecounter) + " relevant results.\n")
    elif int(user_input) == 2:
        for line in contents:
    #insert specific test case criteria here
            if custom_input in line:
                result += line
                linecounter += 1
        if len(result) < 5:
            print("No applicable log entries found.")
        else:
    #file output section
            original_output = sys.stdout
            print("Enter a file name:")
            with open(input(), "x") as f:
                sys.stdout = f
                print((result) + "mAUTHra has found " +str(linecounter) + " relevant results.\n")
                sys.stdout = original_output
    elif int(user_input) == 3:
        for line in contents:
    #insert specific test case criteria here
            if custom_input in line:
                result += line
                linecounter += 1
        if len(result) < 5:
            print("No applicable log entries found.")
        else:
            original_output = sys.stdout
            print("Enter a file name:")
            with open(input(), "x") as f:
                sys.stdout = f
                print(result)
                sys.stdout = original_output
                print((result) + "mAUTHra has found " +str(linecounter) + " relevant results.\n")



#no touchy
if __name__ == "__main__":
    main(False)
