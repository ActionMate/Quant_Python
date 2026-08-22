
while True:
    a=input("Enter anything to find Palindrome (don't type anything to exit) : ")
    if a=='':
        break
    elif a==a[::-1]:
        print('Palindrome')
    else:
        print('not Palindrome')