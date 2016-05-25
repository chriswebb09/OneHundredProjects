#!/usr/bin/env python*
# -*- coding: UTF-8 -*-

def is_palindrome(new_string):
    if new_string[::-1] == new_string:
        return "{} confirmed as palindrome".format(new_string)
    else:
        return "{} is not a palindrome".format(new_string)

if __name__ == "__main__":
    user_string = raw_input("Input string to check : ")
    check_string = is_palindrome(user_string)
    print check_string
