#DAY 9 - CONDITIONALS

#Exercises: Level 1
#1. Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. Output:
    #Enter your age: 30
    #You are old enough to learn to drive.
    #Output:
    #Enter your age: 15
    #You need more years to learn to drive.
your_age = int(input('Enter your age: '))
if your_age >= 18:
    print('You are old enough to learn to drive.')
else:
    print('You need more years to learn to drive.')

#2. Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age. Output:
    #Enter your age: 30
    #You are 5 years older than me.
my_age = 18
if your_age > my_age:
    difference = your_age - my_age
    if difference == 1:
        print("You are 1 year older than me.")
    else:
        print(f'You are {difference} years older than me')
elif your_age < my_age:
    difference = my_age - your_age
    if difference == 1:
        print("I am 1 year older than you.")
    else:
        print(f'You are {difference} years younger than me')
else: 
    print('We are the same age')



#3. Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b. Output:
    #Enter number one: 4
    #Enter number two: 3
    #4 is greater than 3
a = int(input('Enter number one: '))
b = int(input('Enter number two: '))
if a > b:
    print(f"{a} is greater than {b}") 
else: 
    print(f"{a} is not greater than {b}")



#Exercise lever 2 
#1. Write a code which gives grade to students according to theirs scores:
 #90-100, A
 #70-89, B
 #60-69, C
 #50-59, D
 #0-49, F
grade = int(input('Student\'s grade:'))
if 90 <= grade <= 100:
    print('A')
elif 70 <= grade <= 89:
    print('B')
elif 60 <= grade <= 69:
    print('C')
elif 50 <= grade <= 59:
    print('D')
else:
    print('F')

#2.Check if the season is Autumn, Winter, Spring or Summer. If the user input is: September, October or November, the season is Autumn. December, January or February, the season is Winter. March, April or May, the season is Spring June, July or August, the season is Summer

month = str(input('What month is it now?')).capitalize()
if month in ["September", "October", 'November']:
    print('the season is Autumn')
elif month in ['December', 'January', 'February']:
    print("The season is Winter.")
elif month in ['March', 'April', 'May']:
    print("The season is Spring.")
else:
    print("The season is Summer.")


#3. The following list contains some fruits:

fruits = ['banana', 'orange', 'mango', 'lemon']
    #If a fruit doesn't exist in the list add the fruit to the list and print the modified list. If the fruit exists print('That fruit already exist in the list')
your_fruit = str(input('New fruit:'))
if your_fruit in fruits:
    print('That fruit already exist in the list')
else:
    fruits.append(your_fruit)
    print(fruits)

#Exercises: Level 3

person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }
#* Check if the person dictionary has skills key, if so print out the midle skill in the skills list.
if 'skills' in person:
    skills = person['skills']
    middle = len(skills) // 2
    print(f'Middle skill: {skills[middle]} ')
    
#* Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
if 'Python' in person['skills']:
    print('Python')
#* If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'), 
if list(skills) == ['JavaScript', 'React']:
    print('He is a front end developer')
elif list(skills) == ['Node', 'Python', 'MongoDB']:
    print('He is a backend developer')

# if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!
if ['React', 'Node', 'MongoDB'] in person['skills']:
    print('He is a fullstack dev')
else:
    print('unknown title') 

# If the person is married and if he lives in Finland, print the information in the following format:
if person['is_married'] == True and person['country'] == 'Finland':
    print('Asabeneh Yetayeh lives in Finland. He is married.') 
