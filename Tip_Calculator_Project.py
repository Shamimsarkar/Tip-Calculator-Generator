# First welcome text
print("Welcome to the tip calculator!")

# Take total bill input

bill = float(input("What was the total bill? $"))

# Taking how much you pay as gift

tip = int(input("How much tip would you like to give? 10, 12, or 15?"))

# How many people should share the bill

people = int(input("How many people to split the bill?"))

bill_per_person = ( bill / people + ( (tip * bill) / 100 / people))

bill_per_person = round(bill_per_person, 2)

print("Each person should pay:",bill_per_person)


