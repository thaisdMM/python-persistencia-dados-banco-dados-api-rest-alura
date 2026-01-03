import csv
from pathlib import Path

file_path = "students.csv"


def create_file(file_path):
    try:
        with open(file_path, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["student", "grade"])
    except PermissionError:
        print("You don't have permission to access this file.")


def check_path_exists(file_path):
    try:
        return Path(file_path).exists()
    except PermissionError:
        print("You don't have permission to access this file.")


students = []


def register_student():

    while True:
        exit = False
        name = input("Student: ").strip().title()
        grade = float(input("grade: "))
        students.append([name, grade])
        while True:
            choice = (
                input("Type Y to continue or N to exit the program: ").strip().upper()
            )
            if choice in "YN":
                break
            print("Invalid choice.")

        if choice == "N":
            exit = True
        if exit:
            break

    return students


def verify_file(file_path):
    try:
        path_exists = check_path_exists(file_path)
        # print(path_exists)
        if not path_exists:
            create_file(file_path)
    except PermissionError:
        print("You don't have permission to access this file.")


def write_file():
    try:
        verify_file(file_path)

        students_list = register_student()

        with open("students.csv", "a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerows(students_list)
            print("Students registered successfully.")

    except FileNotFoundError:
        print("File was not found.")


write_file()
