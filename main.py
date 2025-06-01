from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def get_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    options.add_argument("--disable-gpu")
    # options.add_argument("--headless")
    options.add_argument("--incognito")

    driver = webdriver.Chrome(options=options)
    driver.get("https://demoqa.com/automation-practice-form")
    return driver

def llenar_formulario(driver):
    datos: dict[str, str] = {
        "firstName": "jesus",
        "lastName": "david",
        "userEmail": "anachurycastro2001@gmail.com",
        "userNumber": "3112445775",
        "subjectsInput": "Maths",
        "uploadPicture": "/home/andres/Descargas/wp2975191.jpg",
        "currentAddress": "Calle 138 # 27 - 67",
    }

    for campo_id, valor in datos.items():
        driver.find_element(By.ID, campo_id).send_keys(valor)
        time.sleep(1)
        
    subjects = driver.find_element(By.ID, "subjectsInput")
    subjects.send_keys("Maths")
    subjects.send_keys(Keys.ENTER)
    time.sleep(1)

def seleccionar_el_genero(driver):
    driver.find_element(By.XPATH, "//label[text()='Male']").click()
    time.sleep(0.5)

def seleccionar_hobbies(driver):
    driver.find_element(By.XPATH, "//label[text()='Sports']").click()
    driver.find_element(By.XPATH, "//label[text()='Music']").click()
    time.sleep(0.5)

def fecha_nacimiento(driver):
    driver.find_element(By.ID, "dateOfBirthInput").click()
    time.sleep(0.5)
    driver.find_element(By.CLASS_NAME, "react-datepicker__month-select").send_keys("November")
    driver.find_element(By.CLASS_NAME, "react-datepicker__year-select").send_keys("1999")
    driver.find_element(By.XPATH, "//div[contains(@class, 'react-datepicker__day') and text()='15']").click()
    time.sleep(0.5)
    
def imagen(driver):
        driver.find_element(By.ID, "uploadPicture").send_keys("/home/andres/Descargas/wp2975191.jpg")
        time.sleep(1)

def seleccionar_estado_y_ciudad(driver):
    driver.find_element(By.ID, "state").click()
    driver.find_element(By.XPATH, "//div[text()='NCR']").click()
    time.sleep(0.5)
    driver.find_element(By.ID, "city").click()
    driver.find_element(By.XPATH, "//div[text()='Delhi']").click() 
    time.sleep(0.5)

def enviar_formulario(driver):
    driver.find_element(By.ID, "submit").click()
    time.sleep(2)
    driver.save_screenshot("despues_de_enviar.png")
    
    
def main():
    driver = get_driver()
    llenar_formulario(driver)
    seleccionar_el_genero(driver)
    seleccionar_hobbies(driver)
    fecha_nacimiento(driver)
    seleccionar_estado_y_ciudad(driver)
    imagen(driver)
    driver.find_element(By.ID, "enviar").click()
    driver.save_screenshot("antes_de_enviar.png")
    enviar_formulario(driver)
    driver.save_screenshot("despues_de_enviar.png")
    driver.quit()

if __name__ == "__main__":
    main()