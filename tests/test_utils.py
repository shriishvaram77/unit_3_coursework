import json

import pytest

from utils import get_data, get_filtered_data, get_last_five, get_formatted_data


def test_get_data():
    """
    Функция тестирует ошибку, если фаил не имеет данных, если фаил имеет пустой список и еслы в списке только одна транзакция
    :param test_data: тестовые файлы - empty_list.json, bad.json, one_transfer.json
    :return: pass/fail
    """

    empty_data = get_data("mocks/empty_list.json")
    assert empty_data == []

    with pytest.raises(json.JSONDecodeError):
        get_data("mocks/bad.json")


    one_transfer = get_data("mocks/one_transfer.json")
    assert type(one_transfer) == list
    assert type(one_transfer[0]) == dict


def test_get_filtered_data(test_data):
    """
    Функция проверяет фильтрацию данных
    :param test_data: тестовый список
    :return: pass/fail
    """
    assert len(get_filtered_data(test_data)) == 3
    assert len(get_filtered_data(test_data, filtered_empty_from=True)) == 2


def test_get_last_five(test_data):
    """
    Функция тестирует колличество транзакций
    :param test_data:
    :return: pass/fail
    """
    data = get_last_five(test_data, count_last_values=2)
    assert data[0]["date"] == "2019-08-26T10:50:58.294041"
    assert len(data) == 2


def test_get_formatted_data(test_data):
    """
    Функция тестирует формат данных
    :param test_data: список данных
    :return: pass/fail
    """
    data = get_formatted_data(test_data[:1])
    assert data == ['26.08.2019 Перевод организации\nMaestro 1596 83** **** 5199 -> Счет **9589\n31957.58 руб.\n']
    data = get_formatted_data(test_data[1:2])
    assert data == ['03.07.2019 Перевод организации\n[HIDDEN]  -> Счет **5560\n8221.37 USD\n']
