# create_user_test.py

import sender_stand_request
import data

def get_user_body(first_name):
    current_body = data.user_body.copy()
    current_body["firstName"] = first_name
    return current_body



# Función de prueba positiva
def positive_assert(first_name):
    # El cuerpo de la solicitud actualizada se guarda en la variable user_body
    user_body = get_user_body(first_name)
    # El resultado de la solicitud para crear un/a nuevo/a usuario/a se guarda en la variable user_response
    user_response = sender_stand_request.post_new_user(user_body)

    # Comprueba si el código de estado es 201
    assert user_response.status_code == 201
    # Comprueba que el campo authToken está en la respuesta y contiene un valor
    assert user_response.json()["authToken"] != ""

    # El resultado de la solicitud de recepción de datos de la tabla "user_model" se guarda en la variable "users_table_response"
    users_table_response = sender_stand_request.get_users_table()

    # String que debe estar en el cuerpo de respuesta
    str_user = user_body["firstName"] + "," + user_body["phone"] + "," \
               + user_body["address"] + ",,," + user_response.json()["authToken"]

    # Comprueba si el usuario o usuaria existe y es único/a
    assert users_table_response.text.count(str_user) == 1

    print(user_response.status_code)
    print(user_response.json()["authToken"] )
    print(users_table_response.text)



def negative_assert_symbol(first_name):
    # El cuerpo de la solicitud actualizada se guarda en la variable user_body
    user_body = get_user_body(first_name)
    # El resultado de la solicitud para crear un/a nuevo/a usuario/a se guarda en la variable user_response
    response = sender_stand_request.post_new_user(user_body)
    print(response.status_code)
    print(response.json()["code"])
    print(response.json()["message"])

    assert response.status_code == 400
    assert response.json()["code"] == 400
    assert response.json()["message"] == "Has introducido un nombre de usuario no válido. El nombre solo puede contener letras del alfabeto latino, la longitud debe ser de 2 a 15 caracteres."

def negative_assert_no_firstname(user_body):
    # Guarda el resultado de llamar a la función a la variable "response"
    response = sender_stand_request.post_new_user(user_body)

    print(response.status_code)
    print(response.json()["code"])
    print(response.json()["message"])

    # Comprueba si la respuesta contiene el código 400
    assert response.status_code == 400

    # Comprueba si el atributo "code" en el cuerpo de respuesta es 400
    assert response.json()["code"] == 400

    # Comprueba si el atributo "message" en el cuerpo de respuesta se ve así:
    assert response.json()["message"] == "No se enviaron todos los parámetros requeridos"

def test_create_user_1_letter_in_first_name_get_error_response():
    negative_assert_symbol("a")

def test_create_user_2_letter_in_first_name_get_success_response():
    positive_assert("Aa")

def test_create_user_15_letter_in_first_name_get_success_response():
    positive_assert("Aaaaaaaaaaaaaaa")

def test_create_user_16_letter_in_first_name_get_error_response():
    negative_assert_symbol("Aaaaaaaaaaaaaaaa")

def test_create_user_has_space_in_first_name_get_error_response():
    negative_assert_symbol("A Aaa")

def test_create_user_has_special_symbol_in_first_name_get_error_response():
    negative_assert_symbol("№%@")

def test_create_user_has_number_in_first_name_get_error_response():
    negative_assert_symbol("123")

def test_create_user_no_first_name_get_error_response():
    # El diccionario con el cuerpo de la solicitud se copia del archivo "data" a la variable "user_body"
    # De lo contrario, se podrían perder los datos del diccionario de origen
    user_body = data.user_body.copy()
    # El parámetro "firstName" se elimina de la solicitud
    user_body.pop("firstName")
    # Comprueba la respuesta
    negative_assert_no_firstname(user_body)

def test_create_user_empty_first_name_get_error_response():
    negative_assert_symbol("")


def test_create_user_number_type_first_name_get_error_response():
    negative_assert_symbol(12)


#test_create_user_1_letter_in_first_name_get_error_response()
#test_create_user_2_letter_in_first_name_get_success_response()
#test_create_user_15_letter_in_first_name_get_success_response()
#test_create_user_16_letter_in_first_name_get_error_response()
#test_create_user_has_space_in_first_name_get_error_response()
#test_create_user_has_special_symbol_in_first_name_get_error_response()
#test_create_user_has_number_in_first_name_get_error_response()
#test_create_user_no_first_name_get_error_response()
#test_create_user_empty_first_name_get_error_response()
test_create_user_number_type_first_name_get_error_response()
