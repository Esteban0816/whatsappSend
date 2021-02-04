from selenium import webdriver
import time
import os, time

driver = webdriver.Chrome("C:/projects/whatsappSend/recursos/chromedriver.exe")
driver.get("https://web.whatsapp.com/")

time.sleep(10)

celular = "573115760089"
mensaje = "prueba"

driver.get("https://wa.me/"+celular+"?text="+mensaje)
time.sleep(5)

btn = driver.find_elements_by_xpath("//*[@id='action-button']")[0]
btn.click()
time.sleep(5)

btn = driver.find_elements_by_xpath("//*[@id='fallback_block']/div/div/a")[0]
btn.click()
time.sleep(30)

btn = driver.find_elements_by_xpath("//*[@id='main']/footer/div[1]/div[3]")[0]
btn.click()
time.sleep(5)

print("fin")

time.sleep(20)

driver.close()