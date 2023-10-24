numbers  = [5, 2, 5, 2, 2]

star = ''
for number in numbers:
    for i in range(number):
        star += "x"
    print(star)
    star = ''