import json
import os

FILE_NAME = "students.jso"

# Load data from JSON file
def load_data():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return {}

# Save data to JSON file
def save_data(data):
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)

# Add student
def add_student():
    data = load_data()
    roll = input("Enter Roll Number: ")
    
    if roll in data:
        print("Student already exists!")
        return
    
    name = input("Enter Name: ")
    marks = input("Enter Marks: ")

    data[roll] = {
        "name": name,
        "marks": marks
    }

    save_data(data)
    print("Student added successfully!")

# View all students
def view_students():
    data = load_data()
    
    if not data:
        print("No students found.")
        return

    for roll, details in data.items():
        print(f"Roll No: {roll}, Name: {details['name']}, Marks: {details['marks']}")

# Search student
def search_student():
    data = load_data()
    roll = input("Enter Roll Number to search: ")

    if roll in data:
        print(data[roll])
    else:
        print("Student not found.")

# Update student
def update_student():
    data = load_data()
    roll = input("Enter Roll Number to update: ")

    if roll in data:
        name = input("Enter new name: ")
        marks = input("Enter new marks: ")

        data[roll] = {
            "name": name,
            "marks": marks
        }

        save_data(data)
        print("Student updated successfully!")
    else:
        print("Student not found.")

# Delete student
def delete_student():
    data = load_data()
    roll = input("Enter Roll Number to delete: ")

    if roll in data:
        del data[roll]
        save_data(data)
        print("Student deleted successfully!")
    else:
        print("Student not found.")

# Main menu
while True:
    print("\n--- Student Management System ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        update_student()
    elif choice == "5":
        delete_student()
    elif choice == "6":
        print("Exiting...")
        break
    else:
        print("Invalid choice!")