"""
###################################
DSL Lab Assignment 6
Chaitanya Nitin Pawar SE B 48
Date : 10/10/2020
###################################

**********************Problem Statement*********************
Write a Python program to store second year percentage 
of students in array. Write function for sorting array of
floating point numbers in ascending order using
a) Insertion sort
b) Shell Sort and display top five scores
"""


strength = int(input("Enter total number of students::"))
percentage = []
for stud in range(strength):
    mark = float(input("Enter second year percentage of students::"))
    percentage.append(mark)
print("First year percentage of students are as follows...")
print(percentage)

def mainMenu():
    print("1. Insertion Sort")
    print("2. Shell sort and display top five scores")
    print("3. Exit")
    ch = int(input("Enter Your Choice::"))
    if ch == 1:
        print("1. Insertion sorted")
        insertionSort(percentage)
        continuous()
    elif ch == 2:
        print("2. Shell sorted and display top five scores")
        shellSort(percentage)
        continuous()
    elif ch == 3:
        exit()
    else:
        print("Enter Valid Choice")
        mainMenu()
        
########### Function To Abort The Program ###########
def exit():
    print("Program Exited. Thanks For Using My Program")
    
########### Function For Insertion sort ###########
def insertionSort(arr): 
    # Traverse through 1 to len(arr) 
    for i in range(1, len(arr)):  
        key = arr[i] 
        # Move elements of arr[0..i-1], that are 
        # greater than key, to one position ahead 
        # of their current position 
        j = i-1
        while j >=0 and key < arr[j] : 
                arr[j+1] = arr[j] 
                j -= 1
        arr[j+1] = key
    print(arr)
    
########### Function For Shell sort ###########
def shellSort(arr):
    n = len(arr)
    # Gap sequence
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            # Compare elements at equal gap.
            while j >= gap and temp < arr[j - gap]:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap = gap // 2
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


