from math import floor, log, sqrt, pi
from constants import fibonacci_sums, powerof2_sums

def answer(total_lambs):
    maxi = fibonacci(total_lambs, 1, 1, 0, 1)
    mini = powerof2(total_lambs, 1, 1, 1)
    return maxi - mini


def test(total_lambs):
    maxi1 = fibonacci(total_lambs, 1, 1, 0, 1)
    mini1 = powerof2(total_lambs, 1, 1, 1)

    #m1 = log(total_lambs * sqrt(5) + 0.5) / log(1.61803398875) - 2
    #m2 = log((total_lambs + 1) * sqrt(5) + 0.5) / log(1.61803398875) - 2
    maxi = floor(log((total_lambs + 1) * sqrt(5) + 0.5) / log(1.61803398875) - 2)
    #n = log(total_lambs + 1, 2)
    mini = floor(log(total_lambs + 1, 2))

    #diff = maxi - mini
    return maxi - mini

def test2():
    s = 10
    while s < 1000000000:
        maxi1 = fibonacci(s, 1, 1, 0, 1)
        mini1 = powerof2(s, 1, 1, 1)
        maxi = next(i for i, v in enumerate(fibonacci_sums) if v > s)
        mini = next(i for i, v in enumerate(powerof2_sums) if v > s)
        if maxi != maxi1:
            print(str(s) + ' MAXI DIFF: ' + str(maxi1) + ' vs ' + str(maxi))
        if mini != mini1:
            print(str(s) + ' MINI DIFF: ' + str(mini1) + ' vs ' + str(mini))
        s *= 10
    print('DONE')

def fibonacci(s, length, total, prev2, prev1):
    # 1, 1, 2, 3, 5, ...
    curr = prev2 + prev1
    if s < total + curr:
        return length
    else:
        length += 1
        return fibonacci(s, length, total + curr, prev1, curr)

def powerof2(total_lambs, length, total, prev):
    # 1, 2, 4, 8, ...
    curr = prev * 2
    if total_lambs < total + curr:
        if total_lambs - total >= prev * 1.5:
            return length + 1
        else:
            return length
    else:
        length += 1
        return powerof2(total_lambs, length, total + curr, curr)


"""
def fibonacci(total_lambs, seq, total, prev2, prev1):
    # 1, 1, 2, 3, 5, ...
    curr = prev2 + prev1
    if total_lambs < total + curr:
        return len(seq) #, total_lambs - total
    else:
        seq.append(curr)
        return fibonacci(total_lambs, seq, total + curr, prev1, curr)
"""

"""
def powerof2(total_lambs, seq, total, prev):
    # 1, 2, 4, 8, ...
    curr = prev * 2
    if total_lambs < total + curr:
        return len(seq) #, total_lambs - total
    else:
        seq.append(curr)
        return powerof2(total_lambs, seq, total + curr, curr)
"""
