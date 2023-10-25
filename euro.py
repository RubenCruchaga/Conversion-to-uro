dollar= 0
euro= 0 
yesNo= input("Would you like to convert dollars to euros?(yes,no): ")
#wihel loop to do it mulitpul times

while yesNo == "yes":
    if yesNo == "yes":
        # ask what amout og moneyu
        dollar = float(input("Enter the Dollar amount to be converted: "))
        euro = dollar * .94540

        print("Your Euro amout is " + str(round(euro, 2)))
        yesNo= input("Would you like to convert dollars to euros?(yes,no): ")
    elif yesNo == "no":
    #tell person what happend
        print("You have side no you hit F5 to try agen")
