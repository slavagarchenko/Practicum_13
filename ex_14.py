def find_substring(main_string, substring, start=0, end=None):
    """
    Finds the index of the first occurrence of a substring in
    a main string.

    Args:
        main_string (str): The string to search in (e.g., DNA sequence).
        substring (str): The substring to search for.
        start (int): Starting index for the search (default 0).
        end (int): Ending index for the search (default None,
                    meaning end of string).

    Returns:
        int: Index of the first occurrence of substring, or
                -1 if not found.
    """
    if end is None:
        end = len(main_string)

    start = max(0, min(start, len(main_string)))
    end = max(start, min(end, len(main_string)))

    for i in range(start, end - len(substring) + 1):
        match = True
        for j in range(len(substring)):
            if main_string[i + j] != substring[j]:
                match = False
                break
        if match:
            return i
    return -1


def find_all_indices(main_string, substring):
    """
    Finds all indices of occurrences of a substring in a main string.

    Args:
        main_string (str): The string to search in (e.g., DNA sequence).
        substring (str): The substring to search for.

    Returns:
        str: Comma-separated string of indices, or
                empty string if not found.
    """
    indices = []

    for i in range(len(main_string) - len(substring) + 1):
        match = True
        for j in range(len(substring)):
            if main_string[i + j] != substring[j]:
                match = False
                break
        if match:
            indices.append(str(i))
    return ','.join(indices) if indices else -1


dna_sequence = input("Введите последовательность ДНК: ")
dna_section = input("Введите искомую часть ДНК: ")
start = int(input("Введите начальный индекс поиска для первого вхождения: "))
end = int(input("Введите конечный индекс для поиска первого вхождений: "))

print(find_substring(dna_sequence, dna_section, start, end))
print(find_all_indices(dna_sequence, dna_section))
