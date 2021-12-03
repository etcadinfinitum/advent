def get_input(filename):
    r = []
    with open (filename, 'r') as f:
        for l in f.readlines():
            a, b = l.split()
            r.append((a, int(b.strip())))
    return r

def first():
    r = get_input('data.txt')
    horizontal = vertical = 0
    for val in r:
        if val[0] == 'forward':
            horizontal += val[1]
        else:
            if val[0] == 'down':
                vertical += val[1]
            else:
                vertical -= val[1]
    return horizontal * vertical

def second():
    r = get_input('data.txt')
    horizontal = depth = aim = 0
    for val in r:
        if val[0] == 'forward':
            horizontal += val[1]
            depth += aim * val[1]
        else:
            if val[0] == 'down':
                aim += val[1]
            else:
                aim -= val[1]
    return horizontal * depth 
    

print(first())
print(second())
