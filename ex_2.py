def print_fibonacci_simple(n):
    """
    
    """
    print(f"Первые {n} чисел последовательности Фибоначчи:")
    
    if n >= 1:
        print("1", end="")
    if n >= 2:
        print(", 1", end="")
    
    prev1 = 1
    prev2 = 1
    
    # Генерируем остальные числа
    for i in range(3, n + 1):
        current = prev1 + prev2
        print(f", {current}", end="")
        
        # Обновляем предыдущие числа для следующей итерации
        prev1, prev2 = prev2, current
    
    print()  # Завершаем вывод

# Демонстрация работы:
numbers_to_print = [1, 2, 5, 8]
for num in numbers_to_print:
    print_fibonacci_simple(num)
    print("---")
