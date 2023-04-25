# Liskov Substitution Principle (LSP) - принцип Барбары Лиско.
# Если есть родительский класс с дочерними классами и есть функция, которая умеет работать с родительским классом,
# в таком случае мы можем в функцию кинуть объект дочернего класса и это будет работать,
# т.к. дочерний класс должен уметь полностью заменять родительский.

class Bird:
    def fly(self):
        print("Flying")


class Duck(Bird):
    def fly(self):
        print("Flying like a duck")


def bird_fly(bird: Bird):
    bird.fly()


if __name__ == '__main__':
    bird = Bird()
    duck = Duck()

    bird_fly(bird)  # prints "Flying"
    bird_fly(duck)  # prints "Flying like a duck"
