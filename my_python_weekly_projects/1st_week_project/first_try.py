# Write a function that takes a dictionary of 10 fictional students and their math scores, 
# and returns the name of the student with the highest score without using built-in max() functions.

students = {'Student_1':77, 'Student_2':89, 'Student_3':45, 'Student_4':87,'Student_5':97, 
            'Student_6':82,'Student_7':33, 'Student_8':76,'Student_9':72, 'Student_10':87}
name=''
max_num=0
for k,v in students.items():
    if v>max_num:
        max_num=v
        name=k
    else:
        continue
print('Highest Marks is ',max_num,'. Scored by ',name)