#   Built-in Functions
#   User-defined Functions
#   Recursive Functions
#   Lambda Functions
#   Higher-Order Functions
#   Generator Functions
#   Decorator Functions



# 1. Build a program that simulates a
# simple ATM transaction, allowing users to
# deposit, withdraw, and check their balance.

# def atm_transaction():
#     balance = 0  # Initial balance is set to 0
#
#     while True:
#         print("\nATM Transaction")
#         print("1. Deposit")
#         print("2. Withdraw")
#         print("3. Check Balance")
#         print("4. Exit")
#
#         choice = input("Enter your choice (1-4): ")
#
#         if choice == '1':
#             amount = float(input("Enter the amount to deposit: "))
#             balance += amount
#             print(f"You have successfully deposited {amount:.2f}")
#
#         elif choice == '2':
#             amount = float(input("Enter the amount to withdraw: "))
#             if amount <= balance:
#                 balance -= amount
#                 print(f"You have successfully withdrawn {amount:.2f}")
#             else:
#                 print("Insufficient balance. Withdrawal failed.")
#
#         elif choice == '3':
#             print(f"Your current balance is {balance:.2f}")
#
#         elif choice == '4':
#             print("Thank you for using the ATM. Goodbye!")
#             break
#
#         else:
#             print("Invalid choice. Please try again.")
#
# atm_transaction()

# 3. Design a program that generates a random password of a specified length, including a combination of uppercase letters, lowercase letters, numbers, and special characters.

# import random
# import string
#
# def password_generator(length):
#     uppercase_letter = string.ascii_uppercase
#     lowercase_letter = string.ascii_lowercase
#     number = string.digits
#     special_characters = string.punctuation
#     all_characters = uppercase_letter+lowercase_letter+number+special_characters
#     password = "".join(random.choice(all_characters) for _ in range(length))
#     return password
# def main():
#     length = int(input("How many number of password you need: "))
#     password = password_generator(length)
#     print(f'Generated Password: {password}')
# main()

# 4. Develop a program that calculates the total cost of a shopping cart, including discounts and taxes, given a list of items and their prices.

# def calculate_total_cost(items):
#     total = sum(price for _, price in items)
#     return total
#
# def apply_discount(total, discount):
#     discount_amount = (total * discount) / 100
#     discounted_total = total - discount_amount
#     return discounted_total
#
# def apply_tax(total, tax_rate):
#     tax_amount = (total * tax_rate) / 100
#     total_with_tax = total + tax_amount
#     return total_with_tax
#
# def shopping():
#     items = []
#     while True:
#         item_name = input("Enter the item name (or 'done' to finish): ")
#         if item_name.lower() == 'done':
#             break
#         item_price = float(input("Enter the item price: "))
#         items.append((item_name, item_price))
#
#     total_cost = calculate_total_cost(items)
#
#     discount = float(input("Enter the discount percentage: "))
#     total_cost_after_discount = apply_discount(total_cost, discount)
#
#     tax_rate = float(input("Enter the tax rate: "))
#     total_cost_with_tax = apply_tax(total_cost_after_discount, tax_rate)
#
#     print(f"\nShopping Cart Summary:")
#     print("================================")
#     for item_name, item_price in items:
#         print(f"{item_name}: ${item_price:.2f}")
#     print("================================")
#     print(f"Total Cost: ${total_cost:.2f}")
#     print(f"Discount: {discount}%")
#     print(f"Total Cost after Discount: ${total_cost_after_discount:.2f}")
#     print(f"Tax Rate: {tax_rate}%")
#     print(f"Total Cost with Tax: ${total_cost_with_tax:.2f}")
#
# shopping()



# 5. Implement a program that analyzes a
# text file and counts the occurrences of each word, displaying the top N most frequent words.
# import string
# def count_word_occurrences(file_path):
#     most_used_word = {}
#     try:
#         with open(file_path, 'r') as file:
#             for line in file:
#                 words = line.split()
#                 for word in words:
#                     most_used_word[word] = most_used_word.get(word,0)+1
#     except FileNotFoundError:
#         print("File not found.")
#         return
#     return most_used_word
#
# def count_char(file_path):
#     most_used_char = {}
#     try:
#         with open(file_path, 'r') as file:
#             text = file.read().lower()
#             text = text.translate(str.maketrans('','', string.punctuation+' '))
#             for char in text:
#                 most_used_char[char] = most_used_char.get(char,0)+1
#     except FileNotFoundError:
#         print("File not found.")
#         return
#     return most_used_char
# def main():
#     file_path = input('Enter the path to the text file: ')
#     most_used_word = count_word_occurrences(file_path)
#     most_used_char = count_char(file_path)
#
#     if most_used_word:
#         print("\nWord Count:")
#         print("===============================")
#         for word, count in most_used_word.items():
#             print(f"{word}: {count}")
#         print("===============================")
#     if most_used_char:
#         for char, count in most_used_char.items():
#             print(char, count)
#
#
# if __name__ == '__main__':
#     main()

# 7. Create a program that simulates a basic
# inventory management system, allowing users to
# add, remove, and update items in the inventory.

# inventory = {}
# def add_inventory():
#     add_inventory = input("Enter the item name: ")
#     quantity = int(input("Enter he quantity: "))
#     inventory[add_inventory] = quantity
#     print(f"{add_inventory} added to the inventory.")
# def remove_inventory():
#     remove_inventory = input("Enter the item name: ")
#     if remove_inventory in inventory:
#         del inventory[remove_inventory]
#         print(f"{remove_inventory} removed from the inventory.")
#     else:
#         print(f"{remove_inventory} not found in the inventory")
# def update_inventory():
#     update_inventory = input("Enter the update item: ")
#     if update_inventory in inventory:
#         quantity = int(input("Enter the new quantity: "))
#         inventory[update_inventory] = quantity
#         print(f"{update_inventory} quantiy updated in the inventory.")
#     else:
#         print(f"{update_inventory} not found in the inventory.")
#
# def inventory_management():
#     print("Current Inventory: ")
#     for item, quantity in inventory.items():
#         print(f"{item}: {quantity}")
# def main():
#     while True:
#         print("*****Inventory Management System*****")
#         print(f'Select Option')
#         print(f"======================"
#               f"\n1. ADD"
#               f"\n2. Remove"
#               f"\n3. Update"
#               f"\n4. Exit"
#               f"\n======================")
#         choice = int(input("Select option according to you choice:"))
#         if choice == 1:
#             add_inventory()
#         elif choice == 2:
#             remove_inventory()
#         elif choice == 3:
#             update_inventory()
#         elif  choice == 4:
#             print("Exiting program.")
#             break
#         else:
#             print("Thank you! now you are exit from inventory system")
#
# if __name__ == '__main__':
#     main()




# 8. Design a program that reads data from a CSV file
# and generates various statistical reports,
# such as average, maximum, and minimum values for different columns.
#
# import pandas as pd
#
# def report(data):
#     result = {}
#     for column in data.columns:
#         average = data["infant deaths"].mean()
#         maximum = data["infant deaths"].max()
#         minimum = data["infant deaths"].min()
#         result[column] = {'average': average, 'maximum': maximum, 'minimum': minimum}
#     return result, data
#
# def main():
#     data = pd.read_csv("/Users/mac/Desktop/Life Expectancy Data.csv")
#     result, data = report(data)
#     print("Result:")
#     print(result)
#     print("\nModified Data:")
#     print(data)
#
# if __name__ == "__main__":
#     main()

# 9. Develop a program that generates a weekly schedule for a school, given a list of courses, teachers, and time slots.
#

# extra = []
# def weekly_schedule(list_of_courses, list_of_teachers,time_slot):
#     for course in list_of_courses.split():
#         extra.append(course)
#     for teacher in list_of_teachers.split():
#         extra.append(teacher)
#     for time in time_slot.split():
#         if time == " ":
#             print("Please enter time in digits.")
#         else:
#             extra.append(time)
#
# def main():
#     list_of_courses = input("Enter name of courses: ")
#     list_of_teachers = input("Enter name of teachers: ")
#     time_slot = input("Enter name of time slots: ")
#     weekly_schedule(list_of_courses,list_of_teachers,time_slot)
#
#     # Accessing the elements in the 'extra' list
#     course = extra[0]
#     teacher = extra[1]
#     time_slot = extra[2]
#
#     print(f'The title of course is {course}, teacher is {teacher} and time slot is {time_slot}')
# main()

# def generate_schedule(courses, teachers, time_slots):
#     schedule = {}
#
#     # Check if the number of courses, teachers, and time slots are the same
#     if len(courses) == len(teachers) == len(time_slots):
#         for i in range(len(courses)):
#             course = courses[i]
#             teacher = teachers[i]
#             time_slot = time_slots[i]
#
#             # Add the course and its details to the schedule
#             if time_slot in schedule:
#                 schedule[time_slot].append((course, teacher))
#             else:
#                 schedule[time_slot] = [(course, teacher)]
#
#         return schedule
#     else:
#         print("Error: The number of courses, teachers, and time slots should be the same.")
#         return None
#
# def main():
#     # Input the list of courses, teachers, and time slots
#     courses = input("Enter the names of courses (separated by commas): ").split(",")
#     teachers = input("Enter the names of teachers (separated by commas): ").split(",")
#     time_slots = input("Enter the time slots (separated by commas): ").split(",")
#
#     # Generate the schedule
#     schedule = generate_schedule(courses, teachers, time_slots)
#
#     # Print the schedule
#     if schedule:
#         print("Weekly Schedule:")
#         for time_slot, course_teacher_list in schedule.items():
#             print(f"\n{time_slot}:")
#             for course_teacher in course_teacher_list:
#                 course, teacher = course_teacher
#                 print(f"Course: {course}, Teacher: {teacher}")
#     else:
#         print("Schedule generation failed.")
#
# main()


# 10. Implement a program that performs sentiment analysis on a collection of text documents, classifying them as positive, negative, or neutral.

# count = 0
# with open('/Users/mac/Desktop/all-data.csv', 'r', encoding='latin-1') as word_file:
#     for line in word_file:
#         columns = line.split(',')
#         if columns[0] == 'negative' or 'positive' or 'neutral':
#             count +=1
#
#
# print(count)









