from selenium import webdriver
from selenium.webdriver.support.select import Select
import pandas as pd
import time
import numpy as np

# Carrego dataframe com planilha
data = pd.read_excel(r'Registro de Fichas - 09.2019.xlsx')
df = pd.DataFrame(data, columns=['CHAMADO', 'CLIENTE', 'Horas'])

# Limpo valores inválidos
df.dropna(0)


# print(df["chamado"])
for index, row in df.iterrows():

    chamado = row['CHAMADO']
    cliente = row['CLIENTE']
    horas = row['Horas']

    print(chamado, cliente, horas)

# brow = webdriver.Firefox()
# brow.implicitly_wait(2)
# # type(brow)
# brow.get("https://www.starsoft.com.br/crmstar/1crm_login.asp")


# time.sleep(2)
# # Acha os campos do form de login
# login = brow.find_element_by_id("login")
# login.send_keys("rpsilva")
# pwd = brow.find_element_by_id("senha")
# pwd.send_keys("Renanzinho300*")
# btn_login = brow.find_element_by_class_name("botao_login")
# btn_login.click()
# time.sleep(1)

# # Entra na pagina da agenda
# brow.get("https://www.starsoft.com.br/crmstar/1crm_calendario.asp")


# # Encontro dropdown com os meses
# select = Select(brow.find_element_by_name("Mes"))

# # Seleciono mês que quero lançar as fichas (DEVE SER STRING)
# select.select_by_value("8")


# # Busca conjunto de agendas
# # agendas = brow.find_elements_by_class_name("cal_fnt")
# agendas = brow.find_elements_by_class_name("cal_sala")

# count = 0

# # Para cada agenda, faço algo
# for agenda in agendas:
#     agenda.click()
#     time.sleep(3)
#     empresa_field = brow.find_element_by_id("Empresa_s")
#     cliente = empresa_field.get_property("value")
#     data = brow.find_element_by_id("DatacadDD").get_property("value")

#     print(data, cliente)
#     time.sleep(5)
#     # Checo se cliente e data estão na planilha

#     if True:
#         # Lanço ficha
#         pass
#     else:
#         pass
#         # Listo item que não foi lançado
#         # print(count)
#         # # except:
#         # # print('Was not able to find an element with that name.')
