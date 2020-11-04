"""
###################################
DSL Lab Assignment 1
Chaitanya Nitin Pawar SE B 48
Date : 22/8/2020
###################################

**********************Problem Statement*********************
Write a Python program to store marks scored in subject
“Fundamental of Data Structure” by N students in the
class. Write functions to compute following:
a) The average score of class
b) Highest score and lowest score of class
c) Count of students who were absent for the test
d) Display mark with highest frequency

"""




########### Reading strength of class ###########
strength = int(input("Enter total number of students::"))
marks = []

########### Reading marks of student ###########
print("\nNOTE : Enter '-1' for absent students")
for stud in range(strength):
    mark = int(input("Enter the marks of student in FDS: "))
    marks.append(mark)
    
########### Printing marks of student ###########
print("The student gets marks in FDS test are as follows...")
print(marks)

########### Main Menu ###########
def mainMenu():
    print("1. The average score of class")
    print("2. Highest score and lowest score of class")
    print("3. Count of students who were absent for the test")
    print("4. Display mark with highest frequency")
    print("5. Exit")
    ch = int(input("Enter Your Choice::"))
    if ch == 1:
        print("1. The average score of class")
        avgScore()
        continuous()
    elif ch == 2:
        print("2. Highest score and lowest score of class")
        highScore()
        lowScore()
        continuous()
    elif ch == 3:
        print("3. Count of students who were absent for the test")
        print("\nNOTE : Enter '-1' for absent students")
        absntStud()
        continuous()
    elif ch == 4:
        print("4. Display mark with highest frequency")
        freqHigh()
        continuous()
    elif ch == 5:
        exit()
    else:
        print("Enter Valid Choice")
        mainMenu()
        
########### Function to abort the program ###########
def exit():
    print("Program Exited. Thanks For Using My Program")
    
########### Function to calculate average marks ###########
def avgScore():
    cnt = 0
    Avg = 0
    Total = 0
    n = len(marks)
    for x in marks:
        if x == -1:
            cnt += 1
        else:
            Total = Total+x
        Avg = Total/(n-cnt)
    print("The Average Score Of Class Is::", Avg)

########### Function to Calculate Maximum marks ###########
def highScore():
    cnt = 0
    max = 0
    for x in marks:
        if x == -1:
            cnt += 1
        elif x > max:
            max = x
    print("Highest Marks in FDS test is::", max)

########### Function to Calculate Minimum marks ###########
def lowScore():
    cnt = 0
    min = 100
    for x in marks:
        if x == -1:
            cnt += 1
        elif x < min:
            min = x
    print("Lowest Marks in FDS test is::", min)
    
########### Function to finding number of absent students ###########
def absntStud():
    absnt = 0
    for x in marks:
        if x == -1:
            absnt += 1
    print("Count of students who were absent for the test is", absnt)

########### Function to finding highest frequency of marks ###########
def freqHigh():
    max = 0
    res = marks[0]
    for i in marks:
        if i == -1:
            pass
        else:
            freq = marks.count(i)
            if freq > max:
                max = freq
                res = i
    op = "The Most Frequent Number is {}, and its frequency is {}".format(
        str(res), max)
    print(op)
    
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

