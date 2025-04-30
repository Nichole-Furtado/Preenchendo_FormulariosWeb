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

##

def fill_prospect(self, prospect_build: ProspectBuilder):
    # 1️⃣ Selecionar "SOLTEIRO" ANTES de começar o preenchimento
    try:
        btn_solteiro = pyautogui.center(
            pyautogui.locateOnScreen(self._prints_estado_civil['SOLTEIRO'], confidence=0.9)
        )
        pyautogui.click(x=btn_solteiro.x, y=btn_solteiro.y)
        time.sleep(0.3)
    except Exception:
        raise MuaButtonNotFoundException(button='estado civil - SOLTEIRO')

    # 2️⃣ Agora segue o preenchimento na sequência padrão (14 TABs funcionam corretamente)
    self._fill_nome_text_field(nome=prospect_build.get_nome())
    self._fill_nome_mae_text_field(nome_mae=prospect_build.get_nome_mae())
    self._fill_nome_pai_text_field(nome_pai=prospect_build.get_nome_pai())
    self._fill_uf_text_field(uf=prospect_build.get_uf())
    self._fill_naturalidade_text_field(naturalidade=prospect_build.get_naturalidade())
    self._fill_nascimento_text_field(nascimento=prospect_build.get_nascimento())
    self._switch_sexo(sexo=prospect_build.get_sexo())
    self._fill_estado_civil_text_field(estado_civil='SOLTEIRO')  # mantido por segurança

    self._fill_tipo_documento_text_field()
    self._fill_n_documento_text_field(n_documento=prospect_build.get_n_documento())
    self._fill_uf_documento_text_field(uf=prospect_build.get_uf_documento())
    self._fill_orgao_emissor_documento_text_field(orgao_emissor=prospect_build.get_orgao_emissor_documento())
    self._fill_emissao_documento_text_field(emissao_documento=prospect_build.get_emissao_documento())
    self._click_sim_button()
    self._click_salvar_button()

    # 3️⃣ Após salvar, agora seleciona o estado civil real (ex: CASADO)
    estado_civil_real = prospect_build.get_estado_civil().upper()
    try:
        if estado_civil_real in self._prints_estado_civil:
            btn_real = pyautogui.center(
                pyautogui.locateOnScreen(self._prints_estado_civil[estado_civil_real], confidence=0.9)
            )
            pyautogui.click(x=btn_real.x, y=btn_real.y)
        else:
            raise MuaUnacceptSexoException(f"Estado civil inválido: {estado_civil_real}")
    except Exception:
        raise MuaButtonNotFoundException(button=f'estado civil - {estado_civil_real}')
