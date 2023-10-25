dollar= 0
euro= 0 
yesNo= input("Enter the Dollar amount to be converted(yes,no): ")
#wihel loop to do it mulitpul times

while yesNo == "yes":
    if yesNo == "yes":
        # ask what amout og moneyu
        dollar = float(input("How maney dollars do you what to covert: "))
        euro = dollar * .94540

        print("Your Euro amout is " + str(round(euro, 2)))
        yesNo= input("Enter the Dollar amount to be converted(yes,no): ")
    elif yesNo == "no":
    #tell person what happend
        print("You have side no you hit F5 to try agen")
