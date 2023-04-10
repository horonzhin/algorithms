# **********************************************************************************************************************
# Single Responsibility Principle (SRP) - принцип единичной ответственности.
# Каждый класс должен выполнять только те цели ради которых он создается.

# wrong
class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def authenticate(self, email, password):
        # authenticate the user
        pass


# correct
class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password


class Authenticator:
    def authenticate(self, email, password):
        # authenticate the user
        pass


# **********************************************************************************************************************
# Open-Closed Principle (OCP)
# Класс должен быть открыт для расширения и закрыт для модификации.

class Calculator:
    def calculate(self, operand1, operand2, operator):
        if operator == '+':
            return operand1 + operand2
        elif operator == '-':
            return operand1 - operand2
        elif operator == '*':
            return operand1 * operand2
        elif operator == '/':
            return operand1 / operand2


class NewCalculator(Calculator):
    def calculate(self, operand1, operand2, operator):
        if operator == '%':
            return operand1 % operand2
        else:
            return super().calculate(operand1, operand2, operator)


# **********************************************************************************************************************
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

# **********************************************************************************************************************
# Interface Segregation Principle (ISP) - принцип разделения интерфейсов.
# Лучше иметь много небольших, чем иметь один большой интерфейс.


# wrong
class Machine:
    def print_document(self):
        pass

    def scan_document(self):
        pass

    def fax_document(self):
        pass

    def cancel_printing(self):
        pass


class MultiFunctionPrinter(Machine):
    def print_document(self):
        print("Printing document")

    def scan_document(self):
        print("Scanning document")

    def fax_document(self):
        print("Faxing document")

    def cancel_printing(self):
        print("Cancelling...")


class OldFashionedPrinter(Machine):
    def print_document(self):
        print("Printing document")

    def scan_document(self):
        # Old fashioned printers cannot scan documents
        raise NotImplementedError

    def fax_document(self):
        # Old fashioned printers cannot fax documents
        raise NotImplementedError

    def cancel_printing(self):
        # Old fashioned printers cannot fax documents
        raise NotImplementedError


# correct
class Printable:
    def print(self):
        pass


class Editable:
    def edit(self):
        pass


class Document(Printable, Editable):
    def print(self):
        print("Printing document")

    def edit(self):
        print("Editing document")


def print_document(printable: Printable):
    printable.print()


if __name__ == '__main__':
    document = Document()
    print_document(document)

# **********************************************************************************************************************
# Dependency Inversion Principle (DIP)
# Должны быть зависимости на классах, а не классы на зависимостях.
# - Верхнеуровневые модули должны зависеть не от низкоуровневых модулей, а от абстракций,
# также как и нижнеуровневые модули.
# - Абстракции не должны зависеть от деталей.
# - Детали (сами исполнительные классы и их методы) должны зависеть от абстракций.


# wrong
class FXConverter:
    def convert(self, from_currency, to_currency, amount):
        print(f'{amount} {from_currency} = {amount * 1.2} {to_currency}')
        return amount * 1.2


class App:
    def start(self):
        converter = FXConverter()
        converter.convert('EUR', 'USD', 100)


if __name__ == '__main__':
    app = App()
    app.start()


# correct
from abc import ABC


class CurrencyConverter(ABC):
    def convert(self, from_currency, to_currency, amount) -> float:
        pass


class FXConverter(CurrencyConverter):
    def convert(self, from_currency, to_currency, amount) -> float:
        print('Converting currency using FX API')
        print(f'{amount} {from_currency} = {amount * 1.2} {to_currency}')
        return amount * 1.15


class AlphaConverter(CurrencyConverter):
    def convert(self, from_currency, to_currency, amount) -> float:
        print('Converting currency using Alpha API')
        print(f'{amount} {from_currency} = {amount * 1.2} {to_currency}')
        return amount * 1.2


class App:
    def __init__(self, converter: CurrencyConverter):
        self.converter = converter

    def start(self):
        self.converter.convert('EUR', 'USD', 100)


if __name__ == '__main__':
    converter = AlphaConverter()
    app = App(converter)
    app.start()

    # output
    # Converting currency using Alpha API
    # 100 EUR = 120.0 USD
