# Factory Method (Фабричный метод) - порождающий паттерн
# Определяет общий интерфейс для создания объектов в суперклассе.
# Эти интерфейсы определяют структуру, но не создают объекты. Создание лежит на конкретном подклассе.
#
# Применяется:
# 1. Когда заранее неизвестны типы и зависимости объектов, с которыми должен работать код.
# 2. Когда хотим дать возможность пользователям расширять части фреймворка или библиотеки.
# 3. Когда хотим экономить системные ресурсы, повторно используя уже созданные объекты, вместо порождения новых.
#
# Пример: реализуем фабрику для создания фигур.
# - Создаем родительский класс (Абстрактный, который называется интерфейсом) Shape с методами calculate_area и
# calculate_area для представления фигур в целом.
# - Конкретные фигуры Rectangle, Square, Circle затем наследуются от нашего базового класса.
# Тем самым мы расширили наш Абстрактный класс.
# - Для того чтобы создать различные объекты фигур, клиенты должны будут знать названия и параметры наших фигур и
# отдельно выполнять их создание. Здесь вступает в игру Фабричный метод. Фабричный метод абстрагирует наши фигуры от
# клиентов, клиент не должен знать все доступные фигуры, он должен создавать только то, что ему нужно в данный момент.
# - Для этого создадим Фабричный класс ShapeFactory с фабричным методом create_shape, который будут вызывать клиенты
# с указанием названия фигуры и ее параметров. И теперь наш фабричный метод за клиента создаст объект нужной ему фигуры,
# фабрика сама вызовет нужный метод из классов фигур.
#
# Фабричный метод позволяет создавать объекты без указания точного класса, необходимого для создания конкретного
# объекта. Это позволяет нам отделить наш код и повышает его повторное использование.
#
# Плюсы:
# - Код слабо связан. Большинство компонентов кода не знают о других компонентах той же кодовой базы.
# - Код легко понять и протестировать.
# - Легко добавить больше функциональности к конкретным компонентам, не затрагивая и не нарушая всю программу.
# - Поддерживает принцип Единой ответственности и Открытости / Закрытости.
#
# Минусы:
# - Создание большего количества классов в конечном итоге приводит к меньшей читабельности.

from abc import ABC, abstractmethod


class Shape(ABC):
    """Абстрактный класс (базовый) для представления всех фигур"""

    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass


class Rectangle(Shape):
    """Расширение для абстрактного класса конкретной фигуры - Прямоугольник"""

    def __init__(self, height, width):
        self.height = height
        self.width = width

    def calculate_area(self):
        return self.height * self.width

    def calculate_perimeter(self):
        return 2 * (self.height + self.width)


class Square(Shape):
    """Расширение для абстрактного класса конкретной фигуры - Квадрат"""

    def __init__(self, width):
        self.width = width

    def calculate_area(self):
        return self.width ** 2

    def calculate_perimeter(self):
        return 4 * self.width


class Circle(Shape):
    """Расширение для абстрактного класса конкретной фигуры - Круг"""

    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius * self.radius

    def calculate_perimeter(self):
        return 2 * 3.14 * self.radius


class ShapeFactory:
    """
    Фабричный класс с методом для создания объектов фигур конкретного класса.
    - Пользователь может не знать всех доступных фигур, он создает только то, что ему нужно в данный момент.
    - Мы не обращаемся к методам конкретных фигур, мы обращаемся к фабрике ShapeFactory и просим ее создать фигуру.
    - ShapeFactory получает имя фигуры и ее параметры и сам создаст за нас объект нужной фигуры.
    """

    def create_shape(self, name):

        if name == 'circle':
            radius = input("Enter the radius of the circle: ")
            return Circle(float(radius))

        elif name == 'rectangle':
            height = input("Enter the height of the rectangle: ")
            width = input("Enter the width of the rectangle: ")
            return Rectangle(int(height), int(width))

        elif name == 'square':
            width = input("Enter the width of the square: ")
            return Square(int(width))


def shapes_client():
    shape_factory = ShapeFactory()
    shape_name = input("Enter the name of the shape: ")
    shape = shape_factory.create_shape(shape_name)
    print(f"The type of object created: {type(shape)}")
    print(f"The area of the {shape_name} is: {shape.calculate_area()}")
    print(f"The perimeter of the {shape_name} is: {shape.calculate_perimeter()}")


if __name__ == '__main__':
    shapes_client()
