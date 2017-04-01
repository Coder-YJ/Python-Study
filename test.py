# -*- coding: utf-8 -*-
def calc(number):
    sum = 0
    n = 0
    while n < number:
            sum = sum + n*n
            n = n + 1
    return sum

def power(x,n):
    sum = 1
    i = 0
    while i < n:
        sum = sum*x
        i = i + 1
    return sum