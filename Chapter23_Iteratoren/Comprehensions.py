"""
Chapter 23 - Iterators: Comprehensions

- Comprehension: Syntax to generate instances of iterable objects like lists, tuples

Author: Oliver Zott
Date: 16.07.2019
Update: 20.09.2019
"""

# ---------------------------------------------------
# Example 1 (page 404)
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
lst_sq = [x**2 for x in lst]  # list comprehension
print(lst_sq)
lst_sq2 = [x**2 for x in lst if x % 2]
lst_sq3 = [x**2 for x in lst if x % 2 == 0]
print(lst_sq2)
print(lst_sq3)
print()

# implementation with 'filter' and 'map' function (page 301 / 307)
fil1 = filter(lambda x: x % 2 == 0, lst)
ls = list(fil1)
result = map(lambda y: y**2, ls)
print(ls)
print(list(result))
print()

# ---------------------------------------------------
# Example 2 (page 405)
print("Example 2: ")
v1 = [1, 7, -5]
v2 = [-9, 3, 12]
v_result = [v1[i] + v2[i] for i in range(len(v1))]
print(v_result)

lst1 = ["A", "B", "C"]
lst2 = ["D", "E", "F"]
lst_result = [(a, b) for a in lst1 for b in lst2]
print(lst_result)
print()

# implementation with 'filer' and 'map'
v = []
for i in range(3):
    v.append(v1[i]+v2[i])
    # print(v)
print(v)

u = list()
w = [0, 1]
for i in range(3):
    for j in range(3):
        w[0] = lst1[i]
        w[1] = lst2[j]
        # print(w)
        u.append(w.copy())  # without copy: just last w overwrites all for some reason!!!??!!!
        # print(u)
print(u)
print()

# ---------------------------------------------------
# Example 3 (page 406)
print("Example 3: Dict-Comprehensions")

names = ["Donald", "Daisy", "Dagobert", "Gustav"]
dict_len = {k: len(k) for k in names}
print(dict_len)
dict_len_D = {k: len(k) for k in names if k[0] == "D"}
print(dict_len_D)

lst3 = [2, 4, 6]
dict2 = {k: [k*i for k in lst1 for i in lst3] for k in lst1}
dict3 = {k: [k*i for i in lst3] for k in lst1}
print(dict2)
print(dict3)
print()

# ---------------------------------------------------
# Example 4 (page 406)
print("Example 4: Set-Comprehensions ")
set1 = {k**2 for k in lst}
print(set1)
