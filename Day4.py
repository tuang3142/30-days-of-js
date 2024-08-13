#DAY 4 - STRINGS
#task 1
var_1 = ['Thirty', 'Days', 'Of', 'Python' ]
concatenate_var_1 = ' '.join(var_1)
print(concatenate_var_1)

#task 2 same as task 1
#task 3 
my_company = 'Coding For All'

#task 4
print(my_company)

#task 5
print(len(my_company))

#task 6
print(my_company.upper())

#task 7
print(my_company.lower())

#task 8
print(my_company.capitalize())
print(my_company.swapcase())
print(my_company.title())

#task 9
print(my_company[0])

#task 10
print(my_company.index('Coding',0, 8)) 

#task 11
my_language = my_company.replace('Coding For All', 'Python')
print(my_language)

#task 12
print(my_language.replace('Python', 'Everyone to Python for All ')) 

#task 13
print(my_company.split(' '))

#task 14
big_tech = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" 
print(big_tech.split(', '))

#task 15,16,17
print(my_company[0])
print(my_company[-1])
print(my_company[10])

#task 18, 19
sentence = 'Python For Everyone'
acronym = sentence[0:6:6] + sentence[7:10:3] + sentence[11:18:8]
print(acronym)


#task 20,21
print(my_company.index('C'))
print(my_company.index('F'))

#task 22
phrase_1 = 'Coding For All People'
print(phrase_1.rfind('l'))

#task 23,24
phrase_2 = "\'You cannot end a sentence with because because because is a conjunction\'"
print(phrase_2.index('because'))
print(phrase_2.rindex('because'))

#task 25,26,27
print(phrase_2[32:48]) #Why is there only 2 'because' when running the code?

#task 28,29
print(my_company.startswith("Coding"))
print(my_company.endswith('coding'))

#task 30
my_company_2 = '   Coding For All      ' 
print(my_company_2.strip())

#task 31 - nothing to do
#task 32
python_libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print(' '.join(python_libraries))

#task 33
print('I am enjoying this challenge.\nI just wonder what is next.')

#task 34 
print('Name\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki')

#task 35
radius = 10
area = 3.14 * radius ** 2
print("The area of a circle with radius {} is {} meters square.".format(radius, area))

#task 36
a = 8 
b = 6
print(f'{a} + {b} = {a +b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} * {b} = {a * b}')
print(f'{a} / {b} = {a / b:.2f}')
print(f'{a} % {b} = {a % b}')
print(f'{a} // {b} = {a // b}')
print(f'{a} ** {b} = {a ** b}')
