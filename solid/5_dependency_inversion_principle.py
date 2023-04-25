# Dependency Inversion Principle (DIP)
# Должны быть зависимости на классах, а не классы на зависимостях.
# - Верхнеуровневые модули должны зависеть не от низкоуровневых модулей, а от абстракций,
# также как и нижнеуровневые модули.
# - Абстракции не должны зависеть от деталей.
# - Детали (сами исполнительные классы и их методы) должны зависеть от абстракций.

from abc import ABC


# wrong
class FXConverterWrong:
    def convert(self, from_currency, to_currency, amount):
        print(f'Wrong output FX: {amount} {from_currency} = {amount * 1.2} {to_currency}')
        return amount * 1.2


class AppWrong:
    def start(self):
        converter = FXConverterWrong()
        converter.convert('EUR', 'USD', 100)


# correct
class CurrencyConverter(ABC):
    def convert(self, from_currency, to_currency, amount) -> float:
        pass


class FXConverter(CurrencyConverter):
    def convert(self, from_currency, to_currency, amount) -> float:
        print(f'Correct output FX: {amount} {from_currency} = {amount * 1.2} {to_currency}')
        return amount * 1.15


class AlphaConverter(CurrencyConverter):
    def convert(self, from_currency, to_currency, amount) -> float:
        print(f'Correct output Alpha: {amount} {from_currency} = {amount * 1.2} {to_currency}')
        return amount * 1.2


class AppCorrect:
    def __init__(self, converter: CurrencyConverter):
        self.converter = converter

    def start(self):
        self.converter.convert('EUR', 'USD', 100)


if __name__ == '__main__':

    # wrong
    app_wrong = AppWrong()
    app_wrong.start()  # Wrong output FX: 100 EUR = 120.0 USD

    # correct
    converter = AlphaConverter()
    app_correct = AppCorrect(converter)
    app_correct.start()  # Correct output Alpha API: 100 EUR = 120.0 USD
