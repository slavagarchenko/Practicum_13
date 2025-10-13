def prime(n):
    """
    Check if a number is prime

    Args:
        n (int): the number to check for primality

    Returns:
        bool: True if the number is prime, False otherwise
    """
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**.5)+1, 2):
        if n % i == 0:
            return False
    return True


number = int(input("Введите число: "))

for i in range(1, number+1):
    if prime(i):
        print(i, end=" ")
