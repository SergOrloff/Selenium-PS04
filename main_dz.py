from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import random
import time

def perform_action(browser):
    print("\nВыберите действие:")
    print("1. Листать параграфы текущей статьи")
    print("2. Перейти на одну из связанных страниц")
    print("3. Выйти из программы")

    choice = input("Введите номер действия: ")

    if choice == "1":
        paragraphs = browser.find_elements(By.TAG_NAME, "p")
        for paragraph in paragraphs:
            print(paragraph.text)
            input("Нажмите Enter для перехода к следующему параграфу...")
        perform_action(browser)  # Повторный вызов для выбора действия после прокрутки
    elif choice == "2":
        hatnotes = []

        for element in browser.find_elements(By.TAG_NAME, "div"):
            cl = element.get_attribute("class")
            if cl == "hatnote navigation-not-searchable":
                hatnotes.append(element)

        if hatnotes:
            hatnote = random.choice(hatnotes)
            link = hatnote.find_element(By.TAG_NAME, "a").get_attribute("href")
            browser.get(link)
            time.sleep(5)  # Ожидание загрузки новой страницы
            perform_action(browser)  # Повторный вызов для выбора действия после перехода
        else:
            print("Связанные страницы не найдены.")
            perform_action(browser)  # Повторный вызов при отсутствии связанных страниц
    elif choice == "3":
        browser.quit()
    else:
        print("Неверный выбор.")
        perform_action(browser)  # Повторный вызов при неверном выборе

query = input("Введите запрос для поиска на Википедии: ")
browser = webdriver.Firefox()
browser.get("https://ru.wikipedia.org/wiki/Заглавная_страница")

search_box = browser.find_element(By.ID, "searchInput")
search_box.send_keys(query)
search_box.send_keys(Keys.RETURN)

time.sleep(5)

try:
    a = browser.find_element(By.PARTIAL_LINK_TEXT, query)
    a.click()
except Exception as e:
    print(f"Ошибка при переходе по ссылке: {e}")
    browser.quit()
    exit()

perform_action(browser)