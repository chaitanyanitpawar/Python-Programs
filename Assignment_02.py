"""
###################################
DSL Lab Assignment 
Chaitanya Nitin Pawar SE B 48
Date : 05/9/2020
###################################

**********************Problem Statement*********************
Write a Python program to compute following operations
on String:
a) To display word with the longest length
b) To determines the frequency of occurrence of
particular character in the string
c) To check whether given string is palindrome or not
d) To display index of first appearance of the
substring
e) To count the occurrences of each word in a given string
"""


########### Reading string ###########
string = input("Enter your string::")

########### Main Menu ###########
def mainMenu():
    print("1. To display word with the longest length")
    print("2. To determines the frequency of occurrence of particular character in the string")
    print("3. To check whether given string is palindrome or not")
    print("4. To display index of first appearance of the substring")
    print("5. To count the occurrences of each word in a given string")
    print("6. Exit")
    ch = int(input("Enter Your Choice::"))
    if ch == 1:
        print("1. Word with the longest length")
        print(LongestWordLength(string))
        continuous()
    elif ch == 2:
        print("2. Frequency of occurrence of particular character in the string")
        freq()
        continuous()
    elif ch == 3:
        print("3. Given string is palindrome or not")
        palindrome()
        continuous()
    elif ch == 4:
        print("4. Index of first appearance of the substring")
        find_pos()
        continuous()
    elif ch == 5:
        print("4. The occurrences of each word in a given string")
        word_count()
        continuous()
    elif ch == 6:
        exit()
    else:
        print("Enter Valid Choice")
        mainMenu()
        
########### Function to count the occurrences of word ###########
def word_count():
    counts = dict()
    words = string.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    print(counts)
    
########### Function to find Index of first appearance of the substring ###########
def find_pos():
    word=input("Enter the substring::")
    for i in range(len(string)):
        if string[i:i+len(word)] == word:
            op="The Index of first appearance of {}, is {}".format(word, i)
            print(op)
            return "Found"
    print("Not Found")
    return "Not Found"

########### Function to reverse the string ###########
def isPalindrome():
    string.upper()
    return string == string[::-1]

########### Function to check whether given string is palindrome or not ###########
def palindrome():
    ans = isPalindrome()
    if ans:
        print("Yes")
    else:
        print("No")
        
########### Function to abort the program ###########
def exit():
    print("Program Exited. Thanks For Using My Program")
    
########### Function to determines the frequency of occurrence of particular character ###########
def freq():
    character=input("Enter the character::")
    character=character.upper()
    count(string,character)
    
########### Function to count of occurrence of each character ###########
def count(strings,chara):
    cnt=0
    word=strings.upper()
    for i in range(len(word)):
        if word[i]==chara:
            cnt+=1
        else:
            pass
    op="The Frequency of {}, is {}".format(chara, cnt)
    print(op)
    
########### Function To display word with the longest length ###########
def LongestWordLength(string):   
    longest = 0
    for words in string.split():
        if len(words) > longest:
            longest = len(words)
            longest_word = words
    return longest_word

########### Function To Ask whether to continue or not ###########
def continuous():
    print("Do you want to continue?")
    print("1. Yes")
    print("2. No")
    cont=int(input())
    if cont == 1:
        mainMenu()
    elif cont == 2:
        exit()
    else:
        print("Enter A Valid Choice")

if __name__ == "__main__":
    mainMenu()


