# https://app.codility.com/programmers/lessons/2-arrays/odd_occurrences_in_array/

from collections import defaultdict

def solution(A):
    data = defaultdict(int)
    
    for item in A:
        data[item] += 1
    
    for index, value in data.items():
        if value % 2 == 1:
            return index
