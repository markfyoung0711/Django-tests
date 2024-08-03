# Django - Student/Class

## Requirements.

### Overview:
#### Basics
1. Create Students
1. Create Courses
1. Assign Courses to Students
1. Print Report
#### Advanced
1. Manage Schedule of Course
1. Manage Status of Course
1. Manage Status of Student
#### Advanced 2
1. Payment/Cost
1. Discount



### GUI

#### Basic
Login
Create Student
Create Course
Student Signup for Course


### Objects:
1. Student
    behavior: modify, deactivate, delete.
    attributes: student_id, name, dob, status

2. Create Course 
    behavior: modify, deactivate, schedcule, delete.
    attributes: course_id, name, description, date, time, cost, status (schedule - advanced)

3. Schedule
    operates like a calendar, but what are the differences from a calendar
    behavior: view, whitelist, blacklist
    attributes: date, time
    examples: winter schedule, fall, etc., holidays

### Design Steps
1. start with GUI screens as HTML templates
2. create DB tables in SQLite to handle User, Student, Course, Enrollment
3. create classes for basics
4. write cli version of application
5. write API for doing the functions/behaviors that can be done at command line

