from selenium import webdriver
from selenium.webdriver.common.by import By

class MainPageLocators():
    first_question_button = [By.XPATH, "//*[text()='Сколько это стоит? И как оплатить?']"]
    second_question_button = [By.XPATH, "//*[text()='Хочу сразу несколько самокатов! Так можно?']"]
    third_question_button = [By.XPATH, "//*[text()='Как рассчитывается время аренды?']"]
    fourth_question_button = [By.XPATH, "//*[text()='Можно ли заказать самокат прямо на сегодня?']"]
    fifth_question_button = [By.XPATH, "//*[text()='Можно ли продлить заказ или вернуть самокат раньше?']"]
    sixth_question_button = [By.XPATH, "//*[text()='Вы привозите зарядку вместе с самокатом?']"]
    seventh_question_button = [By.XPATH, "//*[text()='Можно ли отменить заказ?']"]
    eighth_question_button = [By.XPATH, "//*[text()='Я жизу за МКАДом, привезёте?']"]
    first_question_answer = [By.XPATH, "//p[text()='Сутки — 400 рублей. Оплата курьеру — наличными или картой.']"]
    second_question_answer = [By.XPATH, "//p[text()='Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.']"]
    third_question_answer = [By.XPATH, "//p[text()='Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.']"]
    fourth_question_answer = [By.XPATH, "//p[text()='Только начиная с завтрашнего дня. Но скоро станем расторопнее.']"]
    fifth_question_answer = [By.XPATH, "//p[text()='Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.']"]
    sixth_question_answer = [By.XPATH, "//p[text()='Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.']"]
    seventh_question_answer = [By.XPATH, "//p[text()='Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.']"]
    eighth_question_answer = [By.XPATH, "//p[text()='Да, обязательно. Всем самокатов! И Москве, и Московской области.']"]