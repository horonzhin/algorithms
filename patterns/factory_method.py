# Factory Method (Фабричный метод) - порождающий паттерн
# Определяет общий интерфейс для создания объектов в суперклассе.
# Эти интерфейсы определяют структуру, но не создают объекты. Создание лежит на конкретном подклассе.
#
# Применяется:
# 1. Когда заранее неизвестны типы и зависимости объектов, с которыми должен работать код.
# 2. Когда хотим дать возможность пользователям расширять части фреймворка или библиотеки.
# 3. Когда хотим экономить системные ресурсы, повторно используя уже созданные объекты, вместо порождения новых.
#
# Пример: реализуем фабрику для создания фигур. Создаем родительский класс Shape с методами calculate_area и
# calculate_area. Конкретные объекты Rectangle, Square, Circle затем наследуются от нашего базового класса.
# Чтобы создать фигуру, нам нужно будет определить, какая форма требуется, и создать для нее подкласс.

import abc


class Shape(metaclass=abc.ABCMeta):
    """Абстрактный класс (базовый) для представления всех фигур"""
    @abc.abstractmethod
    def calculate_area(self):
        pass

    @abc.abstractmethod
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
    Фабричный класс с методом для создания объектов фигур конкретного класс.
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


if __name__ == '__main__':
    shape_factory = ShapeFactory()
    shape_name = input("Enter the name of the shape: ")
    shape = shape_factory.create_shape(shape_name)
    print(f"The type of object created: {type(shape)}")
    print(f"The area of the {shape_name} is: {shape.calculate_area()}")
    print(f"The perimeter of the {shape_name} is: {shape.calculate_perimeter()}")


