l1 = [1,1,1,2,2,3,4,5,6,6,7,8,11]
new_list = []
for one_student_choice in l1:
    if one_student_choice not in new_list:
        new_list.append(one_student_choice)

print(new_list)