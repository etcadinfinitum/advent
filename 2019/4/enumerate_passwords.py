#!/bin/env python3

# Part I
# https://adventofcode.com/2019/day/4

def get_bounds():
    with open('data.txt', 'r') as f:
        return int(f.readline()), int(f.readline())

def get_passwords(f):
    lower, upper = get_bounds()
    count = 0
    for i in range(lower, upper + 1):
        if f(i):
            count += 1
    return count

def is_valid(i):
    i = str(i)
    double = False
    for idx in range(len(i) - 1):
        if i[idx + 1] < i[idx]: return False
        if i[idx] == i[idx + 1]: double = True
    return double

if __name__=='__main__':
    print(get_passwords(is_valid))
