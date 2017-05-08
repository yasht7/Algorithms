'''
Q. URLify: Write a function to replace all spaces in a string with '%20'. consequetive white spaces should be replaced with a sinle '%20'.
Therefoire handle this case efficiently.

EXAMPLE 
Input: "Mr John Smith ", 13 
Output: "Mr%20John%20Smith" 
'''

def URLify(string):
    start = 0
    end = 0
    result=''
    i = 0

    while True:
        # When we encounter a space anywhere but the end of the string.
        if string[i]==' ' and i!= len(string)-1:
            end = i
            result += string[start:end] + "%20"
            i+=1
            # For skpping continous whitespaces
            while string[i] == ' ':
                i += 1
            i-=1
        # When we reach the end of the string
        elif i == len(string) -1:
            result += string[start:i+1]
            break
        
        # case when we reset the value of end and start
        elif end != 0:
            start = i
            end =0            
        i += 1
        
    return result

string = "Lets         see this"
URLify(string)
# Output: 'Lets%20see%20this'
