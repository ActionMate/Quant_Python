user_input=int(input('Enter any number : '))

def first_method():
    for number in range(2,user_input):
        count=0

        for divisor in range(2,number):
            if number % divisor == 0:
                count=count+1
            
        if count==0:
            print(number, end=', ')

            
def second_method():
    for number in range(2,user_input):
        is_prime = True

        for divisor in range(2,number):
            if number % divisor == 0:
                is_prime = False
                break

        if is_prime:
            print(number, end=', ')
