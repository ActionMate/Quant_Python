message = input('Enter the English message to translate into pig latin : ')
VOWELS = ('a','e','i','o','u')
pig_latin=[]

for word in message.split():

    '''Separate the non-letters at the start of this word'''
    prefix_non_letter=''
    while len(word)>0 and not word[0].isalpha():
        prefix_non_letter += word[0]
        word=word[1:]
        if len(word)==0:
            pig_latin=pig_latin.append(prefix_non_letter)
            continue

    '''Separate the non-letters at the end of this word'''
    suffix_non_letter=''
    while word[-1].isalpha():
        suffix_non_letter= word[-1] + suffix_non_letter
        word = word[-1]

    ''' If word was in upper or lower case'''
    was_upper = word.isupper()
    was_title = word.istitle()

    word = word.lower()            #makes the word lowercase for translation

    '''Separate Consonant at the start of the word'''
    prefix_consonants = ''
    while len(word) > 0 and not word[0] in VOWELS:
        prefix_consonants += word[0]
        word = word[1:]

    ''' Add the pig latin ending to the word'''
    if prefix_consonants != '':
        word += prefix_consonants + 'ay'
    else:
        word += 'yay'

    ''' Set the word back to uppercase or title case. '''
    if was_upper:
        word = word.upper()

    if was_title:
        word = word.title()

    ''' Add the non-letters back to the start or end of the word.'''
    pig_latin.append(prefix_non_letter + word + suffix_non_letter)

''' Join all the words back together into a single string'''
print(' '.join(pig_latin))