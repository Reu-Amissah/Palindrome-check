#python palindrome

import math

#palindrome-check function with userInput parameter
def palindrome_check(word):
    isPalindrome = bool
    numLimit = math.floor(len(word) / 2)
    for i in range(numLimit):
      
        # compare letters
        if word[i] == word[len(word) - 1 - i]:
            isPalindrome = True
            continue
        else:
            isPalindrome = False
            break

    if isPalindrome:
        print("This is a palindrome")
    else:
        print("This is not a palindrome")

#acquire user - input
userInput= input("Enter your word: ")
palindrome_check(userInput)
