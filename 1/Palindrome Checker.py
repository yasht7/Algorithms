'''
Q. Palindrome Permutation: Given a string, write a function to check if it is a permutation of 
a palindrome. A palindrome is a word or phrase that is the same forwards and backwards. A 
permutation is a rearrangement of letters. The palindrome does not need to be limited to just 
dictionary words.

EXAMPLE 
Input: Tact Coa 
Output: True (permutations: "taco cat'; "atco eta·; etc.) 
'''

'''
Assumptions: The palindrome is not case-sensitive - Therefore, we convert the string to lower case

A function to check if a given character is an alphabet
CHAR  ASCII
  A      65
  Z      90
  a      97
  z      122

'''
import warnings

def charChecker(ch):
    if ord(ch) >= 97 and ord(ch) <= 122:
        return ord(ch) - 65
    else:
        warnings.warn("non-alphabetic character found")
        return -1


def updateTable(table, key, val):
    if key in table.keys():
        table[key] += val
    else:
        table[key] = val

def palindromeChecker(string):
    string = string.lower()
    count,c = {},0
    for ch in string:
        if charChecker(ch) != -1:
            updateTable(count, ch, 1)
            if count[ch] %2 == 1:
                c+=1
            else:
                c-=1
    
    return c == 0

palindromeChecker("akae)ke")
# Output: True
# Warning: "non-alphabetic character found"

palindromeChecker("akake")
# Output: False
