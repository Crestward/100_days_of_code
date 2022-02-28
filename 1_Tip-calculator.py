print("Welcome to the Tip Calculator")

bill = float(input("What was the total bill: $"))

num_of_cus = float(input("How many people to split the bill? "))

per = float(input("What tip percentage would you like to give: 10, 12, or 15?"))

tip_per = per/100 *bill

tip = round((bill + tip_per)/num_of_cus, 2)

print(f"Each person pays: ${tip}")