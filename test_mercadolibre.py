import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import allure


@pytest.fixture
def setup():
    driver = webdriver.Edge()
    yield driver
    driver.quit()

@allure.title("Prueba de busqueda de productos en MercadoLibre")
def initial_time_configurations(driver):
    """Configura el tiempo de espera explícito para los elementos en la página"""
    wait = WebDriverWait(driver, 10)
    return wait

@allure.step("Navegacion inicial a MercadoLibre")
def initial_navegation(driver):
    """Navega a la página principal de MercadoLibre"""
    driver.get("https://www.mercadolibre.com")
    allure.attach(driver.get_screenshot_as_png(), name="Navegacion inicial", attachment_type=allure.attachment_type.PNG)

@allure.step("Seleccionamos el pais")
def select_country(driver, wait, country):
    """Selecciona el país específico en la página de inicio"""
    country_selector = wait.until(EC.element_to_be_clickable((By.ID, country)))
    country_selector.click()
    allure.attach(driver.get_screenshot_as_png(), name="Seleccionar pais", attachment_type=allure.attachment_type.PNG)

@allure.step("Buscar un articulo")
def search_item(driver, item, wait):
    """Busca el artículo especificado en la barra de búsqueda"""
    search_box = wait.until(EC.presence_of_element_located((By.NAME, "as_word")))
    search_box.send_keys(item)
    search_box.send_keys(Keys.RETURN)
    allure.attach(driver.get_screenshot_as_png(), name="Buscar articulo", attachment_type=allure.attachment_type.PNG)

@allure.step("Aplicar filtro 'Nuevo'")
def apply_new_filter(driver, wait):
    """Aplica el filtro de condición 'Nuevo'"""
    new_condition_filter = wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "Nuevo")))
    # Usamos JavaScript para forzar un clic
    driver.execute_script("arguments[0].click();", new_condition_filter)
    allure.attach(driver.get_screenshot_as_png(), name="Filtro 'Nuevo'", attachment_type=allure.attachment_type.PNG)

@allure.step("Seleccionar ubicaci0n")
def select_state(driver, wait, state):
    """Selecciona la ubicación especificada"""
    location_filter = wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, state)))
    # Usamos JavaScript para forzar un clic
    driver.execute_script("arguments[0].click();", location_filter)
    allure.attach(driver.get_screenshot_as_png(), name="Seleccionar ubicacion",attachment_type=allure.attachment_type.PNG)

@allure.step("Ordenar de mayor a menor precio")
def sort_highest_to_lowest(driver, wait):
    """Ordena los resultados de mayor a menor precio"""
    time.sleep(1)
    sort_menu = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "andes-dropdown__trigger")))
    driver.execute_script("arguments[0].click();", sort_menu)
    # Esperamos que la opción "Mayor a Menor" esté visible y clickeable
    highest_to_lowest = wait.until(EC.element_to_be_clickable((By.ID, ":R2m55ee:-menu-list-option-price_desc")))
    driver.execute_script("arguments[0].click();", highest_to_lowest)
    allure.attach(driver.get_screenshot_as_png(), name="Ordenar precio", attachment_type=allure.attachment_type.PNG)

@allure.step("Obtener los primeros 5 artículos")
def first_5_items(driver):
    """Obtiene los nombres y precios de los primeros 5 productos"""
    products = driver.find_elements(By.CSS_SELECTOR,
                                    "ol.ui-search-layout.ui-search-layout--stack.shops__layout li.ui-search-layout__item.shops__layout-item")[
               :5]
    for product in products:
        # Obtenemos el nombre del producto
        name_product = product.find_element(By.TAG_NAME, "a").text
        # Obtenemos     el precio del producto a partir del atributo 'aria-label'
        price_element = product.find_element(By.CSS_SELECTOR, "span.andes-money-amount")
        price = price_element.get_attribute("aria-label") if price_element else "No disponible"
        print(f"Producto: {name_product} - Precio: {price}")
        # Adjuntamos los resultados como una captura
        allure.attach(driver.get_screenshot_as_png(), name=f"Producto: {name_product}",
                      attachment_type=allure.attachment_type.PNG)

def close_driver(driver):
    # Cerramos el navegador
    driver.quit()

def test_mercadolibre(setup):
    driver = setup
    wait = initial_time_configurations(driver)
    item = "playstation 5"
    country = 'MX'
    state = "Distrito Federal"
    initial_navegation(driver)
    select_country(driver, wait, country)
    search_item(driver, item, wait)
    apply_new_filter(driver, wait)
    select_state(driver, wait, state)
    sort_highest_to_lowest(driver, wait)
    first_5_items(driver)
    close_driver(driver)
