"""Simple course grading tool.

This program asks the user for a whole-number score from 0 to 100
and displays the corresponding letter grade.
"""


def determine_letter_grade(score: int) -> str:
    """Return the letter grade associated with a numeric score."""
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


def main() -> None:
    """Run the grading tool."""
    try:
        score = int(input("Enter a numeric score (0-100): "))
    except ValueError:
        print("Invalid input. Please enter a whole number.")
        return

    if score < 0 or score > 100:
        print("Invalid score. Please enter a score between 0 and 100.")
        return

    letter_grade = determine_letter_grade(score)
    print(f"Score: {score} -> Letter grade: {letter_grade}")


if __name__ == "__main__":
    main()
