# Singleton (Одиночка) - порождающий паттерн
# Гарантирует, что у класса есть только один экземпляр, и предоставляет к нему глобальную точку доступа.
# Чаще всего это полезно для доступа к какому-то общему ресурсу, например, базе данных или файлу.
#
# Применяется:
# - Когда в программе должен быть единственный экземпляр какого-то класса, доступный всем клиентам
# (например, общий доступ к базе данных из разных частей программы).
# - Когда вам хочется иметь больше контроля над глобальными переменными.
#
# Пример:
# Реализуем правительство для одной страны. Оно может быть только одно:
# - Cоздадим переменную для определения нашего объекта.
# - Создание объекта одиночки реализуется в статическом методе.
# - Все вызовы этого метода возвращают, либо исходный объект, либо ошибку если исходный объект уже был создан.
# - Метод конструктор __init__ проверит был ли ранее создан объект класса, если да, то выдаст ту самую ошибку.
#
# Плюсы:
# - Гарантирует наличие единственного экземпляра класса.
# - Предоставляет к нему глобальную точку доступа.
# - Реализует отложенную инициализацию объекта-одиночки.
# - Гибкость, поскольку изменения необходимо вносить только в один класс и объект.
#
# Минусы:
# - Нарушает принцип единственной ответственности класса.
# - Маскирует плохой дизайн.
# - Проблемы мультипоточности.
# - Требует постоянного создания Mock-объектов при юнит-тестировании.

class SingletonGovernment:
    __instance__ = None

    def __init__(self):
        """Метод конструктор"""
        if SingletonGovernment.__instance__ is None:
            SingletonGovernment.__instance__ = self
        else:
            raise Exception("You cannot create another SingletonGovernment class")

    @staticmethod
    def get_instance():
        """Статический метод для получения текущего экземпляра класса"""
        if not SingletonGovernment.__instance__:
            SingletonGovernment()
        return SingletonGovernment.__instance__


if __name__ == '__main__':
    government = SingletonGovernment()
    print(government)  # __main__.SingletonGovernment object at 0x00000220B7157FA0>

    same_government = SingletonGovernment.get_instance()
    print(same_government)  # __main__.SingletonGovernment object at 0x00000220B7157FA0>

    another_government = SingletonGovernment.get_instance()
    print(another_government)  # __main__.SingletonGovernment object at 0x00000220B7157FA0>

    new_government = SingletonGovernment()
    print(new_government)  # Exception: You cannot create another SingletonGovernment class
