def load_grade_weights():
    grade_weights = {}
    with open("grade_weights.txt", "r") as file:
        next(file)
        for row in file:
            letter, gpa = row.split(',')
            grade_weights[letter.strip()] = float(gpa.strip())
    return grade_weights

def load_course_credits():
    course_credits = {}
    with open("courses.txt", "r") as file:
        next(file)
        for row in file:
            course, credit = row.split(',')
            course_credits[course.strip()] = int(credit.strip())
    return course_credits

def process_student_grades(grade_weights, course_credits):
    student_grades = {}
    student_credits = {}
    invalid_courses = set()
    invalid_grades = set()
    messages = []

    with open("student_grades.txt", "r") as file:
        next(file)  # Skip header
        for row in file:
            name, course, grade = row.strip().split(',')

            if course not in course_credits:
                if course not in invalid_courses:
                    invalid_courses.add(course)
                    messages.append(f"Course {course} not found.")
            elif grade not in grade_weights:
                if grade not in invalid_grades:
                    invalid_grades.add(grade)
                    messages.append(f"Grade {grade} not found.")
            else:
                credit = course_credits[course]
                gpa_value = grade_weights[grade]

                if name not in student_grades:
                    student_grades[name] = 0.0
                    student_credits[name] = 0

                student_grades[name] += gpa_value * credit
                student_credits[name] += credit

    return student_grades, student_credits, messages

def calculate_gpa_table(student_grades, student_credits):
    gpa_table = []
    for name in student_grades:
        total_points = student_grades[name]
        total_credits = student_credits[name]
        gpa = round(total_points / total_credits, 2)
        gpa_table.append((gpa, name))
    return gpa_table

def organize_gpa_table(gpa_table):
    gpas = {}
    for gpa, name in gpa_table:
        if gpa not in gpas:
            gpas[gpa] = []
        gpas[gpa].append(name)
        gpas[gpa].sort()
    return gpas

def write_gpa_ranking(gpas):
    with open("gpa_ranking.txt", "w") as f:
        for gpa in sorted(gpas.keys(), reverse=True):
            for name in gpas[gpa]:
                f.write(f"{name} {gpa}\n")

def generate_gpa_ranking():
    grade_weights = load_grade_weights()
    course_credits = load_course_credits()
    student_grades, student_credits, messages = process_student_grades(grade_weights, course_credits)
    gpa_table = calculate_gpa_table(student_grades, student_credits)
    gpas = organize_gpa_table(gpa_table)
    write_gpa_ranking(gpas)
    return messages