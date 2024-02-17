Die_A = [1, 2, 3, 4, 5, 6]
Die_B = [1, 2, 3, 4, 5, 6]

total_combinations = len(Die_A) * len(Die_B)
print("Total combinations:", total_combinations)

combinations = [[(Die_A[i], Die_B[j]) for j in range(6)] for i in range(6)]
sum_count = [0] * 13

for i in range(6):
    for j in range(6):
        combination = combinations[i][j]
        sum_val = combination[0] + combination[1]
        sum_count[sum_val] += 1

# Display the 6x6 matrix of combinations
print("\nMatrix of combinations:")
for i in range(6):
    for j in range(6):
        combination = combinations[i][j]
        print(combination, end=" ")
    print()

# Display probabilities for each sum
print("\nProbability of each sum:")
for i in range(2, 13):
    probability = sum_count[i] / total_combinations
    print(f"P(Sum = {i}) = {sum_count[i]}/36 = {probability}")

print("Function ran successfully")
