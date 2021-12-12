def get_input(filename):
    data = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            data.append([int(char) for char in line.strip()])
    return data

def first():
    data = get_input('data.txt')
    flashed = 0
    for i in range(100):
        flashed += flash(data)
    return flashed

def flash(data):
    flashes = 0
    # increment everyone
    to_flash = set() # tuple of x, y
    for x, row in enumerate(data):
        for y, val in enumerate(row):
            data[x][y] += 1
            if data[x][y] > 9:
                to_flash.add((x, y))
    while len(to_flash) > 0:
        (x, y) = to_flash.pop()
        fill_surrounding(x, y, data, to_flash)
        data[x][y] = 0
        flashes += 1
    return flashes

def fill_surrounding(x, y, data, to_flash):
    surroundings = [(x + 1, y), (x + 1, y - 1), (x + 1, y + 1), (x, y - 1), (x, y + 1), (x - 1, y), (x - 1, y - 1), (x - 1, y + 1)]
    for (i, j) in surroundings:
        if i < 0 or i >= len(data) or j < 0 or j >= len(data[0]):
            continue
        if data[i][j] == 0:
            continue
        data[i][j] += 1
        if data[i][j] > 9:
            to_flash.add((i, j))

def second():
    data = get_input('data.txt')
    step = 1
    while True:
        flash(data)
        if all_flashed(data): return step
        step += 1
    

def all_flashed(data):
    for x in data:
        for y in x:
            if y != 0: return False
    return True

print(first())
print(second())
