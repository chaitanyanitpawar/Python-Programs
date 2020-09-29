print("Detection Of Possibility To Get Covid-19 Infection")
print("Press Y for yes and N for No")
positive = 0
negative = 0
response = ["y", "Y", "n", "N"]
q1 = input("Q.1) Are you at home?")
if q1 in response:
    if q1 == "n" or q1 == "N":
        positive = positive+1
    if q1 == "y" or q1 == "Y":
        negative = negative+1
else:
    print("Please provide proper input in the form of y/n")
q2 = input("Q.2) Do you have any travel history abroad?")
if q2 in response:
    if q2 == "y" or q2 == "Y":
        positive = positive+1
    if q2 == "n" or q2 == "N":
        negative = negative+1
else:
    print("Please provide proper input in the form of y/n")
q3 = input("Q.3) Do you have cold,cough,fever or any of the symptoms?")
if q3 in response:
    if q3 == "y" or q3 == "Y":
        positive = positive+1
    if q3 == "n" or q3 == "N":
        negative = negative+1
else:
    print("Please provide proper input in the form of y/n")
q4 = input("Q.4) Do you follow the home quarantine?")
if q4 in response:
    if q4 == "n" or q4 == "N":
        positive = positive+1
    if q4 == "y" or q4 == "Y":
        negative = negative+1
else:
    print("Please provide proper input in the form of y/n")
if positive>1:
    print("There are "+str ((positive/4)*100),"% chances that you are infected")
elif negative>1:
    print("There are "+str ((negative/4)*100),"% chances that you are not infected but still STAY HOME,STAY SAFE")
else:
    print("Enter valid input and run the program again")
