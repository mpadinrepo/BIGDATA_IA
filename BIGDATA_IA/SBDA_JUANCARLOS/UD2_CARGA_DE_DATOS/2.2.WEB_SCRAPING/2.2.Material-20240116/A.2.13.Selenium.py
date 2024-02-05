# ASPECTOS IMPORTANTES A TENER EN CUENTA
#
# A. Después de bastantes intentos los scripts con selenium en Jupyterlab dan problemas con los drivers, sean con geckodriver o con chromedriver. 
# Hay un problema con Selenium4 que parece ser ya se ha reportado
#
# B. No nos olvidemos de instalar selenium en la máquina local (cmd)  ==>  c:>pip install selenium 
#
# C. Fijaos que hay que descargar el geckodriver y situarlo en la misma carpeta donde está el script, para evitar problemas de rutas ==> gecko_driver_path = "/home/joyan/work/geckodriver" 
#
# D. La opción fue reescribirlo como fichero .py (python puro) usando el contenedor docker y jupyterlab. Recordad lo explicado con Scrapy
# 
# E.  Una vez que lo tienes instalado el driver y el código escrito, ya puedes ejecutarlo y debería funcionar sin problema. Se mostrar la web del catastro, y en CMD los print.

#  SUBO ESTE FICHERO AL ALMACEN


from selenium import webdriver
from selenium.webdriver.common.by import By

# Ruta  GeckoDriver ejecutable (hay que descargarlo) ==> https://github.com/mozilla/geckodriver/releases    
gecko_driver_path = "/home/joyan/work/geckodriver"

# Instancias las opciones de firefox que son un conjunto de opciones y configuraciones específicas para el navegador Firefox. Probablemente no habrá que toquetear
firefox_options = webdriver.FirefoxOptions()

# E instanciamos un driver o el nobmre que le quieras dar... lanzará la ventana de firefox
driver = webdriver.Firefox(options=firefox_options)

# Cargamos la web
url = 'https://www1.sedecatastro.gob.es/CYCBienInmueble/OVCBusqueda.aspx'
driver.get(url)

# Así se situa en las cajas de coordenadas clickeando en el link de coordenadas
driver.find_element(By.LINK_TEXT, "COORDENADAS").click()

# Busca una localización, la que sea
driver.find_element(By.ID, "ctl00_Contenido_txtLatitud").send_keys("41.545639")
driver.find_element(By.ID, "ctl00_Contenido_txtLongitud").send_keys("1.893817")

# Clickea el botón de busqueda
driver.find_element(By.ID, "ctl00_Contenido_btnDatos").click()

# Busca los resultados que serán un label
reference = driver.find_element(By.XPATH, "//*[span/text()='Referencia catastral']//label").text
usage = driver.find_element(By.XPATH, "//*[span/text()='Uso principal']//label").text

print("Referencia catastral:", reference)
print("Uso principal:", usage)

# Cerrar el navegador si es neceario.
#driver.quit()

input("Presione una tecla para continuar...")

#   ALGUNAS OPCIONES
#   Texto de la página
html = driver.find_element(By.XPATH,"/html")
print(html.text)

input("Presione una tecla para continuar...")

# elemento hijos
hijos = driver.find_elements(By.XPATH,"/html/body/*")
for element in hijos:
  print(element.tag_name)


input("Presione una tecla para continuar...")

# insertar textos

id = "ctl00_Contenido_tblInmueble"
div = driver.find_element(By.ID,id)
label = div.find_element(By.XPATH,"//label")
print(label.text)
