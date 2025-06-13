def calculate_gpa(grades, credits):
    total_grades = 0
    total_credits = 0
    for grade, credit in zip(grades, credits):
        total_grades += grade * credit
        total_credits += credit
    return total_grades / total_credits if total_credits > 0 else 0

def main():
    # Input student info
    student_name = input("Enter your name: ")
    student_id = input("Enter your ID: ")

    grades = []
    credits = []
    subjects = []

    while True:
        subject = input("Enter subject name (enter 'x' to exit): ")
        if subject.lower() == 'x':
            break
        try:
            grade = float(input(f"Grade of {subject}: "))
            credit = float(input(f"Credit of {subject}: "))
            grades.append(grade)
            credits.append(credit)
            subjects.append(subject)
        except ValueError:
            print("Please enter valid grade and credit again (float)!")

    if len(grades) == 0:
        print("No data to calculate GPA.")
    else:
        gpa = calculate_gpa(grades, credits)
        print(f"\nStudent Name: {student_name}")
        print(f"Student ID: {student_id}")
        print("Subjects and Grades:")
        for s, g, c in zip(subjects, grades, credits):
            print(f" - {s}: Grade = {g}, Credit = {c}")
        print(f"\nCalculated GPA: {gpa:.2f}")


if __name__ == "__main__":
    main()