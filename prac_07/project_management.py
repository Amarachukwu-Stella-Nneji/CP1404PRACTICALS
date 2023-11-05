"""
project_management.py
Estimate - 5 hours
Actual - hours
"""
import csv

from prac_07.project import ProjectManagement

MENU = ("- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n- (F)ilter projects by start_date"
        "\n- (A)dd new project\n- (U)pdate project\n- (Q)uit\n>>> ")


def main():
    choice = input(MENU).upper()
    projects = []
    file_name = "projects.txt "
    while choice != "Q":
        if choice == "L":
            projects = load_project(file_name)
        elif choice == "S":
            filename = input("Enter the filename to save projects to: ")
            save_projects(projects, filename)
        elif choice == "D":
            display_projects(projects)
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


def display_projects(projects):
    incomplete_projects = [project for project in projects if project.completion < 100]
    completed_projects = [project for project in projects if project.completion == 100]

    print("Incomplete projects:")
    incomplete_projects.sort(key=lambda project: project.priority)
    for project in incomplete_projects:
        print(project)

    print("\nCompleted projects:")
    completed_projects.sort(key=lambda project: project.priority)
    for project in completed_projects:
        print(project)


def save_projects(projects, filename):
    with open(filename, 'w', newline='') as out_file:
        writer = csv.writer(out_file, delimiter=',')
        for project in projects:
            writer.writerow([project.name, project.start_date, project.priority, project.estimate, project.completion])


main()
