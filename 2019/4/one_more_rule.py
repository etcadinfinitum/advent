#!/bin/env python3

# Part II
# https://adventofcode.com/2019/day/4

from enumerate_passwords import get_bounds, get_passwords

def is_more_valid(i):
    n = str(i)
    twos_only = False
    if n[0] > n[1] or n[1] > n[2]: return False
    for i in range(2, len(n) - 1):
        if n[i + 1] < n[i]: return False
        if twos_only: continue
        if n[i] == n[i - 1] and n[i + 1] != n[i] and n[i - 2] != n[i]: twos_only = True
    if not twos_only and n[4] == n[5] and n[3] < n[4]: twos_only = True
    if not twos_only and n[0] == n[1] and n[1] < n[2]: twos_only = True
    # if twos_only: print(n)
    return twos_only

if __name__=='__main__':
    print(get_passwords(is_more_valid))
