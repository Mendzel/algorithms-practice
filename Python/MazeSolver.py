directions = [
    [-1, 0],
    [1, 0],
    [0, 1],
    [0, -1]
]

def solve(maze, wall, start, end):
    seen = []
    path = []
    rowLength = len(maze[0])
    for i in range(len(maze)):
        seen.append([])
        for j in range(rowLength):
            seen[i].append(False)


    walk(maze, wall, start, end, seen, path)
    return path

def walk(maze, wall, curr, end, seen, path):
    #Base Cases
    if curr['x'] < 0 or curr['x'] >= len(maze[0]) or curr['y'] < 0 or curr['y'] >= len(maze):
        return False
    if maze[curr['y']][curr['x']] == wall:
        return False
    if curr['x'] == end['x'] and curr['y'] == end['y']:
        path.append(end)
        return True
    if seen[curr['y']][curr['x']]:
        return False
    
    #Recursion
    #pre
    seen[curr['y']][curr['x']] = True
    path.append(curr)

    #recurse
    for dir in directions:
        [x, y] = dir
        newCurr = {
            'x': curr['x'] + x,
            'y': curr['y'] + y,
        }
        if walk(maze, wall, newCurr, end, seen, path):
            return True

    #post
    path.pop()
    return False



maze1 = [
    "#####E#####",
    "#       ###",
    "##S########",
]

print(solve(maze1, '#', {'x': 2, 'y': 2}, {'x': 5, 'y':0}))