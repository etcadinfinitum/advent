def get_input(filename):
    with open(filename, 'r') as f:
        return [int(x) for x in f.readline().split(',')]


def first():
    data = get_input('data.txt')
    upper = max(data)
    fuel = upper * len(data)
    for i in range(1, upper + 1):
        spent = sum([abs(i - x) for x in data])
        if spent < fuel: fuel = spent
    return fuel

def second():
    data = get_input('data.txt')
    upper = max(data)
    fuel = upper ** 2 * len(data)
    for i in range(1, upper + 1):
        spent = sum([(abs(i - x) ** 2 + abs(i - x)) / 2 for x in data])
        if spent < fuel: fuel = spent
    return fuel

print(first())
print(second())
