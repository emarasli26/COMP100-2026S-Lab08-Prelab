from datetime import datetime

# Load exam dates into a dictionary
exam_dates = {}
student_courses = {}

def load_data(exam_dates, student_courses):
    with open("exam_dates.txt", "r") as file:
        next(file)
        for row in file:
            course, date_str = row.split(',')
            exam_dates[course] = datetime.strptime(date_str.strip(), "%Y-%m-%d")

    # Load student courses into a dictionary
    with open("student_courses.txt", "r") as file:
        next(file)
        for row in file:
            student, course = row.split(',')
            if student not in student_courses:
                student_courses[student] = []
            student_courses[student].append(course.strip())


def get_student_schedule(student_name, student_courses, exam_dates):
    output = []
    # Check if student exists
    if student_name not in student_courses:
        #print("Student not found.")
        output.append("Student not found.")
    else:
        timeline = []
        no_midterms = []
        for course in student_courses[student_name]:
            if course in exam_dates:
                timeline.append((exam_dates[course], course))
            else:
                no_midterms.append(course)

        # Sort and print exam schedule
        timeline.sort()
        for date, course in timeline:
            #print(f"{course} {date.strftime('%Y-%m-%d')}")
            output.append(f"{course} {date.strftime('%Y-%m-%d')}")

        if no_midterms:
            no_midterms.sort()
        for course in no_midterms:
            #print(f"No midterm exams scheduled for {course}.")
            output.append(f"No midterm exams scheduled for {course}.")

    return output