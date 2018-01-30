def solution(A):
    # Initialize head to the first element of the array
    #   and the tail to the sum of the array except the first element
    head = A[0]
    tail = sum(A[1:])
    min_dif = abs(head - tail)
 
    # loop over the rest of the possibilities
    for index in range(1, len(A)-1):
        head += A[index]
        tail -= A[index]
        if abs(head - tail) < min_dif:
            min_dif = abs(head-tail)
 
    return min_dif