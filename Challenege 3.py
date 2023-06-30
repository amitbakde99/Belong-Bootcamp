#1.You are given two arrays, nums1 and nums2, both containing integers. Your task is to find the intersection of the two arrays and return it as a sorted list. Write a function find_intersection(nums1, nums2) that takes two lists of integers as input and returns a list of the sorted intersection of the two arrays. Note: The result has to be a sorted list without duplicates
#2.You are given a list of tuples representing the scores of students in a class. Each tuple consists of the student's name (a string) followed by their score (an integer). Your task is to find the student(s) with the highest score(s) and return their names as a list. Write a function find_top_students(scores) that takes a list of tuples as input and returns a list of names of the top-scoring student(s).
#3.You are given a tuple of integers representing the coordinates of points on a 2D plane. Each tuple consists of the x-coordinate followed by the y-coordinate. Your task is to find the distance between the two closest points among all the given points. Write a function find_closest_distance(points) that takes a tuple of points as input and returns the distance between the two closest points as a floating-point number. Note: - The tuple of points will contain at least two tuples. - The coordinates of the points are integers. - The distance between two points (x1, y1) and (x2, y2) can be calculated using the formula: sqrt((x2 - x1)^2 + (y2 - y1)^2). - You can use the math module to calculate the square root using the sqrt() function.
#4.You are given a set of tuples representing the attendance records of students in a class. Each tuple consists of the student's name (a string) followed by their attendance status (a boolean, where True represents present and False represents absent). Your task is to find the names of students who have perfect attendance, i.e., those who have never been absent. Write a function find_perfect_attendance(attendance_records) that takes a set of tuples as input and returns a list containing the names of students with perfect attendance sorted alphabetically. Note: - The set of attendance records will contain at least one tuple. - The names of the students are case-sensitive and may appear in any order in the input set. - Each student's attendance status is either True (present) or False (absent). - If multiple students have perfect attendance, include all of their names in the result set.
#5.You are given two sets of tuples representing the courses taken by students. Each tuple consists of the student's name (a string) followed by the course code (a string). Your task is to find the set of students who have taken all the courses present in the second set. Write a function find_students_with_all_courses(student_courses, required_courses) that takes two sets of tuples as input and returns a set containing the names of students who have taken all the required courses. Note: - The sets of student courses and required courses will contain at least one tuple. - The names of the students and course codes are case-sensitive and may appear in any order in the input sets. - Each tuple in the required courses set represents a unique course code. - If multiple students have taken all the required courses, include all of their names in the result set.
student_courses = {("Alice", "CS101"), ("Bob", "CS101"), ("Charlie", "MATH101"), ("Alice", "MATH101")}
required_courses = {("CS101"), ("MATH101")}

def find_students_with_all_courses(student_courses, required_courses):
    d={}
    l=len(required_courses)
    for i in student_courses:
        try:
            d[i[0]]+=1
        except:
            d[i[0]]=1
    s=[]
    for i in d:
        if d[i]==l:
            s.append(i)
    return sorted(set(s))        
#Run the function
answer=find_students_with_all_courses(student_courses, required_courses)
print(answer)

#6.You are given a sequence of integers representing the scores of students in a class. Your task is to calculate the mean (average) score and the standard deviation of the scores. Write a function calculate_statistics(scores) that takes a sequence of integers as input and returns a tuple containing the mean score and the standard deviation as floating-point numbers. Note: - The sequence of scores will contain at least one integer. - You should calculate the mean score and the standard deviation using formulas, without using any built-in statistics functions or libraries. - You can use basic arithmetic operations, loops, and conditionals to calculate the statistics.

scores = (85, 90, 92, 88, 95)

def calculate_statistics(scores):
    n = len(scores)
    mean = sum(scores) / n
    squared_diff_sum = sum((x - mean) ** 2 for x in scores)
    variance = squared_diff_sum / n
    std_deviation = int(variance ** 0.5)
    return mean, std_deviation
answer= calculate_statistics(scores)
print(answer)

#7.You are given a sequence of integers representing the ages of participants in a marathon race. Your task is to calculate the median age of the participants. Write a function calculate_median_age(ages) that takes a sequence of integers as input and returns the median age as a floating-point number. Note: The median is the middle value in a sorted list of numbers. If the list has an odd number of elements, the median is the middle number. If the list has an even number of elements, the median is the average of the two middle numbers. - The sequence of ages will contain at least one integer. - You should calculate the median age using a sorting algorithm or any other suitable approach. - You are not allowed to use any built-in statistics functions or libraries. - You can use basic arithmetic operations, loops, and conditionals to calculate the median.
ages = (25, 30, 28, 32, 24, 26, 29)

def calculate_median_age(ages):
    sorted_ages = sorted(ages)
    n = len(sorted_ages)

    if n % 2 == 1:  # Odd number of ages
        median_index = n // 2
        median_age = sorted_ages[median_index]
    else:  # Even number of ages
        upper_median_index = n // 2
        lower_median_index = upper_median_index - 1
        median_age = (sorted_ages[lower_median_index] + sorted_ages[upper_median_index]) / 2

    return float(median_age)
answer= calculate_median_age(ages)
print(answer)

#8.You are given a sequence of integers representing the heights of a group of people. Your task is to determine the mode (most frequently occurring height) among the group. Write a function calculate_mode(heights) that takes a sequence of integers as input and returns the mode height as an integer. Note: The mode is the value that appears most frequently in a dataset. - The sequence of heights will contain at least one integer. - You should calculate the mode height using suitable logic or algorithms. - You are not allowed to use any built-in statistics functions or libraries. - You can use basic arithmetic operations, loops, and conditionals to calculate the mode.
heights = (160, 165, 170, 165, 175, 165, 170, 160, 165)

def calculate_mode(heights):
    height_counts = {}

    # Count the frequency of each height
    for height in heights:
        if height in height_counts:
            height_counts[height] += 1
        else:
            height_counts[height] = 1

    # Find the mode (height with the maximum frequency)
    mode = None
    max_count = 0
    for height, count in height_counts.items():
        if count > max_count:
            mode = height
            max_count = count

    return mode
answer= calculate_mode(heights)
print(answer)
