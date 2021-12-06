def get_input(filename):
    with open(filename, 'r') as f:
        d = f.readline()
        return [int(x) for x in d.split(',')]

def better_fish(data):
    fish = {x: 0 for x in range(0, 9)}
    for d in data:
        fish[d] += 1
    print(fish)
    return fish

def first():
    fish = get_input('data.txt')
    for day in range(0, 80):
        new = 0
        for i, f in enumerate(fish):
            if f == 0:
                fish[i] = 6
                new += 1
            else:
                fish[i] = f - 1
        fish.extend([8] * new)
    return len(fish)

def first_again():
    data = get_input('data.txt')
    fish = better_fish(data)
    for i in range(0, 80):
        newgen = fish[0]
        for j in range(0, 8):
            fish[j] = fish[j + 1]
        fish[8] = newgen
        fish[6] = fish[6] + newgen
    return sum([fish[x] for x in range(0, 9)])

def second():
    data = get_input('data.txt')
    fish = better_fish(data)
    for i in range(0, 256):
        newgen = fish[0]
        for j in range(0, 8):
            fish[j] = fish[j + 1]
        fish[8] = newgen
        fish[6] = fish[6] + newgen
    return sum([fish[x] for x in range(0, 9)])


print(first())
print(first_again())
print(second())
