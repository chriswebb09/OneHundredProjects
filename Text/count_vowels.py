#!/usr/bin/env python*
# -*- coding: UTF-8 -*-

def count_vowels(string):
    vowels = ["a", "e", "i", "o", "u"]
    count = 0

    for letter in string:
        if letter in vowels:
            count += 1
    return count

if __name__ == '__main__':
    user_string = raw_input("Input string to check : ")
    check_string = count_vowels(user_string)
    print(check_string)
