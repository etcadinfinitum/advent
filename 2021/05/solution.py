def get_input(filename):
    pairs = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            content = line.split()
            p1 = content[0].split(',')
            p2 = content[2].split(',')
            pairs.append(
                         (
                          (int(p1[0]), int(p1[1])),
                          (int(p2[0]), int(p2[1]))
                         ))
    return pairs

######### Reworking for efficiency ###########
# Use a sparse array with one iteration over dataset instead of
# brute forcing by iterating twice (expensive operation).

def get_presence_pairs(segment):
    (x_a, y_a) = segment[0]
    (x_b, y_b) = segment[1]
    if x_a == x_b:
        return set((x_a, i) for i in range(min(y_a, y_b), max(y_a, y_b) + 1))
    if y_a == y_b:
        return set((i, y_a) for i in range(min(x_a, x_b), max(x_a, x_b) + 1))
    # diagonals
    offset_x = offset_y = 1
    if x_a > x_b: offset_x = -1
    if y_a > y_b: offset_y = -1
    x = range(x_a, x_b + offset_x, offset_x)
    y = range(y_a, y_b + offset_y, offset_y)
    return zip(x, y)

def first_again():
    data = get_input('data.txt')
    data = [x for x in data if x[0][0] == x[1][0] or x[0][1] == x[1][1]]
    sparse = {}
    for line in data:
        presences = get_presence_pairs(line)
        for new_pair in presences:
            if new_pair in sparse:
                sparse[new_pair] += 1
            else: sparse[new_pair] = 1
    count = 0
    for overlaps in sparse.values():
        if overlaps > 1: count += 1
    return count

def second_again():
    data = get_input('data.txt')
    sparse = {}
    for line in data:
        presences = get_presence_pairs(line)
        for new_pair in presences:
            if new_pair in sparse:
                sparse[new_pair] += 1
            else: sparse[new_pair] = 1
    count = 0
    for overlaps in sparse.values():
        if overlaps > 1: count += 1
    return count


print(first_again())
print(second_again())
