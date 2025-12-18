"""
1 Basic Function
1.1 Standard writing function comments
1.2 Nested functions and execution flow(sequence)
1.3 Local variables and global variables
1.4 Comprehensive Exercise: ATM Business Process

2 Advanced Function
2.1 Multiple return values of a function
2.2 Multiple ways to pass parameters to a function
   (a) Positional parameters
   (b) Keyword(Key-Value) parameters
   (c) Default parameters
   (d) Variable-length parameters
      - *args: Positional transfer (Data type: tuple)
      - **kwargs: Keyword/key value transfer(Data type: dictionary)
2.3 lambda expresses anonymous functions
"""

# 1 Basic Function
# 1.1 Standard writing function comments
# Why: It is efficient to recall the logic of code blocks after few weeks and also easy for other people to understand it quickly.
def add(x,y):
    """
    Adds two numbers together.
    :param x: first number
    :param y: second number
    :return: added number
    """
    return x + y
add(1,2) # Mouse hover
print(add(1,2))

# 1.2 Nested functions and execution flow(sequence)
def func_a():
    print("1")

def func_b():
    print("2")
    func_a()
    print("3")

def func_c():
    print("4")
    func_b()
    print("5")

func_c() # 42135

# 1.3 Local variables and global variables
def func():
    num = 100
    print("Internal output", num)
func()

# After the function func() is called and num exists not anymore
# print("External output", num)

num = 100
def func_d():
    global num # In the function num is a global variable
    num = 200
    print(f"d: {num}")

def func_e():
    print(f"e: {num}")

func_d() # d: 200
func_e() # 2: 200
print(f"External output: {num}")

# 1.4 Comprehensive Exercise: ATM Business Process
"""
New knowledge:
\t
${money:,} for example: $5,000,000

Logic which did not consider:
main menu should include all services
if money >= output_number should be considered in the withdrawing service
"""
# global variables
name = input("Enter your name: ")
money = 5000000

def main_menu():
    print()
    print("---------- Main Menu ----------")
    print(f"Dear customer {name}, welcome to use Revolution Online Bank!Please entering your banking service:")
    print("Checking balance service\t[Please enter 1]")
    print("Deposit service\t\t\t\t[Please enter 2]")
    print("Withdraw service\t\t\t[Please enter 3]")
    print("Ending service\t\t\t\t[Please enter 4]")

def check_balance():
    """
    Check customer's balance
    :return: None
    """
    print()
    print("---------- Check Balance ----------")
    print(f"Dear {name}, your current balance is ${money:,}")
    main_menu()

def deposit():
    """
    Customer to deposit money
    :return: None
    """
    print()
    print("---------- Deposit Service ----------")
    input_number = int(input("Please enter the deposit amount: "))
    global money
    money += input_number
    print(f"Dear {name}, your current balance is ${money:,}")
    main_menu()

def withdraw():
    """
    Customer to withdraw money
    :return: None
    """
    print()
    print("---------- Withdraw Service ----------")
    output_number = int(input("Please enter the withdraw amount: "))
    global money
    if money >= output_number:
        money -= output_number
        print(f"Dear {name}, your current balance is ${money:,}")
    else:
        print("Dear customer, your balance is not enough.")
    main_menu()

while True:
    print()
    input_number = int(input("Please input the corresponding number: "))
    if input_number == 1:
        check_balance()
    elif input_number == 2:
        deposit()
    elif input_number == 3:
        withdraw()
    elif input_number == 4:
        print("See you next time and thank you for using Revolution Online Bank!")
        break
    else:
        print("See you next time and thank you for using Revolution Online Bank!")
        break


# 2 Advanced Function
# 2.1 Multiple return values of a function
def func_f():
    return 1, 2 # return a tuple: (1, 2)

# Automatically unpack the tuple (1, 2) and assign the two elements to x and y respectively
x, y = func_f()
print(x,y) # 1 2

# x receive the complete tuple (1, 2)
x = func_f()
print(x, type(x)) # (1, 2) <class 'tuple'>

# 2.2 Multiple ways to pass parameters to a function
"""
2.2 (a) Positional parameters
2.2 (b) Keyword(Key-Value) parameters
2.2 (c) Default parameters
2.2 (d) Variable-length parameters
- *args: Positional transfer (Data type: tuple)
- **kwargs: Keyword/key value transfer(Data type: dictionary)
"""
# 2.2 (a) Positional parameters
def user1(name, age, gender):
    print(f"Your name is {name}, are {age} years old and gender is {gender}")
user1("Wei", 18, "female")

# 2.2 (b) Keyword(Key-Value) parameters
def user2(name, age, gender):
    print(f"Your name is {name}, are {age} years old and gender is {gender}")
user2(name="Wei", age=18, gender="female")

# 2.2 (c) Default parameters
def user3(name, age, gender="female"):
    print(f"Your name is {name}, are {age} years old and gender is {gender}")
user3("Rose", 21)
user3("Mike", 18, "male")

# 2.2 (d) Variable-length parameters: Positional transfer(Data type: tuple)
def member_info(name, *args): # *args = *xxx
    print(f"We are {name}, the members are followed: ")
    for i in args:
        print(i)
    print(args, type(args))

member_info("Member group", 88, "Jodie", "Mike")

# 2.2 (d) Variable-length parameters: Keyword transfer(Data type: dictionary)
def user1_info(**kwargs):
    """
    **kwargs is <class 'dict'>, all the keyword parameters are collected in the dic
    :param kwargs:
    :return: None
    """
    print(kwargs, type(kwargs))
# In the essence we transfer KV(Key Value) which are collected in the kwargs dictionary
user1_info(name= "Tom", age=18, id=100)

def user2_info(name, age, *args, **kwargs):
    print(f"Tuple collection: {args}")
    print(f"Dic collection: {kwargs}")
user2_info("Wei",18, 1,2,3,4,5,6, id=1, gender="female")

# 2.3 lambda expresses anonymous functions
"""
New knowledge:
(a) Difference between lambda and def x()
- lambda(anonymous function) can pass computational logic, lambda can typically ONLY be used once
- def x() can be reused 

(b) lambda grammar
- lambda Input parameters : Function body (ONLY one line of code)
"""
def func(compute):
    result = compute(1,2)
    print(result)
func(lambda x,y: x+y)

def compute(x, y):
    return x + y
func(compute)













