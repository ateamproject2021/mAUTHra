#!/usr/bin/env python3
import sys

with open(sys.argv[1], 'r') as f:
	contents = f.readlines()
result_new_group = ""
result_incorrect_password = ""
result_chmod = ""

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

print("Enter a search parameter. (1) New users created, (2) Incorrect password attempts, (3) File permissions changes")
user_input = input()

if int(user_input) not in range(1,4):
    print("Invalid input, please try again.\nEnter a search parameter. (1) New users created, (2) Incorrect password attempts, (3) File permissions changes")
    user_input = input()

if user_input == "1":
    for line in contents:
        if "new group: " in line:
            result_new_group += line + "\n"
if user_input == "1":
    print(result_new_group)

if user_input == "2":
    for line in contents:
        if "incorrect password" in line:
            result_incorrect_password += line + "\n"
if user_input == "2":
    print(result_incorrect_password)

if user_input == "3":
    for line in contents:
        if "chmod" in line:
            if "+r" in line:
                new_line = line.replace("+r", "user added readability to this file >>>")
                result_chmod += new_line
            else: result_chmod += line
if user_input == "3":
    print(result_chmod)

print("Log entries pertaining to new users:\n"
        + result_new_group
        + "Log entries pertaining to failed passwords:\n"
        + result_incorrect_password
        + "Log entries pertaining to change of file permissions:\n"
        + result_chmod)
	
