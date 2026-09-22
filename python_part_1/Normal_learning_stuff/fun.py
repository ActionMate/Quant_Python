import time
import sys

def dramatic_print(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()  
v=10
k='wood'
c=str(v)+k
dramatic_print(c, 0.08)
dramatic_print("Connecting to the mainframe...", 0.08)
dramatic_print("Access granted...", 0.03)
dramatic_print("Loading..in..",0.08)
dramatic_print("searching...",0.1)
dramatic_print("finding in....3...2...1...",0.4)
dramatic_print("founded",0.1)
dramatic_print("Showing results...",0.1)
dramatic_print("and the result is : Vansh is GAY.",0.08)
