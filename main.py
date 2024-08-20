# Работа на лекции

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import random
import time


browser = webdriver.Firefox()
# browser.get("https://ru.wikipedia.org/wiki/Заглавная_страница")
browser.get("https://ru.wikipedia.org/w/index.php?go=%D0%9F%D0%B5%D1%80%D0%B5%D0%B9%D1%82%D0%B8&search=%D0%A1%D0%BE%D0%BB%D0%BD%D0%B5%D1%87%D0%BD%D0%B0%D1%8F+%D1%81%D0%B8%D1%81%D1%82%D0%B5%D0%BC%D0%B0&title=%D0%A1%D0%BB%D1%83%D0%B6%D0%B5%D0%B1%D0%BD%D0%B0%D1%8F%3A%D0%9F%D0%BE%D0%B8%D1%81%D0%BA&ns0=1")

# assert "Википедия" in browser.title
# time.sleep(5)
#
# search_box = browser.find_element(By.ID, "searchInput")
# search_box.send_keys("Солнечная система")
#
# search_box.send_keys(Keys.RETURN)
#
# time.sleep(5)
# a = browser.find_element(By.LINK_TEXT, "Солнечная система")
# a.click()

paragraphs = browser.find_elements(By.TAG_NAME, "p")
#
#
for paragraph in paragraphs:
    print(paragraph.text)
    input()

# hatnotes = []
#
# for element in browser.find_elements(By.TAG_NAME, "div"):
#     cl = element.get_attribute("class")
#     if cl == "hatnote navigation-not-searchable":
#         hatnotes.append(element)
#
# print(hatnotes)
# hatnote = random.choice(hatnotes)
# link = hatnote.find_element(By.TAG_NAME, "a").get_attribute("href")
# browser.get(link)

