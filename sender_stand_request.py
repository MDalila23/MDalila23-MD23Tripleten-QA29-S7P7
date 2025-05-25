from http.client import responses


import configuration #asdfasdfasdfasd
import requests # asdfasdfasdf
import data

#Realiza la solicitud
def get_docs():
    return requests.get(configuration.URL_SERVICE + configuration.DOC_PATH)

def get_logs():
    return requests.get(configuration.URL_SERVICE + configuration.LOG_MAIN_PATH,params={"count":20})

def get_users_table():
    return requests.get(configuration.URL_SERVICE + configuration.USERS_TABLE_PATH)

def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,  # inserta la dirección URL completa
                         json=body,  # inserta el cuerpo de solicitud
                         headers=data.headers)  # inserta los encabezados



# muestra el código de estado de la respuesta
# response = get_docs()
# print(response.status_code)
#
# #response = get_logs()
# #print(response.status_code)
# #print(response.headers)

#response = get_users_table()
#print(response.status_code)

#response = post_new_user(data.user_body)
#print(response.status_code)
#print(response.json())