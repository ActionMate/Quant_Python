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

a = [8, 3, 7, 3, 1, 9, 3, 5, 3]
k = 4
print(kth_smallest(a, k))