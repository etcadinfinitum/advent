def first():
    count = last = -1
    with open('data.txt', 'r') as f:
        for line in [int(x.strip()) for x in f.readlines()]:
            if line > last:
                count += 1
            last = line
    return count

def second():
    count = last = -1
    with open('data.txt', 'r') as f:
        lines = [int(x.strip()) for x in f.readlines()]
        sums = [sum(lines[i:i+3]) for i in range(0, len(lines) - 2)]
        for s in sums:
            if s > last: count += 1
            last = s
    return count

print(first())
print(second())
