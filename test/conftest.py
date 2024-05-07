import pytest
import random
from selenium import webdriver
from page_url import PageUrl

@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Chrome()
    driver.get(PageUrl.MAIN_PAGE_URL)
    yield driver
    driver.quit()

@pytest.fixture(scope='function')
def new_user():
    random_part = random.randint(100, 999)
    return {'name': f'igorian5{random_part}',
            'email': f'igorkoltakov5{random_part}@ya.ru',
            'password': 'test05#'}

@pytest.fixture
def not_correct_user():
    return {'name': 'igor', 'email': 'igorkoltakov5@ya.ru', 'password': 'test'}


@pytest.fixture
def registered_user():
    return {'name': 'igorian5', 'email': 'igorian5@ya.ru', 'password': 'test05'}