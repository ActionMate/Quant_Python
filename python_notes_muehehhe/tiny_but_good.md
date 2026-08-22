============================================================
                  QUICK OPERATOR TABLE
============================================================

Operator    Meaning                  Example
------------------------------------------------------------
+           Addition                 5 + 2  -> 7
-           Subtraction              5 - 2  -> 3
*           Multiplication           5 * 2  -> 10
/           Division                 5 / 2  -> 2.5
//          Floor division           5 // 2 -> 2
%           Remainder / modulo       5 % 2  -> 1
**          Power                    5 ** 2 -> 25

==          Equal to                 a == b
!=          Not equal to             a != b
>           Greater than             a > b
<           Less than                a < b
>=          Greater/equal             a >= b
<=          Less/equal                a <= b

and         Both conditions true     a and b
or          At least one true        a or b
not         Reverse Boolean          not a

in          Membership               x in items
not in      Not a member             x not in items
is          Same object              x is None
is not      Different objects        x is not None


============================================================
                 PYTHON TINY REFERENCE
============================================================

THING              MEANING / REMINDER
------------------------------------------------------------
=                  Assign a value
==                 Compare values
is                 Check if same object
%                  Remainder / modulo
//                 Floor division
**                 Power / exponent
and                Both conditions must be true
or                 At least one condition must be true
not                Reverse True/False
in                 Check membership
not in             Check non-membership

input()            Always returns a STRING
int()              Convert to integer
float()            Convert to float
str()              Convert to string
bool()             Convert to Boolean

len(x)             Length / number of items
type(x)            Type of an object
range()            Commonly used for loops
round(x)            Round a number
sum(x)             Add values
sorted(x)          Return sorted result
max(x)             Largest value
min(x)             Smallest value

break              Exit the loop
continue           Skip to next iteration
pass               Do nothing / placeholder

split()            STRING -> usually LIST
join()             STRINGS -> ONE STRING
[::-1]             Reverse a sequence

range(5)           0, 1, 2, 3, 4
range(2, 6)        2, 3, 4, 5
                   STOP IS EXCLUDED

text[0:3]          First 3 characters
text[:3]           From beginning to index 2
text[3:]           From index 3 onward
text[-1]           Last character
text[::-1]         Reverse string
text[::2]          Every second character
                   STOP IS EXCLUDED


============================================================
              IF / ELIF / ELSE REMINDER
============================================================

if condition:
    ...

elif another_condition:
    ...

else:
    ...

IMPORTANT:
Python checks from TOP to BOTTOM.

The FIRST condition that is True wins.

So:

if x > 0:
    ...
elif x > 10:
    ...

The elif will NEVER run for x > 10 because x > 0
was already True.


============================================================
              PALINDROME BUG REMINDER 😭
============================================================

''[::-1] == ''

Therefore:

if text == text[::-1]:
    print("Palindrome")
elif text == '':
    break

An empty string will be detected as a palindrome FIRST.

If empty input means "quit", check it FIRST:

if text == '':
    break
elif text == text[::-1]:
    print("Palindrome")
else:
    print("Not palindrome")


============================================================
                 QUICK DEBUG CHECKLIST
============================================================

When something behaves strangely:

1. What are my variable values?
2. What are their TYPES?
3. What does each condition evaluate to?
4. Which if/elif branch is actually running?
5. Is my condition order correct?
6. Am I accidentally using the last loop value?
7. Am I confusing =, == and is?
8. Did input() give me a string?
9. Did I remember what this operator does?
10. Can I isolate the problem in a tiny experiment?


============================================================