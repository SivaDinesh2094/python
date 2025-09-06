#Task 1

student_data = {
    "dinesh" : "90,78,45",
    "karthi" : "89,45,54",
    "arul" : "91,45,89",
    "murugan" : "99,90,76"
    
    }
student_name=input("Enter the Student's name:").lower()
   
if (student_name in student_data):
    print(student_name+"\'s marks:",student_data[student_name])
else:
    print("Student not found.")

#task 2

org_list = [1,2,3,4,5,6,7,8,9,10]

first_five = org_list[0:5]
Reverse_first_five = first_five[::-1]
print("Original list:",org_list)
print("Extracted first five elemets:",first_five)
print("Reversed Extracted elemets:",Reverse_first_five)
