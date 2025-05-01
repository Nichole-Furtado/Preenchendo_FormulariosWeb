from selenium import webdriver as opcoes
from selenium.webdriver.common.by import By
import pyautogui as espera

from selenium.webdriver.support.select import Select


navegador = opcoes.Chrome()

navegador.get("https://form.jotform.com/221436066464051")


navegador.find_element(By.ID, "first_3").send_keys("Nichole")

navegador.find_element(By.ID, "last_3").send_keys("Furtado")

navegador.find_element(By.NAME, "q4_email").send_keys("nichole@gmail.com")


dropdrown = navegador.find_element(By.ID, "input_5")
selecionar_item = Select(dropdrown)
selecionar_item.select_by_index(2)#selecionar index, escolha
espera.sleep(3)

navegador.find_element(By.ID, "label_input_6_0").click()

navegador.find_element(By.ID, "label_input_7_0").click()

navegador.find_element(By.XPATH, '//*[@id="input_8"]/div[5]').click()

navegador.find_element(By.ID, "input_9_0_3").click()
espera.sleep(3)

navegador.find_element(By.ID, "input_9_1_3").click()

navegador.find_element(By.ID, "input_9_1_3").click()

navegador.find_element(By.ID, "input_2").click()
espera.sleep(5)

