while True:
    last_name = input("Please enter your last name (or ZZZ to quit): ")

    if last_name == "ZZZ":
        print("Quitting program")
        break

    first_name = input("Please enter your first name: ")

    gpa = float(input("Enter GPA: "))

    if gpa >= 3.5:
        print(f"{first_name} {last_name} has made the Dean's list.")
    elif gpa >= 3.25:
        print(f"{first_name} {last_name} has made the Honor Roll.")
    else:
        print(f"{first_name} {last_name} did not qualify")
    
    print()
