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
# main recursion
def build_list(lst, level, a, dest):
    lst_nbours = list_nbours(lst, a)
    lst.extend(lst_nbours)
    while dest not in lst_nbours:
        L = []
        for nbour in lst_nbours:
            L2 = list_nbours(lst, nbour)
            if dest in L2:
                return level + 1
            else:
                lst.extend(L2)
                L.extend(L2)
        lst_nbours = L
        level += 1
    return level + 1
"""

"""
# main recursion
def build_list(lst, level, a, dest):
    L = [topleft1(a), topleft2(a),topright1(a), topright2(a),
         botleft1(a), botleft2(a), botright1(a), botright2(a)]
    L = [x for x in L if x is not None and x not in lst]
    if dest in L:
        return level + 1
    else:
        lst.extend(L)
        for nbour in L:
            result = build_list(lst, level + 1, nbour, dest)
            if result is not None:
                return result
        return None
"""


# helper functions to get neighbours of a vertex
def neighbours(a, lst_checked):
    L = [topleft1(a), topleft2(a),topright1(a), topright2(a),
         botleft1(a), botleft2(a), botright1(a), botright2(a)]
    return [x for x in L if x is not None and x not in lst_checked]

def topleft1(v):
    if v % 8 == 0 or v % 8 == 1 or v < 8:
        return None
    else:
        return v - 10

def topleft2(v):
    if v % 8 == 0 or v < 16:
        return None
    else:
        return v - 17

def topright1(v):
    if v % 8 == 7 or v < 16:
        return None
    else:
        return v - 15

def topright2(v):
    if v % 8 == 7 or v % 8 == 6 or v < 8:
        return None
    else:
        return v - 6

def botleft1(v):
    nbour = v + 6
    if v % 8 == 0 or v % 8 == 1 or v > 55:
        return None
    else:
        return v + 6

def botleft2(v):
    if v % 8 == 0 or v > 47:
        return None
    else:
        return v + 15

def botright1(v):
    if v % 8 == 7 or v > 47:
        return None
    else:
        return v + 17

def botright2(v):
    if v % 8 == 7 or v % 8 == 6 or v > 55:
        return None
    else:
        return v + 10

ans = answer(0, 1)
pass