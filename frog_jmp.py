# https://app.codility.com/programmers/lessons/3-time_complexity/frog_jmp/
from math import ceil, floor


def solution(X, Y, D):
    wynik = ceil((Y - X) / D)
    return wynik

print(solution(10, 11, 1000000))
