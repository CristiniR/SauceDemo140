# 1 - Bibliotecas
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

#2 Classe (Opcional)-------------------------------------------------------------------------------------------------------

class Teste_Produtos():

#2.1 Atributos--------------------------------------------------------------------------------------------------------------
   
    url = "https://www.saucedemo.com"                  # endereço site alvo

#2.2 Funções e Métodos-------------------------------------------------------------------------------------------------------

    def setup_method(self, method):                   # método de inicialização dos testes
        self.driver = webdriver.Chrome()               # instancia o objeto do Selenium webdriver como Chrome
        self.driver.implicitly_wait(10)                # define o tempo de espera padrão em 10 segundos 

    def teardown_method(self, method):                 # método de finalização dos testes
        self.driver.quit()                             # encerra / destrói o objeto do Selenium webdriver da memória

    def test_selecionar_produto(self):                 # método de teste
        self.driver.get(self.url)
        self.driver.find_element(By.ID,"user-name").send_keys("standard_user")          # escreve o login 
        self.driver.find_element(By.ID,"password").send_keys("secret_sauce")            # escreve a senha 
