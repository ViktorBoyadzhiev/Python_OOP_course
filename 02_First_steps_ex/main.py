class Person:
    def __inti__(self, name, height):
        self.name = name
        self.height = height

    def grow(self):
        self.height += 1


ivan = Person("Ivan", 183)
print(ivan.name)