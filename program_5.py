#Nathan Parker
#2/4/25
#Program #5: Hot Dog

#define variables
cheese = ''
peppers = ''
grilled_onions = ''

#get the type of hot dog that the user wants
hot_dog_type = input('Would you like a "hot dog" ($3.50) or a "chili dog" ($4.50)?: ')

#if the user wants a hot dog, note the price and ask what toppings the user wants
if hot_dog_type == 'hot dog':
    hot_dog_price = 3.50
    cheese = input('Would you like cheese ($0.50) on your hot dog? (yes or no): ')
    peppers = input('Would you like peppers ($0.75) on your hot dog? (yes or no): ')
    grilled_onions = input('Would you like grilled onions ($1.00) on your hot dog? (yes or no): ')
else:
    hot_dog_price = 0

#if the user wants a chili dog, note the price and ask what toppings the user wants
if hot_dog_type == 'chili dog':
    chili_dog_price = 4.50
    cheese = input('Would you like cheese ($0.50) on your chili dog? (yes or no): ')
    peppers = input('Would you like peppers ($0.75) on your chili dog? (yes or no): ')
    grilled_onions = input('Would you like grilled onions ($1.00) on your chili dog? (yes or no): ')
else:
    chili_dog_price = 0

#if the user wants cheese, note the price
if cheese == 'yes':
    cheese_price = 0.50
else:
    cheese_price = 0

#if the user wants peppers, note the price
if peppers == 'yes':
    peppers_price = 0.75
else:
    peppers_price = 0

#if the user wants grilled onions, note the price
if grilled_onions == 'yes':
    grilled_onions_price = 1.00
else:
    grilled_onions_price = 0

#calculate the cost by adding up the noted prices
hot_dog_cost = hot_dog_price + chili_dog_price + cheese_price + peppers_price + grilled_onions_price

#calculate the tax
tax = 0.07 * hot_dog_cost

#calculate the total cost
total_cost = hot_dog_cost + tax

#print the calculated information for the user
print(f'''Hot Dog Cost: ${hot_dog_cost:,.2f}
Tax: ${tax:,.2f}
Total Cost: ${total_cost:,.2f}''')
