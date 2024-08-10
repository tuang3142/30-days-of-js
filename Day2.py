#Day 2 - Variables, Builtin Functions
#THIS IS EXERCISES LEVEL 1
first_name = 'Dat'
last_name = 'Nguyen'
full_name = first_name +" "+ last_name 
my_country = 'Viet Nam'
my_age = '17'
is_married = False
full_name, my_age, my_country, is_married = first_name +" "+ last_name, '17', 'Viet Nam', False


#THIS IS EXERCISE LEVEL 2
#task 1,2,3
print(type(my_age))
print(len(first_name))
print(len(last_name))

#task 4
num_one = 5
num_two = 4
print(num_one - num_two)
print(num_one + num_two)
print(num_one * num_two)
print(num_one / num_two)
print(num_one % num_two)
print(num_one ** num_two)
print(num_one // num_two)

#task 5
circle_radius = float(input()) 
area_of_circle = 3.14 * (circle_radius**2)
print(area_of_circle)
circum_of_circle = 2 * 3.14 * circle_radius
print(circum_of_circle)

#task 6 
First_name = str(input())
Last_name = str(input())
Country = str(input())
Age = str(input())
print("This is", First_name, Last_name, 'from', Country, 'He is', Age)

#THE END
