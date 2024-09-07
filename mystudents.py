import pandas as pd
import time as t
name1 = input("Student name - 1 : ")
name2 = input("Student name - 2 : ")
name3 = input("Student name - 3 : ")
name4 = input("Student name - 4 : ")
name5 = input("Student name - 5 : ")
name6 = input("Student name - 6 : ")
grade1 = input("Student grade - 1 : ")
grade2 = input("Student grade - 2 : ")
grade3 = input("Student grade - 3 : ")
grade4 = input("Student grade - 4 : ")
grade5 = input("Student grade - 5 : ")
grade6 = input("Student grade - 6 : ")
degree1 = input("Student degree - 1 : ")
degree2 = input("Student degree - 2 : ")
degree3 = input("Student degree - 3 : ")
degree4 = input("Student degree - 4 : ")
degree5 = input("Student degree - 5 : ")
degree6 = input("Student degree - 6 : ")
age1 = input("Student age - 1 : ")
age2 = input("Student age - 2 : ")
age3 = input("Student age - 3 : ")
age4 = input("Student age - 4 : ")
age5 = input("Student age - 5 : ")
age6 = input("Student age - 6 : ")
students = {
    "grades": [grade1, grade2, grade3, grade4, grade5, grade6],
    "degrees": [degree1, degree2, degree3, degree4, degree5, degree6],
    "age": [age1, age2, age3, age4, age5, age6]
}

print(pd.DataFrame(students, index=[name1, name2, name3, name4, name5, name6]))