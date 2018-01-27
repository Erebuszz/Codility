from collections import deque

def solution(A, K):
    
    N = len(A)
    # protect against crazy input
    if not 0 <= N <= 100:
        raise ValueError("The number of array should be between 0 and 100")
    if not 0 <= K <= 100:
        raise ValueError("The shifted times should be between 0 and 100")
    if not isinstance(A, list):
        raise ValueError("<A> should be a list of integers")
        
    for element in A:
        if not (-1000 <= element <= 1000) and isinstance(element, int):
            raise ValueError("Each element in the array should be an integer between -1000 and 1000")
    
    target = deque(A)
    target.rotate(K)
    target = list(target)
    return target
        