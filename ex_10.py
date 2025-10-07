def special_numbers(A, B):
  """
  Prints all numbers in ascending order from A to B (inclusive)
  that contain only digits from the set

  Args:
    A (int): first limit number
    B (int): second limit number
  """
  digits = {"1","3","4","8","9"}
  result = []

  if A > B:
    A, B = B, A

  for i in range(A, B+1):
    if digits.issubset(set(str(i))):
      result.append (i)

  if result:
    print(*result)
  else:
    print("Нет таких чисел")

A = int(input("Введите число А: "))
B = int(input("Введите число В: "))
special_numbers(A,B)
