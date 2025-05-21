from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

driver=webdriver.Chrome()
driver.get("https://demoqa.com/automation-practice-form")

def get_driver():
    
    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    options.add_argument("--disable-gpu")
    # options.add_argument("--headless")
    options.add_argument("--incognito")
    
    driver = webdriver.Chrome(options)
    driver.get("https://demoqa.com/automation-practice-form")
    return driver

def datos_texto_formulario(driver):
    datos : dict[str,str] = {
            "firstName": "jesus",
            "lastName": "david",
            "userEmail": "anachurycastro@gmail.com",
            "userNumber": "3112445754",
            "subjectsInput": "Maths",
            "currentAddress": "Calle 12 # 45 - 67",
}
    
    for id_pag in datos:
        texto: str = datos[id_pag]
        driver.find_element(By.ID, id_pag).send_keys(texto)
        time.sleep(3)

def seleccionar_genero(driver):
    driver.find_element(By.XPATH, "//label[text()='Male']").click()
    time.sleep(0.5)


def seleccionar_hobbies(driver):
    driver.find_element(By.XPATH, "//label[text()='Sports']").click()
    driver.find_element(By.XPATH, "//label[text()='Music']").click()
    time.sleep(0.5)
    
def seleccionar_fecha_nacimiento(driver):

    driver.find_element(By.ID, "dateOfBirthInput").click()
    time.sleep(0.5)

    driver.find_element(By.CLASS_NAME, "react-datepicker__month-select").send_keys("April")

    driver.find_element(By.CLASS_NAME, "react-datepicker__year-select").send_keys("1990")

    driver.find_element(By.XPATH, "//div[contains(@class, 'react-datepicker__day') and text()='15']").click()
    time.sleep(0.5)

def seleccionar_estado_y_ciudad(driver):

    driver.find_element(By.ID, "state").click()
    driver.find_element(By.XPATH, "//div[text()='NCR']").click()
    time.sleep(0.5)

    driver.find_element(By.ID, "city").click()
    driver.find_element(By.XPATH, "//div[text()='Colombia']").click()
    time.sleep(0.5)
    
def main():
    driver: webdriver = get_driver()
    datos_texto_formulario(driver)
    seleccionar_genero(driver)
    seleccionar_hobbies(driver)
    seleccionar_fecha_nacimiento(driver)
    seleccionar_estado_y_ciudad(driver)
    driver.find_element(By.ID, "dateOfBirthInput").click()
    driver.save_screenshot("Antes_de_enviar.png")
    driver.find_element(By.ID, "submit").submit()
    driver.save_screenshot("despues_de_enviar.png")

    time.sleep(2)
    driver.quit()
    
if __name__ == "__main__":
    main()