def show_header(): 
    print("===================================")
    print("=====STUDENT MANAGEMENT SYSTEM=====")
    print("===================================")

def collect_student_info():
    name = input("Enter your name: ")
    student_id = input("Enter your student ID: ")
    department = input("Enter your department: ")
    semester = input("Enter your semister: ")\

    return name, student_id, department, semester


def show_student_info():
    name, student_id, department, semester = collect_student_info()

    print("\nStudent Information")
    print("---------------------")
    print("Name         : ", name)
    print("Student ID   : ", student_id)
    print("Department   : ", department)
    print("Semester     : ", semester)

def collect_academic_status():
    global cgpa, credits, status, standing

    cgpa = input("Enter your CGPA: ")
    credits = input("Enter then credits: ")
    status = input("Enter the status: ")
    standing = input("Enter the standing: ")


def show_academic_status():
    print("\nAcademic Status")
    print("-----------------")
    print("CGPA     : ", cgpa)
    print("Credits  : ", credits)
    print("Status   : ", status)
    print("Standing : ",standing)

def show_footer():
    print("===================================")
    print("======End of Student Profile=======")
    print("===================================")


show_header()
show_student_info()

collect_academic_status()
show_academic_status()
show_footer()


