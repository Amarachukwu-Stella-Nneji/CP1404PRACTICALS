"""
project_management.py
Estimate - 5 hours
Actual - hours
"""
import csv

from prac_07.project import ProjectManagement

MENU = ("- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n- (F)ilter projects by date"
        "\n- (A)dd new project\n- (U)pdate project\n- (Q)uit\n>>> ")


def main():
    choice = input(MENU).upper()
    file_name = "projects.txt "
    while choice != "Q":
        if choice == "L":
            load_project(file_name)
        elif choice == "S":
            pass
        elif choice == "D":
            pass
        elif choice == "F":
            pass
        elif choice == "A":
            pass
        elif choice == "U":
            pass
        else:
            print("Invalid choice")
        choice = input(MENU).upper()
    print("Thank you for using custom-built project management software.")


def load_project(file_name):
    projects = []
    with open(file_name, "r", encoding="UTF-8") as in_file:
        reader = csv.reader(in_file, delimiter='\t')
        in_file.readline()
        for row in reader:
            projects.append(ProjectManagement(row[0], row[1], int(row[2]), float(row[3]), int(row[4])))
    return projects


main()
