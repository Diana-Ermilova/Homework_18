import allure
import requests
from logger import log


BASE_URL = 'https://demowebshop.tricentis.com'
LOGIN = 'diana.ermilova.96@gmail.com'
PASSWORD = '12345678'

@allure.step("Добавление продукта {product_id} в количестве {quantity} в корзину через API")
def add_product_in_cart(product_id, quantity=1):
    url = BASE_URL + f'/addproducttocart/details/{product_id}/1'
    data = {f'addtocart_{product_id}.EnteredQuantity': quantity}
    response = requests.post(url=url, data=data, allow_redirects=False)
    log(response=response, request_body=data, allure_logging=True)
    return response

