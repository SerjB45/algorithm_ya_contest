# Неправильные горы

#  «Правильной» считается та гора, у которой на пути от подножия до вершины
# высота постоянно растёт, а на пути от вершины к подножию — постоянно
# уменьшается. Если у горы есть несколько вершин или в каком-то месте
# встречается горизонтальный участок — это «неправильная гора».
# Напишcать функцию valid_mountain_array, которая принимает на вход массив
# с высотами и возвращать True или False в зависимости от того, «правильная»
# это гора или нет.
# Если в массиве менее 3х элементов, такой массив не может описать
# «правильную» гору.

# Формат ввода
# Массив целых чисел через пробел — отметки о высоте точек рельефа.

# Формат вывода
# True — если гора «правильная», False — если гора «неправильная».

def main():
    hights = list(map(int, input().split()))
    print(valid_mountain_array(hights))


def valid_mountain_array(hights):
    mountain = True
    down = False
    high = False
    if len(hights) <= 2:
        return False

    for index in range(len(hights) - 1):
        if hights[index] == hights[index + 1]:
            mountain = False
            break
        elif hights[index] < hights[index + 1]:
            high = True
            if down:
                mountain = False
                break
        else:
            down = True
    return mountain and down and high


if __name__ == '__main__':
    main()
