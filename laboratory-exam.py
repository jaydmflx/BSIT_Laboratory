students = []
grades = []

while True:
    try:
        num_students = int(input("Enter the number of students: "))

        if num_students <= 0:
            print("Please enter a valid number of students")
            continue

        break

    except ValueError:
        print("Please enter a valid number of students")


for i in range(1, num_students + 1):
    print(f"\nStudent {i}:")

    while True:
        name = input("Enter student name: ").strip()

        if name == "":
            print("Error: Student name cannot be empty")
            continue

        elif name.lower() in [s[0].lower() for s in students]:
            print("Error: Student name already exists. Enter a different name")
            continue

        break

    grades = []

    for activity in range(1, 6):
        while True:
            try:
                grade = float(input(f"Enter Activity {activity} grade: "))

                if grade < 0 or grade > 100:
                    print("Please enter a valid grade between 0 and 100")
                    continue

                grades.append(grade)
                break

            except ValueError:
                print("Please enter a valid grade between 0 and 100")

    final_grade = sum(grades) / 5

    if final_grade >= 90:
        descriptor = "Outstanding"
        remarks = "Passed"
    elif final_grade >= 85:
        descriptor = "Very Satisfactory"
        remarks = "Passed"
    elif final_grade >= 80:
        descriptor = "Satisfactory"
        remarks = "Passed"
    elif final_grade >= 75:
        descriptor = "Fairly Satisfactory"
        remarks = "Passed"
    else:
        descriptor = "Did Not Meet Expectations"
        remarks = "Failed"

    students.append((name, final_grade, descriptor, remarks))


print("\n========= INDIVIDUAL REPORT =========")

for name, final_grade, descriptor, remarks in students:
    print(f"\nStudent Name: {name}")
    print(f"Final Grade: {final_grade:.2f}")
    print(f"Descriptor: {descriptor}")
    print(f"Remarks: {remarks}")