a=[10,20,30,40,50]

def first_method():
    print(a.reverse())

def second_method():
    left = 0
    right = len(a)-1
    while left<right:
        a[left], a[right] = a[right], a[left]
        left += 1
    print(a)

def third_method():
    for i in range(len(a) // 2):
        a[i], a[-1 - i] = a[-1 - i], a[i]
    print(a)

def fourth_method():
    for i in range(len(a)):
        a.insert(i,a.pop(len(a)-1))
    print(a)