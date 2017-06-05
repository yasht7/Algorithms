'''
Q. Given an array arr of unique nonnegative integers, implement a function
getDifferentNumber that finds an integer that is NOT in the array.
Your algorithm should be efficient, both from a time and a space complexity perspective.
'''

## Case1: In-place changing the array is not allowed. This increases the space complexity
##        to O(n)

def getDifferentNumber(arr):
    n = len(arr)

    hset = set()
    for element in arr:
        hset.add(element)

    for i in range(n):
        if not i in hset:
            return i

    return n

if __name__ == "__main__":
    test_arr = [0,1,2,3,4,5,9,6]
    print("Input test array is: ", test_arr)
    print("Answer:", getDifferentNumber(test_arr))
    
# output: 7
