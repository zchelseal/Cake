class Path:
    def __init__(self):
        #self._root = None
        self.vertices = [(0,0)]
        self.wall = None
        #self.last_vertex = (0,0)

class Vertex:
    def __init__(self, coord, dist_nowall, dist_wall):
        self.coordinates = coord    # (x,y)
        self.dist_nowall = dist_nowall
        self.dist_wall = dist_wall

def answer(map):
    # base cases
    h = len(map)
    if h < 1:
        return 0
    w = len(map[0])
    if w < 1:
        return 0
    end_coord = (w-1,h-1)

    # loop
    v = start = Vertex((0,0), 0, 0)
    visited = [v]   # only those that have been focused
    curr_nodes = []
    while v.coordinates != end_coord :
        lst_nbours = neighbours(v,w,h,visited, curr_nodes)

        pass

def answer_new(map):
    MAX = 401  # upper bound on the path length

    # base cases
    h = len(map)
    if h < 1:
        return 0
    w = len(map[0])
    if w < 1:
        return 0

    # loop
    nodes = {}
    x = 0
    y = 0
    dist_nw = 0                         # distance to origin without any walls in between
    dist_w = MAX                        # distance to origin with a wall in between
    nodes[(x,y)] = (dist_nw,dist_w)     # key is (x,y), value is (distance_with_wall, distance_without_wall)
    visited = [(x,y)]                   # only those that have been focused
    while (x,y) != (w-1,h-1):
        #lst_nbours = neighbours(v,w,h,visited, curr_nodes)
        L = [top(x, y), left(x, y), bottom(x, y, h), right(x, y, w)]
        for c in L:
            if c is None or c in visited:
                continue

            value = map[c[1]][c[0]]
            if value == 1:
                if dist_nw < MAX:
                    dist_w = dist_nw + 1
                else:
                    dist_w = MAX
                dist_nw = MAX           # no way to get there without passing a wall
            else:
                dist_w += 1
                dist_nw += 1

            if c in nodes.keys:
                if nodes.get(c) is None \
                        or nodes[c][0] is None \
                        or dist_w < nodes[c][0]:    # c doesn't exist in dict
                    nodes[c][0] = dist_w

            # has it been visited in this level? if so & smaller distance, update

            pass
        pass

def copy_map(h, w):
    copy = []
    for i in range(h):
        row = []
        for j in range(w):
            row[j] = None
        copy[i] = row
    return copy

def answer_newer(map):
    # base cases
    h = len(map)
    if h < 1:
        return 0
    w = len(map[0])
    if w < 1:
        return 0

    MAX = 401  # magic number by the constrains
    map_nw = copy_map(h, w)
    map_w = copy_map(h, w)

    # loop
    nodes = {}
    x = 0
    y = 0
    dist_w = 0                          # distance to origin with a wall in between
    dist_nw = 0                         # distance to origin without any walls in between
    nodes[(x,y)] = (dist_w,dist_nw)     # key is (x,y), value is (distance_with_wall, distance_without_wall)
    visited = [(x,y)]                   # only those that have been focused
    while (x,y) != (w-1,h-1):
        #lst_nbours = neighbours(v,w,h,visited, curr_nodes)
        L = [top(x, y), left(x, y), bottom(x, y, h), right(x, y, w)]
        for c in L:
            if c is None or c in visited:
                continue

            value = map[c[1]][c[0]]
            if value == 1:
                if dist_w < MAX and dist_nw < MAX:
                    dist_w = dist_nw + 1
                else:
                    dist_w = MAX
                dist_nw = MAX           # no way to get there without passing a wall
            else:
                dist_w += 1
                dist_nw += 1

            if c in nodes.keys:
                if nodes.get(c) is None \
                        or nodes[c][0] is None \
                        or dist_w < nodes[c][0]:    # c doesn't exist in dict
                    nodes[c][0] = dist_w

            # has it been visited in this level? if so & smaller distance, update

            pass
        pass


def neighbours(v,w,h,visited, curr_nodes):
    x = v.coordinates[0]
    y = v.coordinates[1]
    dist_nowall = v.dist_nowall
    dist_wall = v.dist_wall

    # list of coordinates neighbour to v
    L = [top(x,y), left(x,y),bottom(x,y,h), right(x,y,w)]
    for c in L:
        if c is None:
            continue
        elif
        # is it none?
        # has it been visited as a central node?
        # has it been visited in this level? if so & smaller distance, update
        # else, if it's 1, dist_wall


        pass

    return [x for x in L if x is not None and x not in any(lst_visited.coordinates)]

# helper functions to get neighbours of a vertex
def top(x,y):
    if y == 0:
        return None
    else:
        return x,y-1

def left(x,y):
    if x == 0:
        return None
    else:
        return x-1,y

def bottom(x,y,h):
    if y == h-1:
        return None
    else:
        return x,y+1

def right(x,y,w):
    if y == w-1:
        return None
    else:
        return x+1,y


def answer(arc, dest):
    lst_checked = [arc]
    level = 0
    if arc == dest:
        return level    # base case: starting and ending squares are the same

    lst_nbours = neighbours(arc, lst_checked)
    lst_checked.extend(lst_nbours)
    level += 1
    while dest not in lst_nbours:
        lst_nextlvl = []
        for nbour in lst_nbours:
            L = neighbours(nbour, lst_checked)
            if dest in L:
                return level + 1
            else:
                lst_checked.extend(L)
                lst_nextlvl.extend(L)
        lst_nbours = lst_nextlvl
        level += 1
    return level
