import configuration
import data
import requests

def get_new_user_token():
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                             json=data.user_body, headers=data.headers)


def post_new_client_kit(kit_body, auth_token):
    headers = data.headers.copy()
    headers["Authorization"] = f"Bearer {auth_token}"
    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                         json=kit_body, headers=headers)

