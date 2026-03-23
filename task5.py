# file_name = "students.txt"

# def add_students():
#     name = input("Enter student name: ").strip()
    
#     if not name:
#         print("Name cannot be empty!")
#         return
    
    
#     students = get_all_students()
#     if name in students:
#         print("student already exists!")
#         return
    
#     with open(file_name, "a") as file:
#         file.write(name + "\n")


#     print("Student added successfully!")
    

# def view_students():
#     try:
#         with open(file_name, "r") as file:
#             students = file.readlines()

#         if not students:
#             print("No students found.")
#             return

#         print("\n--- Student List ---")
#         for i, student in enumerate(students, start=1):
#             print(f"{i}. {student.strip()}")

#     except FileNotFoundError:
#         print("File not found. No students yet.")
        
# def get_all_students():
#     try:
#         with open(file_name, "r") as file:
#             return [line.strip() for line in file.readlines()]
#     except FileNotFoundError:
#         return []

# def menu():
#     while True:
#         print("\n===== Student Management System =====")
#         print("1. Add Student")
#         print("2. View Students")
#         print("3. Exit")

#         choice = input("Enter your choice: ")

#         if choice == "1":
#             add_students()
#         elif choice == "2":
#             view_students()
#         elif choice == "3":
#             print("Exiting program...")
#             break
#         else:
#             print("Invalid choice. Try again.")

# menu()



#        ///////////////////ANOTHER METHODE///////////////////////


try:
    file = open("students.txt", "x")
    file.close()
except:
    pass


while True:
    print("\n--- Student Menu ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter student name: ")

        file = open("students.txt", "a")
        file.write(name + "\n")
        file.close()

        print("Student added!")
        
    elif choice == "2":
        try:
            file = open("students.txt", "r")
            content = file.read()
            file.close()

            if content == "":
                print("No students found.")
            else:
                print("\nStudent List:")
                print(content)

        except:
            print("File not found!")

    elif choice == "3":
        print("Exiting program...")
        break

    else:
        print("Invalid choice!")