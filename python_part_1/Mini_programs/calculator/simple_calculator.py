while True:
    print('''What do you want to do ? 
    1. Addition
    2. Substract
    3. Multiply
    4. Divide
    5. Expotential
    6. leave blank to exit''')
    choice=input('Enter your response : ')
    if choice == '':
        break

    if choice not in ('1','2','3','4','5','6'):
        print('Invalid choice.')

    else : 
        terms = int(input('How many terms you want? :  '))

        if terms <=0:
            print('You must enter atleast 1.')
            continue

        elif choice == '1':
            result = 0
            for i in range(terms):
                user_input=float(input('Enter number(s) :  '))
                result += user_input
            print(result)

        elif choice == '2':
            result = float(input('Enter number(s) :  '))
            for i in range(terms-1):
                user_input=float(input('Enter number(s) :  '))
                result -= user_input

        elif choice == '3':
            result = 1
            for i in range(terms):
                user_input=float(input('Enter number(s) :  '))
                result *= user_input

        elif choice == '4':
            result = float(input('Enter number(s): '))
            for i in range(terms-1):
                user_input=float(input('Enter number(s) : '))
                if user_input == 0:
                    print('Cannot divide by zero.')
                    break
                else:
                    result /= user_input

        if choice == '5':
            result = float(input('Enter number(s) :  '))
            for i in range(terms-1):
                user_input=float(input('Enter number(s) :  '))
                result **= user_input
    print('Result', result)