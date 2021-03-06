#!/usr/bin/env python*
# -*- coding: UTF-8 -*-

import math, sys
from decimal import *

def pi_to_nth(n):
    string_format = "%." + str(n) + "f"
    return (string_format % math.pi)

def shell():
    while True:
        print (">>> ", end='')
        entry = input()
        if entry == "quit":
            break
        else:
            print (pi_to_nth(int(entry)))

if __name__=='__main__':
	shell()
