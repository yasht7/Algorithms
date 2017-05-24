'''

Problem: Please write a function in Python that takes an 8x8 grid of letters and a list of words and returns the longest word from the list (ignoring case) that can be produced from the grid using the following procedure:
Start at any position in the grid, and use the letter at that position as the first letter in the candidate word.
Move to a position in the grid that would be a valid move for a knight in a game of chess, and add the letter at that position to the candidate word.
Repeat step 2 any number of times.
For example, if the list of words is ["algol", "fortran", "simula"] and the grid is:
  1 2 3 4 5 6 7 8
1 Q W E R T n U I
2 O P A a D F G H
3 t K L Z X C V B
4 N M r W f R T Y
5 U I O P A S D F
6 G H J o L Z X C
7 V B N M Q W E R
8 T Y U I O P A S

...then the longest word from the list that can be produced using the rules is “fortran”, by starting at the ‘F’ at position (5, 4), and moving to (4, 6), then (3, 4), (1, 3), back to (3, 4) and then (4, 2) and finally (6,1). Again, note that the match is case-insensitive, and that grid positions can be reused.
Create a list of words found in Shakespeare’s early comedy, Love’s Labour’s Lost (text available at http://shakespeare.mit.edu/lll/full.html). Make sure to remove punctuation and ignore case when generating the word list. What is the output of your function using this word list on the grid below?
    E X T R A H O P
    N E T W O R K S
    Q I H A C I Q T
    L F U N U R X B
    B W D I L A T V
    O S S Y N A C K
    Q W O P M T C P
    K I P A C K E T

'''

# Solution: by Yashaswi Tamta (MS in CS University of Washington); LinkedIn: https://www.linkedin.com/in/yashtamta

'''
Observations:
>> Reusing the grid position is convenient.
>> Starting to search the Letter Matrix form the longest word will help the algorithm to converge faster.

Method:
1. Storing the list of words from "Love's Labour's Lost" in a Dictionary where key will be the word and it's length, the value.
This is done for two major reasons.
    - avoiding duplicates
    - keeping track of the length of the word

2. I plan to choose the longest word from the dictionary and check if the word exist in the matrix.

3. The checking/validating step is best done if incremental and therefore we can opt for a recursion which will lead to
a much cleaner code.

FAULT TOLERANCE:
    >> The code can accept a matrix of any length but will consider only the first 64 i.e 8x8 letters
    and terminate when it reaches that limit
    **Look at creatLetterMatrix()
'''


import re
import numpy as np
import operator
import warnings

# Global variables
matrix_dim = 8
moves = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]


# Code to update the Dictionary storing the words.
# do nothing for duplicates
def updateMap(Map, key, val):
    if not key is Map.keys():
        Map[key] = val


# Ignoring the lower case and punctuations
def filterWord(word):
    word = re.sub(r'[^a-zA-Z0-9]', r'', word)
    word = word.lower()
    return word


# This looks up the words from the online text saved locally in txt format.
# can be edited to using a command line argument or add a web scrapper(That'd be cool)
def getWordMap():
    text = open("shakespeare.txt", 'r')
    wordMap = {}
    for line in text:
        for word in line.split(' '):
            word = filterWord(word)
            if word != '':
                updateMap(wordMap, word, len(word))
    text.close()
    return wordMap


# Creating the letter matrix form the given question.
# can accept larger matrices but will consider the first 8x8 letters
def createLetterMatrix():
    matrixFile = open("matrix.txt", 'r')
    matrix = [[0 for x in range(8)] for x in range(8)]

    row = 0
    for line in matrixFile:
        if row > matrix_dim - 1:
            warnings.warn("Filled the rows")
            break

        col = 0
        for ch in line.split(' '):
            if col > matrix_dim - 1:
                warnings.warn("Filled the Columns")
                break
            matrix[row][col] = filterWord(ch)
            col += 1

        row += 1
    matrixFile.close()
    return matrix


# next possible coordinates from the current coordinates
def getNextCoords(x, y):
    nextCoords = []
    for move in moves:
        nextCoord = (x + move[1], y + move[0])
        if nextCoord[0] < matrix_dim and nextCoord[1] < matrix_dim:
            nextCoords.append(nextCoord)
    return nextCoords


# Main recursive function
# The function builds a substring achieved by concatenating letters from the set of valid next moves.
# This substring is checked against the main word
# The algorithm returns False whenever this check fails thus, pruning the further steps.
# Consecutively it will return True only when the substring matches the word perfectly.

def isInMatrix(word, row, col, cur_str, matrix, flag):
    currentLetter = matrix[row][col]
    cur_str += currentLetter

    if cur_str == word:
        return True

    if cur_str in word:
        # update row, col
        nextCoords = getNextCoords(row, col)
        for x, y in nextCoords:
            # just need one of the possible positions to be true
            if isInMatrix(word, x, y, cur_str, matrix, flag):
                flag = True
                break
    else:
        return False

    return flag


# Function to send the search coordinates for the first letter of the word.
# NOTE: Here we send multiple coordinates because the matrix could have same letter in multiple positions.
def searchMatrix(word, matrix):
    letter = word[0]

    # searching all the locations of the starting letter
    location = np.where(np.array(matrix) == letter)
    flag = False

    if len(location[0]) == 0:
        # the staring letter of the current word is not present in the matrix
        return False

    # iterating through the list of possible start points
    for i in range(len(location[0])):
        row, col = location[0][i], location[1][i]
        # recurse
        flag = flag or isInMatrix(word, row, col, "", matrix, False)
        if flag:
            break

    return flag


# Driver function to build the requisite data structures and also return the results.
def getLongestMatch():
    wordMap = getWordMap()
    letterMatrix = createLetterMatrix()

    iterations = 0
    while iterations <= len(wordMap):
        iterations += 1
        currentWord = max(wordMap.items(), key=operator.itemgetter(1))[0]
        if searchMatrix(currentWord, letterMatrix):
            return currentWord
        else:
            del wordMap[currentWord]

    return "No word Found"

print(getLongestMatch())
'''

Output: "honorificabilitudinitatibus"

Although this seems a weird word but on looking it up i found that this is a valid word in medieval Latin
which means "the state of being able to achieve honours"
* I cross checked this, manually, against the algorithm and this does exist in the question matrix.

'''
