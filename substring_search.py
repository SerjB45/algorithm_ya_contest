# Поиск подстроки
# Необходимо выявить в последовательности самую длинную подстроку, 
# состоящую из уникальных символов: наибольший ряд символов, 
# в котором каждый символ встречается только один раз.
# Использовать метод скользящего окна для решения задачи.

# Формат ввода
# Одна строка, состоящая из строчных латинских букв. 
# Длина строки не превосходит 10 000 символов.

# Формат вывода
# Натуральное число — длина наибольшей подстроки с уникальными символами.

def main():
    text = input()
    max_len = 0
    left = 0
    
    consist_symbols = set()
    
    for right in range(len(text)):
        while text[right] in consist_symbols:
            consist_symbols.remove(text[left])
            left += 1

        consist_symbols.add(text[right])

        max_len = max(max_len, right - left + 1)
  
    print(max_len)


if __name__ == '__main__':
    main()
