'''
Student Attendance Tracking System Prototype
Week 7 Lab Session
I do not use clss yet beacuse i got complicated for that's why i used as my personal easiest way
'''

students = []   # making the list to store all the student records
id_counter = 0  # preparing for auto generating student id


'''
Task 1 : Add the student record
'''

def add_student():

    name = input("Enter student name: ")
    course_name = input("Enter course name: ")
    attendance_percentage = float(input("Enter attendance percentage: "))

    global id_counter   # making the id_counter global so we can use and change it inside the function
    id_counter = id_counter + 1

    student_id = f"STU{id_counter:03d}"     # making the student id like STU001, STU002

    # making a tuple to store all the student info together
    student = (student_id, name, course_name, attendance_percentage)

    students.append(student)    # adding the student tuple into the list

    # printing the confirmation message
    print(f"\nStudent added successfully!")     # using \n for print them into new line
    print(f"Generated Student Id: {student_id}")


'''
Task 2 : Update the existing student record
'''

def update_student():

    student_id = input("\nEnter the student id to update: ")

    # making the loop to search the student by their id
    for i in range(len(students)):

        if students[i][0] == student_id:   # checking the id match or not, [0] is the student_id in the tuple

            print("\nWhat do you want to update?")
            print("1. Attendance Percentage")
            print("2. Course Name")
            choice = input("Enter your choice: ")

            # getting the current values from the tuple so we can keep the ones we dont change
            current_id = students[i][0]
            current_name = students[i][1]
            current_course = students[i][2]
            current_attendance = students[i][3]

            if choice == "1":
                new_attendance = float(input("Enter new attendance percentage: "))
                # replacing the old tuple with a new one with the updated attendance
                students[i] = (current_id, current_name, current_course, new_attendance)
                print("Attendance percentage updated successfully!")     # confirmation message

            elif choice == "2":
                new_course = input("Enter new course name: ")
                # replacing the old tuple with a new one with the updated course
                students[i] = (current_id, current_name, new_course, current_attendance)
                print("Course name updated successfully!")   # confirmation message

            else:
                print("Invalid choice!")

            return  # stopping the loop once we found and updated the student

    print("Student Id not found!")  # printing the message if the id is not in the list


'''
Task 3 : Display all the student records
'''

def display_all():

    print("\nPrinting All Student Records:")  # using \n for print them into new line
    print("-" * 35)     # using dashes to separate the header from the records

    if len(students) == 0:  # checking if the list is empty or not
        print("No student records found!")
        return

    # making the loop to display all the students one by one
    for student in students:

        # getting each value from the tuple using index
        print(f"Student Id:            {student[0]}")
        print(f"Student Name:          {student[1]}")
        print(f"Course Name:           {student[2]}")
        print(f"Attendance Percentage: {student[3]}%")
        print("-" * 35)     # using dashes to separate each student clearly


'''
Task 4 : Calculate the average attendance percentage
'''

def average_attendance():

    if len(students) == 0:  # checking if the list is empty or not
        print("No student records found!")
        return

    total = 0

    # making the loop to add all the attendance percentage together
    for student in students:
        total = total + student[3]  # [3] is the attendance percentage in the tuple

    average = total / len(students)     # dividing the total by number of students

    # printing the average attendance
    print(f"\nAverage Attendance Percentage: {average:.2f}%")  # using .2f to show 2 decimal places


'''
Main Program : running the system with a menu
'''

# making the loop so the menu keeps showing until the user exits
while True:

    # printing the menu options
    print("\n=============================")
    print("  Student Attendance System  ")
    print("=============================")
    print("1. Add Student")
    print("2. Update Student")
    print("3. Display All Students")
    print("4. Average Attendance")
    print("5. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        update_student()

    elif choice == "3":
        display_all()

    elif choice == "4":
        average_attendance()

    elif choice == "5":
        print("Goodbye!")
        break   # breaking the loop to exit the program

    else:
        print("Invalid choice! Please try again.")