# devika_basics.py - Munnabhai teaches Devika Python basics
print("Hello Devika, Aarush ka bhai Munnabhai bolta hai!")

# Basic math
a = 5  # Variable - jaise Aarush ka luck
b = 3  # Devika ka charm
print("5 + 3 =", a + b)  # 8
print("5 - 3 =", a - b)  # 2
print("5 * 3 =", a * b)  # 15
print("5 / 3 =", a / b)  # 1.666...

# Variables
name = "Devika"
age = 25
print(f"Mera naam {name} hai, umar {age} hai!")

# Data types
string_var = "Devika"      # String
int_var = 25              # Integer
float_var = 5.5           # Float
bool_var = True           # Boolean
print("Types:", type(string_var), type(int_var), type(float_var), type(bool_var))

# Type conversion
age_str = str(int_var)    # Int to string
height_int = int(float_var)  # Float to int
print("Age as string:", age_str)
print("Height as int:", height_int)

# String manipulation
greeting = "Hello " + string_var + "!"
upper_name = string_var.upper()
print(greeting)          # Hello Devika!
print(upper_name)        # DEVIKA
print("Length of name:", len(string_var))  # 6