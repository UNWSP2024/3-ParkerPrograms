#Nathan Parker
#2/4/25
#Program #3: Shipping Charges

#get the weight of the item from the user
weight = float(input('Enter the weight of the item in pounds: '))

#determine into which catagory the weight falls
if weight <= 2:
    price = weight * 1.50
elif weight > 2 and weight <= 6:
    price = weight * 3.00
elif weight > 6 and weight <= 10:
    price = weight * 4.00
else:
    price = weight * 4.75

#display the shipping price
print(f'The shipping price is ${price:,.2f}.')
