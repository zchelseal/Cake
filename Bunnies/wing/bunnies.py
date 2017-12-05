def answer(maze):
    h = len(maze)
    w = len(maze[0])

    d = [[[10 ** 7, 10 ** 7] for x in range(w)] for y in range(h)]

    v = [[0 for x in range(w)] for y in range(h)]
    stack = []
    dist = 10 ** 7
    stack.append(((0, 0), 1))

    while stack:
        p = stack.pop()
        r, c = 0, 0
        r = p[0][0]
        c = p[0][1]
        v[r][c] = 1

        d[r][c][0] = min(d[r][c][0], p[1])

        if c - 1 >= 0:  # left
            if v[r][c - 1] == 0 and maze[r][c - 1] == 0:
                stack.append(((r, c - 1), p[1] + 1))
        if c + 1 < w:  # right
            if v[r][c + 1] == 0 and maze[r][c + 1] == 0:
                stack.append(((r, c + 1), p[1] + 1))
        if r - 1 >= 0:  # top
            if v[r - 1][c] == 0 and maze[r - 1][c] == 0:
                stack.append(((r - 1, c), p[1] + 1))
        if r + 1 < h:  # bottom
            if v[r + 1][c] == 0 and maze[r + 1][c] == 0:
                stack.append(((r + 1, c), p[1] + 1))

    v = [[0 for x in range(w)] for y in range(h)]
    stack = []
    stack.append(((h - 1, w - 1), 1))

    while stack:
        p = stack.pop()
        r, c = 0, 0
        r = p[0][0]
        c = p[0][1]
        v[r][c] = 1

        d[r][c][1] = min(d[r][c][1], p[1])

        if c - 1 >= 0:  # left
            if v[r][c - 1] == 0 and maze[r][c - 1] == 0:
                stack.append(((r, c - 1), p[1] + 1))
        if c + 1 < w:  # right
            if v[r][c + 1] == 0 and maze[r][c + 1] == 0:
                stack.append(((r, c + 1), p[1] + 1))
        if r - 1 >= 0:  # top
            if v[r - 1][c] == 0 and maze[r - 1][c] == 0:
                stack.append(((r - 1, c), p[1] + 1))
        if r + 1 < h:  # bottom
            if v[r + 1][c] == 0 and maze[r + 1][c] == 0:
                stack.append(((r + 1, c), p[1] + 1))

    i, j = 0, 0

    #for i in d:
        #print(i)

    dist = d[0][0][1]

    while i < h:
        j = 0
        while j < w:
            if maze[i][j]:
                if i - 1 >= 0 and i + 1 < h and maze[i - 1][j] == 0 and maze[i + 1][j] == 0:
                    # top-bottom
                    dist = min(dist, d[i - 1][j][0] + d[i + 1][j][1] + 1)
                    # bottom-top
                    dist = min(dist, d[i - 1][j][1] + d[i + 1][j][0] + 1)
                if j - 1 >= 0 and j + 1 < w and maze[i][j - 1] == 0 and maze[i][j + 1] == 0:
                    # left-right
                    dist = min(dist, d[i][j - 1][0] + d[i][j + 1][1] + 1)
                    # right-left
                    dist = min(dist, d[i][j - 1][1] + d[i][j + 1][0] + 1)
                if j - 1 >= 0 and i + 1 < h:
                    # turn-right-bottom
                    dist = min(dist, d[i][j - 1][0] + d[i + 1][j][1] + 1)
                    dist = min(dist, d[i][j - 1][1] + d[i + 1][j][0] + 1)
                if j - 1 >= 0 and i - 1 >= 0:
                    # turn-left-top
                    dist = min(dist, d[i][j - 1][0] + d[i - 1][j][1] + 1)
                    dist = min(dist, d[i][j - 1][1] + d[i - 1][j][0] + 1)
                if j + 1 < w and i + 1 < h:
                    # turn-right-bottom
                    dist = min(dist, d[i][j + 1][0] + d[i + 1][j][1] + 1)
                    dist = min(dist, d[i][j + 1][1] + d[i + 1][j][0] + 1)
                if j + 1 < w and i - 1 >= 0:
                    # turn-left-top
                    dist = min(dist, d[i][j + 1][0] + d[i - 1][j][1] + 1)
                    dist = min(dist, d[i][j + 1][1] + d[i - 1][j][0] + 1)
            j += 1
        i += 1

    return dist


a = answer([
    [0,0,0,0,0],
    [1,0,1,1,0],
    [0,0,1,1,0],
    [0,1,1,0,1],
    [0,1,0,0,0],
    [0,0,0,1,0]
])
pass