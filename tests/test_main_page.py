from data.main_page_data import MainPageData
import allure 
import pytest

class TestMainPage():
    
    @allure.title('Проверка появления текста ответа в разделе "Вопросы о важном"')
    @allure.description('Нажимаем на стрелочку рядом с вопросом, открывается текст ответа')
    @pytest.mark.parametrize('index,expected_answer', MainPageData.questions_and_answers_list)
    def test_important_questions_list (self,driver,main_page,index,expected_answer):
        main_page.click_question_button(index)
        actual_text=main_page.get_question_answer(index).text
        assert actual_text == expected_answer