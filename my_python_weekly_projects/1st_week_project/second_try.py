# Write a function that takes a dictionary of 10 fictional students and their math scores, 
# and returns the name of the student with the highest score without using built-in max() functions.

students = {'Student_1':77, 'Student_2':89, 'Student_3':45, 'Student_4':87,'Student_5':97, 
            'Student_6':82,'Student_7':33, 'Student_8':76,'Student_9':72, 'Student_10':87}
d = {'': 0}
def method_1():
    for k, v in students.items():
        if v > list(d.values())[0]:
            d.popitem()
            d[k] = v

    print(d)

def method_2():
    for k, v in students.items():
        if v > list(d.values())[0]:
            d.clear()
            d[k] = v
    print(d)
