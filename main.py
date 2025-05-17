from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#driver=webdriver.Chrome()
#driver.get("https://demoqa.com/automation-practice-form")

# Casillas de formulario
def datos_texto_plano(driver: webdriver):
    dato : dict[str, str] = {
    "firstName": "jesus",
    "lastName": "david",
    "userEmail": "anachurycastro@gmail.com",
    "userNumber": "3112445775",
    "currentAddress": "Calle 123 # 45 - 67"

}
    for id_pag in dato:
        texto: str = dato[id_pag]
        driver.find_element(By.ID, id_pag).send_keys(texto)
        time.sleep(4)


def get_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    driver = webdriver.Chrome(options)
    driver.get("https://demoqa.com/automation-practice-form")
    return driver

def main():
    driver = get_driver()
    datos_texto_plano(driver)
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