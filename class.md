## sample class

```python
class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        print("Moving")

    def draw(self):
        print("Drawing")


point =  Point(10, 20)

point.x = 10

print(point.x, point.y)

```

```python

class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"{self.name} is talking")


person = Person("Raju")

```
