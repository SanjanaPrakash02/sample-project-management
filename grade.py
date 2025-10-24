# main.py
def calculate_grade():
    try:
        assignment = float(input("Enter assignment score (0-100): "))
        exam = float(input("Enter exam score (0-100): "))
        total = (assignment * 0.4) + (exam * 0.6)
        
        if total >= 90:
            grade = "A"
        elif total >= 80:
            grade = "B"
        elif total >= 70:
            grade = "C"
        elif total >= 60:
            grade = "D"
        else:
            grade = "F"
        
        print(f"\nFinal Score: {total:.2f}")
        print(f"Grade: {grade}")
    except ValueError:
        print("Invalid input! Please enter numbers only.")

if _name_ == "_main_":
    calculate_grade()
