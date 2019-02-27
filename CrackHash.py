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
    
    with open('password.txt', 'r') as passwords:
        passwords_list = passwords.read().splitlines()

    
    count = 0

   
    concat = ""

   
    start = time.time()
   
    if len(sys.argv) == 3:
        for password in passwords_list:
            if hashlib.sha1(password).hexdigest() == sys.argv[2]:
                concat = str(password)

    for password in passwords_list:
        if hashlib.sha1(password + concat).hexdigest() == sys.argv[1]:
            end = time.time()
            print "Password:", str(password), "Attempts:", count, "Time it took:", str(end - start)
            quit()
        else:
            count += 1

    for password in passwords_list:
        if hashlib.sha1(concat + password).hexdigest() == sys.argv[1]:
            end = time.time()
            print "Password:", str(password), "Attempts:", count, "Time it took:", str(end - start)
            quit()
        else:
            count += 1

   
    for password in passwords_list:
        for secondPassword in passwords_list:
            if hashlib.sha1(password + ' ' + secondPassword).hexdigest() == sys.argv[1]:
                end = time.time()
                print "Password ", str(password), "Attempts: ", count, "Time it took: ", str(end - start)
                quit()
            else:
                count += 1

def main():

    if len(sys.argv) < 2:
        print("No hash no password go away...")
        quit()
    brute_hash()

main()
