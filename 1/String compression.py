'''
The approach here is to create a hashmap with all the characters of the string as keys and their frequency in the string as values. Once built, we can concat (key, value) pair for every entry ot obtain the desired result.

Run Time: O(n), where n is the length of the string. This seems to be acceptable as amny algorithm has to look at all the characters of the string at least once.
Space Time: O(n) Worst case is when all characters in the string are unique.

'''

# for Ordering the dictioinaries in the order of their insertion
from collections import OrderedDict

def stringcompression(string):
    # Initializing empty dictionaries and result string.
    unique = OrderedDict()
    result = ''
    
    for i in range(len(string)):
        if string[i] in unique.keys():
            unique[string[i]] += 1
        else:
            unique[string[i]] = 1
        
    for key, value in unique.items():
        result += str(key) + str(value)
    
    return result

stringcompression("aabbccbb")
