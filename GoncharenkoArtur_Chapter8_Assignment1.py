import csv

def write_grades_to_csv():
   
    
    file_name = "grades.csv"
    students_data = []

    # Gets the number of students from user
    num_students = int(input("Enter the number of students: "))

    # Collects the student data
    for _ in range(num_students):
        first_name = input("Enter student's first name: ")
        last_name = input("Enter student's last name: ")
        exam1 = int(input("Enter Exam 1 grade: "))
        exam2 = int(input("Enter Exam 2 grade: "))
        exam3 = int(input("Enter Exam 3 grade: "))

        # Stores the student record in a dictionary
        students_data.append({
            "First Name": first_name,
            "Last Name": last_name,
            "Exam 1": exam1,
            "Exam 2": exam2,
            "Exam 3": exam3
        })

    # Writes the data to CSV file
    with open(file_name, mode="w", newline="") as file:
        fieldnames = ["First Name", "Last Name", "Exam 1", "Exam 2", "Exam 3"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        # Writes the header and data rows
        writer.writeheader()
        writer.writerows(students_data)

    print(f"Data successfully written to {file_name}")

# Call function that writes data
write_grades_to_csv()


import csv

def read_grades_from_csv():
    
    file_name = "grades.csv"

    # Opens and reads the CSV file
    with open(file_name, mode="r", newline="") as file:
        reader = csv.DictReader(file)

        # Prints the header row
        print(f"\n{'First Name':<15} {'Last Name':<15} {'Exam 1':<10} {'Exam 2':<10} {'Exam 3':<10}")
        print("-" * 60)

        # Prints each student's data in table format
        for row in reader:
            print(f"{row['First Name']:<15} {row['Last Name']:<15} {row['Exam 1']:<10} {row['Exam 2']:<10} {row['Exam 3']:<10}")

# Call function to read data
read_grades_from_csv()
