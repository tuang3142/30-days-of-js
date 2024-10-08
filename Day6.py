#DAY 6 - TUPLES
#Exercises: Level 1 

#1. Create an empty tuple
empty_tuple = ()

#2. Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
my_bro = ('Tuan', 'Trung')
my_sis = ('Giang','Ha')

#3. Join brothers and sisters tuples and assign it to siblings
my_siblings = my_sis + my_bro 
print(my_siblings)
#4. How many siblings do you have? 
print(len(my_siblings))

#5. Modify the siblings tuple and add the name of your father and mother and assign it to family_members
my_siblings = list(my_siblings)
my_parents = ["Bay", 'Minh']
family_members = my_siblings + my_parents 
print(family_members) 

#Exercises: Level 2

#1.Unpack siblings and parents from family_members
a,b, *rest = family_members
print(a, b, rest)


#2. Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.

fruits = ('orange', 'apple', 'avocado', 'banana')
vegetables = ('spinach', 'morning slory', 'beetroot', 'cabbage')
animal_producs = ('meat', 'pork', 'egg', 'milk')
food_stuff_tp = fruits + vegetables + animal_producs 

#3. Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_tp = list(food_stuff_tp)

#4. Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
food_stuff_tp = food_stuff_tp[1:3]

#5.Slice out the first three items and the last three items from food_staff_lt list 
food_stuff_tp = food_stuff_tp[0:3]
food_stuff_tp = food_stuff_tp[-3:-1]

#6.Delete the food_staff_tp tuple completely
del food_stuff_tp 

#7. Check if an item exists in tuple:
   #Check if 'Estonia' is a nordic country
   #Check if 'Iceland' is a nordic country

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)