def get_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

def main():
    while True:
        try:
            score = int(input("Enter student score (0-100) "))
        except ValueError:
            print("Error: Please enter a valid number.")
            continue

        if score == -1:
            print("Goodbye!")
            break

        if score < 0 or score > 100:
            print("Error: Score must be between 0 and 100.")
        else:
            grade = get_grade(score)
            print(f"Grade: {grade}")
        
        print()

if __name__ == "__main__":
    main()