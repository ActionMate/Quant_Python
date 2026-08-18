============================================================
                 PYTHON DICTIONARIES - NOTES
============================================================

MIND MAP
--------

DICTIONARY
|
+-- Structure
|   +-- key -> value
|   +-- {'key': value}
|
+-- Access
|   +-- d[key]
|   +-- d.get(key)
|
+-- Add / Change
|   +-- d[key] = value
|   +-- d.update(...)
|
+-- Remove
|   +-- del
|   +-- pop()
|   +-- popitem()
|   +-- clear()
|
+-- Loop
|   +-- keys()
|   +-- values()
|   +-- items()
|
+-- Check
|   +-- key in d
|
+-- IMPORTANT
    +-- Dictionary keys MUST be hashable


============================================================
1. WHAT IS A DICTIONARY?
============================================================

A dictionary stores data as KEY-VALUE PAIRS.

Instead of accessing an item using a numeric index like
a list, we normally access a value using its key.

Example:

d = {'arrow': 12, 'gold coin': 42, 'rope': 1}

'arrow', 'gold coin', and 'rope' are KEYS.
12, 42, and 1 are VALUES.

Basic idea:

KEY --------> VALUE
'arrow' -----> 12
'rope' ------> 1


============================================================
2. CREATING DICTIONARIES
============================================================

Empty dictionary:

empty = {}

Dictionary with values:

scores = {'Alice': 92, 'Bob': 81, 'Charlie': 95}

Rules:

key and value are separated by :
different key-value pairs are separated by commas


============================================================
3. ACCESSING VALUES
============================================================

Use the key:

scores['Alice']

If the key does not exist, d[key] raises KeyError.

Use get() when you want a default value:

scores.get('Alice')

scores.get('Dave', 0)

If 'Dave' does not exist, the second example returns 0.


============================================================
4. ADDING AND CHANGING ITEMS
============================================================

The same syntax can ADD a new key or CHANGE an existing value.

Add:

scores['Dave'] = 88

Change:

scores['Alice'] = 97

Multiple updates:

scores.update({'Bob': 90, 'Eve': 85})


============================================================
5. REMOVING ITEMS
============================================================

del
---

Removes a key-value pair.

del scores['Dave']

If the key does not exist, this raises KeyError.


pop()
------

Removes a key and RETURNS its value.

scores.pop('Dave')

A default can be supplied:

scores.pop('Dave', 0)


popitem()
---------

Removes and returns one key-value pair.

d.popitem()

In modern Python, dictionaries preserve insertion order,
so popitem() removes the LAST inserted pair.


clear()
-------

Removes everything from the dictionary.

d.clear()


============================================================
6. LOOPING THROUGH DICTIONARIES
============================================================

Looping directly over a dictionary gives its KEYS:

for name in scores:
    print(name)


keys()
------

Returns the dictionary's keys.

scores.keys()


values()
--------

Returns the dictionary's values.

scores.values()


items()
-------

Returns key-value pairs.

scores.items()


Common pattern:

for name, score in scores.items():
    print(name, score)


============================================================
7. CHECKING WHETHER A KEY EXISTS
============================================================

Use 'in':

'Alice' in scores

Use 'not in':

'Alice' not in scores

IMPORTANT:
'in' checks the DICTIONARY'S KEYS.


============================================================
8. DICTIONARY LENGTH
============================================================

len(d)

Returns the number of key-value pairs.


============================================================
9. DICTIONARY COMPREHENSION
============================================================

A compact way to create a dictionary.

Example:

squares = {x: x*x for x in range(5)}

Result:

{0: 0, 1: 1, 2: 4, 3: 9, 4: 16}


============================================================
10. IMPORTANT: DICTIONARY KEYS MUST BE HASHABLE
============================================================

A dictionary KEY must be HASHABLE.

Common hashable types:

- strings
- integers
- floats
- tuples (if their contents are hashable)
- other immutable hashable objects

Example:

d = {
    'name': 'Bob',
    10: 'ten',
    (1, 2): 'point'
}


These CANNOT be used directly as dictionary keys:

- lists
- dictionaries
- sets

Example:

d = {[1, 2]: 'value'}       # TypeError

d = {{'a': 1}: 'value'}     # TypeError


WHY?

Dictionaries use HASHING to efficiently locate values
using their keys.

Therefore, a key needs a stable hash.


============================================================
11. VALUES DO NOT HAVE THE SAME RESTRICTION
============================================================

Dictionary VALUES can be many different types.

For example, values can be lists or dictionaries:

d = {
    'numbers': [1, 2, 3],
    'profile': {'age': 18}
}


============================================================
12. DICTIONARY VS LIST
============================================================

+----------------------+----------------------+----------------------+
| Feature              | List                 | Dictionary           |
+----------------------+----------------------+----------------------+
| Main idea            | Ordered sequence     | Key -> value mapping |
| Access               | Index                | Key                  |
| Example              | a[0]                 | d['name']            |
| Duplicate keys       | N/A                  | No                   |
| Key requirement      | N/A                  | Keys must be         |
|                      |                      | hashable             |
+----------------------+----------------------+----------------------+


============================================================
13. USEFUL COUNTING PATTERN
============================================================

Dictionaries are very useful for counting occurrences.

Example:

counts = {}

for item in items:
    counts[item] = counts.get(item, 0) + 1


The important idea:

If item already exists:
    increase its count.

If item does not exist:
    get() gives 0, then add 1.


============================================================
14. USEFUL PROBLEM-SOLVING PATTERN
============================================================

For problems involving scores, inventories, frequencies,
lookups, or mappings, ask:

"What should my KEYS represent?"

"What should my VALUES represent?"

Example:

for name, score in scores.items():
    if score > 90:
        print(name)


============================================================
15. QUICK REFERENCE TABLE
============================================================

+----------------------------+----------------------------+
| Operation                  | Syntax                     |
+----------------------------+----------------------------+
| Create                     | d = {}                     |
| Access                     | d[key]                     |
| Safe access                | d.get(key, default)        |
| Add / update               | d[key] = value             |
| Multiple updates           | d.update(...)              |
| Delete                     | del d[key]                 |
| Remove + return value      | d.pop(key)                 |
| Remove last inserted pair | d.popitem()                |
| Empty dictionary           | d.clear()                  |
| Get keys                   | d.keys()                   |
| Get values                 | d.values()                 |
| Get key-value pairs        | d.items()                  |
| Number of pairs            | len(d)                     |
| Check for key              | key in d                   |
+----------------------------+----------------------------+


============================================================
IMPORTANT THINGS TO REMEMBER
============================================================

1. A dictionary stores KEY -> VALUE pairs.

2. d[key] accesses a value using its key.

3. d.get(key, default) is useful when a key may not exist.

4. keys(), values(), and items() are useful when looping.

5. DICTIONARY KEYS MUST BE HASHABLE.

6. Dictionary VALUES do not have to be hashable.

7. Dictionaries preserve insertion order in modern Python,
   but their main purpose is KEY-BASED MAPPING, not
   positional indexing.


============================================================
                 END OF DICTIONARY NOTES
============================================================