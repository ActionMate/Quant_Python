import re,pyperclip

nub=re.compile(r'''(
(?:[a-zA-Z0-9]+\.)?
[a-zA-Z]+
\.[a-zA-Z]{2,4}
)''', re.VERBOSE)

text = input('>> ')
matches = []

for group in nub.findall(text):
    matches.append(group)

if len(matches)>0:
    print('copied to clipboard : ')
    print('\n'.join(matches))
else:
    print('No url addresses found.')
