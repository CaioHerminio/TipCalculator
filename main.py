total_value = float(input("What is the total bill amount? "))
tip_percentage = int(input("What is the tip percentage? 10, 12, or 15? "))
people = int(input("How many people will split the bill? "))
tip_multiplier = tip_percentage / 100
tip_value = total_value * tip_multiplier
amount_each_person_pays = (total_value + tip_value) / people
print(f"Each person will pay: R$ {amount_each_person_pays}")
