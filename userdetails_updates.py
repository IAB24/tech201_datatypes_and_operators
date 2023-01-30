#print("What is your name,age and date of birth")
print(" What is your name?")
name = input()
print("What is your age?")
age = input()
print("What is your date of birth?")
dob = input()

print(f"{name.capitalize()} is {age} years old and was born on {dob}")

house_number = input("House number? ")
street_address = input("Street Address? ")
postcode = input("Postcode? ")

print(f"Your address: {house_number} {street_address.capitalize()},{postcode.upper()}")
