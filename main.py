from selenium import webdriver
import time
brow = webdriver.Firefox()
# type(brow)
brow.get("https://www.star1crm.com.br/crmstar/1crm_login.asp")
# brow.find_element_by_id("td_login")
# Acha os campos do form de login


time.sleep(1)
# try:
login = brow.find_element_by_id("login")
login.send_keys("")
pwd = brow.find_element_by_id("senha")
pwd.send_keys("*")
btn_login = brow.find_element_by_class_name("botao_login")
btn_login.click()
time.sleep(3)
# btn_agenda = brow.find_element_by_class_name("aba_nc hand")
btn_agenda = brow.find_element_by_xpath(
    "/html/body/form/table/tbody/tr[1]/td/a/table[1]/tbody/tr/td[5]")
btn_agenda.click()

time.sleep(2)
agendas = brow.find_elements_by_class_name("cal_fnt")
# agendas = brow.find_elements_by_partial_link_text("Renan Pedro da Silva")
# print(agendas)
count = 0
for agenda in agendas:
    print(agenda.click())
    # time.sleep(5)
    # print(count)
# except:
# print('Was not able to find an element with that name.')
