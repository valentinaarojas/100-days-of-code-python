print("Welcome to the tip calculator!")
bill = float(input("What is the total bill amount?\n$"))
tip = int(input("How much tip would you like to give? (10, 12, 15)\n"))
people = int(input("How many people to split the bill?\n"))

bill += (bill * (tip / 100)) 
bill_per_person = bill / people
total = round(bill_per_person, 2)

print(f"Each person should pay: ${total}")