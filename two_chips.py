# Две фишки
# Формат ввода
# В первой строке записано количество фишек n
# Во второй строке записано n целых чисел —– очки на фишках
# В третьей строке —– загаданное Гошей целое число k

# Формат вывода
# Нужно вывести два числа —– очки на двух фишках, в сумме дающие k.
# Если таких пар несколько, то можно вывести любую из них.
# Если таких пар не существует, то вывести «None».

def main():
    n = int(input())
    score = [int(i) for i in input().split()]
    k = int(input())
    res = find_two_number_by_sum(n, score, k)
    res2 = find_two_number_by_sum2(score, k)
    if res is None:
        print(res)
        print(res2)
    else:
        print(*res)
        print(*res2)

# решение в лоб


def find_two_number_by_sum(n, score, k):

    for i in range(n - 1):
        for j in range(i + 1, n):
            if score[i] + score[j] == k:
                return score[i], score[j]
    return None


def find_two_number_by_sum2(score, k):
    seen_numbers = {}

    for num in score:
        complement = k - num
        if complement in seen_numbers:
            return complement, num
        seen_numbers[num] = True
    return None


if __name__ == '__main__':
    main()
