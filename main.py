import random

# Initialize the array with 35 random grades between 0 and 100
grades = [random.randint(0, 100) for x in range(35)]

# Define a function to display all grades
def display_all_grades():
    print("ALL GRADES")
    #iterate through all parts of the grades list and output it
    for grade in grades:
        print(f"{grade}%")

# Define a function to display honours grades
def display_honours():
    honours_grades = [grade for grade in grades if grade > 80]
    num_honours = len(honours_grades)
    print("HONOURS")
    for grade in honours_grades:
        print(f"{grade}%")
    print(f"Number of Honours: {num_honours}")

# Define a function to display stats about the grades
def display_stats():
    max_grade = max(grades)
    min_grade = min(grades)
    avg_grade = sum(grades) / len(grades)
    print("STATS")
    print(f"Highest Grade: {max_grade}%")
    print(f"Lowest Grade: {min_grade}%")
    print(f"Average Grade: {avg_grade}%")

# Define a function to randomize the grades
def randomize_grades():
    global grades
    grades = [random.randint(0, 100) for x in range(35)]
    print("GRADES HAVE BEEN RANDOMIZED")

# Display the main menu and handle user input
while True:
    print("MAIN MENU")
    print("1. Display All Grades")
    print("2. Display Honours")
    print("3. Stats")
    print("4. Randomize Grades")
    print("5. Exit")
    choice = input("Select an option (1-5): ")
    if choice == "1":
        display_all_grades()
    elif choice == "2":
        display_honours()
    elif choice == "3":
        display_stats()
    elif choice == "4":
        randomize_grades()
    elif choice == "5":
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
