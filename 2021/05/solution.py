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

def first():
    overlaps = set()
    pairs = get_input('data.txt')
    pairs = [x for x in pairs if x[0][0] == x[1][0] or x[0][1] == x[1][1]]
    overlaps = set()
    for i, p in enumerate(pairs):
        for j, compare in enumerate(pairs):
            if i == j: continue
            overlaps = overlaps.union(find_overlap(p, compare))
    return len(overlaps)

def find_overlap(seg_a, seg_b):
    a_pts = []
    if seg_a[0][0] == seg_a[1][0]:
        for i in range(min(seg_a[0][1], seg_a[1][1]), max(seg_a[0][1], seg_a[1][1]) + 1):
            a_pts.append((seg_a[0][0], i))
    elif seg_a[0][1] == seg_a[1][1]:
        for i in range(min(seg_a[0][0], seg_a[1][0]), max(seg_a[0][0], seg_a[1][0]) + 1):
            a_pts.append((i, seg_a[0][1]))
    else:
        offset = 1
        if seg_a[0][0] > seg_a[1][0]: offset = -1
        x = range(seg_a[0][0], seg_a[1][0] + offset, offset)
        offset = 1
        if seg_a[0][1] > seg_a[1][1]: offset = -1
        y = range(seg_a[0][0], seg_a[1][0] + offset, offset)
        a_pts.extend(zip(x, y))



    b_pts = []
    if seg_b[0][0] == seg_b[1][0]:
        for i in range(min(seg_b[0][1], seg_b[1][1]), max(seg_b[0][1], seg_b[1][1]) + 1):
            b_pts.append((seg_b[0][0], i))
    elif seg_b[0][1] == seg_b[1][1]:
        for i in range(min(seg_b[0][0], seg_b[1][0]), max(seg_b[0][0], seg_b[1][0]) + 1):
            b_pts.append((i, seg_b[0][1]))
    else:
        offset = 1
        if seg_b[0][0] > seg_b[1][0]: offset = -1
        x = range(seg_b[0][0], seg_b[1][0] + offset, offset)
        offset = 1
        if seg_b[0][1] > seg_b[1][1]: offset = -1
        y = range(seg_b[0][0], seg_b[1][0] + offset, offset)
        b_pts.extend(zip(x, y))
    return set(a_pts).intersection(set(b_pts))

def second():
    overlaps = set()
    pairs = get_input('data.txt')
    overlaps = set()
    for i, p in enumerate(pairs):
        for j, compare in enumerate(pairs):
            if i == j: continue
            overlaps = overlaps.union(find_overlap(p, compare))
    return len(overlaps)

print(first())
print(second())
