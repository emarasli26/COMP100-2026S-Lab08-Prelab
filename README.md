# COMP100-2025F-Lab08-Prelab


## Question 1: Student Midterm Schedule (35 points)

### Objective:
You are part of the university's exam planning committee. Generate a student-specific midterm exam schedule based on the input files.

Input Files:

exam_dates.txt: CourseName,MidtermDate

```python
CourseName,MidtermDate
COMP100,2025-05-10
COMP130,2025-05-15
COMP131,2025-05-20
MATH102,2025-05-18
...etc.
```

student_courses.txt: StudentName,CourseName

```python
Name,CourseName
Alice,COMP100
Alice,PHYS101
Bob,COMP130
George,COMP130
...etc.
```


**Dates**:

For parsing dates and performing date calculations, familiarize yourself with the `datetime` library by reading the [Python 3 datetime documentation](https://docs.python.org/3/library/datetime.html).

You'll need to convert the `MidtermDate` string for each course to a `datetime` object to work with it. Here's an example of how to do this:


```python
from datetime import datetime

date_object = datetime.strptime(midterm_date, '%Y-%m-%d')
```

.strftime('%Y-%m-%d') formats the date in the "year-month-day" format:
```python
from datetime import datetime

date = datetime(2025, 4, 26)
print(f"{date.strftime('%Y-%m-%d')}") # Output: 2025-04-26
```

You are strongly encouraged to use these two functions for this lab.

**Hint**: You can use the .sort() function of lists to sort the courses and the midterm dates.



### Steps:

1- Read exam schedule and student course enrollments.

2- Given a student name, find enrolled courses.

3- Match courses to midterm dates.

4- Take input as the student's name.

5- If student exists, sort the student's timeline by date; otherwise display the message: "Student not found.".

6- Display "No midterm exams scheduled for coursename." if there is no midterm of the course If there are several courses, first sort the course names alphabetically and then print the messages accordingly.

7- Collect the messages in a list in the correct order and return the list. Displaying the messages is not required; it is essential to return the **list**.

Example 1:
```
get_student_schedule("Alice", student_courses, exam_dates)
```
Output: 
```
COMP100 2025-05-10
PHYS101 2025-05-12
No midterm exams scheduled for MATH101.
```

Example 2:
```
get_student_schedule("Frank", student_courses, exam_dates)
```
Output:
```
COMP100 2025-05-10
PHYS101 2025-05-12
No midterm exams scheduled for PHYS106.
```

Example 3:
```
get_student_schedule("Jerry", student_courses, exam_dates)
```
Output:
```
Student not found.
```

Example 4:
```
get_student_schedule("Bob", student_courses, exam_dates)
```
Output:
```
COMP130 2025-05-15
No midterm exams scheduled for MATH101.
No midterm exams scheduled for PHYS106.
```

## Question 2: Student GPA Ranking (35 points)

### Objective:
You are part of the university's academic records team. Build a program that reads student names and their letter grades from a file, converts them to GPA points, calculates each student's GPA, and generates a GPA ranking table.

student_grades.txt: StudentName,CourseName,Grade

```python
Name,Course,Grade
Alice,COMP100,A
Alice,MATH101,A-
...etc.
```

grade_weights.txt: Grade,Weight
```
Grade,Weight
A+,4.0
A,4.0
A-,3.7
B+,3.3
B,3.0
B-,2.7
C+,2.3
C,2.0
C-,1.7
D+,1.3
D,1.0
F,0.0
```

courses.txt: Course,Credit
```
Course,Credit
COMP100,3
COMP130,4
COMP131,4
... etc.
```

### Steps:

1- Read the files.

2- For each student in student_grades.txt, convert letter grades to GPA according to grade_weights.txt. 

3- While reading student_grades.txt, please pay attention to the following cases:
    
    3.1- If a course does not exist in courses.txt, display the message: "Course {course_name} not found."
    
    3.2- If a letter grade does not exist in grade_weights.txt, display the message: "Grade {letter_grade} not found."
    
    3.3- Display these messages in the same order as they appear while reading student_grades.txt.

4- Compute GPA per student according to courses.txt.

5- Sort the students by GPA (descending). For ties, sort the student names alphabetically.

6- Write the sorted GPA table to gpa_ranking.txt file:
```
Emma 4.0
George 4.0
Alice 3.83
Grace 3.67
Carol 3.43
Bob 3.15
Frank 3.15
David 2.7

```


7- Display (print out) the messages as the following:
```
Grade B! not found.
Course PHYS105 not found.
```

8- Collect the messages in a list in the correct order and return the list. Displaying the messages is not required; it is essential to return the **list**.


The output should be in this structure for gpa_ranking.txt file:

    Name GPA
  
So there should be one whitespace between the student name and the GPA.

**Hint**: You can use the .sort() function of lists to sort the student names with the same GPA.

**Important**: Grading will be based on comparing the gpa_ranking.txt file with the solution.txt file. The two files must match exactly. Please pay careful attention to newlines, whitespace, letter casing, and formatting.


## Question 3: Advanced Anagram Grouping (30 Points)

### **Objective**
Given a list of words, group together all the words that are anagrams of each other.

**What is an anagram?**  
Two words are anagrams if they contain **the exact same letters**, just **in a different order**.  
- Example: `"listen"` and `"silent"` are anagrams.
- Example: `"bat"` and `"tab"` are anagrams.
- Example: `"cat"` and `"act"` are anagrams.

Words must match **letter-for-letter**, ignoring the order of the letters.

You must:
- **Ignore case sensitivity** — treat uppercase and lowercase letters as the same.
- **Ignore non-letter characters** — ignore digits, punctuation, spaces, and other symbols.
- Group words that are anagrams of each other together.
- Return:
  - A **dictionary** where the key is the sorted tuple of letters (after cleaning and lowering) and the value is a list of the **original words**.
  - A **list of groups** containing the grouped words, sorted by **group size descending** and **alphabetically inside each group**.
- Only include groups that have **at least two words**.

### **Inputs**
- A list of strings `words`, where each string may contain letters, numbers, or special characters.
- Words can contain letters (a–z, A–Z), numbers (0–9), and special characters (e.g., `!`, `@`, `.`).

### **Output**
- A tuple of two elements:
  1. A dictionary where:
     - The keys are tuples representing the sorted letters of the normalized word.
     - The values are lists containing the **original words** grouped together.
     - Only include groups with **at least two words**.
  2. A list of lists, where:
     - Each inner list contains original words from one group.
     - Groups are sorted by **size descending**.
     - Words inside each group are sorted **alphabetically**.

### **Examples**

#### **Example 1:**
```python
group_advanced_anagrams(["bat", "Tab", "tap!", "Pat", "cat", "dog", "g.od"])
```
**Expected Output:**
```python
(
  {
    ('a', 'b', 't'): ["bat", "Tab"],
    ('a', 'p', 't'): ["Pat", "tap!"],
    ('d', 'g', 'o'): ["dog", "g.od"]
  },
  [
    ["bat", "Tab"],
    ["dog", "g.od"],
    ["Pat", "tap!"]
  ]
)
```
_Since all groups have the same size (2 words), the order of groups in the list does not matter. Only the content inside each group and the alphabetical order inside groups must be correct._

#### **Example 2:**
```python
group_advanced_anagrams(["listen", "silent", "enlist", "banana", "abc", "cab", "bac", "xyz"])
```
**Expected Output:**
```python
(
  {
    ('e', 'i', 'l', 'n', 's', 't'): ["listen", "silent", "enlist"],
    ('a', 'b', 'c'): ["abc", "cab", "bac"]
  },
  [
    ["listen", "silent", "enlist"],
    ["abc", "bac", "cab"]
  ]
)
```
_"banana" and "xyz" are ignored because they have no anagrams._

#### **Example 3:**
```python
group_advanced_anagrams(["D.o.g", "G-o-d", "God", "dog!"])
```
**Expected Output:**
```python
(
  {
    ('d', 'g', 'o'): ["D.o.g", "G-o-d", "God", "dog!"]
  },
  [
    ["D.o.g", "G-o-d", "God", "dog!"]
  ]
)
```
_All words are treated the same after cleaning special characters._

---

#### **Example 4:**
```python
group_advanced_anagrams(["apple", "banana", "carrot", "date"])
```
**Expected Output:**
```python
(
  {},
  []
)
```
_No groups have at least two anagrams._

### **Hint**

_Hint-1: You may find the `sorted()` function helpful for sorting the letters of a word or sorting the words inside each group.  
For example, `sorted("bat")` gives `['a', 'b', 't']`, and `sorted(["bat", "Tab"])` gives `['Tab', 'bat']`._

Hint-2: In Python, uppercase letters come before lowercase letters when sorting alphabetically (e.g., `'A' < 'a'`).  
To ensure consistent sorting, you should lowercase letters before sorting if needed._
