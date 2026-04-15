# Software-Development-Fundamentals-week7
This is my Week 7 lab activity where I created a Student Attendance Tracking System prototype. I did not use classes because I found them complicated, so I implemented it in a way that was easier for me to manage. The program uses a list to store all student records and a counter to generate unique student IDs automatically.

In the first task, I added a student record. I created a function called add_student that takes input from the user for the student’s name, course, and attendance percentage. I used a global variable id_counter to keep track of student IDs and increment it each time a new student is added. The ID is generated in the format STU001, STU002, and so on. I stored all student information in a tuple and appended it to the list of students. A confirmation message is printed to show the student was added successfully and display the generated student ID.

In the second task, I updated existing student records using the update_student function. This function asks the user for the student ID and searches the list of students to find a match. The user can choose to update either the attendance percentage or the course name. I retrieved the current student information from the tuple so that values not being changed remain the same. I replaced the old tuple with a new one that contains the updated value. A confirmation message is shown if the update is successful, or a message appears if the student ID is not found.

The third task was displaying all student records. I made a function called display_all that prints all students in a formatted way. A loop goes through each student tuple in the list and prints the student ID, name, course, and attendance percentage. A check is included to handle the case when no student records exist.

The fourth task calculates the average attendance percentage of all students. The average_attendance function sums the attendance percentages of all students and divides by the total number of students to find the average. I used .2f formatting to show the result with two decimal places. A check is included to handle the case when the list of students is empty.

The main program runs the system with a menu using a loop. The menu gives options to add a student, update a student, display all students, calculate the average attendance, or exit the program. The loop continues until the user chooses to exit, and input validation handles invalid choices.

This lab activity helped me practice using lists, tuples, functions, loops, and basic input/output in Python. It also allowed me to organize and manage data efficiently without using classes while keeping the program functional and user-friendly.
