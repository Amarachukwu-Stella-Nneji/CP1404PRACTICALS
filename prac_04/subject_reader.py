"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = get_data()
    print(data)
    display_subject_details(data)


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    data = []
    for line in input_file:
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        data.append(parts)  # Append the parts to the data list
    input_file.close()
    return data


def display_subject_details(data):
    for item in data:
        subject = item[0]
        lecturer = item[1]
        students = item[2]
        print(f"{subject} is taught by {lecturer} and has {students} students")


main()
