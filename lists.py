numbers = [3, 4, 5, 3,9,2, 6, 7, 8, 9]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)