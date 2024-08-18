# DAY 8 - DICTIONARIES 
#dictinary : unordered, changeable
 

#1. Create an empty dictionary called dog
#2. Add name, color, breed, legs, age to the dog dictionary
my_dog = {
    'name':'Bob',
    'breed':'shiba',
    'color':'yellow',
    'legs':'4',
    'age':'15'

}

print(my_dog)


#3. Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student_dic = {
    'first_name':'Dick',
    'last_name':'Black',
    'gender':'unknown',
    'age':'19',
    'marital_status':'single',
    'skills':['Python','java'],
    'country':'America',
    'city':'LA'
}
print(student_dic)

#4. Get the length of the student dictionary
print(len(student_dic))

#5. Get the value of skills and check the data type, it should be a list
print(type(student_dic['skills']))


#6. Modify the skills values by adding one or two skills
student_dic['skills'].extend(['JavaScript', 'HTML'])
print(student_dic)

#7. Get the dictionary keys as a list
print(student_dic.keys())

#8. Get the dictionary values as a list
print(student_dic.values() )

#9. Change the dictionary to a list of tuples using items() method
print(student_dic.items())

#10. Delete one of the items in the dictionary
del student_dic['marital_status']
print(student_dic)

#11. Delete one of the dictionaries
del student_dic
