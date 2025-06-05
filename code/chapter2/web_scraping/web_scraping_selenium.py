#brew install chromedriver
#poetry add selenium

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

# Ruta al ejecutable en macOS
chromedriver_path = "/opt/homebrew/bin/chromedriver"

# Establecer la variable de entorno (opcional)
os.environ["webdriver.chrome.driver"] = chromedriver_path

# Crear el servicio y el driver
service = Service(executable_path=chromedriver_path)
driver = webdriver.Chrome(service=service)

# Prueba de navegación
url = 'https://www1.sedecatastro.gob.es/CYCBienInmueble/OVCBusqueda.aspx'
driver.get(url)
print(driver.title)
coord = driver.find_element(By.ID, "tabcoords")
print(coord.get_dom_attribute)
# Activar tab correctamente
driver.find_element(By.CSS_SELECTOR, '#tabcoords a').click()
lat = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "ctl00_Contenido_txtLatitud"))
)
lon = driver.find_element(By.ID, "ctl00_Contenido_txtLongitud")

# Ingresar coordenadas
lat.send_keys("28.2723368")
lon.send_keys("-16.6600606")
driver.find_element(By.ID, 'ctl00_Contenido_btnDatos').click()
html2 = driver.find_element(By.XPATH, "//html/body/*")
print(html2.text)
input("Presiona Enter para cerrar el navegador...")
driver.quit()