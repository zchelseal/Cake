def answer(s):
    length = len(s)
    # base cases
    if length < 1:  return 0
    if length == 1: return 1

    # check occurrences of first character
    i = 0
    first = s[i]
    i += 1 + s[1:].find(first)

    #while not all(s[0:i] == s[j*i:(j+1)*i] for j in range(1,length//i)):
    while not can_cut(s,i,length):
        if s[i+1:].find(first) < 0:
            return 1
        i += 1 + s[i+1:].find(first)
        if i >= len(s)-1:
            return 1
    return length//i


def can_cut(s,i,length):
    if length%i != 0:
        return False
    for j in range(1,length//i):
        if s[0:i] != s[j*i:(j+1)*i]:
            return False
    return True


a = answer('abccbaabccbaabccbaabccbaabccbap')
pass


