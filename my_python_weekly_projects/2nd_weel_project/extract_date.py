'''     QUESTION :  Copy a 5-page Wikipedia article into a string variable. Write a script that
                    instantly extracts every single date (e.g., DD/MM/YYYY or Month YYYY) mentioned
                    in the text.                                                                           '''

import pyperclip, re, time, sys

''' STEP 1 : Create a Regex for DATES. '''
date_re = re.compile(r'''(
    (?:\d{1,2}/\d{1,2}/\d{4}) | (?:\d{1,2}-\d{1,2}-\d{4}) |                                                         # DD/MM/YYYY or MM/DD/YYYY
    (?:\d{4}\s+(?:January|February|March|April|May|June|July|August|September|October|November|December)) |         # YYYY Month
    (?:(?:January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{4}) |         # Month YYYY
    (?:\d{4}/\d{1,2}/\d{1,2}) | (?:\d{4}-\d{1,2}-\d{1,2}) |                                                         # YYYY/DD/MM or YYYY/MM/DD
    (?:[a-zA-Z]+\s\d{1,2},\s\d{4}) | (?:\d{1,2}\s[a-zA-Z]+\s\d{4}) |                                                # Month DD, YYYY or DD Month YYYY
    (?:\b\d{4}\b)                                                                                                   # Standalone Year (isolated)     
)''', re.VERBOSE)

''' STEP 2 : Find All Matches in the Clipboard Text. '''
text = pyperclip.paste()
matches = []
for groups in date_re.findall(text):
    matches.append(groups)


''' STEP 3 :  Join the Matches into a String. '''
def dramatic_print(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()  

if len(matches)>0:
    dramatic_print("Connecting to the mainframe...", 0.08)
    dramatic_print("Access granted...", 0.03)
    dramatic_print("Loading..in...3...2...1...",0.08)
    dramatic_print("Loaded :",0.08)
    dramatic_print("now...searching...",0.1)
    dramatic_print("finding in....3...2...1...",0.5)
    dramatic_print("results : ",0.03)
    dramatic_print('\n'.join(matches),0.03)
else:
    dramatic_print("No Date found",0.08)