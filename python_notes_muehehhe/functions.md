============================================================
                    PYTHON FUNCTIONS - NOTES
============================================================

MIND MAP
--------

FUNCTION
|
+-- Create
|   +-- def
|   +-- function name
|   +-- parameters
|   +-- function body
|
+-- Call
|   +-- function_name()
|   +-- pass arguments
|
+-- Parameters / Arguments
|   +-- parameter = variable in function definition
|   +-- argument = actual value passed during call
|
+-- Return
|   +-- return value
|   +-- immediately exits function
|   +-- returned value can be stored/used
|
+-- Scope
|   +-- local variables
|   +-- global variables
|
+-- Default arguments
|   +-- parameter = default_value
|
+-- Keyword arguments
|   +-- name=value
|
+-- *args
|   +-- multiple positional arguments
|
+-- **kwargs
|   +-- multiple keyword arguments
|
+-- Important
    +-- Calling a function executes it
    +-- Defining a function does NOT execute it
    +-- return != print


============================================================
1. WHAT IS A FUNCTION?
============================================================

A function is a reusable block of code that performs a
particular task.

Instead of writing the same code repeatedly, put it inside
a function and call the function whenever you need it.

Example:

def greet():
    print('Hello!')

Calling it:

greet()

Output:

Hello!


============================================================
2. DEFINING A FUNCTION
============================================================

Basic structure:

def function_name():
    # code
    # code
    # code

Example:

def say_hello():
    print('Hello')


IMPORTANT:

def creates/defines the function.

It does NOT execute the function.

The function runs when you CALL it:

say_hello()


============================================================
3. CALLING A FUNCTION
============================================================

Example:

def greet():
    print('Hello!')

greet()
greet()

Output:

Hello!
Hello!

Every time you call the function, its code runs again.


============================================================
4. PARAMETERS
============================================================

A parameter is a variable written inside the function
definition.

Example:

def greet(name):
    print('Hello', name)

Here, 'name' is a PARAMETER.

When calling:

greet('Diwakar')

'Diwakar' is the ARGUMENT.

Think:

PARAMETER = placeholder in the function

ARGUMENT = actual value supplied to the function


Example:

def add(a, b):
    return a + b

a and b = parameters

add(5, 3)

5 and 3 = arguments


============================================================
5. MULTIPLE PARAMETERS
============================================================

A function can have multiple parameters.

def add(a, b):
    return a + b

add(10, 20)

The values are matched by position:

a = 10
b = 20


============================================================
6. RETURN
============================================================

return sends a value back to the code that called the
function.

Example:

def add(a, b):
    return a + b

result = add(5, 3)

Now:

result = 8


IMPORTANT:

return and print() are NOT the same thing.

print():

Displays something on the screen.

return:

Gives a value back to the caller.


Example:

def add(a, b):
    print(a + b)

x = add(2, 3)

The function prints 5.

But x becomes:

None


Because the function did not return anything.


Compare:

def add(a, b):
    return a + b

x = add(2, 3)

Now:

x = 5


============================================================
7. RETURN IMMEDIATELY ENDS THE FUNCTION
============================================================

Example:

def test():
    print('A')
    return 10
    print('B')

test()

Output:

A

'B' is never printed.

Once Python reaches return, the function immediately
ends and sends the value back.


============================================================
8. A FUNCTION CAN RETURN DIFFERENT TYPES
============================================================

A function can return:

numbers:

return 10

strings:

return 'hello'

lists:

return [1, 2, 3]

dictionaries:

return {'A': 10}

booleans:

return True

It can also return multiple values:

return a, b

Python packs them into a tuple.


============================================================
9. FUNCTIONS WITHOUT RETURN
============================================================

Example:

def greet(name):
    print('Hello', name)

There is no return statement.

If you store the result:

x = greet('Bob')

then:

x = None

A function without an explicit return returns None.


============================================================
10. DEFAULT PARAMETERS
============================================================

A parameter can have a default value.

Example:

def greet(name='Guest'):
    print('Hello', name)

greet()

Output:

Hello Guest

If you provide an argument:

greet('Diwakar')

Output:

Hello Diwakar


The supplied argument replaces the default value.


============================================================
11. KEYWORD ARGUMENTS
============================================================

Arguments can be passed using parameter names.

Example:

def introduce(name, age):
    print(name, age)

introduce(age=18, name='Diwakar')

Python uses the parameter names to match the values.

This is called a KEYWORD ARGUMENT.


============================================================
12. POSITIONAL ARGUMENTS
============================================================

Normally, arguments are matched according to their position.

Example:

def introduce(name, age):
    print(name, age)

introduce('Diwakar', 18)

name = 'Diwakar'
age = 18

These are POSITIONAL ARGUMENTS.


============================================================
13. LOCAL VARIABLES
============================================================

A variable created inside a function normally belongs to
that function.

Example:

def test():
    x = 10
    print(x)

test()

You cannot normally use x outside the function:

print(x)

This causes a NameError because x is local to test().


============================================================
14. GLOBAL VARIABLES
============================================================

A variable created outside a function is in the global scope.

Example:

x = 10

def test():
    print(x)

test()

The function can read the global variable.

However, avoid relying heavily on global variables.

Functions are generally easier to understand when they
receive what they need through parameters and return
results.


============================================================
15. LOCAL VS GLOBAL
============================================================

Example:

x = 100

def test():
    x = 10
    print(x)

test()
print(x)

Output:

10
100

The x inside the function is a different local variable
from the global x.


============================================================
16. FUNCTIONS CAN CALL OTHER FUNCTIONS
============================================================

Example:

def square(x):
    return x * x

def double_square(x):
    return square(x) * 2

double_square(5)

First:

square(5) -> 25

Then:

25 * 2 -> 50


============================================================
17. FUNCTIONS CAN BE USED INSIDE EXPRESSIONS
============================================================

Example:

def add(a, b):
    return a + b

result = add(2, 3) * 10

result = 50

Because add(2, 3) returns 5.


============================================================
18. FUNCTIONS CAN TAKE COLLECTIONS
============================================================

A function can receive a list:

def total(numbers):
    result = 0

    for number in numbers:
        result += number

    return result

total([1, 2, 3, 4])


A function can receive a dictionary:

def display_scores(scores):
    for name, score in scores.items():
        print(name, score)


============================================================
19. FUNCTIONS CAN MODIFY MUTABLE OBJECTS
============================================================

Lists and dictionaries are mutable.

Example:

def add_item(items):
    items.append('apple')

my_list = ['banana']

add_item(my_list)

Now:

my_list = ['banana', 'apple']


A function can modify the same list/dictionary object that
was passed to it.

This is an important concept when working with lists and
dictionaries.


============================================================
20. *args
============================================================

*args allows a function to receive multiple positional
arguments.

Example:

def add_all(*numbers):
    total = 0

    for number in numbers:
        total += number

    return total

add_all(1, 2, 3, 4)

Inside the function, numbers behaves like a tuple.


IMPORTANT:

*args does NOT mean "arguments".

It is a common naming convention.

The * is what matters.


============================================================
21. **kwargs
============================================================

**kwargs allows a function to receive multiple keyword
arguments.

Example:

def show_info(**info):
    print(info)

show_info(name='Bob', age=18)

Inside the function, info is a dictionary:

{'name': 'Bob', 'age': 18}


IMPORTANT:

**kwargs is just a common name.

The ** is what matters.


============================================================
22. DOCSTRINGS
============================================================

A function can contain a description called a docstring.

Example:

def add(a, b):
    """Return the sum of a and b."""
    return a + b

The string immediately inside the function is its
docstring.


============================================================
23. FUNCTIONS AS REUSABLE TOOLS
============================================================

Instead of:

print(5 * 5)
print(10 * 10)
print(20 * 20)

You can write:

def square(x):
    return x * x

print(square(5))
print(square(10))
print(square(20))

The main advantage of functions is REUSABILITY.


============================================================
24. FUNCTION DESIGN
============================================================

A good function generally:

1. Does one clear job.
2. Takes necessary information through parameters.
3. Returns useful results when appropriate.
4. Avoids unnecessary global variables.
5. Has a meaningful name.


Example:

def find_highest_score(students):
    # function does one clear job
    ...


============================================================
25. FUNCTION vs METHOD
============================================================

FUNCTION:

A standalone callable.

Example:

len(my_list)

METHOD:

A function associated with an object and called using dot
notation.

Example:

my_list.append(10)

Here:

append() = method of a list

split() = method of a string

get() = method of a dictionary


Think:

function:
    function_name(...)

method:
    object.method(...)


============================================================
26. IMPORTANT: FUNCTIONS ARE OBJECTS TOO
============================================================

In Python, functions are objects.

This means they can be:

- stored in variables
- passed to other functions
- stored in collections
- returned from functions

Example:

def greet():
    print('Hello')

x = greet

x()

This calls greet().

Notice:

x = greet

does NOT call the function.

x = greet()

would call it and store its returned value.


============================================================
27. THE DIFFERENCE BETWEEN () AND NO ()
============================================================

This is VERY important.

greet

means:

"the function object itself"

greet()

means:

"CALL the function"


Example:

def greet():
    print('Hello')

x = greet

x()   # calls greet


============================================================
28. RECURSION
============================================================

A function can call itself.

Example:

def countdown(n):
    if n == 0:
        return

    print(n)
    countdown(n - 1)

countdown(3)

Output:

3
2
1

IMPORTANT:

A recursive function needs a condition that eventually
stops the recursion.

Otherwise it can continue indefinitely.


============================================================
29. COMMON MISTAKES
============================================================

Mistake 1:

def add(a, b):
    a + b

This does NOT return the result.

Correct:

def add(a, b):
    return a + b


Mistake 2:

Using return when you actually need to display something.

return does not automatically print.


Mistake 3:

Forgetting to call the function.

def greet():
    print('Hello')

This only defines it.

You need:

greet()


Mistake 4:

Confusing parameter and argument.

def greet(name):
    ...

'name' is the parameter.

greet('Bob')

'Bob' is the argument.


Mistake 5:

Trying to use a local variable outside its function.


============================================================
30. QUICK REFERENCE TABLE
============================================================

+--------------------------+----------------------------------+
| Concept                  | Example                          |
+--------------------------+----------------------------------+
| Define function          | def greet():                     |
| Call function            | greet()                          |
| Parameter                | def greet(name):                 |
| Argument                 | greet('Bob')                     |
| Return                   | return value                     |
| Default parameter        | def greet(name='Guest'):         |
| Keyword argument         | greet(name='Bob')                |
| Positional argument      | greet('Bob')                     |
| Multiple positional args | def f(*args):                    |
| Multiple keyword args    | def f(**kwargs):                 |
| Docstring                | """description"""                |
| Local variable           | variable inside function         |
| Global variable          | variable outside function        |
| Method                   | my_list.append(10)               |
+--------------------------+----------------------------------+


============================================================
31. MOST IMPORTANT THINGS TO REMEMBER
============================================================

1. def DEFINES a function.

2. function_name() CALLS the function.

3. A parameter is a placeholder in the function definition.

4. An argument is the actual value passed to the function.

5. return sends a value back to the caller.

6. return immediately ends the function.

7. print() displays something; return gives something back.

8. A function without an explicit return gives None.

9. Variables created inside a function are normally LOCAL
   to that function.

10. Functions are reusable blocks of code.

11. *args collects positional arguments into a tuple.

12. **kwargs collects keyword arguments into a dictionary.

13. Functions can receive and return lists, dictionaries,
    strings, numbers, and other objects.

14. A function can call another function.

15. A function can even be stored in a variable because
    functions are objects in Python.


============================================================
                    END OF FUNCTION NOTES
============================================================