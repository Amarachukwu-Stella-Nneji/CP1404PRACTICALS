"""
project_management.py
Estimate - 5 hours
Actual - 9 hours
"""
import csv
import datetime
from prac_07.project import Project

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
            add_new_project(projects)
        elif choice == "U":
            update_project(projects)
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
            projects.append(Project(row[0], row[1], int(row[2]), float(row[3]), int(row[4])))
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


def add_new_project(projects):
    print("Let's add a new project")
    name = input("Enter project name: ")
    start_date = input("Enter start date (dd/mm/yyyy): ")
    priority = int(input("Enter project priority: "))
    estimate = float(input("Enter cost estimate: "))
    completion = int(input("Enter completion percentage: "))

    new_project = Project(name, start_date, priority, estimate, completion)
    projects.append(new_project)


def update_project(projects):
    display_projects(projects)
    project_choice = int(input("Project choice: "))
    if 0 <= project_choice < len(projects):
        project = projects[project_choice]
        print(
            f"{project.name}, start: {project.start_date}, priority {project.priority}, estimate: ${project.estimate:.2f}, completion: {project.completion}%")
        new_completion = input("New Percentage: ")
        new_priority = input("New Priority: ")

        if new_completion:
            project.completion = int(new_completion)
        if new_priority:
            project.priority = int(new_priority)


def filter_projects_by_date(projects):
    print("Projects filtered by date:")
    date_string = input("Enter the date (dd/mm/yyyy) to filter by: ")
    try:
        user_date = datetime.datetime.strptime(date_string, '%d/%m/%Y').date()
        filtered_projects = [project for project in projects if datetime.datetime.strptime(project.start_date, '%d/%m'
                                                                                                               '/%Y').date() >= user_date]
        display_projects(filtered_projects)
    except ValueError:
        print("Invalid date format. Please use dd/mm/yyyy.")


main()
