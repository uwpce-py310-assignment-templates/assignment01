#1
my_string = "Hello"
my_integer = 10
my_float = 9.9

#2
a = 100
b = 200
c = a + b
#c should be 300
print (c)

#3
d = 1.1
e = 2.2
f = d + e
#f should be 3.3
print (f)

#4
string_1 = 'A'
string_2 = 'B'
#string_3 should be AB
string_3 = string_1 + string_2 

print (string_3)

#5
#answer5 should be 101.1
answer5 = a + d 

print(answer5)
#answer5 should be float

#6
answer6 = my_string + str(my_integer) #answer6 should be Hello10

print (answer6)
#asnwer6 is Hello10 because I convert interger to string type using str function.

def print_out(x):
    return str(x) + " is " + str(type(x))
    

print(print_out(my_string))
print(print_out(my_integer))
print(print_out(my_float))

my_string_integer = "10"

print(print_out(my_string_integer))
my_integer_from_string = int(my_string_integer)
print(print_out(my_integer_from_string))
task_3= round(5*7.654321,3)
print(task_3)

#task4
my_name = input("Enter your name ")
print("my name is: " + my_name)

#task5
favorite_number = input("Enter your favorite_number ")
print("favorite_number is " + favorite_number)
#I expect it's type String
print(print_out(favorite_number))

#favorite_number is type string because input function return type string.  We shouldn't expect integer or float because of object/variable's name.

#task6
number_1 = int(input("Enter your first number "))
number_2 = int(input("Enter your second number "))
number_3 = number_1 + number_2
#number_3 should be total of number_1 and number_2 and should be integer
print(number_3)
print("number_3 is " + str(number_3))
