# Grade Tracker Python Project

def calculate_average(grades):
    return sum(grades) / len(grades)

def main():
    print("Welcome to Grade Tracker")
    num_students = int(input("Enter number of students: "))
    
    student_records = {}

    for i in range(num_students):
        name = input(f"Enter name of student {i+1}: ")
        grades = input(f"Enter grades for {name} separated by commas: ")
        grade_list = [float(x.strip()) for x in grades.split(",")]
        student_records[name] = grade_list

    print("\n--- Report ---")
    for student, grades in student_records.items():
        avg = calculate_average(grades)
        print(f"{student}: Grades = {grades}, Average = {avg:.2f}")

if __name__ == "__main__":
    main()
