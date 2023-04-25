# Abstract Factory (Абстрактная фабрика) - порождающий паттерн
# Позволяет создавать семейства связанных объектов, не привязываясь к конкретным классам создаваемых объектов.
# Расширенная версия Factory Method. Создаем Фабрики для Фабрик.
#
# Применяется:
# 1. Когда бизнес-логика программы должна работать с разными видами связанных друг с другом продуктов,
# не завися от конкретных классов продуктов.
# 2. Когда в программе уже используется Фабричный метод, но очередные изменения предполагают введение
# новых типов продуктов.
#
# Пример: реализуем семейство из двух продуктов Браузер и Мессенджер.
# - Создадим 2 Абстрактных Продукта (класса) один Browser, второй Messenger. Эти классы содержат абстрактные методы,
# которые являются обязательными для построения продуктов. Эти абстрактные классы называются интерфейсами.
# - Создадим классы для Конкретных Продуктов (VanillaBrowser, VanillaMessenger, SecureBrowser, SecureMessenger),
# которые наследуют Абстрактные Продукты с их методами, а также дополнены своим функционалом.
# - Создадим саму Абстрактную Фабрику с интерфейсом для создания Абстрактных Продуктов.
# - Создадим соответствующие Конкретные Фабрики, которые создают Конкретные Продукты в соответствии
# с указанием Абстрактных Фабрик.
#
# Плюсы:
# - Легко добавить больше функциональности к конкретным компонентам, не затрагивая и не нарушая всю программу.
# - Код слабо связан. Большинство компонентов кода не знают о других компонентах той же кодовой базы
# - Гарантирует сочетаемость создаваемых продуктов.
# - Поддерживает принцип Единой ответственности и Открытости / Закрытости.
#
# Минусы:
# - Создание большего количества классов в конечном итоге приводит к меньшей читабельности.
# - Требует наличия всех типов продуктов в каждой вариации.

from abc import ABC, abstractmethod


# ************************************************ Абстрактные продукты ************************************************
# ******************************************************* Browser ******************************************************
class Browser(ABC):
    """Абстрактный продукт (базовый класс) - Browser"""

    # Интерфейс создания панели поиска
    @abstractmethod
    def create_search_toolbar(self):
        pass

    # Интерфейс создания окна браузера
    @abstractmethod
    def create_browser_window(self):
        pass


# ****************************************************** Messenger *****************************************************
class Messenger(ABC):
    """Абстрактный продукт (базовый класс) - Messenger"""

    # Интерфейс создания окна мессенджера
    @abstractmethod
    def create_messenger_window(self):
        pass


# ************************************************ Конкретные продукты ************************************************
# ****************************************************** Vanilla ******************************************************
class VanillaBrowser(Browser):
    """Расширение для абстрактного класса в виде конкретного продукта - VanillaBrowser"""

    # Абстрактный метод базового класса Browser
    def create_search_toolbar(self):
        print("Search Toolbar Created")

    # Абстрактный метод базового класса Browser
    def create_browser_window(self):
        print("Browser Window Created")


class VanillaMessenger(Messenger):
    """Расширение для абстрактного класса в виде конкретного продукта - VanillaMessenger"""

    # Абстрактный метод базового класса Messenger
    def create_messenger_window(self):
        print("Messenger Window Created")


# ******************************************************* Secure *******************************************************
class SecureBrowser(Browser):
    """Расширение для абстрактного класса в виде конкретного продукта - SecureBrowser"""

    # Абстрактный метод базового класса Browser
    def create_search_toolbar(self):
        print("Secure Browser - Search Toolbar Created")

    # Абстрактный метод базового класса Browser
    def create_browser_window(self):
        print("Secure Browser - Browser Window Created")

    # Дополнительный метод для расширения функционала
    def create_incognito_mode(self):
        print("Secure Browser - Incognito Mode Created")


class SecureMessenger(Messenger):
    """Расширение для абстрактного класса в виде конкретного продукта - SecureMessenger"""

    # Абстрактный метод базового класса Messenger
    def create_messenger_window(self):
        print("Secure Messenger - Messenger Window Created")

    # Дополнительный метод для расширения функционала
    def create_privacy_filter(self):
        print("Secure Messenger - Privacy Filter Created")

    # Дополнительный метод для расширения функционала
    def disappearing_messages(self):
        print("Secure Messenger - Disappearing Messages Feature Enabled")


# ************************************************* Абстрактная фабрика ************************************************
class AbstractFactory(ABC):
    """Абстрактная фабрика (базовый класс)"""

    @abstractmethod
    def create_browser(self):
        pass

    @abstractmethod
    def create_messenger(self):
        pass


# ************************************************* Конкретные фабрики *************************************************
# ****************************************************** Vanilla ******************************************************
class VanillaProductsFactory(AbstractFactory):
    """Конкретная фабрика реализации конкретных продуктов - Vanilla"""

    def create_browser(self):
        return VanillaBrowser()

    def create_messenger(self):
        return VanillaMessenger()


# ******************************************************* Secure *******************************************************
class SecureProductsFactory(AbstractFactory):
    """Конкретная фабрика реализации конкретных продуктов - Secure"""

    def create_browser(self):
        return SecureBrowser()

    def create_messenger(self):
        return SecureMessenger()


# ******************************************************* Client *******************************************************
def product_client():
    for factory in (VanillaProductsFactory(), SecureProductsFactory()):
        product_a = factory.create_browser()
        product_b = factory.create_messenger()
        product_a.create_browser_window()
        product_a.create_search_toolbar()
        product_b.create_messenger_window()


if __name__ == '__main__':
    product_client()
