from planner import generate_schedule

def main():
    print("=== AI Study Planner ===")

    subjects = []
    n = int(input("Enter number of subjects: "))

    for i in range(n):
        name = input(f"Enter subject {i+1} name: ")
        priority = int(input(f"Enter priority for {name} (1-5): "))
        subjects.append((name, priority))

    total_hours = int(input("Enter total available study hours per day: "))

    schedule = generate_schedule(subjects, total_hours)

    print("\n--- Generated Study Plan ---")
    for subject, hours in schedule.items():
        print(f"{subject}: {hours} hours")

    with open("sample_output.txt", "w") as f:
        for subject, hours in schedule.items():
            f.write(f"{subject}: {hours} hours\n")

    print("\nPlan saved to sample_output.txt")

if __name__ == "__main__":
    main()