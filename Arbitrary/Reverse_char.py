'''
Q. Given a character array, where the words are delimited by a white space and we need to reverse
the order of the words.

'''

# Self defined array for testing the initial algorithm

arr = ['t','h','i','s',' ','i','s',' ','a',' ','w','o','r','d']

out = []
word = []

# use stack for the order of words and queue for the word itself
for ch in arr:
    if ch == ' ' or ch == arr[len(arr) - 1]:
        if ch == arr[len(arr) - 1]:
            word.append(ch)
        if(word != None):
            out.append(word)
            word = []
    else:
        word.append(ch)

# now my out has all the words in order. Time to wrote them back
newArr = []
n = len(out)-1
for i in range(len(out)):
    for ch in out[n-i]:
        newArr.append(ch)
    newArr.append(' ')
    
newArr = newArr[:len(newArr)-1]
newArr
print("Input array is:", arr)
print("Output:")
print(newArr)
