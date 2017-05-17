'''
Given an array arr of distinct integers and a nonnegative integer k, write a function findPairsWithGivenDifference that returns an array of all pairs [x,y] in arr, such that x - y = k. If no such pairs exist, return an empty array.

'''

import copy
def findPairsWithGivenDifference(arr, k):
    output = []
  
    if len(arr) < 2:
        return output
  
    arr2 = copy.copy(arr)

    arr2.sort()
    start,end = 0, 1

    while start < len(arr2)-1:
        diff = arr2[start] - arr2[end]
        diff = diff if diff > 0 else 0-diff
    
        if diff < k:
            start += 1
        elif diff >k:
            start += 1
            end += 1
        else:
            output.append([arr2[start],arr2[end]])
            start +=1
            end +=1
    return output
    
print(findPairsWithGivenDifference([0, -1, 2, 2, 1],1))
