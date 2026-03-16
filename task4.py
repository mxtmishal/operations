students = []

while True:
    print("1. Add student name")
    print("2. Display students")
    print("3. Edit student name")
    print("4. Delete student name")
    print("5. Exit")

    choice = input("Enter your choice: ")

    match choice:
        case "1":
            name = input("Enter student's name: ")
            students.append(name)

        case "2":
            if len(students) == 0:
                print("No students added!!")
                continue

            for student in students:
                print(student)

        case "3":
            old_name = input("Enter the student name to edit: ")
            if old_name in students:
                new_name = input("Enter new name: ")
                index = students.index(old_name)
                students[index] = new_name
            else:
                print("Student not found")

        case "4":
            name = input("Enter the student name to delete: ")
            if name in students:
                students.remove(name)
            else:
                print("Student not found")

        case "5":
            print("Exiting program...")
            break

        case _:
            print("Invalid choice")