```python

users = ['raju', 'shagir', 'shariful', 'khan', 'sholaiman']

print(users[2:3 ])

```

## find big number

```python

numbers = [10, 11, 12, 13, 4, 120]

max = 0
for number in numbers:
    if number > max:
        max = number


print(max)


```

```python

numbers = [3, 4, 5, 6, 7, 8, 9]

# numbers.append(10)

# numbers.insert(1, [1, 2, 3])
# numbers.remove(3)

# numbers.pop()
numbers.sort()
numbers.reverse()
# numbers2 = numbers.copy()
numbers2 = numbers[:]
numbers2.append(10)

print(numbers)

```

```python

numbers = [3, 4, 5, 3,9,2, 6, 7, 8, 9]
numbers.sort()
for number in numbers:
    if numbers.count(number) > 1:
        numbers.remove(number)

print(numbers)

```
