import requests
import configuration
import data

def post_new_user(products_ids):
    return requests.post(configuration.URL_SERVICE + configuration.PRODUCTS_KITS_PATH,  # inserta la dirección URL completa
                         json=products_ids,
                         headers=data.headers)  # inserta los encabezados


response = post_new_user(data.product_ids)
print(response.status_code)
print(response.json())