# 1. Calculating compound interest: Write a program that continuously prompts the user for the principal amount, interest rate, and time period, and calculates the compound interest until the user chooses to exit.
#

while True:
    user_choice = input("Do you want to continue press (y/n) :  ")
    if user_choice == "n":
        print("Thank you for choosing us.")
        break
    else:
        principal_amount = int(input("Please enter the principal amount: "))
        interest_rate = int(input("Please enter the interest rate: "))
        time_period = int(input("Please enter the time period: "))
        interest_rate_decimal = (interest_rate/100)
        compound_interest = principal_amount * (1 + interest_rate_decimal) ** time_period
        interest_earned = compound_interest - principal_amount
        print(f"Compound Interest: {round(compound_interest)} \nInterest earned: {round(interest_earned)}")

# 2. Tracking inventory:
# Create a program for a small store that allows the store owner to continuously update the stock of items until they decide to stop. Use a while loop to repeatedly prompt  for item names and quantities.

warehouse_data = [
    {"product_name": "Product A", "inventory_level": 10},
    {"product_name": "Product B", "inventory_level": 5},
    {"product_name": "Product C", "inventory_level": 3},
]
low_inventory = 5
low_inventory_products = []

while True:
    user_choice = input("Do you want to enter inventory (y/n) :  ")
    if user_choice != "y":
        print("You are out.")
        break
    else:
        for product in warehouse_data:
            product_name = product["product_name"]
            inventory_level = product["inventory_level"]
            if inventory_level<=low_inventory:
                input_str = input("Enter a dictionary in the format key1:value1, key2:value2, ...: ")
                pairs = input_str.split(", ")
                input_dict = {}
                for element in pairs:
                    key, value = element.split(":")
                    input_dict[key] = value
                    low_inventory_products.append(input_dict)
                    print(input_dict, end='\n')
                print(f"Inventory {product_name} is low.")
        print("Products with low inventory levels:")
        for product in low_inventory_products:
            print(product)


stock = {}  # Dictionary to store the stock items and quantities

while True:
    item = input("Enter the item name (or 'q' to quit): ")

    if item.lower() == 'q':
        break

    quantity = int(input("Enter the quantity: "))

    stock[item] = stock.get(item, 0) + quantity

print("\nStock Updated:")
for item, quantity in stock.items():
    print(f"{item}: {quantity}")

# 3. Temperature conversion: Build a temperature conversion program that repeatedly asks the user for a temperature in Celsius and converts it to Fahrenheit using a while loop until the user indicates they are done.

while True:
    celsius = input("Enter a temperature in Celsius (or 'q' to quit): ")
    if celsius.lower() == 'q':
        break

    fahrenheit = (float(celsius) * 9 / 5) + 32
    print(f"{celsius}°C is equal to {fahrenheit}°F\n")
print("Temperature conversion program ended.")

# 4. Guessing game: Implement a number guessing game where the
# program generates a random number and prompts the user to guess it.
# The program should provide hints and continue until the user
# correctly guesses the number.

import random
number = random.randint(1, 100)

while True:
    user = int(input("Please enter the number: "))
    if user < number:
        print(f"Your number is less and actual number is {number} ")
    elif user > number:
        print(f"Your Number is greater and actual number is {number} ")
    else:
        print(f"Congratulations you number is  {user}  and actual number is {number} ")
        break
# 5. Countdown timer: Develop a countdown timer that
# asks the user to input the desired time in seconds and
# then counts down from that value to zero,
# displaying the remaining time after each second.

import time
#  Get user input for the desired time in seconds
seconds = int(input("Enter the desired time in seconds: "))
print("Countdown Timer Started!")
while seconds > 0:
    print(f"Remaining Time: {seconds} seconds")
    time.sleep(1)  # Pause the program for 1 second
    seconds -= 1

print("Countdown Timer Ended!")
# 6. Data validation: Create a program that asks the user for their age and verifies whether it is within a valid range (e.g., 18 to 65). If the age is not valid, keep prompting the user until a valid age is provided.

while True:
    age = int(input("Please enter your age: "))
    if age >= 18 and age <= 65:
        print(f"Your age is {age} and this is valid age.")
        break
    else:
        print(" You are under age.")

# 7. Password strength checker: Write a program that repeatedly asks
# the user to enter a password and checks its strength based on
# certain criteria (e.g., length, inclusion of special characters).
# The loop should continue until a strong password is entered.

password = input("Please enter the new password: ")
while True:
    for char in password:
        new = char.split()
        print(new, end=",")
    break


for article in articles:
    word = article.split()
    word_count = len(word)
    total_word_count += word_count


# 8. User input validation: Build a program that requests a positive integer from the user and continues to ask for input until a valid positive integer is provided.

while True:
    positive_integer = int(input("Please enter the positive integer: "))
    if positive_integer > 0:
        print("You have entered a right number")
        break
    else:
        print("You are the entering wrong number.")


# 9. Polling system: Design a polling system that allows users to vote for their favorite option. Use a while loop to continuously display the options and accept votes until the user decides to end the polling.
#
options = {}  # Dictionary to store the options and vote counts

print("Welcome to the Polling System!")

while True:
    print("\nOptions:")
    for option, count in options.items():
        print(f"{option}: {count} votes")

    print("\nMenu:")
    print("1. Add Option")
    print("2. Vote")
    print("3. End Polling")

    choice = input("Enter your choice: ")

    if choice == "1":
        new_option = input("Enter the new option: ")
        options[new_option] = 0
        print(f"Option '{new_option}' added.")

    elif choice == "2":
        vote_option = input("Enter the option you want to vote for: ")
        if vote_option in options:
            options[vote_option] += 1
            print(f"You voted for '{vote_option}'.")
        else:
            print("Invalid option. Please try again.")

    elif choice == "3":
        print("\nPolling Ended.")
        break

    else:
        print("Invalid choice. Please try again.")

print("\nPolling Results:")
for option, count in options.items():
    print(f"{option}: {count} votes")

# 10. Grade calculator: Develop a program that requests scores from a
# teacher and calculates the average grade for a class.
# The loop should continue until the teacher enters a
# specific termination code to indicate the end of data input.

enter_grade = {}
print("Welcome to HSCB School Grading System")
while True:
    print("Select the option according to your choice")

    for subject, grade in enter_grade.items():
        print(f"{subject}: {grade}")

    print("\nMenu:")
    print("1. Add subject")
    print("2. Add grades")
    print("3. Quit")

    choice = input("Enter your choice: ")

    if choice == '1':
        subjects = input("Enter the name of subject" )
        enter_grade[subjects] = 0
        print(f"Subjects '{subjects}' added.")

    elif choice == '2':
        grade = int(input("Enter the the grade: "))
        if grade in enter_grade:
            enter_grade[grade] += 1
            print(f"Your grades are {grade}")
        else:
            print("Invalid option")
    elif choice == '3':
        print(f"Thank you have entered {subjects} and {grade}")
    else:
        print("Invalid option")

for subject, grade in enter_grade.items():
    print(f"Thank you have entered {subjects} and {grade}")