def custom_find(text, substring, start=0, end=None):
    """
    Аналог строкового метода find без использования встроенного find
    Возвращает индекс первого вхождения подстроки или -1 если не найдено
    """
    if end is None:
        end = len(text)

    # Проверка корректности параметров
    if not substring:
        return -1
    if start < 0:
        start = 0
    if end > len(text):
        end = len(text)

    substring_len = len(substring)
    text_len = end - start

    # Если подстрока длиннее оставшегося текста
    if substring_len > text_len:
        return -1

    # Линейный поиск
    for i in range(start, end - substring_len + 1):
        match = True
        for j in range(substring_len):
            if text[i + j] != substring[j]:
                match = False
                break
        if match:
            return i

    return -1


def find_all_occurrences(text, substring):
    """
    Находит все вхождения подстроки в тексте
    Возвращает строку с индексами, разделенными запятыми
    """
    if not substring:
        return ""

    indices = []
    current_pos = 0
    text_len = len(text)
    substring_len = len(substring)

    while current_pos <= text_len - substring_len:
        # Используем нашу функцию custom_find для поиска
        pos = custom_find(text, substring, current_pos)
        if pos == -1:
            break
        indices.append(str(pos))
        current_pos = pos + 1  # Ищем следующее вхождение

    return ",".join(indices)


"""
def boyer_moor_find_all(text, substring):
    if not substring:
        return
    
    indices = []
    current_pos = 0
    text_len = len(text)
    
    while current_pos <= text_len - len(substring):
        pos = boyer_moor_find(text, substring, current_pos)
        if pos == -1:
            break
        indices.append(str(pos))
        current_pos = pos + 1
    
    return ",".join(indices)
"""
