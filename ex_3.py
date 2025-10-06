def calculate_final_price(price, has_discount_card, is_holiday):
    """
    Calculates the final price of the product, taking into account all discounts
    
    Args:
        price (float): initial purchase price
        has_discount_card (bool): availability of a discount card
        is_holiday (bool): is the day a holiday
    
    Returns:
        float: the final price, including all discounts (rounded to hundredths)
    """
    base_discount = 0
    
    if price > 30000:
        base_discount = 10
    elif price > 20000:
        base_discount = 7
    elif price > 15000:
        base_discount = 5
    elif price > 5000:
        base_discount = 3
    
    card_discount = 5 if has_discount_card else 0
    holiday_discount = 3 if is_holiday else 0
    
    total_discount = base_discount + card_discount + holiday_discount
    
    total_discount = min(total_discount, 15)
    
    final_price = price * (1 - total_discount / 100)
    
    return round(final_price, 2)

print("Введите данные о покупке")

while True:
  price = float(input("Введите стоимость покупки (руб.): "))
        if price >= 0:
            break
        else:
            print("Ввдеите правильную стоимость")

while True:
    card_input = input("Есть ли у вас дисконтная карта? (да/нет): ").lower()
    if card_input == "да":
        has_discount_card = True
        break
    elif card_input == "нет":
        has_discount_card = False
        break
    else:
        print("Введите да или нет")

while True:
    holiday_input = input("Сегодня праздничный день? (да/нет): ").lower()
    if holiday_input == "да":
        is_holiday = True
        break
    elif holiday_input == "нет":
        is_holiday = False
        break
    else:
        print("Введите да или нет")
      
final_price = calculate_final_price(price, has_discount_card, is_holiday)
print(f"Исходная стоимость: {price} руб.")
print(f"Дисконтная карта: {'да' if has_discount_card else 'нет'}")
print(f"Праздничный день: {'да' if is_holiday else 'нет'}")
print(f"Окончательная стоимость: {final_price} руб.")
