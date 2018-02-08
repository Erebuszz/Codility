#!/usr/bin/python3

def solution(A):
    
    total = sum(A)
    N = len(A)
    
    # use // instead of / to make the result type <int> instead of <float>
    expected = (N + 1) * (N + 2) // 2

    return expected - total
    
    # ### Sol 2 ###
    # N = len(A)
    # # array of 1 to N+1
    # arr = list(range(1, N+2))
    # A.sort()
    # # Make A as long as arr to prevent (index out of range) error
    # A.append(0)
    
    # count = 0
    # for element in arr:
    #     if not element == A[count]:
    #         return element
    #     else:
    #         count += 1

