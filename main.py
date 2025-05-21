from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

#driver=webdriver.Chrome()
#driver.get("https://demoqa.com/automation-practice-form")

OPTIONS: list[str] = [
    "--disable-extensions",
    "--disable-gpu",
    "start-maximized",
]    

def get_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    driver = webdriver.Chrome(options)
    driver.get("https://demoqa.com/automation-practice-form")
    return driver

def scroll_to_element(driver: webdriver, element):
    driver.execute_script("arguments[0].scrollIntoView();", element)
    sleep(1)







def llamar_texto_by_id(driver: webdriver, element_id: str):
    elemento = driver.find_element(By.ID, element_id)
    return elemento





def seleccionar_fecha(driver: webdriver):


    WebDriverWait(driver,10).until(
        EC.element_to_be_clickable((By.ID, "dateOfBirthInput"))
    ).click()


    
    # Selecciona el select de los a os
    driver.find_element(
        By.CLASS_NAME, "react-datepicker__year-select"
    )
    sleep(1)
    Select(year_select).select_by_value("1999")

    # Selecciona el select de los meses
    month_select: WebElement = driver.find_element(
        By.CLASS_NAME, "react-datepicker__month-select"
    )
    # Espera 1 segundo
    sleep(1)
    Select(month_select).select_by_visible_text("October")

    day_select: WebElement = driver.find_element(
        By.CLASS_NAME, "react-datepicker__day react-datepicker__day--017"
    )   
    sleep(1) 
    day_select.click()
    sleep(1)



   


    

def texto_autocompletado(driver : webdriver, element_id: str, texto: str):
    llamar_texto_by_id(driver=driver, element_id=element_id, texto=texto)
    elemento_autocomplete: WebDriverWait = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(By.XPATH, f"//div[contains(@class,' subjects-auto-complete_option') and  text()='{texto}']"))
    elemento_autocomplete.click()
    
    time.sleep(1)






# Casillas de formulario
def datos_texto_plano(driver: webdriver):
    dato : dict[str, str] = {
    "firstName": "jesus",
    "lastName": "david",
    "userEmail": "anachurycastro@gmail.com",
    "userNumber": "3112445775",
    "currentAddress": "Calle 123 # 45 - 67",
    "subjectsInput": "Matematicas",
    #"uploadPicture": "C:\Users\DELL\Desktop\\Imagen de WhatsApp 2025-04-12 a las 21.28.24_06c4dc94.jpg.",

}
    for id_pag in dato:
        texto: str = dato[id_pag]
        driver.find_element(By.ID, id_pag).send_keys(texto)
        sleep(4)





def llenar_radio_button(driver:webdriver, element_value: str):
    radio_button: WebElement = driver.find_element(
        By.XPATH, f"//label[contains(text(),'{element_value}')]"  
    )
    scroll_to_element(driver=driver, element=radio_button)
    radio_button.click()
    sleep(1)


def llenar_ciudad(driver: webdriver, state: str,city: str):
    estado: WebElement = driver.find_element( By.ID, "state")
    scroll_to_element(driver=driver, element=estado)
    estado.click()
   

    estado: WebElement = driver.find_element(By.XPATH, f"//div[contains(@id,'react-select-4-option') and contains(text(),'{state}')]")
    
    estado.click()

    estado: WebElement = driver.find_element(By.ID, "city")
    scroll_to_element(driver=driver, element=estado)
    estado.click()
   

    estado: WebElement = driver.find_element(By.XPATH, f"//div[contains(@id,'react-select-3-option') and contains(text(),'{city}')]")
    
    estado.click()
def enviar_formulario(driver: webdriver):
    submit_button = driver.find_element(By.ID, "submit")
    scroll_to_element(driver=driver, element=submit_button)
    submit_button.click()
    sleep(1)

def main():

    driver = get_driver()
    datos_texto_plano(driver=driver) 
    sleep(3)
    for subject in ["Matematicas", "Ingles", "Fisica"]:
        texto_autocompletado(driver=driver, element_id="subjectsInput", texto=subject)
    
        sleep(1)

    seleccionar_fecha(driver=driver)
    llenar_ciudad(driver=driver, state="NCR", city="Delhi")#llena el estado y la ciudad
    llenar_radio_button(driver=driver, element_value="Male")  # Replace "Male" with the desired value
    sleep(1)  







    driver.save_screenshot("antes de enviar.png")#tomar capture antess de enviar
    driver.find_element(By.ID, "submit").submit()#enviar formulario}
    driver.save_screenshot("despues de enviar.png")#tomar capture despues de enviar
    sleep(5)
    driver.quit()


if __name__ == "__main__":
    main()
    
    
   # driver.quit()   





    
#time.sleep(3)
#driver.quit()