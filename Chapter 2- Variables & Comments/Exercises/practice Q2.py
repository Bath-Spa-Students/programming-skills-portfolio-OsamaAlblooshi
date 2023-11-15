#Write a python program that takes courses 
#marks as input and then calculates average of all the courses. 
#After calculating the average, calculate the percentage of a 
#student using total marks. Assume the total of all the courses marks is 500 
#or take the total marks from the user as input.
# Function to calculate average and percentage
def calculate_percentage(total_marks, num_courses):
    # Taking course marks as input
    marks = [float(input(f"Enter marks for course {i + 1}: ")) for i in range(num_courses)]

    # Calculating average
    average = sum(marks) / num_courses

    # Calculating percentage
    percentage = (sum(marks) / total_marks) * 100

    return average, percentage

# Taking total marks as input
total_marks = float(input("Enter the total marks for all courses: "))

# Assuming there are 5 courses for simplicity
num_courses = 5

# Calculate average and percentage
average_marks, student_percentage = calculate_percentage(total_marks, num_courses)

# Displaying the results
print(f"\nAverage marks: {average_marks:.2f}")
print(f"Student's percentage: {student_percentage:.2f}%")
