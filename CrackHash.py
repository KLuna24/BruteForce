#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""

@author: Kevin Luna
GSU 4980

"""

import sys 
import time
import hashlib 

def brute_hash():

    # The passwords list in txt file
    with open('password.txt', 'r') as passwords:
        passwords_list = passwords.read().splitlines()

    # keeps track of the number of comparisons
    count = 0

    # store the string form of the salt.
    concat = ""

    # starts the timer.
    start = time.time()
    #checks to see if theres salt and stores string
    if len(sys.argv) == 3:
        for password in passwords_list:
            if hashlib.sha1(password).hexdigest() == sys.argv[2]:
                concat = str(password)
#concate salt after password
    for password in passwords_list:
        if hashlib.sha1(password + concat).hexdigest() == sys.argv[1]:
            end = time.time()
            print "Password:", str(password), "Attempts:", count, "Time it took:", str(end - start)
            quit()
        else:
            count += 1
#concate the salt before password and checks to see if passed hash matches
    for password in passwords_list:
        if hashlib.sha1(concat + password).hexdigest() == sys.argv[1]:
            end = time.time()
            print "Password:", str(password), "Attempts:", count, "Time it took:", str(end - start)
            quit()
        else:
            count += 1

    # Loop checks for all possible combinations
    for password in passwords_list:
        for secondPassword in passwords_list:
            if hashlib.sha1(password + ' ' + secondPassword).hexdigest() == sys.argv[1]:
                end = time.time()
                print "Password ", str(password), "Attempts: ", count, "Time it took: ", str(end - start)
                quit()
            else:
                count += 1
#If theres no hash print message
def main():

    if len(sys.argv) < 2:
        print("No hash no password go away...")
        quit()
    brute_hash()

main()
