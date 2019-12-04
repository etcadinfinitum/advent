#!/bin/env python3

'''
--- Part Two ---

It turns out that this circuit is very timing-sensitive; you actually need to minimize the signal delay.

To do this, calculate the number of steps each wire takes to reach each intersection; choose the intersection where the sum of both wires' steps is lowest. If a wire visits a position on the grid multiple times, use the steps value from the first time it visits that position when calculating the total value of a specific intersection.

The number of steps a wire takes is the total number of grid squares the wire has entered to get to that location, including the intersection being considered. Again consider the example from above:

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

In the above example, the intersection closest to the central port is reached after 8+5+5+2 = 20 steps by the first wire and 7+6+4+3 = 20 steps by the second wire for a total of 20+20 = 40 steps.

However, the top-right intersection is better: the first wire takes only 8+5+2 = 15 and the second wire takes only 7+6+2 = 15, a total of 15+15 = 30 steps.

Here are the best steps for the extra examples from above:

    R75,D30,R83,U83,L12,D49,R71,U7,L72
    U62,R66,U55,R34,D71,R55,D58,R83 = 610 steps
    R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51
    U98,R91,D20,R16,D67,R40,U7,R15,U6,R7 = 410 steps

What is the fewest combined steps the wires must take to reach an intersection?

'''

from crossed_wires import *

def get_corner(x, y, turn):
    dist = int(turn[1:])
    if turn[0] == 'U':
        return dist, x, y + dist
    elif turn[0] == 'D':
        return dist, x, y - dist
    elif turn[0] == 'R':
        return dist, x + dist, y
    return dist, x - dist, y

def get_signal_delay():
    paths, intersection_points = crossed_wires()
    wire_1_paths = paths[0].split(',')
    wire_2_paths = paths[1].split(',')
    signal_cost = { pair: (None, None) for pair in intersection_points }
    # where wire crosses identified points, track the sum for that wire
    # do wire 1 pathsum first
    x = 0
    y = 0
    path = 0
    for item in wire_1_paths:
        dist, new_x, new_y = get_corner(x, y, item)
        for intersection in signal_cost.keys():
            if min(x, new_x) <= intersection[0] <= max(x, new_x) and min(y, new_y) <= intersection[1] <= max(y, new_y) and not signal_cost[intersection][0]:
                signal_cost[intersection] = (path + abs(intersection[0] - x) + abs(intersection[1] - y), signal_cost[intersection][1])
        x = new_x
        y = new_y
        path += dist
    # do wire 2 pathsum
    x = 0
    y = 0
    path = 0
    for item in wire_2_paths:
        dist, new_x, new_y = get_corner(x, y, item)
        for intersection in signal_cost.keys():
            if min(x, new_x) <= intersection[0] <= max(x, new_x) and min(y, new_y) <= intersection[1] <= max(y, new_y) and not signal_cost[intersection][1]:
                signal_cost[intersection] = (signal_cost[intersection][0], path + abs(intersection[0] - x) + abs(intersection[1] - y))
        x = new_x
        y = new_y
        path += dist
    # now find sums and min thereof
    result = None
    for intersection in signal_cost.keys():
        if signal_cost[intersection][0] and signal_cost[intersection][1]:
            r = signal_cost[intersection][0] + signal_cost[intersection][1]
            if (not result and r) or (r and r < result): result = r
    print('Lowest signal propogation cost is %s' % str(result))
    return result

if __name__=='__main__':
    get_signal_delay()
