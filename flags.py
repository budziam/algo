# https://app.codility.com/programmers/lessons/10-prime_and_composite_numbers/

from math import ceil

def attempt(peaks, x):
    visited_peaks = 1
    last_peak = peaks[0]
    
    for peak in peaks[1:]:
        if peak - last_peak >= x:
            last_peak = peak
            visited_peaks += 1
            
    return visited_peaks >= x

def solution(A):
    # write your code in Python 3.6
    peaks = []
    
    for i in range(1, len(A) - 1):
        if A[i-1] < A[i] and A[i] > A[i+1]:
            peaks.append(i)
            
    if not peaks:
        return 0

    p, q = 1, len(peaks)
    
    while q > p:
        s = ceil((q - p) / 2) + p
        
        if attempt(peaks, s):
            p = s
        else:
            q = s - 1
    
    return p
