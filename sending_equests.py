import configuration
import requests


# Создание нового заказа
def post_new_order(creating_an_order):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
                         json=creating_an_order)


# Получения заказа по треку заказа
def get_by_track(track):
    return requests.get(configuration.URL_SERVICE + configuration.GET_BY_TRACK + f'{track}')