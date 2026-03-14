import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent))

from src.api.aeroplanes_api import AeroplanesAPI
from src.models.aeroplane import Aeroplane
from src.storage.json_saver import JSONSaver
from src.utils.helpers import filter_aeroplanes, get_top_aeroplanes, print_aeroplanes


def user_interaction():
    """Функция взаимодействия с пользователем через консоль."""

    api = AeroplanesAPI()
    saver = JSONSaver()

    try:
        country = input("Введите страну: ").strip()

        top_n = int(input("Введите количество самолетов для вывода: "))

        filter_words = input(
            "Введите страны регистрации самолетов (через пробел): "
        ).split()

        print("\nПолучаем данные из API...\n")

        data = api.get_aeroplanes(country)

        if not data:
            print("Самолеты в данном воздушном пространстве не найдены.")
            return

        aeroplanes = Aeroplane.cast_to_object_list(data)

        print(f"Найдено самолетов: {len(aeroplanes)}")

        # сохраняем данные в JSON
        for plane in aeroplanes:
            saver.add_aeroplane(plane)

        # фильтрация
        filtered = filter_aeroplanes(aeroplanes, filter_words)

        if not filtered:
            print("\nСамолеты по стране регистрации не найдены.")
            return

        # сортировка и топ
        top = get_top_aeroplanes(filtered, top_n)

        if not top:
            print("Самолеты не найдены по заданным параметрам.")
            return

        print("\nТоп самолетов по высоте:\n")

        print_aeroplanes(top)

    except ValueError:
        print("Ошибка: количество самолетов должно быть числом.")

    except Exception as e:
        print(f"Произошла ошибка: {e}")


if __name__ == "__main__":
    user_interaction()