
# 1. Print the numbers from 1 to 10.
for i in range(1, 10):
    print(i)

# 2. Print the square of the numbers from 1 to 5.
for x in range(1,6):
    print(x**2)

# 3. Print the even numbers from 1 to 20.
for num in range(1,20):
    if num>0 and num%2==0:
        print(num)
for num in range(2,21,2):
    print(num)
# 4. Print the sum of all the numbers from 1 to 100.
sum = 0
for num in range(1,101):
    sum += num
    print(sum)
# 5. Print the factorial of a given number.
given_number = int(input("Enter the Number: "))

if given_number <0:
    print("Factorial is not defined for negative numbers.")
else:
    result = 1
    for num in range(1, given_number+1):
        result *=num
    print(f"the number is {num} and {result}")

# 6. Print the Fibonacci sequence up to a certain limit.
limit = int(input("Enter the limit: "))
num1 = 0
num2 = 1
if limit >0:
    for _ in range( limit - 2):
        next_num = num1 + num2
        print(next_num)
        num1, num2 = num2, next_num
# 7. Print the multiplication table of a given number.
number = int(input("Please enter the number: "))

for num in range(1, 11):
    table = number*num
    print(f"{number} x {num} = {table} ")

# 8. Calculate the average of a list of numbers.

number = [5, 10, 34, 45, 32,56]

total = 0
count = len(number)
for num in number:
    total = total+num
average = total/count
print(average)

# 9. Print the uppercase letters of the alphabet.
alphabet = "there are Two Big Planes, One is Small and Other is big"

for char in alphabet:
    if char.isupper():
        print(char)
import string
uppercase_letter = string.ascii_uppercase
for letter in uppercase_letter:
    print(letter)


# 10. Print the ASCII values of all the lowercase letters.
import string
lowercase_letter = string.ascii_lowercase

for letter in lowercase_letter:
    ascii_values = ord(letter)
    print(letter, ascii_values)

# 11. Print the sum of all odd numbers from 1 to 50.
sum = 0

for sum_of in range(1,50,2):
    sum += sum_of
print(sum)

# 12. Print the reverse of a given string.
#
alphabet = "there are Two Big Planes, One is Small and Other is big"

for char in alphabet:
    reversed(char)
print(char)
text = input("Enter a string: ")
reverse_text = ""

for char in text:
    reverse_text = char + reverse_text

print("Reversed string:", reverse_text)

# 13. Print the common elements in two lists.
list1 = [1, 2, 'ert', '3df&', 675]
list2 = ['vfgg', 'sdfg', 34256, 9827, 1, 675]

common_elements = []
for element in list1:
    if element in list2:
        common_elements.append(element)
print("Common elements:", common_elements)

# 14. Print the prime numbers between 1 and 100.

for prime in range(1,101):
    is_prime = True
    for num in range(2,prime):
        if prime % num ==0:
            is_prime = False
            break
    if is_prime:
        print(prime)


# 15. Print the first n terms of the geometric progression.

first_term = float(input("Enter the first term: "))
common_ratio = float(input("Enter the common ratio: "))
num_terms = int(input("Enter the number of terms: "))

# Calculate and print the first n terms of the geometric progression
print("Geometric Progression:")
for i in range(num_terms):
    term = first_term * (common_ratio ** i)
    print(term)


# 16. Print the number of vowels in a given string.

given_string = input("Enter the string: ")
given_string.lower()
count  = 0

for vowels in given_string:
    if vowels in "aeiou":
        count += 1
print(count, end= ' ')

# 17. Print the elements of a list in reverse order.

elements_list = [12,32,'dfee','#453jsdfja',['sfs','dsfa',[1223,4567,56,],234],654]
for element in elements_list[::-1]:
    print(element, end=' ')
# 18. Calculate the sum of digits of a given number.

given_number = input("Enter the number: ")

sum=0

for digit in given_number:
    sum += int(digit)
print(sum, end=" ")
# 19. Print the ASCII art representation of a given symbol.
symbol = input("Enter a symbol: ")
#
# # Define the ASCII art patterns for different symbols
ascii_art = {
    "#": [
        "  ##",
        " ####",
        "######",
        " ####",
        "  ##"
    ],
    "@": [
        " @@@@ ",
        "@    @",
        "@ @@ @",
        "@    @",
        " @@@@ "
    ],
    "$": [
        "  $$$ ",
        "$ $   ",
        "  $$$ ",
        "   $ $",
        " $$$ "
    ],
    # Add more symbols and their respective ASCII art patterns as needed
}

# Print the ASCII art representation of the given symbol
if symbol in ascii_art:
    print("ASCII art representation for symbol", symbol)
    for line in ascii_art[symbol]:
        print(line)
else:
    print("ASCII art representation not available for symbol", symbol)


# 20. Print a pattern of asterisks in a triangle shape.
rows = int(input("Enter the number of rows: "))

# Print the triangle pattern
for i in range(1, rows + 1):
    for j in range(i):
        print("*", end=" ")
    print()


# 1. Calculate the total sales for each product category in a dataset.
# Sample dataset (replace with your actual dataset)
dataset = [
    {"product": "Product A", "category": "Category 1", "sales": 100},
    {"product": "Product B", "category": "Category 2", "sales": 150},
    {"product": "Product C", "category": "Category 1", "sales": 200},
    {"product": "Product D", "category": "Category 3", "sales": 75},
    {"product": "Product E", "category": "Category 2", "sales": 300},
]

category_sale = {}

for data in dataset:
    category = data["category"]
    sales = data["sales"]
    category_sale[category] = category_sale.get(category,0)+sales
print("Sales for each product category:")
for category,sales in category_sale.items():
    print(category,':', sales)

# 2. Find the average daily website traffic for each month.
traffic = {}
dataset = [
    {"Month": "January",  "Pageviews": 1000, "Unique_Visitors": 800, "Bounce_Rate": 0.35, "Average_Time_on_Page": '12:02:30 AM'},
    {"Month": "January",  "Pageviews": 1200, "Unique_Visitors": 950, "Bounce_Rate": 0.32, "Average_Time_on_Page": '12:03:10 AM'},
    {"Month": "January", "Pageviews": 950, "Unique_Visitors": 780,  "Bounce_Rate": 0.38, "Average_Time_on_Page": '12:02:45 AM'},
    {"Month": "February", "Pageviews": 1100, "Unique_Visitors": 850, "Bounce_Rate": 0.34, "Average_Time_on_Page": '12:02:55 AM'},
    {"Month": "February","Pageviews": 1300, "Unique_Visitors": 980, "Bounce_Rate": 0.31, "Average_Time_on_Page": '12: 03:25 AM'},
    {"Month": "February", "Pageviews": 900, "Unique_Visitors":  720,  "Bounce_Rate": 0.37, "Average_Time_on_Page": '12:02:40 AM'},
    {"Month": "March", "Pageviews": 1150, "Unique_Visitors": 880, "Bounce_Rate": 0.33, "Average_Time_on_Page": '12:03:05 AM'},
    {"Month": "March", "Pageviews": 1400, "Unique_Visitors": 1050,"Bounce_Rate": 0.29, "Average_Time_on_Page": '12:03:40 AM'},
    {"Month": "March", "Pageviews": 920, "Unique_Visitors": 760,  "Bounce_Rate": 0.36, "Average_Time_on_Page": '12:02:50 AM'}
]
for website_traffic in dataset:
    monthly_traffic = website_traffic["Month"]
    pageviews = website_traffic["Pageviews"]
    unique_visitors = website_traffic['Unique_Visitors']
    bounce_rate = website_traffic["Bounce_Rate"]
    average_time_on_page = website_traffic["Average_Time_on_Page"]
    traffic[monthly_traffic] = traffic.get(monthly_traffic,0)+pageviews
print("Sales for each product category:")
for monthly_traffic,pageviews in traffic.items():
    print(monthly_traffic,':', pageviews)


# Define a dictionary with the total monthly traffic for each month
monthly_traffic = {
    "January": 50000,
    "February": 60000,
    "March": 55000,
    # Add more months and corresponding traffic values
}

# Define a dictionary with the number of days in each month
days_in_month = {
    "January": 31,
    "February": 28,
    "March": 31,
    # Add more months and corresponding days
}

# Calculate the average daily traffic for each month
average_daily_traffic = {}

for month, traffic in monthly_traffic.items():
    days = days_in_month[month]
    average_daily_traffic[month] = traffic / days

# Print the average daily traffic for each month
for month, average_traffic in average_daily_traffic.items():
    print(f"Average Daily Traffic in {month}: {average_traffic:.2f}")


# 9.Calculate the total expenses for each department in a financial dataset.
total_expenses = [
    {"Marketing": 1000},
    {"HR": 500},
    {"IT": 800},
    {"Marketing": 1500},
    {"IT": 1200},
    {"HR": 900}
]
total_financial_expenses = {}

for department in total_expenses:
    for department_name, expense in department.items():
        total_financial_expenses[department_name] = total_financial_expenses.get(department_name, 0)+expense

# Print the total expenses for each department
for department, expense in total_financial_expenses.items():
    print(f"{department}: {expense}")

# 10. Extract the names of all products with low inventory levels in a warehouse dataset.
warehouse_data = [
    {"product_name": "Product A", "inventory_level": 10},
    {"product_name": "Product B", "inventory_level": 5},
    {"product_name": "Product C", "inventory_level": 3},
    # ... more products
]

low_inventory = 5
low_inventory_products = []

for product in warehouse_data:
    product_name = product["product_name"]
    inventory_level = product["inventory_level"]
    if inventory_level<=low_inventory:
        low_inventory_products.append(product_name)
        print(f"Inventory {product_name} is low.")
print("Products with low inventory levels:")
for product in low_inventory_products:
    print(product)
# 11. Calculate the total hours worked by employees in different roles.
employee_data = [
    {"name": "Employee A", "role": "Manager", "hours_worked": 40},
    {"name": "Employee B", "role": "Engineer", "hours_worked": 35},
    {"name": "Employee C", "role": "Manager", "hours_worked": 45},
    {"name": "Employee D", "role": "Technician", "hours_worked": 30},
    # ... more employee data
]
total_hours_worked = {}

for employees in employee_data:
    name = employees['name']
    role = employees['role']
    hours_worked = employees['hours_worked']
    # total_hours_worked[role] = total_hours_worked.get(role,0)+hours_worked
    if role in total_hours_worked:
        total_hours_worked[role] += hours_worked
    else:
        total_hours_worked[role] = hours_worked
for role, hours_worked in  total_hours_worked.items():
    print(f"Total hours worked by {role}s : {hours_worked}")

# 12. Determine the highest and lowest sales recorded for each region in a dataset.
sales_data = [
    {"region": "North", "sales_amount": 1000},
    {"region": "North", "sales_amount": 1200},
    {"region": "South", "sales_amount": 800},
    {"region": "South", "sales_amount": 1500},
    {"region": "East", "sales_amount": 900},
    {"region": "East", "sales_amount": 700},
    # ... more sales data
]

sales_by_region = {}

for sales in sales_data:
    region = sales['region']
    sales_amount = sales['sales_amount']
    if region in sales_by_region:
        if sales_amount > sales_by_region[region]["highest"]:
            sales_by_region[region]["highest"] = sales_amount
        elif sales_amount < sales_by_region[region]["lowest"]:
            sales_by_region[region]['lowest'] = sales_amount
    else:
        sales_by_region[region] = {"highest": sales_amount, "lowest": sales_amount}
# Print the highest and lowest sales by region
for region, sales_info in sales_by_region.items():
    highest_sales = sales_info["highest"]
    lowest_sales = sales_info["lowest"]
    print(f"Region: {region}")
    print(f"Highest Sales: {highest_sales}")
    print(f"Lowest Sales: {lowest_sales}")
    print()

# 13. Extract the steps of a process from a sequence of events.
import re
event_sequence = [
    '1. Start the machine',
    '2. Load raw material',
    '3. Set the operating parameters',
    '4. Begin the production',
    '5. Monitor the process',
    '6. Stop the machine'
]

process_steps = []
pattern = r'\d+\. (.+)'  # Assuming the steps are numbered with digits and a dot

for event in event_sequence:
    match = re.match(pattern, event)
    if match:
        process_steps.append(match.group(1))
print(process_steps)

# 14. Calculate the total cost of marketing campaigns, including ad spend and creative production.
campaign_costs = [
    {"ad_spend": 5000, "creative_production": 3000, "other_expenses": 1000},
    {"ad_spend": 4000, "creative_production": 2500, "other_expenses": 800},
    {"ad_spend": 6000, "creative_production": 3500, "other_expenses": 1200}
]

total_cost = 0

for campaign in campaign_costs:
    ad_spend = campaign['ad_spend']
    creative_production = campaign['creative_production']
    other_expenses = campaign['other_expenses']
    campaign_cost = ad_spend+creative_production+other_expenses

    total_cost += campaign_cost

print(total_cost)


# 15. Extract the titles of all books in a library database.


# 16. Calculate the total word count of articles in a content management system.

articles = [
    "This is the first article.",
    "The second article is a bit longer.",
    "The third article has the most words among all."
]

total_word_count = 0

for article in articles:
    word = article.split()
    word_count = len(word)
    total_word_count += word_count

print(total_word_count)
total_character_count = 0
for char in articles:
    character_count = len(char)  # Count the number of characters in the article
    total_character_count += character_count  # Add the character count to the total

print("Total character count of articles:", total_character_count)

# 17. Extract the names of all attendees from event registration data.
registration_data = [
    {"name": "John Doe", "email": "john@example.com", "ticket_type": "VIP"},
    {"name": "Jane Smith", "email": "jane@example.com", "ticket_type": "Regular"},
    {"name": "Alex Johnson", "email": "alex@example.com", "ticket_type": "Regular"},
    # Additional registration entries...
]
attendee_names = []

for registration in registration_data:
    attendee_name = registration["name"]
    attendee_names.append(attendee_name)

print("Attendee names:")
for name in attendee_names:
    print(name)
# 18. Determine the average rating of products based on customer feedback in a review dataset.

review_data = [
    {"product_id": 1, "rating": 4.5, "review": "Great product overall."},
    {"product_id": 2, "rating": 3.8, "review": "Could be better."},
    {"product_id": 1, "rating": 4.2, "review": "Satisfied with the purchase."},
    # Additional review entries...
]

total_rating = 0
review_count = len(review_data)

for review in review_data:
    rating = review['rating']
    total_rating += rating
    average_rating = total_rating/review_count
print(average_rating)

# 19. Extract the details of all orders with specific characteristics in an e-commerce dataset.
# 20. Calculate the total profit for each product category in a sales dataset.
# 21. Extract the names of all songs in a music streaming dataset.
# 22. Determine the average performance score of employees in different departments.
# 23. Extract the details of all customers who made a purchase from a CRM database.
# 24. Calculate the total time spent on different projects in a project management dataset.
# 25. Extract the names of all cities from a geographical dataset.
# 26. Determine the average rating of movies based on user ratings in a movie database.
# 27. Extract the names of all artists from a music streaming dataset.
# 28. Calculate the total cost of materials for different construction projects in a dataset.
# 29. Extract the details of all patients from a healthcare database.
# 30. Determine the average salary of employees in different job roles.
# 31. Extract the names of all participants from event attendance data.
# 32. Calculate the total distance covered by athletes in different sports events.
# 33. Extract the details of all students from a school database.
# 34. Determine the average price of products in different categories in an e-commerce dataset.
# 35. Extract the names of all actors from a movie database.
# 36. Calculate the total revenue generated by a business in different regions in a sales dataset.
# 37. Extract the titles of all articles from a magazine dataset.
# 38. Determine the average rating of restaurants based on customer reviews in a restaurant review dataset.
# 39. Extract the details of all transactions from a bank statement dataset.
# 40. Calculate the total quantity of items sold for different product categories in an e-commerce dataset.
# 41. Extract the names of all players from a sports team dataset.
# 42. Determine the average age of employees in different departments.
# 43. Extract the names of all attendees from conference registration data.
# 44. Calculate the total distance traveled by delivery vehicles in different regions in a logistics dataset.
# 45. Extract the details of all customers from a retail store database.
# 46. Determine the average rating of products based on user feedback in a product review dataset.
# 47. Extract the names of all tracks from a music album dataset.
# 48. Calculate the total cost of supplies for different school semesters in an education dataset.
# 49. Extract the details of all patients from a medical clinic database.
# 50. Determine the average score of students in different subjects.
