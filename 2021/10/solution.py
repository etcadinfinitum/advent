def get_input(filename):
    with open(filename, 'r') as f:
        return [x.strip() for x in f.readlines()]

def first():
    data = get_input('data.txt')
    illegal_char_values = { ')': 3, ']': 57, '}': 1197, '>': 25137 }
    illegal_char_counts = { ')': 0, ']': 0, '}': 0, '>': 0 }
    for line in data:
        char = resolve_stack(line)
        if not char: continue
        else: illegal_char_counts[char] += 1
    total = 0
    for char in illegal_char_values:
        total += illegal_char_values[char] * illegal_char_counts[char]
    return total

def resolve_stack(line, want_stack: bool = False):
    matches = { '(': ')', '{': '}', '[': ']', '<': '>' }
    stack = []
    for char in line:
        if char in '([{<':
            stack.append(char)
        else:
            if len(stack) == 0: return None if want_stack else char
            match = stack.pop()
            if matches[match] != char: return None if want_stack else char
    if want_stack: return stack
    return None

def second():
    data = get_input('data.txt')
    matches = { '(': ')', '{': '}', '[': ']', '<': '>' }
    fixer_char_values = { ')': 1, ']': 2, '}': 3, '>': 4 }
    fixed_scores = []
    for line in data:
        remaining = resolve_stack(line, True)
        if not remaining: continue
        score = 0
        while len(remaining) > 0:
            char = remaining.pop()
            score *= 5
            fixer_char = matches[char]
            score += fixer_char_values[fixer_char]
        fixed_scores.append(score)
    idx = len(fixed_scores) // 2
    return sorted(fixed_scores)[idx]

print(first())
print(second())
