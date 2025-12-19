"""
1 Tuple
Tuple traits:
- Tuple CANNOT be modified
- The list in the tuple can be modified

Why we need tuple? Because after the definition of a tuple, which can NOT be modified
1.1 Tuple literal(字面量)
1.2 Empty tuple
1.3 Only one element in the tuple (specific writing)
1.5 Common operations
1.6 Iterating over tuple

2 str
2.1 Elements of str CANNOT be modified
2.2 Common operations
Often used
-str.replace(old_str, new_str)
-str.split()
-str.strip()
-len()

3 Sequence slicing operations: including head but not trail

4 Set
4.1 Set literal(字面量)
4.2 Common operations
4.3 Iterating over set
"""

# 1 Tuple
# 1.1 Tuple literal(字面量)
tuple1 = ("Welcome in Hamburg", 188, 192)

# 1.2 Empty tuple
tuple1 = ()
print(f"tuple1: {tuple1}")

tuple2 = ("Welcome in Hamburg", 188, 192)
tuple2 = tuple()
print(f"tuple2: {tuple2}")

# 1.3 Only one element in the tuple (specific writing)
tuple3 = (1)
print(type(tuple3)) # <class 'int'>
tuple4 = (1,)
print(type(tuple4)) # <class 'tuple'>

# 1.4 Nested tuple
tuple5 = ((1,2,3), (4,5,6))
print(f"tuple5[-1][-2]: {tuple5[-1][-2]}") # 5 Exactly same as the list

# 1.5 Common operations
# index(), count(element), len(tuple)
# * tuple CANNOT be modified but the list in the tuple can be modified. Because elements in the tuple are saved as a data, but the list in the tuple is saved a cursor(address), which points the memory area in the list. Pic see Notes

tuple5 =(1,2,[6,7,8])
tuple5[2][2] = 80
print(f"tuple5: {tuple5}")

# Why it cannot be modified? Because the list in the tuple is saved in a cursor, actually it is an address. It points out the outside list. So changing all the list means changes the address, which obeys the rule (elements in the tuple cannot be modified) of tuple
# tuple5[2] = [9,8,7] # TypeError: 'tuple' object does not support item assignment
print(tuple5[2])

# 1.6 Iterating over tuple
# (1) while loop
tuple6 = ("Welcome in Hamburg", 188, 192)
index = 0
while index < len(tuple6):
    print(tuple6[index])
    index += 1

# (2) for loop
for i in tuple6:
    print(i)


# 2 str
# 2.1 Elements of str CANNOT be modified
s = "itheimahaha666"
print(s[7]) # h
"""
s[7] = "90"
print(f"After changing: {s}") # TypeError: 'str' object does not support item assignment
"""

s = "90"
print(f"After changing: {s}") # After changing: 90

# 2.2 Common operations
"""
Often used
-str.replace(old_str, new_str)
-str.split()
-str.strip()
-len()
"""
# (a) str.index(element)

# (b) str.replace(old_str, new_str)
"""
s1 itself cannot be modified but replace() returns a new string
"""
s1 = "Serafina|Jodie|Mike"
s2 = s1.replace("|", ",")
print(f"After changing s1: {s1}")
print(f"s2: {s2}")

# (c) str.split()
# split() can base on the requirement to split string and the splitting elements are saved in a new list
s3 = "Serafina|Jodie|Mike"
s4 = s3.split("|")
print(f"After splitting s3: {s3}")
print(f"s4: {s4}")

# (d) str.strip()
# Remove leading and trailing spaces and newline characters from a string
s5 = "   Serafina|Jodie|Mike"
s6 = s5.strip()
print(f"After striping s5: {s5}")
print(f"s6: {s6}")

s7 = "|||Serafina|Jodie|Mike"
s8 = s7.strip("|")
s9 = s7.replace("|", "")
print(f"After splitting s8: {s8}") # After splitting s8: Serafina|Jodie|Mike
print(f"After replacing s9: {s9}") # After replacing s9: SerafinaJodieMike

# (e) str.count(element)

# (f) len()
s10 = "abc987Hej"
num = len(s10)
print(num)


# 3 Sequence slicing operations: including head but not trail
list1 = ["aa", "bb", 3, 5, 6]
# ["bb", 3]
print(list1[1:3])

# Take 5,3,"bb"
print(list1[3:0:-1])
print(list1[-2:-5:-1])

tuple1 = (1,3,5,7,9,11,13,15,17)
# Take 3, 7
print(tuple1[1:4:2])
# Take 15,9,3
print(tuple1[-2:-9:-3])
print(tuple1[-2:0:-3])

str1 = "itheima 666 and itcast"
# tsacti dna 666 amiehti
print(str1[::-1])
# d a 6 6 a
print(str1[-8:-17:-2])
print(str1[-8:5:-2]) # special
print(str1[8:11:]) # step is default 1


# 4 Set
"""
Set trait:
-Duplicate elements are not supported (built-in deduplication function is included).
-Content disordered
"""
# 4.1 Set literal(字面量)
#set = {1,2,3}
# It is not okay to write empty_set = {} because it stands for dict
empty_set = set()
empty_dict = {}
print(type(empty_set))
print(type(empty_dict))

set1 = {"bbb", "bbb", "aaa", "ccc"}
print(set1)

# 4.1 Set literal(字面量)
# It is not okay to write empty_set = {} because it stands for dict
empty_set = set()
empty_dict = {}
print(type(empty_set))
print(type(empty_dict))

set1 = {"bbb", "bbb", "aaa", "ccc"}
print(set1)

# 4.2 Common operations
"""
(a) set.add()
(b) set.remove()
(c) set.pop()
(d) set.clear()
(e) set.difference()
(f) set.union()
"""
# (a) set.add()
set2 = {"a", "b", "c", "d"}
set2.add("e")
print(f"After add: {set2}")

# (b) set.remove()
set3 = {"a", "b", "c", "d"}
set3.remove("a")
print(f"After remove set3: {set3}")

# (c) set.pop()
# pop() randomly selects an element and returns it; this element is removed from the collection
set4 = {"a", "b", "c", "d"}
set4.pop()
print(f"After pop set4: {set4}")

# (d) set.clear()

# (e) set.difference()
set5 = {1,2,3}
set6 = {1,4,5}
set7 = set5.difference(set6)
print(f"After difference: {set7}")
# (f) set.union()
set8 = set5.union(set6)
print(f"After Union: {set8}")

# 4.3 Iterating over set
# set does not have index, therefore it cannot use while loop
for i in set1:
    print(i)















