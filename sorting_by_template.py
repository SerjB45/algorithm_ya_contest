from collections import Counter
# Сортировка по шаблону

# написать программу, которая:
# будет принимать на вход массив для сортировки и массив-шаблон,
# в соответствии с которым должна быть выполнена сортировка;
# вернёт массив, отсортированный в соответствии с шаблоном.

# Формат ввода
# В первой строке передаётся количество чисел, которые нужно отсортировать, n.
# Во второй строке передаются n чисел, которые надо отсортировать.
# В третьей строке передаётся длина массива-шаблона m.
# В четвёртой строке передаётся массив-шаблон, в соответствии с которым нужно
# отсортировать первый массив. Значения в этом массиве не превосходят 1000.
# В первом массиве гарантированно присутствуют все числа из массива-шаблона.

# Формат вывода
# Выведите в строку через пробел отсортированные значения из первого массива.


def main():
    n_lst = int(input())
    lst = [int(i) for i in input().split()]
    lst_2 = lst.copy()
    n_sort = int(input())
    template = [int(i) for i in input().split()]
    template_2 = template.copy()

    print(*sorted_by_template(n_lst, lst, n_sort, template))
    print(*sorted_by_template_2(n_lst, lst_2, n_sort, template_2))

# решение 1 - рабочее


def sorted_by_template(n_lst, lst, n_sort, template):
    tmp_sort_lst = []
    for n in template:
        offset = 0
        for i in range(len(lst)):
            if n == lst[i - offset]:
                tmp_sort_lst.append(n)
                del lst[i - offset]
                offset += 1
    lst = tmp_sort_lst + sorted(lst)
    return lst


# Пояснения:
# Counter(lst) — собирает частоты элементов массива.
# Первый проход по шаблону добавляет элементы в требуемом порядке, учитывая
# частоту их появления. Оставшиеся элементы собираются через метод
# counter.elements(), который генерирует список с учётом частоты, и
# сортируются. Всё объединяется в финальный результат.

def sorted_by_template_2(n_lst, lst, n_sort, template):
    counter = Counter(lst)  # Счётчик частот элементов
    res = []

    # Элементы из шаблона идут первыми
    for t in template:
        freq = counter.get(t, 0)
        res.extend([t]*freq)
        del counter[t]  # Убираем обработанный элемент из счёта

    # Остаточные элементы сортируем и добавляем в конец
    remaining_elements = sorted(counter.elements())
    res.extend(remaining_elements)

    return res


if __name__ == '__main__':
    main()
