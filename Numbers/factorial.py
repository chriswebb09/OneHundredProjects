#!/usr/bin/env python*
# -*- coding: UTF-8 -*-

def factorial(n):
    if not n:
        return 1
    return n * factorial(n - 1)

if __name__ == "__main__":
    print(factorial(4))
