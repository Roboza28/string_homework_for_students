"""
Панграмма - предложение, которое использует каждую букву алфавита (в нашем случае - английского алфавита).
Необходимо реализовать код, который скажет, является предложение панграммой или нет.
Буквы в верхнем и нижнем регистрах считаются эквивалентными.
Предложения содержат только буквы английского алфавита, без пробелов и т.п.
Проверка:
pytest ./2_sentence_is_pangram/test.py
"""
import string

def is_sentence_is_pangram(sentence: str) -> bool:
    original_elements = set()
    power_alphabet = len(string.ascii_lowercase)
    for i in sentence:
        original_elements.add(i.lower())
    if len(original_elements) == power_alphabet:
        return True
    else:
        return False
