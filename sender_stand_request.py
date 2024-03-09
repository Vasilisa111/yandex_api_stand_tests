# Импорт необходимых модулей и данных для запроса
import requests
import configuration
import data


def post_new_user(body):
    return requests.post(url=configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)


def post_new_client_kit(body, headers):
    return requests.post(url=configuration.URL_SERVICE + configuration.CREATE_USERS_KIT_PATH,
                         json=body,
                         headers=headers)
