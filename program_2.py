#Nathan Parker
#2/4/25
#Program #2: Age Classifier

#get the age of the user
age = int(input('Enter your age: '))

#determine into which catagory the user's age falls
if age <= 1:
    print('You are an infant.')
elif age > 1 and age < 13:
    print('You are a child.')
elif age >= 13 and age < 20:
    print('You are a teenager.')
else:
    print('You are an adult.')
