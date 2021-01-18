#!/usr/bin/env python3

#import modules corresponding to specific test case functions
#no ".py" necessary
#examples:
#import incorrect_password_checker
#import new_users_created
#import change_file_permissions

import sys
import tester_case1

def main():
    
#ascii art
    print("""
                               _   _   _ _____ _   _ 
                  _ __ ___    / \ | | | |_   _| | | |_ __ __ _
                 | '_ ` _ \  / _ \| | | | | | | |_| | '__/ _` |
                 | | | | | |/ ___ \ |_| | | | |  _  | | | (_| |
                 |_| |_| |_/_/   \_\___/  |_| |_| |_|_|  \__,_|
                MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
                MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
                MMMMMMMMNmmNMMMMMMMNMMMMMMMMNMMMMMMMMMMmmMMMMMMMMM
                MMMMMMMd....-:/oydNMNNmNdNmmMMMMdyo/:-...-NMMMMMMM
                MMMMMMMN.```.......-+yy:`.+hs+-.....`````-MMMMMMMM
                MMMMMMMMy`````....`````    `.``........``yMMMMMMMM
                MMMMMMMMMd/.```......-.```..-...`..`.../dMMMMMMMMM
                MMMMMMMMMMM/...-.-..``:.``..`....----sMMMMMMMMMMMM
                MMMMMMMMMMMs``....````s-:-++```.......yMMMMMMMMMMM
                MMMMMMMMMMMMm+-````..sh//-od-.``..``-yMMMMMMMMMMMM
                MMMMMMMMMMMMMMMmdhhmNMm+--yMNd+:/+sdMMMMMMMMMMMMMM
                MMMMMMMMMMMMMMMMMMMMMMMh:+NMMMMMMMMMMMMMMMMMMMMMMM
                MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
                MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\n\n\n""")

#this print statement prompts the user to make a decision
#must be modified with each new test case added
    print("Enter a search parameter. (1) New users created, (2) Incorrect password attempts, (3) File permissions changes")

#this variable stores the user's test case specifier selection
    user_input = input()

#error message for unapproved user selections
#must also be modified with each new test case to allow for proper 

#this is where we call the test case import functions
#make sure to indent once
    #if user_input == "1":
        #example_module.main()
    #if user_input == "2":
        #example2_module.main()
    if user_input == "1":
        tester_case1.main()














#allows the modular functionality we desire
#no touchy!
if __name__ == "__main__":
    main()
