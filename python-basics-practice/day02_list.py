"""
1 List
1.1 List literal(字面量)
1.2 Nested lists
1.3 Empty list
1.4 Index and inverted index
1.5 Common operations
-list.append(element)
-len(list)
1.6 Iterating over list
(1) while loop
(2) for loop
"""

# 1 List
# 1.1 List literal(字面量)
def func(compute):
    result = compute(1, 2)
    print(result)


func(lambda x, y: x + y)


def compute(x, y):
    return x + y


func(compute)

list1 = ["Welcome the new year", 2026, "in Hamburg", (6, 9)]
print(list1)

# 1.2 Nested lists
list2 = [["New year", 2026, "in HH"], [1, 2, 3]]
print(list2)

# 1.3 Empty list
list3 = []
list4 = list()
print(f"list3: {list3}")
print(f"list4: {list4}")

# 1.4 Index and inverted index
# Index from left to right: 0, 1,2...
list5 = ["Welcome the new year", 2026, "in Hamburg", (6, 9)]
print(list1[0])  # Welcome the new year

list6 = [["New year", 2026, "in HH"], [1, 2, 3]]
print(f"list6[1][2]: {list6[1][2]}")  # list6[1][2]: 3
print(f"list6[1][-1]: {list6[1][-1]}")  # list6[1][-1]: 3

list7 = [
    [
        [1, 2, 3],
        [4, 5, 6]
    ],
    [
        [7, 8, 9],
        [10, 11, 12]
    ]
]
print(f"list7[0][1][-1]: {list7[0][1][-1]}")  # 6

# Inverted index from right to left: -1, -2, -3...
print(list1[-1])  # (6, 9)
print(list1[-2])  # in Hamburg

# 1.5 Common operations
"""
Difference between function and method:
- Under a class, a function is named as a method

list is essentially a class which offers many built-in functions(methods);
When people want call built-in functions, then should write like list_name.built-in_function()

list.append(element) and len(list) are normally used frequently
"""
# (a) list.index(the element being searched)
list8 = ["Welcome to the new year", 2026, "in Hamburg", (6, 9)]
print(f"list8.index(2026): {list8.index(2026)}")
print(f"2026 in list8: {2026 in list8}")

# (b) Modify the value of the element at the specific index
list8[0] = 2025
print(f"The modified list8[0] : {list8[0]}")

# (c) list.insert(index, element)
list9 = ["Welcome to the new year", 2026, "in Hamburg", (6, 9)]
list9.insert(0, "Dear!")
print(f"After inserting list9: {list9}")

# (d) list.append(): add the element at the end of the list
list9.append([21, 12])
print(f"After appending list9: {list9}")

# (e) list.extend(): add a batch of elements at the end of the list
list9.extend([21, 12, 66, 99, 100])
print(f"After extending list9: {list9}")

# (f) Delete elements in a list
# (f).1 del list[index]
list10 = [1, 2, 3, 4, 5, 6, 7, 8]
del list10[-1]
print(f"After deleting list10: {list10}")
# (f).2 list.pop(index) and pop() returns a value
print(f"pop() returns a value: {list10.pop(0)}")
print(f"After poping list10: {list10}")

# (g) list.remove(element): delete the first matching item of a certain element in the list
list11 = [1, 2, 3, 4, 5, 3, 6, 7, 8, 3]
list11.remove(3)
print(f"After removing list11: {list11}")
# (h) list.clear()
list11.clear()
print(f"After clear list11: {list11}")

list12 = [1, 2, 3, 4, 5, 3, 6, 7, 8]
list12 = []
print(f"After clear list12: {list12}")

# (i) list.count(element): count the number of a specific element in a list
list13 = [1, 2, 3, 4, 5, 3, 6, 7, 8, 3]
print(f"How many 3 in the list13: {list13.count(3)}")

# (j) len(list): count how many elements in the list
list14 = [1, 2, 3, 4, 5, 3, 6, 7, 8, 3]
print(f"How many elements in the list14: {len(list14)}")

# 1.6 Iterating over list
# (1) while loop
list15 = [1,3,5,7,9]
index = 0
while index < len(list15):
    element = list15[index]
    print(element)
    index += 1

# (2) for loop
for i in list15:
    print(i)
