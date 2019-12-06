#!/bin/env python3

# Part II
# https://adventofcode.com/2019/day/6

from checksum_orbits import build_tree

def invert_tree():
    paths = build_tree()
    inverted = {}
    for inner in paths.keys():
        for outer in paths[inner]:
            # every object in space is in orbit around 
            # exactly one other object
            inverted[outer] = inner
    return inverted

def get_path_to_com(paths, target):
    path = []
    curr = target
    while curr in paths:
        path.append(curr)
        curr = paths[curr]
    return path

def find_common_path():
    paths = invert_tree()
    # we only care about the object SANTA is orbiting; he could feasibly 
    # be an ancestor in the tree relative to YOU
    santa = get_path_to_com(paths, 'SAN')[1:]
    you = get_path_to_com(paths, 'YOU')
    result = None
    for obj in santa:
        if obj in you:
            r = santa.index(obj) + you.index(obj)
            if not result or r < result:
                result = r
    # remove common parent duplicate occurence
    return result - 1

if __name__=='__main__':
    print(find_common_path())
