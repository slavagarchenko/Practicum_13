from math import gcd

def common_multiples(A, B, N):
    """
    Print all common multiples of two natural numbers A and B in ascending order, not exceeding N.

    Args:
        A (int): first natural number
        B (int): second natural number
        N (int): upper limit for multiples
    Returns:
        multiples (list): common multiples not exceeding N
    """
    lcm = A * B // gcd(A, B)
    
    multiples = []
    multiple = lcm
    
    while multiple <= N:
        multiples.append(multiple)
        multiple += lcm 
    
    return multiples
while True:
    try:
        A = int(input("Введите натуральное число A: "))
        if A > 0:
            break
        else:
            print("Введите натуральное число для А (больше 0)")
    except ValueError:
        print("Введите целое число для А")

while True:
    try:
        B = int(input("Введите натуральное число B: "))
        if B > 0:
            break
        else:
            print("Введите натуральное число для B (больше 0)")
    except ValueError:
        print("Введите целое число для B")

while True:
    try:
        N = int(input("Введите натуральное число N: "))
        if N > 0:
            break
        else:
            print("Введите натуральное число для N (больше 0)")
    except ValueError:
        print("Введите целое число для N")

result = common_multiples(A, B, N)
print(f"Общие кратные чисел {A} и {B}, не превосходящие {N}:")
if result:
    print(" ".join(map(str, result)))
else:
    print("Общих кратных не найдено")
