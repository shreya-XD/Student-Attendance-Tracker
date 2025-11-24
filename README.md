# Student-Attendance-Tracker

A simple command-line Python application to manage student attendance.
Users can add students, mark them present/absent, view attendance status, and remove students from the record.

## Features
Feature	Description
 1.Add Student	Add a new student to the attendance list
 2.View Attendance	Display the list of students with their attendance status
 3.Mark Attendance	Mark a student as Present or Absent
 4.Remove Student	Remove a student from the list
 5.Exit	Quit the program safely
## How It Works (Flow)
```bash
Start
   ↓
Display Main Menu
   ↓
User Selects Option
   → Add Student → Enter Name → Stored in List
   → View Attendance → Display Students + Status
   → Mark Attendance → Choose Number → Mark P/A
   → Remove Student → Choose Number → Remove Record
   → Exit Program → End
```
## Requirements

Python 3.x

Runs directly in a terminal or command prompt

No external libraries required

## How to Run

Copy the Python code into a file named:
```bash
attendance_tracker.py


Open a terminal in the file directory

Run the script:

python attendance_tracker.py
```

Use the number-based menu to interact with the program

## Code Structure
add_student()       # Add a student name


view_attendance()   # Display list and status


mark_attendance()   # Mark selected student P/A


remove_student()    # Remove student by number


main_menu()         # Application loop


## Known Limitations / Future Improvements
Improvement	Status
Prevent duplicate names	Not yet implemented
Mark attendance for all students at once	Planned
Save data to file (CSV / JSON)	Planned
Convert to OOP format	Optional enhancement
GUI version (Tkinter / PyQt)	Future update
## Author
## SHREYA DHAVAN
Student Attendance Tracker – Python Project
