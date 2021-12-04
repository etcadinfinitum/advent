def get_input(filename):
    with open(filename, 'r') as f:
        return [int(l.strip(), 2) for l in f.readlines()]

def first():
    nums = get_input('data.txt')
    counts = {exp: 0 for exp in range(0, 12)}
    for n in nums:
        for exp in range(0, 12):
            counts[exp] += ((n & (2 ** exp)) > 0)
    gamma = sum([(v > len(nums) / 2) * (2 ** k) for k, v in counts.items()])
    epsilon = 2**12 - 1 - gamma
    return gamma * epsilon

def second():
    data = []
    with open('data.txt', 'r') as f:
        data = [l.strip() for l in f.readlines()]
    co2 = oxygen = data

    idx = 0
    res = ''
    while len(co2) > 1:
        if len(co2) < 1:
            raise ValueError('eliminated all possibilities!')
        count = sum([1 for x in co2 if x[idx] == '1'])
        if count * 2 < len(co2): res += '1'
        else: res += '0'
        co2 = [x for x in co2 if x.startswith(res)]
        idx += 1

    idx = 0
    res = ''
    while len(oxygen) > 1:
        if len(oxygen) < 1:
            raise ValueError('eliminated all possibilities!')
        count = sum([1 for x in oxygen if x[idx] == '1'])
        if count * 2 >= len(oxygen): res += '1'
        else: res += '0'
        oxygen = [x for x in oxygen if x.startswith(res)]
        idx += 1

    return int(co2[0], 2) * int(oxygen[0], 2)

    '''
    nums = get_input('data.txt')
    co2 = nums
    exp = 11
    partition = 0
    while len(co2) > 1:
        if len(co2) < 1:
            raise ValueError('eliminated all possibilities!')
        if exp < 0:
            print('partition', partition)
            print(co2)
            raise ValueError('did not eliminate enough possiblities!')
        count = sum([(x & (2 ** exp)) > 0 for x in co2])
        if count * 2 < len(co2):
            partition |= 2**exp
        window = 2**12 - 2**exp
        co2 = [x for x in co2 if ((window & x) ^ partition) > 0]
        exp -= 1
        print(exp)
    print(co2)

    oxygen = nums
    # TODO
    # return sum(co2) * sum(oxygen)
    pass
    '''

print(first())
print(second())
