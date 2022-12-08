import numpy as np
import random as rnd
import string as st


def matrix(list_of_words):
    array = np.array(list_of_words)
    return array


def generate_random_string(length):
    letters = st.ascii_lowercase
    rand_string = ''.join(rnd.choice(letters) for _ in range(length))
    return rand_string


def generate_matrix_values(M):
    return [generate_random_string(4) for _ in range(M ** 2)]


def check_word(word):
    return len(word) == 4 or word in 'abcdefghijklmnopqrstuvwxyz'


def user_word(M):
    arr = []
    itter = 1
    m = M ** 2
    while m:
        print(itter, " Иттерация")
        user_st = input()
        if check_word(user_st):
            arr.append(user_st)
            m -= 1
            itter += 1
        else:
            print('try again')
    return arr


def count_consonant(word):
    vowels = 'aiueoy'
    consonant = 0
    for i in word:
        if i not in vowels:
            consonant += 1
    return consonant


def list_consonant(list_of_words):
    lst = []
    for word in list_of_words:
        lst.append(count_consonant(word))
    return lst


def check_M(M):
    return M < 2 or M > 5 or M not in range(2, 6)


if __name__ == "__main__":
    print("Введите M размерность матрицы в диапазоне от 2 до 5 включительно")

    while True:
        M = int(input())
        if not check_M(M):
            break
        else:
            print("попробуй еще раз")

    print("""Выберете способ заполнения матрицы
    0 - автоматическое (рандомное)
    1 - ручное """)

    text = int(input())
    if text == 1:
        mat = matrix(user_word(M))
        print("Количество согласных букв в матрице слов")
        print(sorted((list_consonant(mat))))

    if text == 0:
        mati = matrix(generate_matrix_values(M))
        print("Количество согласных букв в матрице слов")
        print(sorted((list_consonant(mati))))
