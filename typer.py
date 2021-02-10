import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

type_url = 'http://play.typeracer.com'
wait = WebDriverWait(driver, 10)

driver.get(type_url)
start_race = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Enter a Typing Race')))
start_race.click()


time_count = -1
while time_count != ":00":
    try:
        time_now = wait.until(EC.visibility_of_all_elements_located((By.XPATH, '//span[@class="time"]')))[1].text
    except IndexError:
        continue
    if time_now != time_count:
        time_count = time_now
        print(time_count)

    time.sleep(0.1)

time.sleep(1)
print("GO")

texts = wait.until(EC.visibility_of_all_elements_located((By.XPATH, '//span[@unselectable="on"]')))
rest_of_word = texts[1].text
rest_of_everything = texts[2].text
input_keys = driver.find_element_by_class_name('txtInput')
input_keys.send_keys(texts[0].text)
for letter in rest_of_word:
    input_keys = driver.find_element_by_class_name('txtInput')
    input_keys.send_keys(letter)

input_keys = driver.find_element_by_class_name('txtInput')
input_keys.send_keys(Keys.SPACE)

for letter in rest_of_everything:
    input_keys = driver.find_element_by_class_name('txtInput')
    if letter != ' ':
        input_keys.send_keys(letter)
    else:
        input_keys.send_keys(Keys.SPACE)

print("DONE")



