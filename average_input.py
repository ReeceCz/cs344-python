# Script 2: Average from User-Entered Values
# Repeatedly prompts the user for numbers until they enter 'q'.
# Accumulates a running total and counts how many valid numbers were entered,
# then prints the average (or a message if nothing valid was entered).

total = 0.0   # accumulator: running total of entered numbers
count = 0     # counter: how many valid numbers were entered

while True:
    user_input = input("Enter a number (or 'q' to quit): ").strip()

    if user_input.lower() == "q":
        break

    try:
        value = float(user_input)
    except ValueError:
        print("That's not a valid number. Please try again.")
        continue

    # accumulate total and increment counter for each valid entry
    total += value
    count += 1

if count > 0:
    average = total / count
    print(f"\nYou entered {count} number(s).")
    print(f"The average is: {average}")
else:
    print("\nNo valid numbers were entered, so no average can be computed.")
