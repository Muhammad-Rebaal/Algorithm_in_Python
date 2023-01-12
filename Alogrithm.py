#Algorithm is  a way of solving task into steps 

def Palindrome(str):
    startindex=0
    endindex=len(str)-1

   
    if str[startindex] != str[endindex]:
            return False
    return True
print(Palindrome("racecar"))
