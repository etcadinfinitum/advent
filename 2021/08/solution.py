def get_input(filename):
    data = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            i, output = line.split('|')
            data.append((i.strip().split(), output.strip().split()))
    return data

def first():
    data = get_input('data.txt')
    count = 0
    for l in data:
        for digit in l[1]:
            if len(digit) in [2, 3, 4, 7]:
                count += 1
    return count

def second():
    data = get_input('data.txt')
    count = 0
    for f in data:
        nums = get_configuration(f[0])
        output = f[1]
        value = 0
        for i, d in enumerate(output):
            num = nums[tuple(sorted([c for c in d]))]
            value += num * (10 ** (len(output) - 1 - i))
        count += value
    return count

def get_configuration(full):
    two_five_three = []
    six_nine_zero = []
    one = four = seven = eight = two = five = three = six = nine = zero = ''
    for num in full:
        if len(num) == 2:
            one = num
        elif len(num) == 7:
            eight = num
        elif len(num) == 5:
            two_five_three.append(num)
        elif len(num) == 4:
            four = num
        elif len(num) == 3:
            seven = num
        else:
            six_nine_zero.append(num)

    # sanity check
    if one == '' or four == '' or seven == '' or eight == '':
        raise ValueError('benchmark values are not available! benchmarks are one=%s, four=%s, seven=%s, eight=%s' % (one, four, seven, eight))
    if len(six_nine_zero) != 3 or len(two_five_three) != 3:
        raise ValueError('incorrect parsing of duped number groups! groups are two_five_three=%s, six_nine_zero=%s' % (str(two_five_three), str(six_nine_zero)))

    # 6, 9, 0
    for item in six_nine_zero:
        # union of 6 and 7 gets full 7 segments, no other combo does
        res = set([c for c in item]) | set([c for c in seven])
        if len(res) == 7:
            six = item
            six_nine_zero.remove(item)
    if len(six_nine_zero) == 3: raise ValueError('incorrect parsing of six')
    for item in six_nine_zero:
        # similarly, union of 4 and nine produces only 6 segments, both other candidates would produce 7 segments
        res = set([c for c in four]) | set([c for c in item])
        if len(res) == 6:
            nine = item
            six_nine_zero.remove(item)
    if len(six_nine_zero) > 1: raise ValueError('incorrect parsing of nine')
    zero = six_nine_zero[0]
    # 2, 5, 3
    # union of 2 members and 4 members gets full 7 segments, neither other option does
    for item in two_five_three:
        res = set([c for c in item]) | set([c for c in four])
        if len(res) == 7:
            two = item
            two_five_three.remove(item)
            break
    if two == '': raise ValueError('incorrect parsing of two')
    for item in two_five_three:
        # union of 2 and 5 produces all seven segments, whereas 2 and 3 only produce 6
        res = set([c for c in item]) | set([c for c in two])
        if len(res) == 7: five = item
        elif len(res) == 6: three = item
    return { tuple(sorted([c for c in zero])): 0,
             tuple(sorted([c for c in one])): 1,
             tuple(sorted([c for c in two])): 2,
             tuple(sorted([c for c in three])): 3,
             tuple(sorted([c for c in four])): 4,
             tuple(sorted([c for c in five])): 5,
             tuple(sorted([c for c in six])): 6,
             tuple(sorted([c for c in seven])): 7,
             tuple(sorted([c for c in eight])): 8,
             tuple(sorted([c for c in nine])): 9 }

print(first())
print(second())
