#Day 3 - Operators
#task 1 
my_age = 18

#task 2 
my_height = 1.83 

#task 3
com_num = 1 + 3j

#task 4 
triagle_base = float(input())
triagle_height = float(input())
triagle_area = triagle_base * triagle_height * 0.5
print('The area of the triangle is', triagle_area)

#task 5,6,7 same as task 4

#task 8 & 9 : Wtf is the slope ? 
x = int(input())
y = 2 * x - 2
z = int(input())
t = 2 * z - 2
point_A = x, y 
point_B = z, t 
slope = (t - y) / (z - t)   #What if happen division by zero ?
print(slope)

#task 10 
#task 11 
X = int(input())
Y = X ** 2 + 6 * X + 9
print(Y)

#task 12
var_1 = len("python")
var_2 = len("dragon")
print(var_1 > var_2)
 
#task 13 
print("on" in "python" and 'on' in "dragon") 

#task 14 same as task 13
#task 15
print(not("on" in "python" and 'on' in "dragon"))


#task 16
print(float(var_1))
print(str(var_1))


#task 17 (Wtf must to use If else loop) 
even_number = int(input())
print(even_number % 2 == 0)


#task 18 
a = 7 // 3
b = int(2.7) 
print(a == b)


#task 19
print(type(10) == type('10'))

#task 20
print(int('9.8') == 10)

#task 21 
m = int(input("Hours:"))
n = float(input("rate per hour:"))
print("Your weekly earning", m * n) 

#task 22
j = float(input('number of years you have lived:'))
k = j * 365 * 24 * 60 * 60 
print("You have lived for", ' ', k, 'seconds')

#task 23



