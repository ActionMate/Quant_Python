a = [1, 2, 3, 1, 5]                             #to remove multiple same element
a = [x for x in a if x != 1]        
print(a)

---------------------------------------------------------------------------------------------------------

PYTHON LISTS — QUICK REFERENCE
================================

1. CREATING A LIST
----------------------------------------------------------
a = [1, 2, 3, 4]

Lists can contain different types:
a = [10, "hello", 3.14, True]

Lists can contain other lists:
a = [1, [2, 3], 4]


2. LISTS ARE ORDERED
------------------------------------------------------------
The order of elements is preserved.


3. LISTS ARE MUTABLE
------------------------------------------------------------
You can change individual elements.

a = [10, 20, 30]
a[1] = 99

# [10, 99, 30]


4. INDEXING
---------------------------------------------------------
Python starts counting from 0.

a = ['a', 'b', 'c', 'd']

a[0]  # 'a'
a[1]  # 'b'
a[3]  # 'd'

Negative indexes count from the end:

a[-1]  # 'd'
a[-2]  # 'c'


5. SLICING
--------------------------------------------------------
Syntax:
a[start:stop]

The stop index is NOT included.

a = [0, 1, 2, 3, 4]

a[1:4]   # [1, 2, 3]
a[:3]    # first 3
a[2:]    # from index 2 onward
a[:]     # entire list
a[::2]   # every second element
a[::-1]  # reversed


6. len()
-------------------------------------------------------
Returns the number of elements.

len([10, 20, 30])
# 3


7. in / not in
-------------------------------------------------------
Checks whether an item exists.

'a' in ['a', 'b', 'c']       # True
'x' not in ['a', 'b', 'c']   # True


8. append()
---------------------------------------------------------
Adds ONE item to the end.

a = [1, 2]
a.append(3)

# [1, 2, 3]

Important:
a.append([4, 5])

# [1, 2, 3, [4, 5]]

The list [4, 5] is added as one element.


9. extend()
------------------------------------------------------------
Adds multiple elements from another iterable.

a = [1, 2]
a.extend([3, 4])

# [1, 2, 3, 4]

Difference:

append([3, 4])
# [1, 2, [3, 4]]

extend([3, 4])
# [1, 2, 3, 4]


10. insert()
-------------------------------------------------------------
Inserts an item at a specific index.

a = [1, 2, 4]
a.insert(2, 3)

# [1, 2, 3, 4]

Syntax:
list.insert(index, value)


11. remove()
---------------------------------------------------------------
Removes the FIRST matching value.

a = [1, 2, 3, 1, 5]
a.remove(1)

# [2, 3, 1, 5]

It does NOT remove every occurrence.

If the value isn't present, remove() raises an error.


12. pop()
---------------------------------------------------------------
Removes AND returns an item.

a = ['a', 'b', 'c']

x = a.pop()

# x == 'c'
# a == ['a', 'b']

You can give it an index:

a.pop(0)

removes the first element.

Mental model:
remove(value) -> "I know WHAT I want to remove."
pop(index)    -> "I know WHERE the thing I want is."


13. del
----------------------------------------------------------------
Deletes an element using its index.

a = [10, 20, 30]
del a[1]

# [10, 30]

Can also delete a slice:

del a[1:3]

Unlike pop(), del does not return the deleted value.


14. index()
------------------------------------------------------------------
Finds the index of a value.

a = ['a', 'b', 'c']
a.index('b')

# 1

If the value occurs multiple times, it gives the FIRST occurrence.


15. count()
-------------------------------------------------------
Counts how many times a value occurs.

a = [1, 2, 1, 1, 3]
a.count(1)

# 3


16. sort()
----------------------------------------------------------
Sorts the list IN PLACE.

a = [3, 1, 2]
a.sort()

# [1, 2, 3]

Reverse order:
a.sort(reverse=True)

Case-insensitive sorting:
a.sort(key=str.lower)

sort() modifies the original list.


17. sorted()
-----------------------------------------------------------------
Returns a sorted result WITHOUT changing the original list.

a = [3, 1, 2]
b = sorted(a)

a
# [3, 1, 2]

b
# [1, 2, 3]

Remember:
list.sort()  -> changes the original list
sorted(list) -> returns a sorted result


18. reverse()
-------------------------------------------------
Reverses the list IN PLACE.

a = [1, 2, 3]
a.reverse()

# [3, 2, 1]


19. reversed()
--------------------------------------------------------------------------------
Returns a reversed iterator instead of modifying the original list.

a = [1, 2, 3]
list(reversed(a))

# [3, 2, 1]

Remember:
reverse()  -> modifies the list
reversed() -> gives a reversed iterator


20. for LOOPS
---------------------------------------------------
Lists can be iterated with for.

a = ['apple', 'banana', 'mango']

for fruit in a:
    print(fruit)

Python takes each element one at a time.


21. enumerate()
-----------------------------------------------------
Useful when you need BOTH the index and the value.

a = ['apple', 'banana', 'mango']

for i, fruit in enumerate(a):
    print(i, fruit)

# 0 apple
# 1 banana
# 2 mango


22. LIST CONCATENATION
----------------------------------------------------
Lists can be joined with +.

a = [1, 2]
b = [3, 4]

a + b
# [1, 2, 3, 4]

Lists can also be repeated:

[1, 2] * 3
# [1, 2, 1, 2, 1, 2]


23. ASSIGNMENT DOES NOT COPY A LIST
------------------------------------------------------
spam = [1, 2, 3]
eggs = spam

spam and eggs refer to the SAME list.

eggs.append(4)

spam
# [1, 2, 3, 4]


24. MAKING A SEPARATE LIST COPY
-----------------------------------------------------
eggs = spam.copy()

or:
eggs = list(spam)

or:
eggs = spam[:]

These create separate shallow copies of the list.


25. LISTS CONTAIN REFERENCES
--------------------------------------------------------
Conceptually, a list contains references to objects.

list
 |
 +--> reference -> object
 +--> reference -> object
 +--> reference -> object

This becomes especially important with nested lists and copying.


26. NESTED LISTS
----------------------------------------------------
A list can contain other lists.

board = [
    ['X', 'O', 'X'],
    ['O', 'X', 'O'],
    ['X', ' ', 'O']
]

Access a nested element:

board[0][1]
# 'O'

First board[0] gives the first inner list.
Then [1] accesses its second element.


27. LISTS CAN CONTAIN ALMOST ANYTHING
--------------------------------------------------------
a = [
    10,
    "hello",
    [1, 2],
    (3, 4),
    {"name": "Bob"}
]

Lists are flexible containers.


28. METHODS AND None
-----------------------------------------------------------
Many list methods modify the list and return None.

a = [3, 1, 2]
result = a.sort()

print(result)
# None

sort() changes a directly; it does not return the sorted list.

Do NOT do:
a = a.sort()


29. QUICK MENTAL MAP

---------------------------------------------------------------------------------------------------------

ADD
├── append(x)       → add x to end
├── extend(iterable)→ add multiple items
└── insert(i, x)    → add x at index i

REMOVE
├── remove(x)       → remove first matching VALUE
├── pop(i)          → remove/return item at INDEX
└── del a[i]        → delete item at INDEX

SEARCH
├── x in a          → does x exist?
├── index(x)        → first index of x
└── count(x)        → number of occurrences

ORDER
├── sort()          → sort original list
├── sorted(a)       → return sorted result
├── reverse()       → reverse original list
└── reversed(a)     → reversed iterator

COPY
├── b = a           → SAME list
├── b = a.copy()    → separate shallow copy
├── b = list(a)     → separate shallow copy
└── b = a[:]        → separate shallow copy

----------------------------------------------------------------------------------------------------------

⭐ Lists are mutable.
⭐ Indexing starts at 0.
⭐ remove(value) ≠ pop(index).
⭐ append(x) ≠ extend(iterable).
⭐ b = a does NOT copy the list.
        (Both names refer to the same list.)
