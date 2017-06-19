#!/usr/bin/env python*
# -*- coding: UTF-8 -*-

def word_count(string):
    return len(string.split())

def shell():
    while True:
        print (">>> ", end='')
        entry = input()
        if entry == "quit":
            break
        else:
            print (word_count("new five hello"))

if __name__=='__main__':
	shell()
