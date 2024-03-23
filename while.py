"""
Created a program that asks the user to add numbers.
Check the data given by the user is a valid number.
The program stops asking for another number when the user types in -1.
Summarised the previously typed in numbers excludes the last one the -1.
Calculate the average of all numbers except the last one -1.
Print out the result.
"""

# Defining 2 variables for the calculation what depending on user input data:
count = 0
usernumber = 0

# Make a loop until user input not equal with -1:
while True:
    try:
        userinput = float(input("Enter a number here: "))
        if userinput == -1:
            break
        #  Ignore Zero or negative numbers.
        if userinput <= 0:
            print("Invalid option please type in a positive number.")
        if userinput > 0:
            usernumber += userinput
            count += 1
    except ValueError:
        print("Invalid data, please type in a valid number: ")

# Average number calculation:
total = usernumber/count
r_total = round(total, 2)

print(f"\nThe average of your numbers: {r_total}")