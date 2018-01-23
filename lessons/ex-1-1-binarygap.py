# Written in python 3.6

# A binary gap within a positive integer N is any maximal sequence of consecutive zeros 
#  that is surrounded by ones at both ends in the binary representation of N.

# Write a function:
# 		def solution(N)
#  that, given a positive integer N, returns the length of its longest binary gap. 
# The function should return 0 if N doesn't contain a binary gap.

# For example, given N = 1041 the function should return 5,
#  because N has binary representation 10000010001 and so its longest binary gap is of length 5.

# Assume that:
# 		N is an integer within the range [1..2,147,483,647].
# Complexity:
# 		expected worst-case time complexity is O(log(N));
# 		expected worst-case space complexity is O(1).


MAXINT = 2147483647

def solution(N):

    # protect against crazy inputs
    if not isinstance(N, int):
        raise TypeError("Input must be an integer")
    if N < 1:
        raise ValueError("Input must be a positive integer")
    if N > MAXINT:
        raise ValueError("Input must be a positive integer less than 2,147,483,647")

    # convert the number to a string containing '0' and '1' chars
    bin_string = format(N, 'b')

    max_num = 0
    counter = 0
    start = 0

    # loop over all the 0/1 chars in the string
    for bit in bin_string:
        # if we meet the first char of 1
        if(bit == '1' and counter == 0):
            start = 1
        # if we meet the second char of 1
        elif(bit == '1' and counter > 0):
            # compare the current value to the max value
            if(counter > max_num):
                # if bigger, then replace the max value
                max_num = counter
            # reset the counter
            counter = 0
        # if we already met the first 1, and we meet 0 now
        elif(bit == '0' and start == 1):
            # start counting
            counter += 1
            
    return max_num
    
def main():
    num = 1376796946
    answer = solution(num)
    print("answer is: %d" % answer)

main()
