a = [4, 2, 7, 4, 9, 2, 4, 7, 2, 2]

def first_target_method():
    target = int(input('what number you wanna find? : '))
    print(a.count(target))

def second_target_method():
    count = 0
    target = int(input('what number you wanna find? : '))
    for i in a:
        if i==target:
            count+=1
    print(count)

def first_all_method():
    frequency = {}
    for i in a:
        if i in frequency:
            frequency[i]+=1
        else:
            frequency[i]=1
    print(frequency)

def second_all_method():
    unique = []
    for search in a:
        if search not in unique:
            unique.append(search)
    for unique_element in unique:   
        count = 0
    for target in a:
        if target == unique_element:
            count += 1
    print(unique_element, "appears", count, "time(s)")
