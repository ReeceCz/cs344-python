# Script 1: Sum and Count of Positive Numbers
# Iterates over a list of integers, counting how many are positive
# and accumulating the sum of just the positive ones.

numbers = [12, -4, 7, 0, -9, 23, 5, -1, 8, -15]

positive_count = 0   # counter: how many positive numbers we've seen so far
positive_sum = 0     # accumulator: running total of the positive numbers

for num in numbers:
    if num > 0:
        # accumulate sum of positive numbers
        positive_count += 1
        positive_sum += num

print("List:", numbers)
print("Count of positive numbers:", positive_count)
print("Sum of positive numbers:", positive_sum)
