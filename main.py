from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.wait import WebDriverWait
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.webdriver import WebDriver

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
    time.sleep(1)


def llamar_texto_by_id(driver: webdriver, element_id: str):
    elemento = driver.find_element(By.ID, element_id)
    return elemento





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
    "uploadPicture": "C:\\Users\\jesus\\Pictures\\Captura.png",

}
    for id_pag in dato:
        texto: str = dato[id_pag]
        driver.find_element(By.ID, id_pag).send_keys(texto)
        time.sleep(4)



def main():
    driver = get_driver()
    datos_texto_plano(driver=driver) 
    time.sleep(3)
    for subject in ["Matematicas", "Ingles", "Fisica"]:
        texto_autocompletado(driver=driver, element_id="subjectsInput", texto=subject)
        time.sleep(1)

    driver.save_screenshot("antes de enviar.png")#tomar capture antess de enviar

    driver.find_element(By.ID, "submit").submit()#enviar formulario}
    driver.save_screenshot("despues de enviar.png")#tomar capture despues de enviar
    time.sleep(5)
    driver.quit()


if __name__ == "__main__":
    main()
    
    
   # driver.quit()   





    
#time.sleep(3)
#driver.quit()