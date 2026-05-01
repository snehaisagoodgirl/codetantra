import numpy as np

a = np.loadtxt("Sample.csv", delimiter=',', skiprows=1)

# 1Print all student detals
print("All student Details:\n", a)
# 2Print total stidents
print("Total Students:", a.shape[0])
# 3 Print all studens rollnumbers
print("All Student Roll Nos", a[:, 0])
#  4Print subject1 marks
print("Subject 1 Marks", a[:, 1])
# 5print minimun marks of subject2
print("Min marks in Subject 2", np.min(a[:, 2]))
# 6print maximun marks of subjerct3
print("Max marks in Subject 3", np.max(a[:, 3]))
# 7print all subject marks
print("All subject marks:", a[:, 1:])
# 8 print total marks of students
print("Total Marks", np.sum(a[:, 1:], axis=1))
# 9print avarage marks of each students
print(np.round(np.mean(a[:, 1:], axis=1), 1))
# 10print avarage marks of each subject
print("Average Marks of each subject" ,np.round(np.mean(a[:, 1:], axis=0), 1))
# 11print avarage marks of s1 and s2
print("Average Marks of S1 and S2", np.round(np.mean(a[:, 1:3], axis=0), 1))
# 12print avarage marks of s1 and s3
print("Average Marks of S1 and S3", np.round(np.mean(a[:, [1, 3]], axis=0), 1))
# 13print roll number who got maximum marks in subject3
print("Roll no who got maximum marks in Subject 3", a[np.argmax(a[:, 3]), 0])
# 14 print roll number who got minium marks in subject2
print("Roll no who got minimum marks in Subject 2", a[np.argmin(a[:, 2]), 0])
# 15print roll number who got 24 marks in subject2
print("Roll no who got 24 marks in Subject 2", a[a[:, 2] == 24][:, [0]])
# 16print count of students who got marks in subject1<40
print("Count of students who got marks in Subject 1 < 40", np.sum(a[:, 1] < 40))
# 17print count of students who got marks in sssubject2 >90
print("Count of students who got marks in Subject 2 > 90:", np.sum(a[:, 2] > 90))
# 18print count of students in each subject who got marks>=90
print("Count of students in each subject who got marks >= 90:", np.sum(a[:, 1:] >= 90, axis=0))
# 18print count of subjects in which each students who got marks>=90
print("Roll no:", a[:, 0])
print("Count of subjects in which student got marks >= 90:", np.sum(a[:, 1:] >= 90, axis=1))
# 20print s1 marks in assending order
print(np.sort(a[:, 1]))
#21 print s1marks >=50 and <=90
print(a[(a[:, 1] >= 50) & (a[:, 1] <= 90)])

print(a)
# 22print the index position of marks 79
print(np.where(a[:, 1] == 79))
