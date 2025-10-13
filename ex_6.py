def check_message_length(message):
    """
    Check and adjust message length to comply with SMS character limits

    Args:
      message (str): the text message to be checked for length comliance

    Returns:
      str: the original message if under 160 characters, 
            or truncated to first 160 characters if over the limit
    """
    if len(message) <= 160:
        return message
    else:
        return message[:160]


message = input("Введите текст сообщения: ")

print(check_message_length(message))
