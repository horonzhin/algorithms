# Декоратор (Decorator) — структурный паттерн
# Позволяет добавлять объектам новую функциональность, оборачивая их в полезные «обёртки».
# Эти объекты помещаются внутрь объектов-оболочек, содержащих модели поведения.
#
# Шаблон декоратора используется как в ООП, так и в функциональном программировании.
########################################################################################################################
# Применяется:
# - Когда нужно добавлять обязанности объектам на лету, незаметно для кода, который их использует.
# - Когда нельзя расширить обязанности объекта с помощью наследования.
# - Когда обязанности накладываемые на объект, можно с него снять.
########################################################################################################################
# Плюсы:
# - Большая гибкость, чем у наследования.
# - Позволяет добавлять обязанности на лету.
# - Можно добавлять несколько новых обязанностей сразу.
# - Позволяет иметь несколько мелких объектов вместо одного объекта на все случаи жизни.
########################################################################################################################
# Минусы:
# - Трудно конфигурировать многократно обёрнутые объекты.
# - Обилие крошечных классов.
########################################################################################################################

from abc import ABC


class WrittenText:
    """Изначальный текст"""

    def __init__(self, input_text: str):
        self._text = input_text

    def render(self) -> str:
        return self._text


class DecoratorText(ABC, WrittenText):
    """Базовый интерфейс декораторов"""

    def __init__(self, wrapped: WrittenText) -> None:
        self._wrapped = wrapped

    @property
    def written_text(self) -> WrittenText:
        """Инициализация завернутого объекта"""
        return self._wrapped

    def render(self) -> str:
        return self._wrapped.render()


class UnderlineDecorator(DecoratorText):
    """Декоратор. Оборачивает текст в тэг <u>. Подчеркнутый текст"""

    def render(self) -> str:
        return f"<u>{self._wrapped.render()}</u>"


class ItalicDecorator(DecoratorText):
    """Декоратор. Оборачивает текст в тэг <i>. Курсив"""

    def render(self) -> str:
        return f"<i>{self._wrapped.render()}</i>"


class BoldDecorator(DecoratorText):
    """Декоратор. Оборачивает текст в тэг <b>. Жирный шрифт"""

    def render(self) -> str:
        return f"<b>{self._wrapped.render()}</b>"


if __name__ == '__main__':
    text = WrittenText("Изначальный текст")
    print("До декорирования :", text.render())
    italic = ItalicDecorator(text)
    print("С декоратором ItalicDecorator:", italic.render())
    underline = UnderlineDecorator(text)
    print("С декоратором UnderlineDecorator:", underline.render())
    bold = BoldDecorator(text)
    print("С декоратором BoldDecorator:", bold.render())
    all_deco = ItalicDecorator(UnderlineDecorator(BoldDecorator(text)))
    print("Со всеми декораторами :", all_deco.render())
    print(italic.written_text == text)
