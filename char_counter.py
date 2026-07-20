# Script 3: Character Counter
# Traverses a line of text one character at a time, counting how many times
# a chosen character appears.

text = input("Enter a line of text: ")

target_char = input("Enter a single character to search for: ")
while len(target_char) != 1:
    # keep asking until we actually get exactly one character
    target_char = input("Please enter exactly one character: ")

char_count = 0   # counter: occurrences of target_char found so far

# traverse the text one character at a time
for ch in text:
    if ch == target_char:
        char_count += 1

print(f"\nThe character '{target_char}' appears {char_count} time(s) in the text.")
