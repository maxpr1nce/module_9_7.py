def sum_three(a, b, c):
    """Функция для сложения трех чисел."""
    return a + b + c

def is_prime(func):
    """Декоратор, проверяющий, является ли число простым."""
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if result < 2:
            print("Составное")
            return result
        for i in range(2, int(result**0.5) + 1):
            if result % i == 0:
                print("Составное")
                return result
        print("Простое")
        return result
    return wrapper

# Применение декоратора к функции sum_three
sum_three = is_prime(sum_three)

# Пример использования
result = sum_three(2, 3, 6)  # 2 + 3 + 6 = 11 (простое число)
print(result)  # Выводит: Простое \n 11

result = sum_three(1, 2, 3)  # 1 + 2 + 3 = 6 (составное число)
print(result)  # Выводит: Составное \n 6