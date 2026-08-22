user_input=int(input('Enter any number : '))
count=0

for divisor in range(2,user_input//2):
    if user_input % divisor == 0:
        count=count+1
            
if count==0:
    print('is prime')
else:
    print('not prime')