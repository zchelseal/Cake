"""
class Path:
    def __init__(self):
        #self._root = None
        self.vertices = [(0,0)]
        self.wall = None
        #self.last_vertex = (0,0)
"""

"""
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
"""

class Vertex:   # store these in a matrix
    def __init__(self, x, y, path_wall, path_nowall):
        self.x = x
        self.y = y
        self.path_wall = path_wall
        self.path_nowall = path_nowall
        # self.dist_nowall = dist_nowall
        # self.dist_wall = dist_wall

MAX = [-1] * 401    # upper bound on the path length

def answer(map):
    # base cases
    h = len(map)
    if h < 1:   return 0
    w = len(map[0])
    if w < 1:   return 0

    map_paths = copy_map(h, w)

    x = 0
    y = 0
    nbours = neighbours(x, y, w, h, map, map_paths)
    while 1==1:
        lst_nextlvl = []
        for nbour in nbours:
            x = nbour[0]
            y = nbour[1]
            if (x, y) != (w - 1, h - 1):    # reached bottom-right corner
                break
            L = neighbours(x, y, w, h, map, map_paths)
            lst_nextlvl.extend(L)
        nbours = lst_nextlvl

    lengths = []
    for c in nbours:
        v = map_paths[c[1]][c[0]]
        lengths.append(len(v.path_nowall))
        lengths.append(len(v.path_wall))

    return min(lengths)


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
            row[j] = Vertex(j, i, None, None)   # FIXME: None later needs case handling
        copy[i] = row
    return copy

"""
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

    v = (0,0)
    nbours = neighbours(v, path)
    #lst_checked.extend(lst_nbours)
    #level += 1
    while v != (w-1,h-1):
        lst_nextlvl = []
        for nbour in lst_nbours:
            L = neighbours(nbour, lst_checked)
            #if dest in L:
                #return level + 1
            else:
                #lst_checked.extend(L)
                lst_nextlvl.extend(L)
        lst_nbours = lst_nextlvl
        level += 1
    return level



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
        """

"""
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
"""

def neighbours(x, y, w, h, map, map_paths):
    # need x, y, path_nowall, path_wall from v
    v = map_paths[y][x]
    old_path_nw = v.path_nowall
    old_path_w = v.path_wall
    L = [top(x,y), left(x,y), bottom(x,y,h), right(x,y,w)]
    nbours = []
    for c in L:     # c is a coordinate (i,j)
        if c is None:   continue
        c_x = c[0]
        c_y = c[1]
        value = map[c_y][c_x]

        new_path_w = old_path_w[:]
        new_path_nw = old_path_nw[:]
        """
        # first check no wall
        if c not in path_nw:
            if value == 0:
                if new_path_nw is not None:
                    new_path_nw.append(c)   # add to path_nw
            else:       # value == 1
                new_path_nw = None      # no no-wall path for this vertex
                if new_path_w is not None:
                    new_path_w = path_nw[:] # note: not new_path_nw[:]
                    new_path_w.append(c) # add to path_nw FIXME: this is a valid 1-wall path
        # then check wall
        if c not in path_w:
            if value == 0:
                if new_path_w is not None:
                    new_path_w.append(c)   # add to path_nw
            else:
                # two 1's cannot form a valid path
                new_path_w = None   # FIXME: maybe the condition above did?
        """
        if value == 1:
            new_path_nw = MAX  # no no-wall path for this vertex
            if old_path_w is not None and c not in old_path_w:     # FIXME: handle None situation
                new_path_w = MAX    # 2-wall path is invalid
            if old_path_nw is not None and c not in old_path_nw:    # FIXME: handle None situation
                new_path_w = old_path_nw[:]  # note: not new_path_nw[:]
                new_path_w.append(c)    # path_nw + c makes a valid 1-wall path
        else:       # value == 0
            if old_path_w is not MAX and c not in old_path_w:   # FIXME: handle None situation
                new_path_w.append(c)  # add to path_w
            if old_path_nw is not MAX and c not in old_path_nw: # FIXME: handle None situation
                new_path_nw.append(c)  # add to path_nw

        # check map_paths to see if there's a shorter path
        old_v = map_paths[c[1]][c[0]]
        path_w = new_path_w if len(new_path_w) < len(old_v.path_wall) else old_v.path_wall
        path_nw = new_path_nw if len(new_path_nw) < len(old_v.path_no_wall) else old_v.path_no_wall
        new_v = Vertex(c[1],c[0], path_w, path_nw)
        # add new_v to map_path
        map_paths[c_y][c_x] = new_v
        if path_w != MAX or path_nw != MAX:
            nbours.append(c)

        return nbours



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

"""
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
"""
