import sender_stand_request
import data
import pytest

def get_kit_body(name):
    current_body = data.kit_bodies[0].copy()
    current_body["name"] = name
    return current_body

def positive_assert(kit_body, auth_token):
    response = sender_stand_request.post_new_client_kit(kit_body,auth_token)
    assert response.status_code == 201
    assert response.json()["name"] == kit_body["name"]

def negative_assert_code_400(kit_body, auth_token):
    response = sender_stand_request.post_new_client_kit(kit_body, auth_token)
    assert response.status_code == 400
    assert response.json()["code"] == 400
    assert response.json()["message"] == "No se han aprobado todos los parámetros requeridos"

@pytest.fixture(scope="module")
def auth_token():
    return sender_stand_request.get_new_user_token()

#Prueba 1
def test_create_kit_name_1_char(auth_token):
    kit_body = data.kit_bodies[1]
    positive_assert(kit_body, auth_token)

#Prueba 2
def test_create_kit_name_511_chars(auth_token):
    kit_body = data.kit_bodies[2]
    positive_assert(kit_body,auth_token)

#Prueba 3
def test_create_kit_name_0_chars(auth_token):
    kit_body = data.kit_bodies[3]
    negative_assert_code_400(kit_body, auth_token)

#Prueba 4
def test_create_kit_name_512_chars(auth_token):
    kit_body = data.kit_bodies[4]
    negative_assert_code_400(kit_body, auth_token)

#Prueba 5
def test_create_kit_name_special_chars(auth_token):
    kit_body = data.kit_bodies[5]
    positive_assert(kit_body, auth_token)

#Prueba 6
def test_create_kit_name_with_spaces(auth_token):
    kit_body = data.kit_bodies[6]
    positive_assert(kit_body, auth_token)

#Prueba 7
def test_create_kit_name_with_numbers(auth_token):
    kit_body = data.kit_bodies[7]
    positive_assert(kit_body, auth_token)

#Prueba 8
def test_create_kit_no_name(auth_token):
    kit_body = data.kit_bodies[8]
    negative_assert_code_400(kit_body, auth_token)

#Prueba 9
def test_create_kit_name_number(auth_token):
    kit_body = data.kit_bodies[9]
    negative_assert_code_400(kit_body, auth_token)