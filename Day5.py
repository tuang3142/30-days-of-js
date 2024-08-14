#Day 5 - LISTS
#task 1 
empty_list = []

#task 2
new_list = ['I', 'fell', 'googley', 'coding', 'python']

#task 3
print(len(new_list))

#task 4
first_item, *middle_item, last_item = new_list
print(first_item, middle_item, last_item)

#task 5
mixed_data_types = ['Dat', 17, 185, 'single', 'Viet Nam']

#task 6, 7, 8, 9 
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', ' IBM', 'Oracle', 'Amazon']
print(it_companies)
print(len(it_companies))
first_company, *middle_company, last_company = it_companies
print(first_company, middle_company, last_company)

#task 10 
it_companies[4] = 'Samsung'
print(it_companies)
#task 11
it_companies.append('Spotify')
print(it_companies)

#task 12
it_companies.insert(3, 'Huawei')
print(it_companies)

#task 13
it_companies[1].upper()
print(it_companies)

#task 14
print(it_companies + ['#'])

#task 15
print('Facebook' in it_companies)

#task 16 
it_companies.sort()
print(it_companies)

#task 17
it_companies.reverse()
print(it_companies)

#task 18,19,20
print(it_companies[:3])
print(it_companies[-4:])
print(it_companies[2:6:1])

#task 21,22,23,24(just remove)
del it_companies[0]
print(it_companies)

#task 25 
it_companies.clear()
print(it_companies)

#task 26
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
joined_list = front_end + back_end
print(joined_list)

#task 27
full_stack = joined_list.copy()
full_stack.insert(6, 'Python')
full_stack.insert(7, 'SQL')
print(full_stack)


#EXERCISE LEVEL 2
#task 1
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
min_age = ages[0]
print(min_age)
max_age = ages[-1]
print(max_age)

ages.append(min_age)
ages.append(max_age)
print("Ages after adding min and max again:", ages)

ages.sort()
min_age = ages[0]
max_age = ages[-1]
#how to find the median age (one middle item or two middle items divided by two)

print('Average age:', sum(ages)/len(ages)) 

print('Range of ages:', max_age-min_age)

min_diff = abs(min_age - sum(ages)/len(ages))
max_diff = abs(max_age - sum(ages)/len(ages))
print("Absolute difference between min age and average age:", min_diff)
print("Absolute difference between max age and average age:", max_diff)


#task 2 
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
]
first_country, *middle_country, last_country = countries 
print(len(countries))

divided_list = countries[0:96]
print(divided_list)


new_countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
country_1, country_2, country_3, *scandic_countries = new_countries
print(country_1, country_2, country_3, scandic_countries)