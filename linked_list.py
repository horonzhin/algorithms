# Linked List (Связанные списки)
#
# Массив где каждый элемент является отдельным объектом и состоит из двух элементов: данных и ссылки на следующий узел.
# Первый элемент списка - Head, промежуточные - Node, последний - Tail, он ссылается на NULL.
# Связные списки похожи на массивы, однако добавление и удаление элементов из середины или из начала списка здесь проще,
# так как нет необходимости менять индексы всех последующих элементов.
# Сложность вставки в начало и конец O(1), а вставка в середину, перебор и удаление произвольного O(n*).
# Пример связанного списка на JSON:
# {value: 1, next: {
#     value: 2, next: {
#         value: 3, next: {None}}}}
#
# Алгоритмы работы со связанными списками:
# - перемещение (по узлам и указателям),
# - поиск (по заголовку, углу или хвосту),
# - вставка (заголовка, узла, хвоста),
# - удаление (узла, хвоста).


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """Реализация того, что нужно делать с узлами"""

    def traversal(self):
        """Перемещение по узлам и распечатка их"""
        first = self.head
        while first:
            print(first.data)
            first = first.next

    def insert_new_header(self, new_data):
        """Вставить новый заголовок"""
        new_node = Node(new_data)  # создали новый узел
        new_node.next = self.head  # назначаем его следующим узлом для себя
        self.head = new_node  # а затем назначаем его head для узла

    def search_node(self, x):
        """Поиск узла"""
        temp = self.head  # временную переменную делаем заголовком
        while temp is not None:  # пройтись по узлам
            if temp.data == x:  # если узел равен тому что в "x"
                return True  # то нашли True
            temp = temp.next  # если нет переходим к следующему узлу
        else:  # если не нашли то False
            return False

    def delete_node(self, data):
        """Удаление узлов"""
        temp = self.head  # временную переменную делаем заголовком
        while temp is not None:  # пройтись по узлам
            if temp.data == data:  # если узел не равен тому что в "data"
                break
            prev = temp  # задаем текущему узлу значение предыдущего узла
            temp = temp.next  # а следующему задаем значение следующего узла
        # когда нашли этот узел, он оказывается между предыдущим и следующим которые связаны между собой и тот,
        # что искали вылетает.
        prev.next = temp.next

    def delete_tail(self):
        """Удаление хвоста"""
        temp = self.head  # временную переменную делаем заголовком
        # до тех пор пока указатель next.next имеется, т.е. указатель на два узла впереди
        while temp.next.next is not None:
            temp = temp.next  # делаем временную точку следующим узлом
        temp.next = None  # задаем ей значение None


if __name__ == "__main__":
    # Создадим head и узлы
    family = LinkedList()
    family.head = Node("Bob")
    wife = Node("Anny")
    first_kid = Node("Max")
    second_kid = Node("Jenny")

    # Создадим связи узлов
    family.head.next = wife
    wife.next = first_kid
    first_kid.next = second_kid

    family.traversal()  # -> Bob Anny Max Jenny

    # Меняем head
    # Чтобы изменить head создаем новый узел, назначаем его next для самого себя, а затем назначаем этот узел head'ом.
    family.insert_new_header("Dave")
    family.traversal()  # -> Dave Bob Anny Max Jenny

    # Ищем узел
    # Чтобы удалить узел его сперва нужно найти
    family.traversal()  # -> Dave Bob Anny Max Jenny True
    print(family.search_node("Bob"))

    # Удаляем узел
    family.delete_node("Bob")
    family.traversal()  # -> Dave Anny Max Jenny
    # Но если удалить другой узел (например "Anny"), то удаленный узел вернется,
    # т.к. чтобы полностью удалить узел, нужно удалить его объект.

    # Удаляем tail
    family.delete_tail()
    family.traversal()  # -> Dave Anny Max
