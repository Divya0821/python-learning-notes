# this is called comment
#python doesn't print this line
# called as pound or hashtag
#This is my first python program
print("I love tulips")
print("they are beautiful")

# variables= a reusable container for a value (string, integer, float, boolean)
# a variable behaves as if was the value it contains
# each variable should contain a unique variable name
# to assign a variable we use assignment =

# strings
#  A string is a series of character, it can include numbers but you treat them as characters like in email we have number treated as char
first_name = "sri"
Food = "pizza"
email = "sri0099@gmail.com"
# you can use single quotes ' ' or double quotes " "
print(first_name)
print("first_name")
# in second case print you literally print first_name as you use " " in the print function we don't use " for variable
# u can use your variable along with text using f string
# f-string formatted string begin with a string with f or F before the opening quotation mark or triple quotation mark. Inside this string, you can write a python expression between { and } characters that can refer to variables or literal values
print(f"Hello {first_name}")
print(f"you like {Food}")
print(f"your email is: {email}")


# Integers
# An integers is a whole number
# your integer should not be in a quote technically if it's in quote then it will be a string

age = 23
quantity = 5 # no decimal otherwise it will be float
num_of_students = 30

print(f"you are {age} years old")
print(f"You are buying {quantity} items")
print(f"your class has {num_of_students} students")


#Float is a number contains a decimal portion or value

price = 10.54
gpa = 3.5
distance = 5.5

print(f"The price is ${price}")
print(f"Your gpa is: {gpa}")
print(f"You ran {distance}km ")


#Boolean is either TRUE or FALSE. They are binary
#mostly used in if else statements

is_student = True
for_sale = False
if for_sale:
    print("That item is for sale")
else:
    print("That item is NOT for sale")

if is_student:
    print("you are a student")
else:
    print("you are NOT a student")
print(f"Are you a student: {is_student}")


