student_heights = (input("Enter the height\'s of students\'s\n")).split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

tot_height = 0
for heights in student_heights:
   tot_height += heights
print(f"Total Height of all Student's = {tot_height}")

tot_stu = 0
for students in student_heights:
   tot_stu += 1
print(f"Number of Student\'s = {tot_stu}")

print(f"Average height = {round(tot_height/tot_stu)}")