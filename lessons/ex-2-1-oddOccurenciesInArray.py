MAXINT = 1000000000


def solution(A):
    N = len(A)
    # check the assumptions
    if not isinstance(A, list):
        raise TypeError("Input must be a list of integers")
    if N < 1:
        raise ValueError("Input should not be empty")
    if N > 1000000:
        raise ValueError("The length of array shouldn't be longer that 1,000,000")
    if N % 2 == 0:
        raise ValueError("The length of array should be an odd number")

    # # Solution 1
    # unmatched = dict()
    # # loop over every element in the array
    # for element in A:
    #     # element limitation check
    #     if not 1 <= element <= MAXINT:
    #         raise ValueError("Elements of array A should be between 1 and %d" % MAXINT)
    #     # if you can delete it, then it's matched
    #     try:
    #         del unmatched[element]
    #     except KeyError:
    #         unmatched[element] = True
    #
    # # if there is only one value left unmatched
    # if len(unmatched) == 1:
    #     return list(unmatched.keys())[0]
    # else:
    #     raise Exception("There are %d unmatched numbers!" % len(unmatched))

    # Solution 2
    result = 0
    # loop over every element in the array
    for element in A:
        # element limitation check
        if not 1 <= element <= MAXINT:
            raise ValueError("Elements of array A should be between 1 and %d" % MAXINT)
        # Use Xor to find unmatched numbers (eg. 1 ^ 1 = 0, 1 ^ 2 ^ 2 = 1)
        result ^= element
    # if the result isn't in A
    if result in A:
        return result
    else:
        # e.g. 1 ^ 2 = 3, 1 ^ 1 = 0
        raise Exception("There are no unmatched or more than 1 unmatched")


def main():
    arr1 = [9, 3, 9, 3, 9, 7, 9]
    print(solution(arr1))


main()