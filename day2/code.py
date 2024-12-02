def is_safe(report):
    """
    Checks if a single report (list of numbers) is safe.
    A report is safe if:
    1. All numbers are either increasing or decreasing.
    2. The difference between any two adjacent numbers is between 1 and 3.
    """
    differences = [abs(report[i + 1] - report[i]) for i in range(len(report) - 1)]
    # Check if the list is strictly increasing or strictly decreasing
    is_increasing = all(report[i] < report[i + 1] for i in range(len(report) - 1))
    is_decreasing = all(report[i] > report[i + 1] for i in range(len(report) - 1))
    # Check if all differences are between 1 and 3
    valid_differences = all(1 <= diff <= 3 for diff in differences)
    return (is_increasing or is_decreasing) and valid_differences


def count_safe_reports(filename):

    safe_count = 0
    with open(input_file, 'r') as file:
        for line in file:
            # Convert the line into a list of integers
            report = list(map(int, line.split()))
            # Check if the report is safe
            if is_safe(report):
                safe_count += 1
    return safe_count


def is_safe_with_dampener(report):
    
    # Checks if a report is safe, either directly or by removing a single level.
    
    # If the report is already safe, return True
    if is_safe(report):
        return True

    # Try removing each level and check if the resulting report is safe
    for i in range(len(report)):
        modified_report = report[:i] + report[i + 1:]
        if is_safe(modified_report):
            return True

    # If no single-level removal makes it safe, return False
    return False


def count_safe_reports_with_dampener(filename):

    safe_count = 0
    with open(filename, 'r') as file:
        for line in file:
            report = list(map(int, line.split()))

            if is_safe_with_dampener(report):
                safe_count += 1
    return safe_count


if __name__ == "__main__":
    input_file = "D:\Folders\AOC\Advent_of_code_2024\day2\input.txt"  
    safe_reports = count_safe_reports(input_file)
    print(f"Number of safe reports: {safe_reports}")
    safe_reports_with_dampener = count_safe_reports_with_dampener(input_file)
    print(f"Number of safe reports with Problem Dampener: {safe_reports_with_dampener}")