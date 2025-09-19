#  Лишняя задача

# Технические условия задания
# Перечень заданий хранится в связном списке.
# Для выполнения задания используется прекод.
# Написать функцию solution(), которая принимает на вход голову связного
# списка и индекс элемента. Функция должна удалить из списка элемент
# с указанным индексом и вернуть голову обновлённого списка.


# Импорт модуля os из стандартной библиотеки
# для взаимодействия с операционной системой.
import os
# Считывание переменной окружения REMOTE_JUDGE, чтобы определить,
# локально выполняется код или на удалённом сервере.
LOCAL = os.environ.get('REMOTE_JUDGE', 'false') != 'true'

# Если код выполняется на локальном компьютере, то...
if LOCAL:
    # Класс, описывающий элементы связного списка:
    class Node:
        def __init__(self, value, next_item=None):
            self.value = value
            self.next_item = next_item


def solution(node, idx):
    # Случай, когда надо удалить первую ноду (голову)
    if idx == 0:
        new_head = node.next_item
        del node
        return new_head

    current_node = node
    prev_node = None
    count = 0

    while current_node is not None:
        if count == idx:
            # Изменяем связь предыдущей ноды на следующую после удаляемой
            prev_node.next_item = current_node.next_item
            del current_node  # Удаление ненужной ноды
            break
        prev_node = current_node
        current_node = current_node.next_item
        count += 1

    return node


# Тестирующая функция для проверки решения.
def test():
    node3 = Node("Задача 4: Обследовать грунт в радиусе 3 м", None)
    node2 = Node("Задача 3: Измерить температуру атмосферы", node3)
    node1 = Node("Задача 2: Пробурить скважину глубиной 0.5 м", node2)
    node0 = Node("Задача 1: Фотосъёмка 360°", node1)

    new_head = solution(node0, 1)
    # Выражение, начинающееся с ключевого слова assert,
    # проверяет, что утверждение в выражении истинно.
    # Если утверждение ложно - в этом месте возникнет ошибка.
    assert new_head is node0
    assert new_head.next_item is node2
    assert new_head.next_item.next_item is node3
    assert new_head.next_item.next_item.next_item is None
    # result is node0 -> node2 -> node3


if __name__ == '__main__':
    test()
