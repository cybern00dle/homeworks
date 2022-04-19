# Описание класса: у кошки есть кличка, возраст, порода и окрас.
# Кошка может поиграть с мячиком цвета её окраса и мяукнуть столько раз, сколько букв и цифр в её кличке.
# Класс: Cat
# Атрибуты объектов данного класса:
# - name
# - age
# - breed
# - colour
# Методы объектов данного класса:
# - play_ball()
# - meow_meow()

class Cat:
    def __init__(self, name, age, breed, colour):
        self.name = name
        self.age = age
        self.breed = breed
        self.colour = colour

    def play_ball(self):
        print(f"The cat starts playing with a {self.colour} ball.")

    def meow_meow(self):
        meowmeow_name = self.name.strip()
        meowmeow_number = len(meowmeow_name)
        for i in meowmeow_name:
            if not i.isalnum():
                meowmeow_number -= 1
            else:
                continue
        meowmeow = " meow"*meowmeow_number
        print(f"The cat says:{meowmeow}.")


kittycat = Cat(name="Emir", age=5, breed="abyssinian", colour="brown")
print("Name:", kittycat.name)
print("Age:", kittycat.age)
print("Breed:", kittycat.breed)
print("Colour:", kittycat.colour)
kittycat.play_ball()
kittycat.meow_meow()
print()
lil_meow = Cat(name="Little Meow Meow 666", age=10, breed="oriental", colour="black")
print("Name:", lil_meow.name)
print("Age:", lil_meow.age)
print("Breed:", lil_meow.breed)
print("Colour:", lil_meow.colour)
lil_meow.play_ball()
lil_meow.meow_meow()
