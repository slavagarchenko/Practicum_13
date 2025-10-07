def telephone_card_value():
  """
  Calculate the total value of a phone card including bonus offers.
  Bonus Structure:
    - $5 card: $0 bonus
    - $10 card: $0 bonus
    - $25 card: $3 bonus
    - $50 card: $8 bonus
    - $100 card: $20 bonus 

  Returns:
    total_value (int): total card value including bonus, or None if invalid input
  """
  try:
    bonuses = {5:0, 
               10:0, 
               25:3, 
               50:8, 
               100:20}

    if card_value in bonuses:
      total_value = card_value+bonuses[card_value]
      return total_value
    else:
      print("Неверная стоимость карты")
      return None

  except ValueError:
    print("Введите целое число")
    return None

card_value = int(input("Введите стоимость карты: "))

result = telephone_card_value()
if result is not None:
  print(f"Общая стоимость карты с учётом бонусов: ${result}")
