studentList = []


def addStudent():
    name = input("Enter the name of the student :")
    rno = int(input("Enter the roll no. of the student :"))
    mark = int(input("Enter the mark of the student :"))
    studentTup = (rno,name,mark)
    studentList.append(studentTup)
    print("Student Details successfully added!!")


def remStudent():
    rno = int(input("Enter the roll no. of the student to be removed :"))
    for student in studentList:
        if student[0] == rno:
            studentList.remove(student)
            print("Student successfully removed!!")
            return
    print("No such roll no has been found")


def searchStudent():
    rno = int(input("Enter the roll no. of the student :"))
    for student in studentList:
        if student[0] == rno:
            print("Name : ",student[1])
            print("Roll No : ",student[0])
            print("Mark : ",student[2])
            print("=============================")
            return
    print("No such roll no has been found")


def maxStudent():
    maxMark = max([student[2] for student in studentList])
    maxMarkStudent = [student for student in studentList if student[2] == maxMark]
    print("Details of Students with Highest Mark:")
    for student in maxMarkStudent:
        print("Name : ",student[1])
        print("Roll No : ",student[0])
        print("Mark : ",student[2])
        print("=============================")


while 1:
    print()
    print("1)add")
    print("2)remove")
    print("3)search")
    print("4)Max")
    print("5)Exit")
    op = int(input("Choose operation :"))
    if op == 1:
        addStudent()
    elif op == 2:
        remStudent()
    elif op == 3:
        searchStudent()
    elif op == 4:
        maxStudent()
    elif op == 5:
        break
    else:
        print("Invalid input!!")