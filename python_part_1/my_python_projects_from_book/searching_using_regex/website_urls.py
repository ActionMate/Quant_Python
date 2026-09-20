import re, pyperclip

url_re = re.compile(r'''(
(?:http://|https://)
(?:www\.)?
(?:[a-zA-Z0-9-]+\.)+
(?:com|org|edu|gov|net|co|io|info)
)''', re.VERBOSE)

text = input('>> ')
matches = []

for group in url_re.findall(text):
    matches.append(group)

if len(matches)>0:
    print('copied to clipboard : ')
    print('\n'.join(matches))
else:
    print('No url addresses found.')
