"""
###################################
DSL Lab Assignment 5
Chaitanya Nitin Pawar SE B 48
Date : 10/10/2020
###################################

**********************Problem Statement*********************
Write a Python program to store first year percentage of
students in array. Write function for sorting array of
floating point numbers in ascending order using
a) Selection Sort
b) Bubble sort and display top five scores.
"""


strength = int(input("Enter total number of students::"))
percentage = []
for stud in range(strength):
    mark = float(input("Enter first year percentage of students::"))
    percentage.append(mark)
print("First year percentage of students are as follows...")
print(percentage)

def mainMenu():
    print("1. Selection Sort")
    print("2. Bubble sort and display top five scores")
    print("3. Exit")
    ch = int(input("Enter Your Choice::"))
    if ch == 1:
        print("1. Selection Sorted")
        selection_sort(percentage)
        continuous()
    elif ch == 2:
        print("2. Bubble sorted and top five scores")
        bubbleSort(percentage)
        continuous()
    elif ch == 3:
        exit()
    else:
        print("Enter Valid Choice")
        mainMenu()
        
########### Function To Abort The Program ###########
def exit():
    print("Program Exited. Thanks For Using My Program")
    
########### Function For Selection sort ###########
def selection_sort(L):
    for i in range(len(L)-1):
        min_index = i
        for j in range(i+1, len(L)-1):
            if L[j] < L[min_index]:
                min_index = j
        L[i], L[min_index] = L[min_index], L[i]
    print(L)
    
########### Function For Bubble sort ###########
def bubbleSort(arr): 
    n = len(arr)  
    for i in range(n): 
        swapped = False
        for j in range(0, n-i-1): 
            if arr[j] > arr[j+1] : 
                arr[j], arr[j+1] = arr[j+1], arr[j] 
                swapped = True 
        if swapped == False: 
            break
    arr=arr[::-1]
    if len(arr)>=5:
        for i in range(5):
            print ("%d" %arr[i],end=" ")
        print("\n")
    else:
        for i in range(len(arr)):
            print ("%d" %arr[i],end=" ")
        print("\n")
        

########### Function to Ask whether to continue or not ###########
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


