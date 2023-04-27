# Builder (Строитель) - порождающий паттерн
# Позволяет создавать сложные объекты пошагово. Строитель даёт возможность использовать один и тот же код строительства
# для получения разных представлений объектов.
########################################################################################################################
# Применяется:
# - Когда вы хотите избавиться от «телескопического конструктора».
# - Когда ваш код должен создавать разные представления какого-то объекта. Например, деревянные и железобетонные дома.
# - Когда вам нужно собирать сложные составные объекты, например, деревья Компоновщика.
########################################################################################################################
# Пример:
# Реализуем строителя робота. Робот может быть с двумя ногами, четырьмя ногами, на колесах, с лопастями, хвостом,
# крыльями, может иметь камеры и т.д.
#
# Обычный конструктор имел вид «телескопического конструктора» и выглядел бы примерно так:
#
# def __init__(self, left_leg, right_leg, left_arm, right_arm, left_wing,
# right_wing, tail, blades, cameras, infrared_module, ...):
# 	self.left_leg = left_leg
# 	if left_leg == None:
# 		bipedal = False
# 	self.right_leg = right_leg
# 	self.left_arm = left_arm
# 	self.right_arm = right_arm # ...
#
# Создание экземпляра этого класса было бы крайне нечитабельным, было бы очень легко ошибиться
# с некоторыми типами аргументов.
#
# Кроме того, что, если мы не хотим, чтобы робот реализовывал все поля в классе?
#
# Python не поддерживает перегружающие конструкторы, которые помогли бы нам определить такие случаи
# (и даже если бы мы могли, это привело бы только к еще более запутанным конструкторам).
#
# - Создадим класс Robot, опустим конкретные инициализации в нем, вместо этого используем значения по умолчанию.
# Будем использовать абстрактный класс RobotBuilder для инициализации этих значений.
# - Cоздадим абстрактный класс RobotBuilder наш интерфейс для строительства, который строит наш объект и
# добавляет соответствующие модули к нашему роботу. Будем создавать экземпляр объекта и добавлять необходимые
# компоненты с помощью функций.
# - Создадим конкретных строителей AndroidBuilder и CarBuilder которые будут подчиняться интерфейсу -
# главному строителю RobotBuilder
# - Создадим Director для управления конкретными строителями AndroidBuilder и CarBuilder.
# - Клиенту Client останется только привязать конкретного строителя AndroidBuilder или CarBuilder к Director,
# а затем получить у конкретного строителя готовый результат.
########################################################################################################################
# Плюсы:
# - Позволяет создавать продукты пошагово.
# - Позволяет использовать один и тот же код для создания различных продуктов.
# - Изолирует сложный код сборки продукта от его основной бизнес-логики.
#
# Минусы:
# - Усложняет код программы из-за введения дополнительных классов.
# - Клиент будет привязан к конкретным классам строителей, так как в интерфейсе директора
# может не быть метода получения результата.
########################################################################################################################

from abc import ABC, abstractmethod


class Robot:
    def __init__(self):
        self.bipedal = False
        self.quadripedal = False
        self.wheeled = False
        self.flying = False
        self.traversal = []
        self.detection_systems = []

    def __str__(self):
        string = ""
        if self.bipedal:
            string += "BIPEDAL "
        if self.quadripedal:
            string += "QUADRIPEDAL "
        if self.flying:
            string += "FLYING ROBOT "
        if self.wheeled:
            string += "ROBOT ON WHEELS\n"
        else:
            string += "ROBOT\n"

        if self.traversal:
            string += "Traversal modules installed:\n"

        for module in self.traversal:
            string += "- " + str(module) + "\n"

        if self.detection_systems:
            string += "Detection systems installed:\n"

        for system in self.detection_systems:
            string += "- " + str(system) + "\n"

        return string


# *********************************** Значения для построения робота ***************************************************
class BipedalLegs:
    def __str__(self):
        return "two legs"


class QuadripedalLegs:
    def __str__(self):
        return "four legs"


class Arms:
    def __str__(self):
        return "two arms"


class Wings:
    def __str__(self):
        return "wings"


class Blades:
    def __str__(self):
        return "blades"


class FourWheels:
    def __str__(self):
        return "four wheels"


class TwoWheels:
    def __str__(self):
        return "two wheels"


class CameraDetectionSystem:
    def __str__(self):
        return "cameras"


class InfraredDetectionSystem:
    def __str__(self):
        return "infrared"


# ********************************************** Абстрактный строитель *************************************************
class RobotBuilder(ABC):
    """Интерфейс строителя. Инициализация значений для конструирования робота"""

    @abstractmethod
    def reset(self):
        """Сброс конфигураций робота"""
        pass

    @abstractmethod
    def build_traversal(self):
        """Конструирование внешнего вида робота"""
        pass

    @abstractmethod
    def build_detection_system(self):
        """Добавление дополнительных функций"""
        pass


# ********************************************** Конкретные строители **************************************************
class AndroidBuilder(RobotBuilder):
    """Строитель робота-гуманоида"""
    def __init__(self):
        self.product = Robot()

    def reset(self):
        """Сброс конфигураций робота"""
        self.product = Robot()

    def get_product(self):
        """Вывод на экран результата"""
        return self.product

    def build_traversal(self):
        """Конструирование внешнего вида робота"""
        self.product.bipedal = True
        self.product.traversal.append(BipedalLegs())
        self.product.traversal.append(Arms())

    def build_detection_system(self):
        """Добавление роботу-гуманоиду камеры наблюдения"""
        self.product.detection_systems.append(CameraDetectionSystem())


class AutonomousCarBuilder(RobotBuilder):
    """Строитель робота-автомобиля"""
    def __init__(self):
        self.product = Robot()

    def reset(self):
        """Сброс конфигураций робота"""
        self.product = Robot()

    def get_product(self):
        """Вывод на экран результата"""
        return self.product

    def build_traversal(self):
        """Конструирование внешнего вида робота"""
        self.product.wheeled = True
        self.product.traversal.append(FourWheels())

    def build_detection_system(self):
        """Добавление роботу-автомобилю инфракрасной камеры"""
        self.product.detection_systems.append(InfraredDetectionSystem())


# *************************************************** Директор *********************************************************
class Director:
    """Управление конкретными строителями"""

    def make_android(self, builder):
        """Управление строителем робота-гуманоида"""
        builder.build_traversal()
        builder.build_detection_system()
        return builder.get_product()

    def make_autonomous_car(self, builder):
        """Управление строителем робота-автомобиля"""
        builder.build_traversal()
        builder.build_detection_system()
        return builder.get_product()


# **************************************************** Client **********************************************************
def robot_client():
    director = Director()
    builder = AndroidBuilder()
    print(director.make_android(builder))


if __name__ == "__main__":
    robot_client()
