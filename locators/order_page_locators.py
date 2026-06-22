from selenium import webdriver
from selenium.webdriver.common.by import By

class OrderPageLocators():
    name_field = [By.XPATH,"//input[@placeholder='* Имя']"]
    surname_field = [By.XPATH,"//input[@placeholder='* Фамилия']"]
    address_field = [By.XPATH,"//input[@placeholder='* Адрес: куда привезти заказ']"]
    station_field = [By.XPATH,"//input[@placeholder='* Станция метро']"]
    phone_field = [By.XPATH,"//input[@placeholder='* Телефон: на него позвонит курьер']"]
    forward_button = [By.XPATH, "//button[text()='Далее']"]
    second_order_header = [By.XPATH,".//div[text()='Про аренду']"]
    order_date_field = [By.XPATH,"//input[@placeholder='* Когда привезти самокат']"]
    order_duration_field = [By.XPATH, "//div[contains(text(), 'Срок аренды')]"]
    one_day_duration = [By.XPATH,".//div[text()='сутки']"]
    scooter_colour_field = [By.XPATH,".//div[text()='Цвет самоката']"]
    black_colour = [By.ID, 'black']
    comment_field = [By.XPATH,"//input[@placeholder='Комментарий для курьера']"]
    return_button = [By.XPATH, "//button[text()='Назад']"]
    order_button = [By.XPATH, "//div[contains(@class, 'Order_Buttons')]//button[text()='Заказать']"]
    yes_button = [By.XPATH, "//button[text()='Да']"]
    no_button = [By.XPATH, "//button[text()='Нет']"]
    watch_status_button = [By.XPATH, "//button[text()='Посмотреть статус']"]