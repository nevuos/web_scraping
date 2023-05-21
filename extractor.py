import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def extrair_dados_vivareal(url):
    chrome_service = ChromeService(executable_path='C:/webdriver/chromedriver.exe') # Substitua pelo caminho do ChromeDriver em seu computador
    driver = webdriver.Chrome(service=chrome_service)

    driver.get(url)

    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "property-card__content"))
    )

    imoveis = driver.find_elements(By.CLASS_NAME, "property-card__content")
    data = []

    for imovel in imoveis:
        try:
            tipo = imovel.find_element(By.CLASS_NAME, "property-card__title").text.strip()
        except:
            tipo = ""

        try:
            localizacao = imovel.find_element(By.CLASS_NAME, "property-card__address").text.strip()
        except:
            localizacao = ""

        try:
            area = imovel.find_element(By.CLASS_NAME, "property-card__detail-value--area").text.strip()
        except:
            area = ""

        try:
            vagas = imovel.find_element(By.CLASS_NAME, "property-card__detail-garage").text.strip()
        except:
            vagas = ""

        try:
            aluguel = imovel.find_element(By.CLASS_NAME, "property-card__price").text.strip()
        except:
            aluguel = ""

        data.append({"tipo": tipo,
                    "localizacao": localizacao,
                    "area": area,
                    "vagas": vagas,
                    "aluguel": aluguel})
    driver.quit()

    return data
