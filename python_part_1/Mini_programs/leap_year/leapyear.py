while True:
    year = input('Enter any year(don\'n type anything to quit): ')

    if year=='':
        break

    elif int(year)%100==0:
        if int(year)%400==0:
            print(year, 'is Leap year')
        else:
            print(year, 'is Not leap year')

    elif int(year)%4==0:
        print(year, 'is Leap year')
    else:
        print(year, 'is Not leap year')