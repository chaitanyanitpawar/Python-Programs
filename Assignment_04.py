"""
###################################
DSL Lab Assignment 4
Chaitanya Nitin Pawar SE B 48
Date : 19/9/2020
###################################

**********************Problem Statement*********************
a) Write a Python program to store names and mobile
numbers of your friends in sorted order on names.
Search your friend from list using binary search
(recursive and non- recursive). Insert friend if not
present in phonebook
b) Write a Python program to store names and mobile
numbers of your friends in sorted order on names.
Search your friend from list using Fibonacci search.
Insert friend if not present in phonebook.
"""


########### Declaring Phonebook ###########
phbk = [["Aditya","4567890123"],["Mufaddal","1234567890"],["Gaurav","2345678901"],["Rupesh","3456789012"],["Manas","5678924347"],["Rupesh","8478423234"],["Sarthak","0998901234"],["Onkar","8788783234"],["Pratik","78317460234"],["Swaroop","4567890123"],["Pranav","5678901234"],["Yash","5678913124"],["Shivam","8934501234"]] 
n=len(phbk)
########### Main Menu ###########
def mainMenu():
    print("1. To Search your friend from list using binary search (recursive)")
    print("2. To Search your friend from list using binary search (non-recursive)")
    print("3. To Search your friend from list using fibonaccy search")
    print("4. To View The PhoneBook")
    print("5. Exit")
    ch = int(input("Enter Your Choice::"))
    if ch == 1:
        print("1. Search your friend from list using binary search (recursive)")
        sort(phbk)
        x=input("Enter The Name That You Want To Search::")
        x=x.capitalize()
        result = binarySearchAppr(phbk, 0, len(phbk)-1, x)
        if result != -1:
            print ("Element is present at index "+str(result))
        else:
            print(x,"is not present in phonebook")
            print("Record",x,"is being inserted in phonebook.....")
            insert(phbk,x)
            print("Record for",x," added successfully")
        continuous()
    elif ch == 2:
        print("2. Search your friend from list using binary search (non-recursive)")
        sort(phbk)
        x=input("Enter The Name That You Want To Search::")
        x=x.capitalize()
        result = binarySearch(phbk, 0, len(phbk)-1, x)
        if result != -1:
            print ("Element is present at index "+str(result))
        else:
            print(x,"is not present in phonebook")
            print("Record",x,"is being inserted in phonebook.....")
            insert(phbk,x)
            print("Record for",x," added successfully")
        continuous()
    elif ch == 3:
        print("3. Search your friend from list using fibonaccy search")
        sort(phbk)
        x=input("Enter The Name That You Want To Search::")
        x=x.capitalize()
        result = FibonacciSearch(phbk, x)
        if result != -2:
            print ("Element is present at index "+str(result))
        else:
            print(x,"is not present in phonebook")
            print("Record",x,"is being inserted in phonebook.....")
            insert(phbk,x)
            print("Record for",x," added successfully")
        continuous()
    elif ch == 4:
        print("Elements of phonebook are:", end="\n")
        n=len(phbk)
        print(phbk)
        mainMenu()
    elif ch == 5:
        exit()
    else:
        print("Enter Valid Choice")
       continuous()
        
########### Function for Binary search(Recursive) ###########
def binarySearchAppr (arr, start, end, x):
# check condition
    if end >= start:
        mid = start + (end- start)//2
   # If element is present at the middle
        if arr[mid][0] == x:
            return mid
   # If element is smaller than mid
        elif arr[mid][0] > x:
            return binarySearchAppr(arr, start, mid-1, x)
   # Else the element greator than mid
        else:
            return binarySearchAppr(arr, mid+1, end, x)
    else:
   # Element is not found in the array
      return -1
    
########### Function for binary search(Non-Recursive) ###########
def binarySearch(arr, start, end, x):

   if end >= start:
      mid = start + (end- start)//2
      # If element is present at the middle
      if str(arr[mid][0]) == x:
          return mid
      # If element is smaller than mid
      elif str(arr[mid][0]) > x:
          return binarySearchAppr(arr, start, mid-1, x)
      # Else the element greator than mid
      else:
          return binarySearchAppr(arr, mid+1, end, x)
   else:
      # Element is not found in the array
      return -2
    
########### Function for sorting ###########
def sort(phbk):
    for j in range(len(phbk)):
        swapped=False
        i=0
        while i<len(phbk)-1:
            if phbk[i][0]>phbk[i+1][0]:
                phbk[i], phbk[i+1]=phbk[i+1], phbk[i]
                swapped=True
            i=i+1
        if swapped==False:
            break
        
########### Function for making entry ###########
def insert(phbk,x1):
    c=[x1]
    mob=int(input("Enter mobile number of your friend"))
    c.append(mob)
    print(c)
    phbk.append(c)
    sort(phbk)
    
########### Function for fibonacci number generator ###########
def FibonacciGenerator(n):
    if n < 1:
        return 0
    elif n == 1:
        return 1
    else:
        return FibonacciGenerator(n - 1) + FibonacciGenerator(n - 2)
    
########### Function for fibonacci search ###########
def FibonacciSearch(arr, x):
    m = 0 
    while FibonacciGenerator(m) < len(arr): # 
        m = m + 1 
    offset = -1    
    while (FibonacciGenerator(m) > 1):
        i = min( offset + FibonacciGenerator(m - 2) ,
                 len(arr) - 1)
        if (x > arr[i][0]):
            m = m - 1
            offset = i
        elif (x < arr[i][0]):
            m = m - 2
        else:
            return i
        if(FibonacciGenerator(m - 1) and arr[offset + 1][0] == x):
            return offset + 1
    return -2

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


