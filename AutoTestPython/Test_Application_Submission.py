from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


def send_key(xpath, key, time_to_wait=10, tries=3):

    for i in range(tries):
        try:
            el = driver.find_element(by=By.XPATH, value=xpath)
            el.send_keys(key)
            driver.implicitly_wait(time_to_wait)
            return True
        except Exception:
            time.sleep(0.5)
            continue
    return False

def click_ENTER(xpath, time_to_wait=10, tries=3):

    for i in range(tries):
        try:
            el = driver.find_element(by=By.XPATH, value=xpath)
            el.send_keys(Keys.ENTER)
            driver.implicitly_wait(time_to_wait)
            return True
        except Exception:
            time.sleep(0.5)
            continue
    return False

def click(xpath, time_to_wait=10, tries=3):

    for i in range(tries):
        try:
            el = driver.find_element(by=By.XPATH, value=xpath)
            el.click()
            driver.implicitly_wait(time_to_wait)
            return True
        except Exception:
            time.sleep(0.5)
            continue
    return False

def test_assert(xpath,time_to_wait=10):

    try:
        el = driver.find_element(by=By.XPATH, value=xpath)
        el.click
        driver.implicitly_wait(time_to_wait)
        return print("201")
    except Exception:
        time.sleep(0.5)

    return print("не отправлена")

for i in range(5):
# создание веб драйвера
    driver = webdriver.Chrome()
    driver.get("https://piter-online.net/")
    driver.implicitly_wait(10)
# поисковая строка и ввод улицы:"Тестовая линия"
    step1 = send_key("/html/body/div/div/div[1]/div[4]/div[1]/div/div/div/div[2]/div/div[1]/div/div[1]/div/div/div/div/div[1]/input", "Тестовая линия")
    assert step1, "ввод имени пользователя не прошел"
# прожать Enter после ввода улицы:"Тестовая линия"
    click_ENTER("/html/body/div/div/div[1]/div[4]/div[1]/div/div/div/div[2]/div/div[1]/div/div[1]/div/div/div/div/div[1]/input")
    click_ENTER("/html/body/div/div/div[1]/div[4]/div[1]/div/div/div/div[2]/div/div[1]/div/div[1]/div/div/div/div/div[1]/input")
# ввода номера дома:"1"
    send_key("//*[@class='app152 app159 app158 app154 app172']", "1")
# прожать Enter после ввода номера дома:"1"
    send_key("//*[@class='app152 app160 app161 app159 app158 app154 app172']", Keys.ENTER)
# нажимаем на выплывающий список "В КВАРТИРУ"
    click("//*[@class='app187']")
# В выплывающем списке выбираем в офис
    click("//*[@class='app198'][2]", 10)
# прожать кнопку "Показать тарифы"
    click("//*[@class='app218 app251 app247 app242 app231 app248']", 10)
# вводим имя "Автотест"
    send_key("//*[@type='text']", "Автотест")
# вводим номер телефона "1111111111"
    send_key("//*[@type='tel']", "1111111111")
# прожимаем кнопку "Отправить заявку"
    click("//*//*[@id='root']/div/div[1]/div[4]/form/div/div/div/div[1]/div[4]/div[1]", 10)
    print(f"Тест №{i+1} завершен")
# проверка отправлена заявка"201" или нет "не отправлена"
    test_assert('//*[@id="root"]/div/div[1]/div[4]/div/div/div/div/div[1]/span')
# явное ожидание что бы убедиться в выполнении отправки заявки
    time.sleep(1)
    driver.quit()