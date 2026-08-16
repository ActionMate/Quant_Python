                                            PYTHON IMP NOTES
                            ================================================

---------------------------------------------------------------------------------------------------------------
In Python, variables never contain values. They contain only references to values.
In Python, the = assignment operator copies only references. It never copies values.

---------------------------------------------------------------------------------------------------------------
.split() — IMPORTANT
------------------------
"move e2 e4".split()
# ['move', 'e2', 'e4']
split() breaks a string into a list of pieces by whitespace by default.
# Example:
response = input('> ').split()
If the user types:
move e2 e4
# then:
response = ['move', 'e2', 'e4']
Therefore:
response[0]  # 'move'
response[1]  # 'e2'
response[2]  # 'e4'

---------------------------------------------------------------------------------------------------------------
Dictionary key → must be hashable.
List/dictionary → unhashable → cannot be keys.
Tuple → can be a key (provided its contents are themselves hashable).
Why? → learn later.

---------------------------------------------------------------------------------------------------------------
LIST
.pop()
→ removes + returns last element


SET
.pop()
→ removes + returns an arbitrary element


DICTIONARY
.pop(key)
→ removes that key + returns its VALUE

.popitem()
→ removes + returns a key-value pair
   (last inserted pair)

--------------------------------------------------------------------------------------------------------------