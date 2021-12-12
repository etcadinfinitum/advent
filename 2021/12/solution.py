class Graph:
    def __init__(self):
        self.neighbors = {}
    def add(self, start, end):
        if start in self.neighbors:
            self.neighbors[start].add(end)
        else:
            self.neighbors[start] = set([end])
        if end in self.neighbors:
            self.neighbors[end].add(start)
        else:
            self.neighbors[end] = set([start])
    def __getitem__(self, key):
        return self.neighbors[key] 
    def __str__(self):
        return str(self.neighbors)

def get_input(filename):
    g = Graph()
    with open(filename, 'r') as f:
        for line in f.readlines():
            (start, end) = line.strip().split('-')
            g.add(start, end)
    return g

def first():
    graph = get_input('data.txt')
    paths = []
    dfs('start', [], paths, graph)
    return len(paths)

def dfs(current, path, paths, graph):
    try:
        path.index(current)
        if current == current.lower(): return
    except ValueError:
        pass
    path.append(current)
    if current == 'end': paths.append(path)
    for next_item in graph[current]:
        new_path = path.copy()
        dfs(next_item, new_path, paths, graph)

def second():
    graph = get_input('data.txt')
    paths = []
    dfs_allows_doubles('start', [], paths, graph)
    return len(paths)

def is_allowable_with_2_visits(path, new_item):
    if new_item.upper() == new_item:
        return True
    # all lowercase from here on out
    visits = {}
    for item in path:
        if item.upper() == item:
            continue    # We don't care about uppercase anything
        if item in visits:
            visits[item] += 1
        else:
            visits[item] = 1
    if new_item not in visits: return True
    if new_item in visits and (new_item == 'start' or new_item == 'end'): return False
    for item in visits:
        if visits[item] > 1: return False
    return True

def dfs_allows_doubles(current, path, paths, graph):
    if not is_allowable_with_2_visits(path, current): return
    path.append(current)
    if current == 'end': paths.append(path)
    for next_item in graph[current]:
        new_path = path.copy()
        dfs_allows_doubles(next_item, new_path, paths, graph)


print(first())
print(second())
