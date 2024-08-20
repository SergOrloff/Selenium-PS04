from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import time

# geckodriver_path = "/geckodriver"

def perform_action(browser):
    """
    Функция для выполнения действий на странице Википедии.
    """
    while True:
        print("\nВыберите действие:")
        print("1. Листать параграфы текущей статьи")
        print("2. Перейти на одну из связанных страниц")
        print("3. Выйти из программы")

        choice = input("Введите номер действия: ")

        if choice == "1":
            # Получаем все параграфы статьи
            paragraphs = browser.find_elements(By.TAG_NAME, "p")
            for paragraph in paragraphs:
                print(paragraph.text)
                input("Нажмите Enter для перехода к следующему параграфу...")
            continue  # Возвращаемся к выбору действия после прокрутки
        elif choice == "2":
            hatnotes = []

            # Ищем элементы, которые содержат связанные страницы
            for element in browser.find_elements(By.TAG_NAME, "div"):
                cl = element.get_attribute("class")
                if cl == "hatnote navigation-not-searchable":
                    hatnotes.append(element)

            if hatnotes:
                # Переходим на случайную связанную страницу
                hatnote = random.choice(hatnotes)
                link = hatnote.find_element(By.TAG_NAME, "a").get_attribute("href")
                browser.get(link)
                WebDriverWait(browser, 10).until(
                    EC.presence_of_element_located((By.TAG_NAME, "p")))  # Ожидание загрузки новой страницы
                continue  # Возвращаемся к выбору действия после перехода
            else:
                print("Связанные страницы не найдены.")
                continue  # Возвращаемся к выбору действия, если страницы нет
        elif choice == "3":
            browser.quit()
            break  # Завершаем цикл и программу
        else:
            print("Неверный выбор.")
            continue  # Повторный выбор действия при неверном вводе


def main():
    query = input("Введите запрос для поиска на Википедии: ")
    service = FirefoxService()  # Стартуем сервис для Firefox
    browser = webdriver.Firefox(service=service)

    try:
        # Переходим на главную страницу Википедии
        browser.get("https://ru.wikipedia.org/wiki/Заглавная_страница")

        # Находим поле поиска и вводим запрос
        search_box = browser.find_element(By.ID, "searchInput")
        search_box.send_keys(query)
        search_box.send_keys(Keys.RETURN)

        # Ожидаем загрузки страницы результатов
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, query)))

        # Переход на страницу найденной статьи
        a = browser.find_element(By.PARTIAL_LINK_TEXT, query)
        a.click()

        # Выполнение действий на странице
        perform_action(browser)
    except Exception as e:
        print(f"Ошибка: {e}")
        browser.quit()


if __name__ == "__main__":
    main()