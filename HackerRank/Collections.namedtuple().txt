from collections import namedtuple
n = int(input())
columns = input().split()
Student = namedtuple('Student', columns)
total = 0
for i in range(n):
    row = input().split()
    student = Student(*row)
    total = total + int(student.MARKS)

average = total / n

print("{:.2f}".format(average))