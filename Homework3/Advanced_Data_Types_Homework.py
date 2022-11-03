# 1 (a).
print('1.a')
int_a = 55
print(id(int_a))

# (b) str_b = 'cursor'
print('1.b')
str_b = 'cursor'
print(id(str_b))

# (c) set_c = {1, 2, 3}
print('1.c')
set_c = {1, 2, 3}
print(id(set_c))

# (d) lst_d = [1, 2, 3]
print('1.d')
lst_d = [1, 2, 3]
print(id(lst_d))

# (e) dict_e = {'a': 1, 'b': 2, 'c': 3}
print('1.e')
dict_e = {'a': 1, 'b': 2, 'c': 3}
print(id(dict_e))

# 2.
print('2')
lst_d.append(4)
lst_d.append(5)
print(lst_d)
print(id(lst_d))

# alternative solution:
lst_d.extend((4, 5))
print(lst_d)
print(id(lst_d))
# defined id is identical for instance 1(d) and 2.

# 3.
print('3')
# Define the type of each object from step 1.
# Note to myself: Unlike procedure-oriented programming, where the main emphasis is on functions, object-oriented programming stresses on objects.
# An object is simply a collection of data (variables) and methods (functions) that act on those data.
# map () - built-in function that allows you to process and transform all the items in an iterable without using an explicit for loop,
# a technique commonly known as mapping. map() is useful when you need to apply a transformation function to each item in an iterable and transform them into a new iterable.
print(list(map(type, (int_a, str_b, set_c, lst_d, dict_e))))
# result -> [<class 'int'>, <class 'str'>, <class 'set'>, <class 'list'>, <class 'dict'>]

# 4.
print('4')
# Check the type of the objects by using isinstance.
print(isinstance(int_a, int))
print(isinstance(str_b, str))
print(isinstance(set_c, set))
print(isinstance(lst_d, list))
print(isinstance(dict_e, dict))

# Replacement of placeholders "Anna has ___ apples and ___ peaches."

# 5.
print('5')
# With .format and curly braces {}
print("Anna has {} apples and {} peaches.".format(5,7))
# result -> Anna has 5 apples and 7 peaches.

# 6.
print('6')
# By passing index numbers into the curly braces.
print("Anna has {0} apples and {1} peaches.".format(5,7))
# result -> Anna has 5 apples and 7 peaches.

# 7.
print('7')
# By using keyword arguments into the curly braces.
print("Anna has {apples} apples and {peaches} peaches.".format(apples=5, peaches=7))
# result -> Anna has 5 apples and 7 peaches.

# 8.
print('8')
# With indicators of field size (5 chars for the first and 3 for the second)
print("Anna has {apple:5} apples and {peache:3} peaches." .format(apple=4, peache=9))

# 9.
print('9')
# With f-strings and variables:
apples = 5
peaches = 7
print(f"Anna has {apples} apples and {peaches} peaches.")

# 10.
print('10')
# With % operator: s is representation of "string"
print("Anna has %s apples and %s peaches." % (apples, peaches))

# 11.
print('11')
dict = {'apples': 5, 'peaches': 10}
print(f"Anna has {dict['apples']} apples and {dict['peaches']} peaches.")

# 12.
print('12')
# Convert (1) to list comprehension:
lst = [num ** 2 if num % 2 == 1 else num ** 4 for num in range(10)]
print(lst)

# 13.
print('13')
# Convert (2) to regular for with if-else:
list_comprehension = []
for num in range(10):
    if num % 2 == 0:
        list_comprehension.append(num // 2)
    else:
        list_comprehension.append(num * 10)
print(list_comprehension)

# 14.
print('14')
# Convert (3) to dict comprehension:
d = {num: num ** 2 for num in range(1, 11) if num % 2 == 1}
print(d)

# 15.
print('15')
# Convert (4) to dict comprehension:
d = {num: num ** 2 if num % 2 == 1 else num // 0.5 for num in range(1, 11)}
print(d)

# 16.
print('16')
# Convert (5) to regular for with if:
dict_comprehension = {}
for x in range(10):
    if x ** 3 % 4 == 0:
        dict_comprehension[x] = x ** 3
print(dict_comprehension)

# 17.
print('17')
# Convert (6) to regular for with if-else:
dict_comprehension = {}
for x in range(10):
    if x**3 % 4 == 0:
        dict_comprehension[x] = x**3
    else:
        dict_comprehension[x] = x
print(dict_comprehension)

# 18.
print('18')
# Convert (7) to lambda function:
lmb = lambda x, y: x if x < y else y
print(lmb(3, 5))

# 19.
print('19')
# Convert (8) to regular function:
def foo(x, y, z):
    if y < x and x > z:
        return z
    else:
        return y
print(foo(5, 6, 7))

# 20.
print('20')
# Sort lst_to_sort from min to max:
lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]
print(sorted(lst_to_sort))

# 21.
print('21')
# Sort lst_to_sort from max to min:
print(sorted(lst_to_sort, reverse=True))

# 22.
print('22')
# Use map and lambda to update the lst_to_sort by multiply each element by 2
print(list(map(lambda x: x * 2, lst_to_sort)))

# 23.
print('23')
# Raise each list number to the corresponding number on another list:
list_A = [2, 3, 4]
list_B = [5, 6, 7]
list_C = list(map(pow, list_A, list_B))
print(list_C)

# 24.
print('24')
# Use filter and lambda to filter the number of a lst_to_sort with elem % 2 == 1.
lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]
filtered_list = list(filter(lambda elem: elem % 2 == 1, lst_to_sort))
print(filtered_list)

# 25.
print('25')
# Considering the range of values: b = range(-10, 10), use the function filter to return only negative numbers:
filtered_list = list(filter(lambda elem: elem < 0, range(-10, 10)))
print(filtered_list)

# 26.
print('26')
# Using the filter function, find the values that are common to the two lists:
list_1 = [1,2,3,5,7,9]
list_2 = [2,3,5,6,7,8]
print(list(filter(lambda x: x in list_1, list_2)))




