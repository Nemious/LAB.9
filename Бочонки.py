import random
import logging

logging.basicConfig(filename='barrel_game.log', level=logging.INFO, format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')

def main():
    N = int(input("Введите количество бочонков N: "))
    logging.info(f"Начинаем игру с {N} бочонками")

    if N <= 0:
        logging.error("Число бочонков должно быть натуральным числом.")
        print("Число бочонков должно быть натуральным числом.")
        return

    barrel_sequence = list(range(1, N + 1))
    random.shuffle(barrel_sequence)  # перемешиваем порядок бочонков

    print("Нажмите любую клавишу для вытягивания бочонка или 'q' для выхода.")
    pulled_barrels = []

    while True:
        user_input = input()
        if user_input == 'q':
            logging.info("Игра завершена")
            break
        if not barrel_sequence:
            print("Бочонки закончились!")
            logging.warning("Бочонки закончились")
            break
        random_barrel = barrel_sequence.pop()  # берем бочонок из конца списка
        pulled_barrels.append(random_barrel)  # добавляем бочонок в список вытянутых
        print("Вытянут бочонок под номером:", random_barrel)
        logging.info(f"Выпал бочонок под номером: {random_barrel}")

    print("Последовательность вытянутых бочонков:", pulled_barrels)  # вывод последовательности вытянутых бочонков

if __name__ == "__main__":
    main()