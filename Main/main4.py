#!/usr/bin/env python3

#all empty comments denote a area which must be modifed in order to add new test case modules

import sys
#from colorama import Fore, Style

#test case modules
#
import custom
import file_permissions
import incorrect_password
import logo
import newly_installed_programs
import password_change
import ssh
import sudo_usage
import users

error = False

def main(error):
    
#file input
    with open(sys.argv[1], 'r') as f:
        contents = f.readlines()
        
    if error == False:
#ascii art
        logo.main()
    else: print("Incorrect input!!!")

#success catcher list
    alls = ["all", "All", "ALL"]
    custom_list = ["custom", "Custom", "CUSTOM"]

#this print statement prompts the user to make a decision
#
    print("\nEnter a search parameter. (1) User account creation/deletion, (2) Incorrect password attempts, (3) Password Modifications (4) File permissions changes, (5) SSH activity, "
    "(6) New program installs, (7) Sudo usage\nTo search for custom input enter 'custom'\nTo search all test cases enter \'all\'.")

#this variable stores the user's test case specifier selection
    user_input = input()

    for elem in alls:
        if user_input == elem:
            #
            print("\n***The following log entries pertain to the creation/deletion of users***\n")
            users.main()
            print("***The following log entries pertain to incorrect password entries***\n")
            incorrect_password.main()
            print("***The following log entries pertain to the modification of passwords***\n")
            password_change.main()
            print("***The following log entries pertain to the modification of file permissions***\n")
            file_permissions.main()
            print("***The following log entries pertain to SSH activity***\n")
            ssh.main()
            print("***The following log entries pertain to newly installed programs***\n")
            newly_installed_programs.main()
            print("***The following log entries pertain to sudo usage***\n")
            sudo_usage.main()
            return None
            
    for elem in custom_list:
        if user_input == elem:
            return custom.main()
        
    if user_input.isdigit() == False:
        return main(True)
        #
    elif int(user_input) not in range(1, 8):
        return main(True)
    else:
        #spacing purposes
        print("\n")
        #this is where we call the test case import functions
        #
        if user_input == "1":
            users.main()
        elif user_input == "2":
            incorrect_password.main()
        elif user_input == "3":
            password_change.main()
        elif user_input == "4":
            file_permissions.main()
        elif user_input == "5":
            ssh.main()
        elif user_input == "6":
            newly_installed_programs.main()
        elif user_input == "7":
            sudo_usage.main()

#no touchy!
if __name__ == "__main__":
    main(False)