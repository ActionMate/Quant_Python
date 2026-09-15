def swap_two_values():
    a=input('Enter 1st value : ')
    b=input('Enter 2nd value : ')
    a,b=b,a
    print('First value : ',a,', second value : ',b)

def count_digit():
    a=int(input('Enter digits : '))
    print('No. of digits : ', len(str(a)))

def sum_number():
    c=0
    while True:
        a=input('Enter number(s) or enter nothing to exit and get result: ')
        if a=='':
            break
        else:
            c+=int(a)
    print(c)

def factorial():
    n=int(input('Enter number you want factorial of : '))
    c=1
    for i in range(1,n+1):
        c*=i
    print('factorial : ',c)

def fibonacci():
    n=int(input('Enter number of terms : '))
    i,c=0,1
    for i in range(n):
        print(i)
        i,c=c,c+i

def reverse_number():
    '''   USING STRING 
    a=input('Enter a number : ')
    print('reverse number : ',a[::-1])
    '''

    '''  NO STRING  '''

    n=int(input('Enter a number : '))
    c=0
    while n>0:
        i=n%10
        c=c*10+i
        n=n//10
    print(c)

def base_conversion():
    # Program for Base Conversion
    n = int(input("Enter a decimal number: "))

    # Decimal to Binary
    num = n
    binary = ""

    if num == 0:
        binary = "0"
    else:
        while num > 0:
            remainder = num % 2
            binary = str(remainder) + binary
            num = num // 2

    # Decimal to Octal
    num = n
    octal = ""

    if num == 0:
        octal = "0"
    else:
        while num > 0:
            remainder = num % 8
            octal = str(remainder) + octal
            num = num // 8

    # Decimal to Hexadecimal
    num = n
    hexadecimal = ""

    digits = "0123456789ABCDEF"

    if num == 0:
        hexadecimal = "0"
    else:
        while num > 0:
            remainder = num % 16
            hexadecimal = digits[remainder] + hexadecimal
            num = num // 16

    print("Binary      :", binary)
    print("Octal       :", octal)
    print("Hexadecimal :", hexadecimal)

def characters_to_number():
    a=input('Enter characters : ')
    c=''
    for i in a:
        b=ord(i)
        c+=str(b)
    print('Number of your characters : ',c)

print('''
Welcome to Diwakar's coding assignment,
Type the respective number to interact:
1. Swap two values.
2. Count the Number of Digits.
3. Calculate the Sum of Numbers.
4. Calculate the Factorial of a Number.
5. Fibonacci Sequence.
6. Reverse a Number.
7. Base Conversion from decimal to binary/octal/hexadecimal.
8. Convert Characters to Numbers.
9. Exit''')

while True:
    user_input = input('Enter your choice : ')
    def choices(n):
        match n:
            case '1':
                swap_two_values()
            case '2':
                count_digit()
            case '3':
                sum_number()
            case '4':
                factorial()
            case '5':
                fibonacci()
            case '6':
                reverse_number()
            case '7':
                base_conversion()
            case '8':
                characters_to_number()
            case '9':
                return False
            case _:
                print("Please type from given choice")
        return True
    if choices(user_input) == False:
        break