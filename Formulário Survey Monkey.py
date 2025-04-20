from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver as opcoes
from selenium.webdriver.common.by import By
import pyautogui as espera
from selenium.webdriver.support.select import Select

navegador = opcoes.Chrome()

navegador.get("https://pt.surveymonkey.com/r/7GX9XRZ")
espera.sleep(3)

navegador.find_element(By.NAME, "72542598").send_keys("Nichole")
espera.sleep(3)

navegador.find_element(By.NAME, "72542821").send_keys("nichole@gmail.com")
espera.sleep(5)

navegador.find_element(By.XPATH,'//*[@id="question-field-72542994"]/div/fieldset/div/div/div/div[2]/label/span[1]').click()

espera.sleep(3)

pegaDropdown = navegador.find_element(By.XPATH, '//*[@id="question-field-72543178"]/div/fieldset/div/select')
itemSelecionado = Select(pegaDropdown)
itemSelecionado.select_by_index(1)
espera.sleep(3)

navegador.find_element(By.XPATH, '//*[@id="view-pageNavigation"]/div/button').click()