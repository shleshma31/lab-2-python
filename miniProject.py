#STUDENT RECORD MANAGEMENT SYSTEM

students = {}

while True:
    print("1. Add Student Record")
    print("2. View All Reports")
    print("3. Display Topper(s)")
    print("4. Search by Roll Number")
    print("5. Display Failed Students")
    print("6. Update Marks")
    print("7. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        roll = input("Enter roll number: ")
        name = input("Enter name: ")
        marks = []
        for i in range(3):
            m = float(input(f"Enter marks for subject {i+1}: "))
            marks.append(m)
        students[roll] = [name, marks]
        print("Student added\n")

    elif choice == "2":
        for roll, data in students.items():
            name, marks = data
            avg = sum(marks) / 3
            print(f"Roll: {roll}, Name: {name}, Marks: {marks}, Average: {avg:.2f}")
        print()

    elif choice == "3":
        max_avg = -1
        toppers = []
        for roll, data in students.items():
            avg = sum(data[1]) / 3
            if avg > max_avg:
                max_avg = avg
                toppers = [(roll, data[0])]
            elif avg == max_avg:
                toppers.append((roll, data[0]))
        print("Topper(s):")
        for r, n in toppers:
            print(f"Roll: {r}, Name: {n}, Average: {max_avg:.2f}")
        print()

    elif choice == "4":
        roll = input("Enter roll number: ")
        if roll in students:
            name, marks = students[roll]
            print(f"Roll: {roll}, Name: {name}, Marks: {marks}")
        else:
            print("Student not found")
        print()

    elif choice == "5":
        print("Failed Students:")
        for roll, data in students.items():
            name, marks = data
            failed = False
            for m in marks:
                if m < 40:
                    failed = True
                    break
            if failed:
                print(f"Roll: {roll}, Name: {name}, Marks: {marks}")
        print()

    elif choice == "6":
        roll = input("Enter roll number to update: ")
        if roll in students:
            marks = []
            for i in range(3):
                m = float(input(f"Enter new marks for subject {i+1}: "))
                marks.append(m)
            students[roll][1] = marks
            print("Marks updated")
        else:
            print("Student not found")
        print()

    elif choice == "7":
        break

    else:
        print("Invalid choice\n")