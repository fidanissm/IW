def save_to_file():
    with open("students.json", "w") as f:
        json.dump(students, f)
    print("Data saved to students.json")
