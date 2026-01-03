import csv


file_path = "students.csv"


def read_csv_file(file_path):
    try:
        with open(file_path, "r", newline="", encoding="utf-8") as read_file:
            data = csv.reader(read_file)
            for row in data:
                print(row)

    except FileNotFoundError:
        print("File was not found.")
    except PermissionError:
        print("You don't have permission to access this file.")


def read_csv_grades_equal_above_7(file_path):
    try:
        with open(file_path, "r", newline="", encoding="utf-8") as read_file:
            data = csv.reader(read_file)
            # skip header
            next(data)
            print("\nStudents with grades equal or above 7:\n")
            for row in data:
                try:
                    grade = float(row[1])
                    if grade >= 7:
                        print(f"Student: {row[0]} | grade: {row[1]}")
                except (ValueError, IndexError):
                    continue

    except FileNotFoundError:
        print("File was not found.")
    except PermissionError:
        print("You don't have permission to access this file.")


read_csv_file(file_path)

read_csv_grades_equal_above_7(file_path)
