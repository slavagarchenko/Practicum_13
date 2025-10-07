def make_payment(payment):
    """
    Processes a credit card payment.
    
    Args:
        payment (float): payment amount
    
    Prints:
        "Успех" or "Повторить попытку" with the reason
    """
    credit_limit = 1000
    min_payment = 20
    
    if not isinstance(payment, (int, float)):
        print("Повторить попытку: Неверный тип данных. Введите числовое значение.")
        return
      
    if payment > credit_limit:
        print(f"Повторить попытку: Платеж ${payment} превышает кредитный лимит ${credit_limit}.")
        return
    
    if payment < min_payment:
        print(f"Повторить попытку: Платеж ${payment} меньше минимального платежа ${min_payment}.")
        return
    
    print(f"Успех: Платеж ${payment} принят.")
