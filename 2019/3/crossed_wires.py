#!/bin/env python3

'''
--- Day 3: Crossed Wires ---

The gravity assist was successful, and you're well on your way to the Venus refuelling station. During the rush back on Earth, the fuel management system wasn't completely installed, so that's next on the priority list.

Opening the front panel reveals a jumble of wires. Specifically, two wires are connected to a central port and extend outward on a grid. You trace the path each wire takes as it leaves the central port, one wire per line of text (your puzzle input).

The wires twist and turn, but the two wires occasionally cross paths. To fix the circuit, you need to find the intersection point closest to the central port. Because the wires are on a grid, use the Manhattan distance for this measurement. While the wires do technically cross right at the central port where they both start, this point does not count, nor does a wire count as crossing with itself.

For example, if the first wire's path is R8,U5,L5,D3, then starting from the central port (o), it goes right 8, up 5, left 5, and finally down 3:

...........
...........
...........
....+----+.
....|....|.
....|....|.
....|....|.
.........|.
.o-------+.
...........

Then, if the second wire's path is U7,R6,D4,L4, it goes up 7, right 6, down 4, and left 4:

...........
.+-----+...
.|.....|...
.|..+--X-+.
.|..|..|.|.
.|.-X--+.|.
.|..|....|.
.|.......|.
.o-------+.
...........

These wires cross at two locations (marked X), but the lower-left one is closer to the central port: its distance is 3 + 3 = 6.

Here are a few more examples:

    R75,D30,R83,U83,L12,D49,R71,U7,L72
    U62,R66,U55,R34,D71,R55,D58,R83 = distance 159
    R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51
    U98,R91,D20,R16,D67,R40,U7,R15,U6,R7 = distance 135

What is the Manhattan distance from the central port to the closest intersection?
'''
# strategy:
# for each R/L path in a wire, map the Y coord (constant) to an inclusive range of X values.
# do the same for the U/D paths in each wire.
# repeat this behavior for second path.
# create a set of tuples for crossed wire coordinates to choose from at the end.
# then:
#       iterate over the keyset for wire 1 R/L paths, getting a static Y value for each key.
#           handle parallel wires like so:
#               check for same Y key in wire 2 R/L paths
#               if present:
#                   check for overlap, get minimum overlapping X coord, add to coordinate set
#           handle perpendicular wires like so:
#               iterate over wire 2 U/D entries, getting static X value for wire 2:
#                   if wire 1 Y key is in the range of wire_2_ud[wire_2_x]:
#                       an intersection exists! add to coordinate set
#       repeat same logic for wire 2 R/L paths.
#       invert logic, and perform same analysis for wire 1 U/D and wire 2 U/D keys. (TODO: is this necessary?)
# for each item now in coordinate set:
#   get sum(abs_val(x), abs_val(y))
#   if sum is minimum of previously processed coordinates, update sum
# sum should be the minimum manhattan coordinates for crossed wires.

def walk_path_get_ranges(l):
    x = y = 0
    ud = {}
    lr = {}
    for item in l:
        dist = int(item[1:])
        # TODO: handle overlap between entries!? (not like, totally necessary...)
        if item[0] == 'U':
            # handle existing entr[ies] 
            ceil = y + dist
            if x in ud: ud[x].append((y, ceil))
            else: ud[x] = [(y, ceil)]
            y = ceil
        elif item[0] == 'D':
            floor = y - dist
            if x in ud: ud[x].append((floor, y))
            else: ud[x] = [(floor, y)]
            y = floor
        elif item[0] == 'R':
            ceil = x + dist
            if y in lr: lr[y].append((x, ceil))
            else: lr[y] = [(x, ceil)]
            x = ceil
        else:
            floor = x - dist
            if y in lr: lr[y].append((floor, x))
            else: lr[y] = [(floor, x)]
            x = floor
        print('(%d, %d) after new command %s' % (x, y, item))
    return ud, lr

def parallel_and_perpendicular(wire_1_lr, wire_2_lr, wire_2_ud):
    coordinates = []    # could be pairs of (x,y) or (y,x)
    # import pdb; pdb.set_trace()
    for y in wire_1_lr.keys():
        # parallel
        if y in wire_2_lr:
            for xpair_1 in wire_1_lr[y]:
                for xpair_2 in wire_2_lr[y]:
                    if xpair_2[0] <= xpair_1[0] <= xpair_2[1] and xpair_1[0] >= 0:
                        coordinates.append((xpair_1[0], y))
                    if xpair_1[0] <= xpair_2[0] <= xpair_1[1] and xpair_2[0] >= 0:
                        coordinates.append((xpair_2[0], y))
                    if xpair_2[0] <= xpair_1[1] <= xpair_2[1] and xpair_1[1] <= 0:
                        coordinates.append((xpair_1[1], y))
                    if xpair_1[0] <= xpair_2[1] <= xpair_1[1] and xpair_2[1] <= 0:
                        coordinates.append((xpair_2[1], y))
        # perpendicular
        for x in wire_2_ud.keys():
            for ypair in wire_2_ud[x]:
                for xpair in wire_1_lr[y]:
                    if ypair[0] <= y <= ypair[1] and xpair[0] <= x <= xpair[1]:
                        coordinates.append((x, y))
    return coordinates

def crossed_wires():
    paths = []
    with open('data.txt', 'r') as f:
        for l in f.readlines():
            paths.append(l)
    wire_1_paths = paths[0].split(',')
    wire_2_paths = paths[1].split(',')
    # strategy:
    # for each R/L path in a wire, map the Y coord (constant) to an inclusive range of X values.
    # do the same for the U/D paths in each wire.
    # repeat this behavior for second path.
    wire_1_ud, wire_1_lr = walk_path_get_ranges(wire_1_paths)
    wire_2_ud, wire_2_lr = walk_path_get_ranges(wire_2_paths)
    # create a set of tuples for crossed wire coordinates to choose from at the end.
    coordinates = set()
    # then:
    #       iterate over the keyset for wire 1 R/L paths, getting a static Y value for each key.
    #           handle parallel wires like so:
    #               check for same Y key in wire 2 R/L paths
    #               if present:
    #                   check for overlap, get minimum overlapping X coord, add to coordinate set
    #           handle perpendicular wires like so:
    #               iterate over wire 2 U/D entries, getting static X value for wire 2:
    #                   if wire 1 Y key is in the range of wire_2_ud[wire_2_x]:
    #                       an intersection exists! add to coordinate set
    y_keypairs = parallel_and_perpendicular(wire_1_lr, wire_2_lr, wire_2_ud)
    for y_x in y_keypairs:
        coordinates.add((y_x[1], y_x[0]))
    #       repeat same logic for wire 2 R/L paths.
    y_keypairs = parallel_and_perpendicular(wire_2_lr, wire_1_lr, wire_1_ud)
    for y_x in y_keypairs:
        coordinates.add((y_x[1], y_x[0]))
    #       invert logic, and perform same analysis for wire 1 U/D and wire 2 U/D keys. (TODO: is this necessary?)
    x_keypairs = parallel_and_perpendicular(wire_1_ud, wire_2_ud, wire_2_lr)
    for x_y in x_keypairs:
        coordinates.add(x_y)
    x_keypairs = parallel_and_perpendicular(wire_2_ud, wire_1_ud, wire_1_lr)
    for x_y in x_keypairs:
        coordinates.add(x_y)
    # for each item now in coordinate set:
    #   get sum(abs_val(x), abs_val(y))
    #   if sum is minimum of previously processed coordinates, update sum
    result = None
    for pair in coordinates:
        # print(str(pair))
        dist = abs(pair[0]) + abs(pair[1])
        if dist and (result is None or dist < result):
            print('Current result is %s; new min is %d because of coordinate pair %s' % (str(result), dist, str(pair)))
            result = dist
    # sum should be the minimum manhattan coordinates for crossed wires.
    print('Closest intersection to origin is %d' % result)
    return coordinates

if __name__=='__main__':
    crossed_wires()
