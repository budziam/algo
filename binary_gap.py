# https://app.codility.com/programmers/lessons/1-iterations/binary_gap/

def solution(N):
    result = []
    
    size = 0
    max_size = 0
    
    while N > 0:
        result.append(N % 2)
        N //= 2
        
    for i in result[::-1]:
        if i == 0:
            size += 1
        else:
            max_size = max(max_size, size)
            size = 0
        
    return max_size
