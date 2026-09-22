a = [8, 3, 7, 3, 1, 9, 3, 5]
k=4
'''

for i in range(len(a)):
    for j in range(len(a)-i-1):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]
print(a[k-1])

'''

def partition(a, left, right):
    pivot = a[(left + right) // 2]
    while left <= right:
        while a[left] < pivot:
            left += 1
        while a[right] > pivot:
            right -= 1
        if left <= right:
            a[left], a[right] = a[right], a[left]
            left += 1
            right -= 1
    return left

def kth_smallest(a, k):
    target = k - 1
    left = 0
    right = len(a) - 1
    while left < right:
        point = partition(a, left, right)
        if target < point:
            right = point - 1
        else:
            left = point
    return a[left]

print(kth_smallest(a, k))