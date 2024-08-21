#Day 10 - Loops
#BONUS : the last exercise in Day 3
for number in range(1,6):
    print(number, number ** 0, number ** 1 ,number ** 2, number ** 3)

#DAY 10 : EXERCISES
    #Exercises: Level 1
        #1. Iterate 0 to 10 using for loop, do the same using while loop.
for number in range (11):
    print(number)

        #2. Iterate 10 to 0 using for loop, do the same using while loop.
for number in range(10,-1,-1):
    print(number)  #need to explain how while loops work ? 
#3.
print('TASK 3:')
for i in range(8):
    print('#' * i)

#4. Use nested loops to create the following: 
print('TASK 4:')
for i in range(9):
    print('#' * 8) #how to nest the loop in this situation ? 

#5. Print the following pattern:
print('TASK 5:')
for a in range (11):
    print(f"{a} * {a} = {a ** 2} ")

#6. Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.
print('TASK 6:')
for lst in ['Python', 'Numpy','Pandas','Django', 'Flask']:
    print(lst)

#7. Use for loop to iterate from 0 to 100 and print only even numbers
#8. Use for loop to iterate from 0 to 100 and print only odd numbers

print('TASK 7 and 8:')
print('\nEven nums:')
for even in range (101):
    if even % 2 == 0:
        print(even)
print('\nOdd nums:')
for odd in range(101):
    if odd %2 != 0 :
        print(odd) 
print("THE END OF EXERCISE LEVEL 1 ")

#EXCERCISE LEVEL 2
#1. Use for loop to iterate from 0 to 100 and print the sum of all numbers.
print('\nTASK 1 - LEVEL 2')
sum = 0
for i in range(101):
    sum += i
print('The sum of all numbers is',sum)

#2. Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.
print('\nTASK 2- LEVEL 2')
even_sum = 0
odd_sum = 0
for i in range(101):
    if i % 2 == 0:
        even_sum += i
    else:
        odd_sum += i  
print('The sum of all evens is', even_sum, '.And the sum of all odds is', odd_sum)



#LEVEL 3
print('\nTASK 1 - EXCERCISE LEVEL 3')
countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
];
#1 Go to the data folder and use the countries.py file. Loop through the countries and extract all the countries containing the word land. 
land_coun = []
for country in countries:
    if 'land' in country:
        land_coun.append(country)
print(land_coun)
#2.This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop 
print('\nTASK 2 - EXCERCISE LEVEL 3')

fruit_list  = ['banana', 'orange', 'mango', 'lemon']
reverse_list = []
for i in range(len(fruit_list) -1, -1, -1):
    reverse_list.append(fruit_list[i])
print(reverse_list)

print('\n TASK 3 - LEVEL 3') #funkin' long data, take a look 


        







