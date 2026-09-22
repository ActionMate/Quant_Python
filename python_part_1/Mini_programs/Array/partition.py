a = [8, 3, 7, 1, 5, 9, 2, 6, 4]
pivot = 5
def first_method():
    smaller = []
    larger = []
    for i in a:
        if i<pivot:
            smaller.append(i)
        elif i>pivot:
            larger.append(i)
    print(smaller+[pivot]+larger)

def second_method():
    a = [8, 3, 7, 1, 9, 2, 3, 4]
    pivot = 5
    left = 0
    right = len(a)-1
    while left<right:
        while left<right and a[left]<pivot:
            left+=1
        while left<right and a[right]>pivot:
            right-=1
        if left<right:
            a[left], a[right] = a[right], a[left]
    print(a)
second_method()