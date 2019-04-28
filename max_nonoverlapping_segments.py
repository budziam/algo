# https://app.codility.com/programmers/lessons/16-greedy_algorithms/max_nonoverlapping_segments/

def solution(A, B):
    last_end = -1
    count = 0
    
    for i in range(len(B)):
        if A[i] > last_end:
            count += 1
            last_end = B[i]
            
    return count

