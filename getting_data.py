import data
import pytest

from sending_equests import post_new_order, get_by_track


def test_create_new_order():
    # Выполнить запрос на создание заказа
    respOrder = post_new_order(data.creating_an_order)

    assert respOrder.status_code == 201


def test_get_by_track():
    # Выполнить запрос на создание заказа
    respOrder = post_new_order(data.creating_an_order)

    assert respOrder.status_code == 201

    # Сохранить номер трека заказа
    track = respOrder.json()['track']

    # Выполнить запрос на получения заказа по треку заказа
    resp = get_by_track(track)

    # Проверить, что код ответа равен 200
    assert resp.status_code == 200

