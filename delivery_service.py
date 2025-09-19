# ID посылки: 142522213

# Для перевозки роботов есть неограниченное количество транспортных платформ,
# каждая из которых способна выдерживать определённый вес limit.
# На одной платформе можно перевезти 1-2х роботов, при условии,
# что их совокупный вес не превышает limit. Роботы имеют разный вес.
# Программа получает на вход массив, каждый элемент которого — это вес робота.
# Второй параметр — это limit,грузоподъёмность одной платформы.
# Нужно определить минимальное количество транспортных платформ.

# Количество платформ неограниченно.
# Каждая платформа выдерживает максимальный вес limit.
# На каждой платформе можно перевезти не более 2х роботов при условии, что
# их совокупный вес не превышает limit.
# Вес отдельного робота не может превышать limit

def calc_numbers_of_platforms(weights_in: list[int], limit: int) -> int:
    """
    Расчет минимального количества платформ.
    Ограничения: не превышать вес(limit) и не более 2-х роботов на платформе.
    Описание алгоритма:
    1. определяем кол-во роботов, сортируем по весу.
    2. Берем робота с максимальным весом и если не превышаем limit,
    то пытаемся к нему добавить робота с минимальным весом.
    3. При успешном выполнении условий по весу делаем сдвиг по массиву.
    4. Повторяем 2-3 пока не обработаем данные по всем роботам(number_robots=0)
    На каждом цикле увеличиваем счетчик платформ.
    """
    platforms = 0
    offset_min_weight = 0
    number_robots = len(weights_in)
    offset_max_weight = number_robots - 1
    weights = sorted(weights_in)

    while number_robots > 0:

        first_weight = weights[offset_max_weight]  # get first max weight
        offset_max_weight -= 1
        number_robots -= 1

        if first_weight > limit:  # don`t to add on the platform
            continue

        platforms += 1

        if first_weight < limit and number_robots > 0:  # try to add min weight
            if weights[offset_min_weight] <= limit - first_weight:
                offset_min_weight += 1
                number_robots -= 1

    return platforms


if __name__ == '__main__':
    weights = [int(i) for i in input().split()]

    limit = int(input())

    platforms = calc_numbers_of_platforms(weights, limit)
    print(platforms)
