def get_input(filename):
    data = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            data.append([int(c) for c in line.strip()])
    return data

def first():
    data = get_input('data.txt')
    lows = []
    for i, a in enumerate(data):
        for j, b in enumerate(a):
            up = 10 if i == 0 else data[i - 1][j]
            down = 10 if i == len(data) - 1 else data[i + 1][j]
            left = 10 if j == 0 else data[i][j - 1]
            right = 10 if j == len(a) - 1 else data[i][j + 1]
            if up > b and down > b and left > b and right > b:
                lows.append(b)
    return sum(lows) + len(lows)


def second():
    data = get_input('data.txt')    
    lows = []
    for i, a in enumerate(data):
        for j, b in enumerate(a):
            up = 10 if i == 0 else data[i - 1][j]
            down = 10 if i == len(data) - 1 else data[i + 1][j]
            left = 10 if j == 0 else data[i][j - 1]
            right = 10 if j == len(a) - 1 else data[i][j + 1]
            if up > b and down > b and left > b and right > b:
                lows.append((i, j))
    basin_sizes = []
    for (x, y) in lows:
        visited = [[0 for _ in data[0]] for _ in data]
        basin = find_basin(x, y, data, visited)
        basin_size = 0
        for i, row in enumerate(basin):
            for j, col in enumerate(row):
                basin_size += basin[i][j]
        basin_sizes.append(basin_size)
    sorted_basins = sorted(basin_sizes)
    total = 1
    for i in sorted_basins[-3:]:
        total *= i
    return total

def find_basin(x, y, data, visited):
    if x < 0 or x >= len(data) or y < 0 or y >= len(data[0]):
        return visited
    if visited[x][y] == 1 or data[x][y] == 9:
        return visited
    visited[x][y] = 1
    visited = find_basin(x + 1, y, data, visited)
    visited = find_basin(x - 1, y, data, visited)
    visited = find_basin(x, y + 1, data, visited)
    visited = find_basin(x, y - 1, data, visited)
    return visited

print(first())
print(second())
