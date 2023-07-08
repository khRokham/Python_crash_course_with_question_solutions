# 1. You have a website that requires a user to enter their age. Write a program that determines if the user is old enough to access certain content (age >= 18).
age = int(input("Enter your age: "))
if age >= 18:
    print("You can access the web content")
else:
    print("You are under age.")
# 2. Create a program for a movie ticket booking system. Implement an if-else statement to check if a user is eligible for a discounted ticket based on their age.
if age >=12 and age<=18:
    print("You can get discount of 10%")
else:
    print("No discount")
# 3. Write a program for a library that checks if a book is available based on the user's input (if book_available == True).
book_code = input("Please enter book code: ")
book_available = [234,455,876,890,678,456]

if book_code:
    if book_available==True:
        print("book is available")
    else:
        print("Books are not available")
else:
    print("Book not found in the database")
# 4. Implement a program for a restaurant that determines if a customer is eligible for a senior citizen discount (age >= 60).
if age >= 60:
    print("Customer is eligible for a senior citizen discount")
else:
    print("Customer is not eligible for a senior citizen discount")
# 5. Create a program for a store that calculates the total bill amount after applying a discount based on the customer's membership status (if member == True).
discounts = {
    "Regular": 0,
    "Silver": 10,
    "Gold": 20,
    "Platinum": 30
}
customer = input("Enter your type: ")
if customer in discounts:
    print("Customer can get discount of", discounts)
else:
    print("sorry no discount is available")
# 6. You have an online shopping platform. Write a program that checks if a product is in stock and updates the inventory accordingly (if in_stock == True).

product = {"name": "Laptop", "quantity": 5}

print(f"Product: {product['name']}")
print(f"Available Quantity: {product['quantity']}")

user_input = input("Press 'P' to purchase: ")
if user_input.lower() == 'p':
    if product["quantity"] > 0:
        product["quantity"] -= 1
        print("Product purchased. Inventory updated.")
    else:
        print("Product is out of stock.")

print(f"Updated Available Quantity: {product['quantity']}")

# 7. Implement a program for a banking system that checks if a customer's account balance is sufficient to make a withdrawal (if balance >= withdrawal_amount).

balance = 353
withdrawal_amount = int(input("Please enter withdrawal amount: "))
if balance > withdrawal_amount:
    remaining_balance = balance-withdrawal_amount
    print(f"Congradutation you have successfully withdrawal the amount of : {withdrawal_amount} and the remaining balane is {remaining_balance}")
else:
    print("insufficient balance")
# 9. Write a program for a travel agency that determines if a customer is eligible for a group discount based on the number of people in the booking (if num_people >= 5).
num_people = int(input("Enter the number of people: "))
if num_people>=5:
    print("customer is eligible for a group discount")
else:
    print("customer is not eligible for a group discount")
# 10. Implement a program for a car rental service that checks if a customer is eligible to rent a specific car model based on their age and driver's license validity.
age = int(input("Please enter your age: "))
driving_license = input("Press Y if you have driving license: ")

if age>=18:
    if driving_license.lower() == 'y':
        print("customer is eligible to rent a specific car model based on their age and driver's license validity ")
    else:
        print("customer is not eligible to rent a specific car model based on their age and driver's license validity")
else:
    print("customer is not eligible to rent a specific car model based on their age")



# 1. Implement a program for an e-commerce platform that calculates the final price of an order based on the product price, quantity, and applicable discounts (if discount_available == True).
product_price = int(input("Product price is: "))
quantity = int(input("Please enter the quantity: "))
applicable_discounts = 10

if product_price:
    if quantity >= 3:
        total_price = product_price*quantity
        discount = total_price * 0.1
        print(f"Your Discount is {discount} and you remaining  balance is {total_price - discount}")
    else:
        print("No discount available")
else:
    print("sorry!")

# 2. Write a program for a grading system that assigns letter grades to students based on their numerical score (if score >= 90: grade = 'A', elif score >= 80: grade = 'B', etc.).

score = int(input("Enter your score: "))
if score >= 90:
    print("Grade = 'A'")
elif score >= 80 and score <=89:
    print("Grade = 'B'")
elif score >= 70 and score <= 79:
    print("Grade = 'C'")
else:
    print("You are fail")

# 3. Create a program for a bank that determines if a customer is eligible for a loan based on their credit score, income, and existing debts (if loan_eligible == True).
#
credit_score = int(input("Please enter your credit score: "))
income = int(input("Please enter your income: "))
existing_debts = int(input("Please enter your existing_debts: "))
loan_eligible = True

minimum_credit_score = int(input("Please enter your minimum_credit_score: "))
minimum_income = int(input("Please enter your minimum_income: "))
maximum_debts = int(input("Please enter your maximum_debts: "))
if loan_eligible == True:
    loan_eligible = (credit_score >= minimum_credit_score) and (income >= minimum_income) and (existing_debts <= maximum_debts)
    print("you are eligible for loan")
else:
    print("You are not eligible for the loan")

# 4. Implement a program for a flight booking system that checks if a passenger is eligible for an upgrade to a higher class based on their frequent flyer status and seat availability (if frequent_flyer == True and seat_available == True).Input passenger details
frequent_flyer = input("Is the passenger a frequent flyer? (yes/no): ")
seat_available = input("Is there an available seat in the higher class? (yes/no): ")

# Check upgrade eligibility
upgrade_eligible = (frequent_flyer.lower() == "yes") and (seat_available.lower() == "yes")

# Display upgrade eligibility result
if upgrade_eligible:
    print("Congratulations! The passenger is eligible for an upgrade.")
else:
    print("Sorry, the passenger is not eligible for an upgrade.")


# 5. Write a program for a shipping company that determines the shipping cost based on the destination, weight, and dimensions of a package (if destination in special_zones and weight <= 20 and volume <= 500: apply_discount()).


# # Declaration of special zones
special_zones = ["Zone A", "Zone B", "Zone C"]

# Input package details
destination = input("Enter the destination: ")
weight = float(input("Enter the weight of the package (in kg): "))
volume = float(input("Enter the volume of the package (in cubic cm): "))

# Calculate the shipping cost (assuming a fixed cost for simplicity)
shipping_cost = 10.0  # Replace with actual shipping cost calculation

# Check if the destination is in special zones, weight is <= 20, and volume is <= 500
if destination in special_zones and weight <= 20 and volume <= 500:
    # Apply discount
    shipping_cost *= 0.9

# Display the shipping cost
print("The shipping cost is:", shipping_cost)



# 6. Create a program for a health app that assesses a user's BMI (Body Mass Index) and provides a health classification based on the BMI value (if bmi < 18.5: classification = 'Underweight', elif bmi < 25: classification = 'Normal weight', etc.).
bmi = int(input("Please enter your BMI: "))
classification = True
if bmi < 18.5:
    classification = 'Underweight'
elif bmi < 25:
    classification = 'Normal weight'
else:
    classification = 'Over Weight'

print(classification)

# 7. Implement a program for a car rental service
# that determines the rental price based on the car model, rental duration, and any additional services
# (if car_model in luxury_cars and duration > 7: apply_discount()).

luxury_cars = ['Rolls-Royce Phantom', 'Bentley Continental GT', 'Mercedes-Benz S-Class', 'BMW 7 Series', 'Audi A8', 'Porsche Panamera','Jaguar XJ'
               ,'Lexus LS', 'Aston Martin DB11', 'Maserati Quattroporte']
rental_price = int(input("PLease enter the rent: "))
car_models = input("Enter the car model: ").lower()
rental_durations = int(input("Enter rental duration: "))
apply_discount = 0
if car_models in [car.lower() for car in luxury_cars] and rental_durations > 7:
    apply_discount = rental_price * 0.3
    print(f"You got a discount of {apply_discount}")
else:
    print("Something is not working")
# 8. Write a program for a game that determines the player's rank based on their score and gameplay time (if score >= 1000 and time <= 60: rank = 'Master', elif score >= 500 and time <= 120: rank = 'Advanced', etc.).


score = int(input("Please Enter the score: "))
gameplay_time = int(input("Please enter gameplay time: "))
rank = True
# player_rank =
if score >= 1000 and gameplay_time <= 60:
    rank = 'Master'
elif score >= 500 and gameplay_time <= 120:
    rank = 'Advanced'
print(rank)

# 9. Create a program for a ticket booking system that checks if a selected seat is available for a specific event and reserves it for the user (if seat_available == True: reserve_seat()).

selected_seat = ['21a','34d','45f','56d']
seat_num = input("Enter seat number: ")
seat_available = True


if seat_num in selected_seat and seat_available ==True:
    selected_seat.remove(seat_num)
    print(f"Seat {seat_num} has been reserved.")
else:
    print("Sorry, the selected seat is not available.")

# 10. Implement a program for a restaurant ordering system that checks if a menu item is available and calculates the total bill based on the selected items and any applicable discounts (if item_available == True and discount_available == True).

menu_items = ['Burger', 'Pizza', 'Salad', 'Pasta', 'Sandwich', 'Soup']


select_item = input("Enter the item: ")
price = int(input("Enter the price: "))
discount_available = True
item_available = True
if select_item in menu_items and price>=0:
    discount_available = price * 0.1
    price -=discount_available
    print(f"Price after the discount {price}")
else:
    print("Not Satisfy")




# 2. Write a program for a social media platform that determines the user's account status (active, inactive, suspended) based on their login activity and violation history (if login_attempts <= 3 and violations == 0: account_status = 'Active', etc.).

account_status = ['active', 'inactive', 'suspended']
login_attempts = int(input("Enter login activity: "))
violations = int(input("Enter the violations: "))

if login_attempts <=3 and violations ==0:
    account_status = 'active'
elif login_attempts >= 3 and violations ==2:
    account_status = "inactive"
else:
    account_status = 'suspended'
print(account_status)
