student_scores=[1,2,3,4,5,6,7,8,9]

max=student_scores[0]
for n in range(0,len(student_scores)):
  if student_scores[n]>=max:
    max=student_scores[n]
print(max)