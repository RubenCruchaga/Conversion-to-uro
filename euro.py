dollar= 0
euro= 0 
yesNo= input(" do you whatr to convert Dollars to Euros.(yes,no): ")
#wihel loop to do it mulitpul times

while yesNo == "yes":
    if yesNo == "yes":
        # ask what amout og moneyu
        dollar = float(input("Enter the Dollar amount to be converted: "))
        euro = dollar * .94540

        print("Your Euro amout is " + str(round(euro, 2)))
        yesNo= input(" do you what to convert Dollars to Euros agen.(yes,no): ")
    elif yesNo == "no":
    #tell person what happend
        print("You have side no you hit F5 to try agen")
