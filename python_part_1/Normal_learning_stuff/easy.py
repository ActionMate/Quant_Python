import random
def get_answer(ans_number):
    if ans_number==1:
        return 'it is certain'
    elif ans_number==2:
        return 'is is idk'
    elif ans_number==3:
        return 'damn, you suck'
    elif ans_number==4:
        return 'yes'
    elif ans_number==5:
        return 'nah, dawg'
    elif ans_number==6:
        return 'My reply is....no'
    elif ans_number==7:
        return 'Toasted'
    elif ans_number==8:
        return 'Toaster is BROKEN !'
    elif ans_number==9:
        return 'You want to play, Less play'
    
while True:
    i = input('wanna gamble? (Yes/No) : ').upper()
    if i=='YES':
        r=random.randint(1,9)
        fortune=get_answer(r)
        print(fortune)
    elif i=="NO":
        print('okay')
        break
    else: 
        print('Please write yes or no because my love told me to 🤷‍♂️')