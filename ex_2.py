def print_fibonacci_sequence(n):
    """
    Prints the first N numbers of the Fibonacci sequence.

    Args:
        n (int): the number if Fibonacci numbers to print
    Returns:
        None
    """
    print(f"Первые {n} чисел последовательности Фибоначчи:")
    
    if n >= 1:
        print("1", end="")
    if n >= 2:
        print(", 1", end="")
    
    prev1 = 1
    prev2 = 1
    
    for i in range(3, n + 1):
        current = prev1 + prev2
        print(f", {current}", end="")
        
        prev1, prev2 = prev2, current

number = int(input())

while number<0:
    print("Введите положительное число порядка")
    number = int(input())

print_fibonacci_sequence(number)
