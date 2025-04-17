import numpy as np
import csv

# Loads the CSV data without the header and name columns
def load_exam_data(filename):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)
        data = []
        for row in reader:
            scores = list(map(int, row[2:]))
            data.append(scores)
    return np.array(data)

# Computes the statistics for each exam
def compute_exam_statistics(data):
    stats = {
        'Mean': np.mean(data, axis=0),
        'Median': np.median(data, axis=0),
        'Standard Deviation': np.std(data, axis=0),
        'Minimum': np.min(data, axis=0),
        'Maximum': np.max(data, axis=0)
    }
    return stats

# Computes all the statistics for all exams combined
def compute_overall_statistics(data):
    flat_data = data.flatten()
    stats = {
        'Mean': np.mean(flat_data),
        'Median': np.median(flat_data),
        'Standard Deviation': np.std(flat_data),
        'Minimum': np.min(flat_data),
        'Maximum': np.max(flat_data)
    }
    return stats

# Determines the pass/fail statistics
def compute_pass_fail_stats(data, passing_grade=60):
    pass_counts = np.sum(data >= passing_grade, axis=0)
    fail_counts = np.sum(data < passing_grade, axis=0)
    total_passes = np.sum(data >= passing_grade)
    total_grades = data.size
    overall_pass_percentage = (total_passes / total_grades) * 100
    return pass_counts, fail_counts, overall_pass_percentage

# Main program
def main():
    filename = 'grades.csv'
    exam_data = load_exam_data(filename)

    exam_stats = compute_exam_statistics(exam_data)
    overall_stats = compute_overall_statistics(exam_data)
    pass_counts, fail_counts, overall_pass_percentage = compute_pass_fail_stats(exam_data)

    print("=== Per-Exam Statistics ===")
    for i in range(exam_data.shape[1]):
        print(f"\nExam {i + 1}:")
        print(f"Mean: {exam_stats['Mean'][i]}")
        print(f"Median: {exam_stats['Median'][i]}")
        print(f"Standard Deviation: {exam_stats['Standard Deviation'][i]}")
        print(f"Minimum: {exam_stats['Minimum'][i]}")
        print(f"Maximum: {exam_stats['Maximum'][i]}")

    print("\n=== Overall Statistics (All Exams Combined) ===")
    for stat, value in overall_stats.items():
        print(f"{stat}: {value}")

    print("\n=== Pass/Fail Statistics ===")
    for i in range(len(pass_counts)):
        print(f"Exam {i + 1}: Pass: {pass_counts[i]}, Fail: {fail_counts[i]}")
    print(f"\nOverall Pass Percentage: {overall_pass_percentage:.2f}%")

if __name__ == '__main__':
    main()
