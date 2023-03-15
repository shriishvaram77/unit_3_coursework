import json
from datetime import datetime


def get_data(filename: str):
    """
    Функция получает данные из файла operations.json в корне проекта
    :param filename: operations.json
    :return: Список операций в виде списка словарей
    """
    operations = []

    with open(filename, 'rt', encoding='utf-8') as file:
        return json.load(file)


def get_filtered_data(data, filtered_empty_from=False):
    """
    Функция возвращает отфильтрованный список по ключу 'state' и 'from'
    :param data: Исходный список
    :param filtered_empty_from: ключи 'state' и 'from'
    :return: Отфильтрованный список операций
    """
    data = [x for x in data if "state" in x and x["state"] == "EXECUTED"]
    if filtered_empty_from:
        data = [x for x in data if "from" in x]
    return data


def get_last_five(data, count_last_values):
    """
    Функция возвращает отфильтрованный по дате список последних 5 транзакций
    :param data: Исходный список
    :param count_last_values: ключь 'date'
    :return: список последних 5 транзакций
    """
    data = sorted(data, key=lambda x: x["date"], reverse=True)
    return data[:count_last_values]


def get_formatted_data(data):
    """
    Функция получает список с данными операции и возвращает отформатированные данные для вывода
    :param data: словарь с данными по операции
    :return: отформатированные данные по операции - дата, описание, источник, назначение, сумма и валюта операции
    """
    formatted_data = []
    for row in data:
        date = datetime.strptime(row["date"], "%Y-%m-%dT%H:%M:%S.%f").strftime("%d.%m.%Y")
        description = row["description"]

        if "from" in row:
            sender = row["from"].split()
            sender_bill = sender.pop(-1)
            sender_bill = f"{sender_bill[:4]} {sender_bill[4:6]}** **** {sender_bill[-4:]}"
            sender_info = " ".join(sender)
        else:
            sender_bill, sender_info = "", "[HIDDEN]"

        recipient = f"-> Счет **{row['to'][-4:]}"
        amount = f"{row['operationAmount']['amount']} {row['operationAmount']['currency']['name']}"

        formatted_data.append(f"""\
{date} {description}
{sender_info} {sender_bill} {recipient}
{amount}
""")
    return formatted_data
