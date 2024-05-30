def grades(a,b,c,d,i,j,k,l):
    students=[]
    studentsscore=[]
    studentsgrades=[]
    studentsname=[]
    h=[]
    q=[]
    t=[]
    e=[]
    print("Welcome Professor Mojo Jojo,")
    num=int(input("how many students would you be submitting grades for today? "))
    for i in range(num):
        studentsname.append(input("please enter the student's name: "))
        h.append(int(input("please enter the homework grade: ")))
        q.append(int(input("please enter the quizzes grade: ")))
        t.append(int(input("please enter the tests grade: ")))
        e.append(int(input("please enter the exam grade: ")))
        studentsscore.append((a*h[i])+(b*q[i])+(c*t[i])+(d*e[i]))
    for i in range(num):
        if (studentsscore[i]>=i):
         studentsgrades.append("A")
        elif (studentsscore[i]>=j):
         studentsgrades.append("B")
        elif (studentsscore[i]>=k):
         studentsgrades.append("C")
        elif (studentsscore[i]>=l):
         studentsgrades.append("D")
        else:
         studentsgrades.append("F")
    print(studentsname)
    print("The grade(s) for your "+str(num)+" student(s) is(are): "+str(studentsgrades))
    for j in range(num):
        print(studentsname[j] + " got a(n) "+studentsgrades[j]+".")
 
grades(0.06,0.24,0.3,0.4,90,80,70,60)
