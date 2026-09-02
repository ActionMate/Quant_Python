n=int(input('Enter any number : '))
if n<=1:
    print('neither prime nor composite')
    c=2
    while c*c<=n:
        if n%c==0:
            print('Not prime')
            break
        else:
            c=c+1
    print('Prime')
    