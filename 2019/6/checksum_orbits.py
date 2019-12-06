#!/bin/env python3

# Part I
# https://adventofcode.com/2019/day/6

def build_tree():
    paths = {}
    with open('data.txt', 'r') as f:
        for line in f.readlines():
            inner, outer = line.strip().split(')')
            if inner not in paths:
                paths[inner] = [outer]
            else:
                paths[inner].append(outer)
    return paths

def checksum():
    paths = build_tree()
    if 'COM' not in paths: return 0
    return count_orbits(paths, 'COM', 0)

def count_orbits(paths, key, dist):
    if key not in paths: return dist
    return dist + sum([count_orbits(paths, k, dist + 1) for k in paths[key]])

if __name__=='__main__':
    print(checksum())
