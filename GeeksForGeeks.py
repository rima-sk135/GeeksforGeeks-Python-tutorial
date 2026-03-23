print("Hello World, I don't give a bug!")
#sample comment
#This is Python comment
""" this is a
multiline
 comment"""
name = "Geeks for Geeks"
print(name)

#DATA TYPES in Python - Numeric (Integer, Float, Complex no.); Dictionary; Boolean; Set; Sequence type (String, List, Tuple)..

x = "Hello World" # string
x = 50 # integer
x = 60.5 # float
x = 6j # complex number


x = ["geeks", "for", "geeks"] # list
x = {"geeks", "for", "geeks"} # set
x = {"name": "Rima", "age": "21"} # dict
x = ("geeks", "for", "geeks") # tuple
x = True # bool
x = b"Geeks" # binary
print(type(x))

# Input and output python prog
val = input("enter your value")
print("you entered: ", val)

#The input() function in Python always returns data as a string, regardless of what the user enters. If we want to store the input as another data type (like int, float, etc.), we need to explicitly convert (typecast) it.
name = input("enter your name: ")
print(type(name))
age = input("enter your age: ")
print(type(age))
#Now typecasting the age variable as an integer
age = int(input("Enter your age: "))
print(type(age))

#Python operators = Operators in Python are symbols used to perform operations on values and variables, such as calculations, comparisons, and logical checks.

#1. Arithmetic Operators: These are used to perform basic mathematical operations like addition, subtraction, multiplication, and division.
#Precedence of Arithmetic Operators are as follows: P - Parentheses E - Exponentiation M - Multiplication (Multiplication and division have the same precedence) 
# D - Division A - Addition (Addition and subtraction have the same precedence) S - Subtraction
a = 9
b = 4
add = a + b 
sub = a - b 
mul = a * b 
mod = a % b 
exp = a ** b 

print(add) 
print(sub) 
print(mul) 
print(mod) 
print(exp)

#2. Comparison Operators: These are used to compare two values. They return a Boolean value either True or False depending on whether the comparison is correct.
a = 10
b = 20

print(a == b)   # False, because 10 is not equal to 20
print(a != b)   # True, because 10 is not equal to 20
print(a > b)    # False, 10 is not greater than 20
print(a < b)    # True, 10 is less than 20
print(a >= b)   # False, 10 is not greater than or equal to 20
print(a <= b)   # True, 10 is less than or equal to 20
