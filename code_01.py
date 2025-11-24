#Student Attendance Tracker

#Features:
#1. Add Student
#2. Mark Student Present/Absent
#3. View Attendance
#4. Remove Student
#5. Exit Application

students=[] #list of student names
attendance=[] #matching attendance list (Present/Absent)

def add_student():
    name=input('Enter student name: ')
    if name=="":
        print("Name cannot be empty")
    else:
        students.append(name)
        attendance.append('Not Marked')
        print(f"Student '{name}' added successfully!\n")

def view_attendance():
    print("\n---Attendance List---\n")
    if len(students)==0:
        print('No students added yet.\n')
        return
    for i, name in enumerate(students,1):
        print(f'{i}).{name}-{attendance[i-1]}')
    print()

def mark_attendance():
    if len(students)==0:
        print('No Students to mark attendance for.\n')
        return

    view_attendance()

    try:
        num=int(input("Enter Student Number:"))
        if 1<=num<=len(students):
            status=input('Enter P for Present or A for Absent:').upper()
            if status=='P':
                attendance[num-1]='Present'
                print('Attendance marked as present.\n')
            elif status=='A':
                attendance[num-1]='Absent'
                print('Attendance marked as absent.\n')
            else:
                print('Invalid Input.\n')
        else:
            print('Invalid Student Number.\n')

    except ValueError:
        print('Please enter a valid number.\n')

def remove_student():
    if len(students)==0:
        print('No Students To Remove.\n')
        return

    view_attendance()

    try:
        num=int(input("Enter Student Number:"))
        if 1<=num<=len(students):
            removed_name=attendance.pop(num-1)
            attendance.pop(num-1)
            print(f"Student '{removed_name}' removed successfully!\n")
        else:
            print('Invalid Student Number.\n')

    except ValueError:
        print('Please enter a valid number.\n')


def main_menu():
    while True:
        print('---Attendance Menu---\n')
        print('1. Add Student')
        print('2. View Attendance')
        print('3. Mark Attendance')
        print('4. Remove Student')
        print('5. Exit')

        choice=(input('Enter Your Choice'))

        if choice=='1':
            add_student()
        elif choice=='2':
            view_attendance()
        elif choice=='3':
            mark_attendance()
        elif choice=='4':
            remove_student()
        elif choice=='5':
            print('Exiting Attendance Tracker, Thank You!')
            break
        else:
            print('Invalid Option, Please Try Again.\n')

main_menu()



