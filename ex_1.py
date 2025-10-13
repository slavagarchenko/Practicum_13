def count_vowels_consonants(sentence):
    """
    The function accepts a sentence in Russian 
    and prints the total number of vowels and consonants

    Args:
      sentence (str): analysed sentence

    Returns:
      None
    """
    sentence_lower = sentence.lower()

    vowels = set('аеёиоуыэюя')
    consonants = set('бвгджзйклмнпрстфхцчшщ')

    vowel_count = 0
    consonant_count = 0

    for char in sentence_lower:
        if char.isalpha():
            if char in vowels:
                vowel_count += 1
            elif char in consonants:
                consonant_count += 1

    print(f"Количество гласных букв: {vowel_count}")
    print(f"Количество согласных букв: {consonant_count}")


sentence = input("Введите текст для анализа: ")
count_vowels_consonants(sentence)
