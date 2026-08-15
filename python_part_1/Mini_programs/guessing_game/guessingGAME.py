#Guess the Number GAME
import random

secret_number=random.randint(1,30)

print('Lets Play a guessing GAME')
print('Think a Number between 1 to 30')

#Guess limit is 10
for guess_taken in range(1,11):
    guess=int(input('Take a Guess : '))
    if guess==secret_number:
        print('Congrats, you got it in',guess_taken,'Attempts.')
        break

#This if if the guess is HIGH 
    elif guess>secret_number:
        difference=guess-secret_number
        if difference<=3:
            print('Your guess is little bit high')
        elif difference<=5:
            print('Your guess is high')
        else:
            print('Your guess is way too high')
        print("Retry again!")

#This is if the guess is LOW
    elif guess<secret_number:
        difference=secret_number-guess
        if difference<=3:
            print('Your guess is little bit low')
        elif difference<=5:
            print('Your guess is Low')
        else:
            print('Your guess is way too Low')
        print("Retry again!")
    
if guess!=secret_number:
    print('You ran out of limits ! the secrect number was', secret_number,".")
    