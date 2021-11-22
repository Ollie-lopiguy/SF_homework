"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np
import random

def random_predict(number: int = 1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    lower = 1
    upper = 101    
    number = np.random.randint(lower, upper)
    count = 0
    while count < 20:
        count += 1
        number = (lower+upper)//2
	    # Вводим предполагаемый ответ
        guess = int(input("Загаданное число это: "))
	    # Проверяется условие
        if number > guess:
            print('Это число больше')
        elif number < guess:
            print('Это число меньше')
        else: 
            print("Поздравляю! Вы справились за ", count, " попыток")
            break

    
def score_game(random_predict) -> int:
    """За какое количество попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(random_predict)