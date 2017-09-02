class Vertex:   # store these in a matrix
    def __init__(self, x, y, path_wall, path_nowall):
        self.x = x
        self.y = y
        self.path_wall = path_wall
        self.path_nowall = path_nowall

MAX = [-1] * 401    # upper bound on the path length

def answer(maze):
    # base cases
    h = len(maze)
    if h < 1:
        return 0
    w = len(maze[0])
    if w < 1:
        return 0
    maze_paths = [[Vertex(j, i, None, None) for j in range(w)] for i in range(h)]

    x = 0
    y = 0
    maze_paths[y][x].path_nowall = [(x,y)]      # path_no_wall should never be none
    maze_paths[y][x].path_wall = None            # to show there hasn't been a wall yet
    nbours = neighbours(x, y, w, h, maze, maze_paths)
    while nbours != []:
        lst_nextlvl = []
        for nbour in nbours:
            x = nbour[0]
            y = nbour[1]
            if (x, y) == (w - 1, h - 1):    # reached bottom-right corner
                break
            if (x, y) == (1, 0):    # reached bottom-right corner
                pass    # for debugging
            L = neighbours(x, y, w, h, maze, maze_paths)
            lst_nextlvl.extend([l for l in L if l not in lst_nextlvl])
        nbours = lst_nextlvl

    # check 2 nodes closest to bottom-right corner FIXME
    # check last node?
    last_v = maze_paths[h-1][w-1]
    if last_v.path_nowall is None:
        return len(last_v.path_wall)
    elif last_v.path_wall is None:
        return len(last_v.path_nowall)
    else:
        return min(len(last_v.path_wall),len(last_v.path_nowall))

"""
    lengths = []
    for c in nbours:
        v = map_paths[c[1]][c[0]]
        lengths.append(len(v.path_nowall))
        lengths.append(len(v.path_wall))

    return min(lengths)
"""

"""
def copy_map(h, w):
    return [[Vertex(j, i, None, None) for j in range(w)] for i in range(h)]
"""

def neighbours(x, y, w, h, maze, maze_paths):
    # need x, y, path_nowall, path_wall from v
    v = maze_paths[y][x]
    parent_nw = v.path_nowall
    parent_w = v.path_wall

    L = [top(x,y), left(x,y), bottom(x,y,h), right(x,y,w)]
    nbours = []
    for c in L:     # c is a coordinate (i,j)
        if c is None:  # already visited in both paths
            continue
        if (parent_w is None or parent_w is MAX or c in parent_w) \
                and (parent_nw is MAX or c in parent_nw):
            continue
        c_x = c[0]
        c_y = c[1]
        value = maze[c_y][c_x]

        new_path_w = None if parent_w is None else parent_w[:]  # FIXME: None-handling
        new_path_nw = parent_nw[:]
        if value == 1:
            new_path_nw = MAX  # no no-wall path for this vertex
            if parent_w is not None and c not in parent_w:     # FIXME: handle None situation
                new_path_w = MAX    # 2-wall path is invalid
            if parent_nw is not MAX and c not in parent_nw:    # FIXME: handle None situation
                new_path_w = parent_nw[:]  # note: not new_path_nw[:]
                new_path_w.append(c)    # path_nw + c makes a valid 1-wall path
        else:       # value == 0
            if parent_w is not None \
                    and parent_w is not MAX \
                    and c not in parent_w:   # FIXME: handle None situation
                new_path_w.append(c)  # add to path_w
            if parent_nw is not MAX and c not in parent_nw: # FIXME: handle None situation
                new_path_nw.append(c)  # add to path_nw

        # check maze_paths to see if there's a shorter path
        old_c = maze_paths[c_y][c_x]
        old_path_w = old_c.path_wall
        old_path_nw = old_c.path_nowall

        path_w = new_path_w if old_path_w is None or len(new_path_w) < len(old_path_w) else old_path_w
        path_nw = new_path_nw if old_path_nw is None or len(new_path_nw) < len(old_path_nw) else old_path_nw
        new_v = Vertex(c_x,c_y,path_w, path_nw)

        # add new_v to maze_path
        maze_paths[c_y][c_x] = new_v
        if path_w == MAX and path_nw == MAX:    # no feasible path
            continue
        if ((old_path_w is None and path_w is None) or old_path_w == path_w) \
            and ((old_path_nw is None and path_nw is None) or old_path_nw == path_nw):
            continue
        nbours.append(c)

    return nbours


# helper functions to get neighbours of a vertex
def top(x,y):
    return None if y==0 else (x,y-1)

def left(x,y):
    return None if x==0 else (x-1,y)

def bottom(x,y,h):
    return None if y==h-1 else (x,y+1)

def right(x,y,w):
    return None if x==w-1 else (x+1,y)

a = answer([[0,1,1],[0,0,0],[1,1,0]])
pass