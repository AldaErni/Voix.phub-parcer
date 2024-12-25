from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

# Настройка драйвера (например, Chrome)
driver = webdriver.Chrome()

# Переход на страницу логина
driver.get('https://phab.voix.io/maniphest/query/BEKe.bqYbKOF/?after=19888')

# Заполнение полей логина
username_input = driver.find_element(By.NAME, 'username')
password_input = driver.find_element(By.NAME, 'password')

username_input.send_keys('Aldazhar')
password_input.send_keys('331010588753k')
password_input.send_keys(Keys.RETURN)

# Ждем загрузки страницы после логина
driver.implicitly_wait(5)

# Переход на целевую страницу и получение ее исходного кода
driver.get('https://phab.voix.io/maniphest/query/BEKe.bqYbKOF/?after=19779')
page_source = driver.page_source
soup = BeautifulSoup(page_source, 'html.parser')

# Пример: Получение элементов по классу 'your-class'
elements = soup.find_all(class_='phui-oi-link')

# Отладка: Печать количества найденных элементов
print(f"Found {len(elements)} elements with class 'your-class'.")

# Если элементов нет, выведем содержимое страницы для анализа
if not elements:
    print("No elements found. Here is the page content:")
    print(soup.prettify())

# Печать текста элементов до точки
for element in elements:
    text = element.text.split('.')[1]
    print(text)

# Закрытие драйвера
driver.quit()
