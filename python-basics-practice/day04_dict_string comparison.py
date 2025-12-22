"""
1 Dict
1.1 dict definition
1.2 Nested dict
1.3 Common  operations
1.4 Exercise: promotion and salary increase

2. String comparison
"""

# 1 Dict
# 1.1 dict definition
# dict literal(字面量): {"Serafina": "happy", "Jodi": 30, "Mike":33}

# dict variable
dict1 = {"Serafina": "happy", "Jodi": 30, "Mike":33}

# empty dict
dict2 = {} # set cannot use {}
dict3 = dict()

# key cannot be repeated: the value of second repeated key will cover the first value
dict4 = {"Serafina": "happy", "Jodi": 30, "Mike":33, "Jodi": 18}
print(dict4) # {'Serafina': 'happy', 'Jodi': 18, 'Mike': 33}

# 1.2 Nested dict
"""
Normally the data type of Key are string or int; the data type of Value is arbitrary
"""
# Sample1
student_score = {
    "Lihong Wang":{
        "Chinese":77,
        "Math":66,
        "English":33
    },
    "Jay Chou":{
        "Chinese":88,
        "Math":86,
        "English":55
    },
    "Junjie Lin":{
        "Chinese":99,
        "Math":96,
        "English":66
    }
}
print(f"The grade of Jay Chou's math: {student_score['Jay Chou']['Math']}")

# Sample2
student_hobby = {
    "Serafina": ["study", "gym", "travel"],
    "Jodie": ["read", "badminton", "travel"],
    "Mike": ["startup", "gym", "sleep"],
}
print(f"One hobby from Mike: {student_hobby['Mike'][0]}")

# 1.3 Common  operations
"""
(1) Add new elements
(2) Updated old elements
(3) Delete elements
(4) clear()
(5) Get all keys
(6) Traversing dict
(7) Length of dict
"""
# (1) Add new elements
student_score["Dehua Liu"] = {
    "Chinese":66,
    "Math":78,
    "English":62}
print(f"After adding student_score: {student_score}")

# (2) Updated old elements
student_score["Lihong Wang"] = {
    "Chinese":99,
    "Math":98,
    "English":66
}
print(f"After updating student_score: {student_score}")

# (3) Delete elements
print()
Liu = student_score.pop("Dehua Liu")
print(f"Liu: {Liu}", f"After deleting: {student_score}")

# (4) clear()
# clear_student_score = student_score.clear()
# student_score = dict()
student_score = {}

# (5) Get all keys
student_score = {
    "Lihong Wang":{
        "Chinese":77,
        "Math":66,
        "English":33
    },
    "Jay Chou":{
        "Chinese":88,
        "Math":86,
        "English":55
    },
    "Junjie Lin":{
        "Chinese":99,
        "Math":96,
        "English":66
    }
}
print()
print(f"student_score.keys(): {student_score.keys()}")
print(f"The data type of student_score.keys(): {type(student_score.keys())}") # <class 'dict_keys'>

# (6) Traversing dict
print()
i = 1
for key in student_score.keys():
    print(f"key {i}: {key}")
    i += 1

# (7) Length of dict
print()
print(f"How many Key-values:{len(student_score)}")

# 1.4 Exercise: promotion and salary increase
"""
Logic:
(1)Input information
(2)"Level" iterates and "salary" increases
"""
employee_info = {
    "Lihong Wang":{
        "Department":"Tech dep",
        "Salary":3000,
         "Level":1
    },
    "Jay Chou": {
        "Department": "Marketing dep",
        "Salary": 5000,
        "Level": 2
    },
    "Junjie Lin": {
        "Department": "Marketing dep",
        "Salary": 7000,
        "Level": 3
    },
    "Xueyou Zhang": {
        "Department": "Tech dep",
        "Salary":4000,
        "Level": 1
    },
    "Dehua Liu": {
        "Department": "Marketing dep",
        "Salary": 6000,
        "Level": 2
    }
}
print(f"The current information of the all employees:")
print(employee_info)

for key in employee_info.keys():
    if employee_info[key]["Level"] == 1:
        employee_info[key]["Level"] += 1
        employee_info[key]["Salary"] += 1000

print()
print(f"After increasing the 1 level for the level 1 employees and their salaries:")
print(employee_info)

# 2. String comparison
"""
String comparison is based on the digit-by-digit comparison from left to right.
content > empty
lowercase letter > uppercase letter > number > symbol
The english,number and symbol are saved in ASCII table
The world language are saved in the UTF-8 table
"""
print("a" > "A") # True a = 87, A= 65
print("abc" > "abcd") # False because content > empty
print("123" > "2") # False because 2 is bigger than 1
