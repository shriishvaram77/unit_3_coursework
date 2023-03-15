import os
from utils import get_data, get_filtered_data, get_last_five, get_formatted_data


def main():
    """
    Функция получает список транзакций, фильтрует их по дате и выводит в список последние 5 в заданном формате
    :return: список последние 5 в заданном формате
    """
    count_last_values = 5
    filtered_empty_from = True

    OPERATION_DIR = os.path.abspath(os.path.dirname(__file__))
    data_file = os.path.join(OPERATION_DIR, 'operations.json')
    
    # проверяет, если данные полученны и выдает предупреждение
    data = get_data(data_file)
    if not data:
        print("WARNING: No data was retrieved!")
    print("INFO: Data retrieved successfully!", end="\n\n")
    
    #выводит в список последние 5 в заданном формате
    data_filtered = get_filtered_data(data, filtered_empty_from)
    data_five = get_last_five(data_filtered, count_last_values)
    data_formatted = get_formatted_data(data_five)
    for row in data_formatted:
        print(row)


if __name__ == "__main__":
    main()
