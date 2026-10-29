#This is a comment in Python
'''this is a multi-line 

comment in Python'''

new_age = 45

new_name = "John Doe"
print("Hello, I am", new_name, "and I am", new_age, "years old.")

first_name = "Brian"
last_name = "Githua"
long_dash = "-" * 15

full_name = first_name + " " + last_name
print(full_name)

age = 10

can_vote = age >= 18

my_list = ["Amanda", 25, "John", 30, "Mary", 22]

name = my_list[0:6:2]
age = my_list[1:6:2]

person = {
    "name": "John Doe",
    "age": 30,
    "city": "New York"
}

person["city"]


def greet():
    print("Hello, welcome to the program!")
    print("Hello again, welcome to the program!")

greet()


def temp():
    temperature = 35
    if temperature > 30:
        print("It's hot outside.")
    else:
        print("It's not too hot outside.")

temp()
temp()
temp()
temp()

def add_print(a, b):
    print(a, b)

add_print(a=5, b=10)

def add_return(a=5, b=10):
    return a + b

result = add_return(a=5, b=10)
print("The sum is:", result)