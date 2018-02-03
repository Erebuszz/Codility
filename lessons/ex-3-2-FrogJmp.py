def solution(X, Y, D):
    # if the frog can get to the destination in just the number of steps
    if (Y - X) % D == 0:
        return int((Y - X) / D)
    else:
        return int((Y - X) // D + 1)