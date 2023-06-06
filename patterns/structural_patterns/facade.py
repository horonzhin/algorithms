# Фасад (Facade) — структурный паттерн
# Простой интерфейс для работы со сложной подсистемой, содержащей множество классов
# Фасад может иметь урезанный интерфейс, не имеющий 100% функциональности, которой можно достичь, используя сложную
# подсистему напрямую. Но он предоставляет именно те инструменты, которые нужны клиенту, и скрывает все остальные.
########################################################################################################################
# Применяется:
# - Когда вам нужно представить простой или урезанный интерфейс к сложной подсистеме.
# - Когда вы хотите разложить подсистему на отдельные слои.
########################################################################################################################
# Плюсы:
# - Изолирует клиентов от компонентов сложной подсистемы.
# - Cлабая связь между клиентами и подсистемами.
########################################################################################################################
# Минусы:
# - Фасад рискует стать "божественным объектом" (хранит и делает слишком много), привязанным ко всем классам программы.
########################################################################################################################

class TakeOrder:
    def order(self):
        print("Getting the order.")


class CookPizza:
    def cook(self):
        print("Cooking the Pizza...")


class Delivery:
    def deliver(self):
        print("Delivered the Pizza.")


class Operator:
    """Фасад в виде оператора, принимающего заказ клиента"""

    def __init__(self):
        self.ordering = TakeOrder()
        self.cooking = CookPizza()
        self.delivering = Delivery()

    def complete_order(self):
        self.ordering.order()
        self.cooking.cook()
        self.delivering.deliver()
        print("Order completed successfully.")


if __name__ == '__main__':
    operator = Operator()
    operator.complete_order()
