def dice_A_combo(elements, length):
    if length == 0:
        return [[]]
    combos = []
    for element in elements:
        sub_combos = dice_A_combo(elements, length - 1)
        for sub_combo in sub_combos:
            combos.append([element] + sub_combo)
    return combos

def dice_B_combo(elements, length, start):
    if length == 0:
        return [[]]
    combos = []
    for i in range(start, len(elements)):
        sub_combos = dice_B_combo(elements, length - 1, i + 1)
        for sub_combo in sub_combos:
            combos.append([elements[i]] + sub_combo)
    return combos

def prob_sum(arr1, arr2):
    psum = [0.0] * 12
    for i in arr1:
        for j in arr2:
            k = i + j
            psum[k - 1] += 1
    for i in range(len(psum)):
        if psum[i] != 0:
            psum[i] /= 36
    return psum

def transform(die_A, die_B):
    elements1 = [1, 2, 3, 4]
    length = 6
    combos1 = dice_A_combo(elements1, length)

    elements2 = [1, 2, 3, 4, 5, 6, 7, 8]
    start = 0
    combos2 = dice_B_combo(elements2, length, start)

    psum = [0.0, 1.0 / 36, 2.0 / 36, 3.0 / 36, 4.0 / 36, 5.0 / 36, 6.0 / 36, 5.0 / 36, 4.0 / 36, 3.0 / 36, 2.0 / 36, 1.0 / 36]

    for i in combos1:
        for j in combos2:
            if prob_sum(i, j) == psum:
                print("new die_a:", i)
                print("new die_b:", j)
                return

if _name_ == "_main_":
    die_A = [1, 2, 3, 4, 5, 6]
    die_B = [1, 2, 3, 4, 5, 6]
    transform(die_A, die_B)
