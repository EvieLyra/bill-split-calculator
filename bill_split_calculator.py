print("Bill Split Calculator\n")
print("Please give me the following information in the right order: bill amount, tip percentage and number of people paying for the bill:\n")
bill = float(input())
tip_percentage = float(input())
people = int(input())
tip_amount = (tip_percentage / 100) * bill
total = float(bill + tip_amount)
amount_person = total / people
print(f"\nThe total amount of the bill is: {total}")
print(f"The amount every person has to pay is: {amount_person}\n")
