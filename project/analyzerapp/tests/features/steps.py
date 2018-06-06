from aloe import *
from selenium import webdriver
from aloe import before, step, world
from selenium.webdriver.support.ui import WebDriverWait
from project.djangoweb import *
import time


@before.all
def before_all():
    world.browser = webdriver.Firefox()
    world.browser.get("http://localhost:8000/index/")

@after.all
def after_all():
    world.browser.close()

@step (r'I dont set a date')
def date_field_blank(self):
    campoDate = world.browser.find_element_by_id("id_my_date")
    date = campoDate.get_attribute('value')
    assert date == ""

@step (r'I should see the results:')
def see_result(self):
    resultado = WebDriverWait(world.browser, 600).until(lambda browser: world.browser.find_element_by_id("resultado"))
    texto = resultado.text
    assert texto != ""

@step (r'I put a date into DateField')
def fill_dateField (self):
    campoDate = world.browser.find_element_by_id("id_my_date")
    campoDate.send_keys(time.strftime('%Y-%m-%d'))
    textDate = campoDate.get_attribute('value')
    assert textDate == (time.strftime('%Y-%m-%d'))

@step (r'I click the analyze button')
def click_analyze_button(self):
    botonExecute = world.browser.find_element_by_id("analyze")
    botonExecute.click()

@step(r'I write an invalid date in the dateField')
def write_in_dateField_to_reset(self):
    campoTexto = world.browser.find_element_by_id("id_my_date")
    campoTexto.send_keys("Texto de prueba")

@step (r'I should see the error message')
def see_error_message(self):
    resultArea = WebDriverWait(world.browser, 600).until(lambda browser: world.browser.find_element_by_id("resultado"))
    texto = resultArea.text
    assert 'no data' in texto

@step (r'I click the reset button')
def click_the_reset_button(self):
    botonBorrar = world.browser.find_element_by_id("reset")
    botonBorrar.click()

@step (r'I should see the resultarea empty')
def see_textarea_empty(self):
    resultArea = WebDriverWait(world.browser, 600).until(lambda browser: world.browser.find_element_by_id("resultado"))
    texto = resultArea.text
    assert texto == ""

@step (r'I write a date into datefield')
def write_random_in_datefield(self):
    campoTexto = world.browser.find_element_by_id("id_my_date")
    campoTexto.send_keys("Texto de prueba")

@step (r'The datefield looks empty')
def see_datefield_empty(self):
    campoTexto = WebDriverWait(world.browser, 600).until(lambda browser: world.browser.find_element_by_id("id_my_date"))
    textoEscrito = campoTexto.get_attribute('value')
    assert textoEscrito == ""

@step (r'I have the datefield empty')
def datefield_empty(self):
    campoTexto = world.browser.find_element_by_id("id_my_date")
    textoEscrito = campoTexto.get_attribute('value')
    assert textoEscrito == ""

@step (r'The datefield continues empty')
def datefield_continues_empty(self):
    campoTexto = world.browser.find_element_by_id("id_my_date")
    textoEscrito = campoTexto.get_attribute('value')
    assert textoEscrito == ""

@step (r'The results should be in order')
def see_result(self):
    resultado = WebDriverWait(world.browser, 600).until(lambda browser: world.browser.find_element_by_id("resultado"))
    texto = resultado.text
    elementos = texto.split("\n")
    elementosAntiguos = []
    elementosActuales = []
    for x in range(0, len(elementos)):
        if elementosAntiguos != []:
            elementosAntiguos = elementosActuales
            elementosActuales = elementos[x].split(" ")
            assert int(elementosAntiguos[1]) >= int(elementosActuales[1])