# https://app.codility.com/programmers/lessons/13-fibonacci_numbers/fib_frog/

from queue import PriorityQueue

def solution(A):
    A = [1] + A
    fibonacci = [0, 1]
    visited = [float("inf")] * len(A)
    
    while fibonacci[-1] <= len(A):
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    
    q = PriorityQueue()
    q.put((0, 0))
    
    result = float("inf")
    
    while not q.empty():
        item, jumps = q.get()
        item = -item
        new_jumps = jumps + 1
        
        if new_jumps >= result:
            continue
        
        for fib in fibonacci:
            value = item + fib
            
            if value > len(A):
                break
            
            if value == len(A):
                result = min(result, new_jumps)
                break
                
            if visited[value] <= new_jumps:
                continue
            
            if not A[value]:
                continue
            
            visited[value] = new_jumps
            q.put((-value, new_jumps))
    
    return result if result != float("inf") else -1

