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
    

print(first())
