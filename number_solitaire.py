# https://app.codility.com/programmers/lessons/17-dynamic_programming/number_solitaire/


def solution(A):
    results = [-float("inf")] * len(A)
    results[0] = A[0]

    for i in range(len(A)):
        for j in range(max(0, i - 6), i):
            results[i] = max(results[i], results[j] + A[i])

    return results[len(A) - 1]
