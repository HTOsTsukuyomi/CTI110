# Eric Risher
# 07/11/2024
# P4 HomeWork 1
# Loop to display score(s) average


# Ask for number of scores user want to enter

score_num = int(input("How many scores do you want to enter? "))

print()
# Create empty list

scores = []

# Enter scores into the list.
for num in range(1, score_num + 1):
    # Collect Scores.
    score = float(input('Enter score #' + str(num) + ": "))
    # Validate entry
    while score < 0 or score > 100:
        print("\nINVALID Score entered!")
        print("Score must be between 0 and 100!")
        score = float(input('Enter score #' + str(num) + ": "))
    scores.append(score)

# Find lowest score.

lowest = min(scores)

scores_modified = scores
# Drop lowest score from new list.
scores_modified.remove(lowest)


# calculate average

avg = sum(scores_modified) / len(scores_modified)


# determine letter grade for average
print()
if avg >= 90:

    grade = "A"
elif avg >= 80:

    grade = "B"

elif avg >= 70:

    grade = "C"
elif avg >= 60:

    grade = "D"
else:

    grade = "F"

# display results

print("\n--------------Results-----------")
print("Lowest Score  : {}".format(lowest))
print("Modified List : {}".format(scores_modified))
print("Scores Average: {:.2f}".format(avg))
print("Grade         : {}".format(grade))
print("----------------------------------")

# Exit
print()
input('Press Enter to Exit')