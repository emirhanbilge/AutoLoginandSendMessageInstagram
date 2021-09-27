# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 15:55:00 2021

@author: EBB
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
import time 


driver = webdriver.Chrome()
driver.get("https://www.instagram.com/accounts/login/?hl=tr")


def clickFunctions(xpathURL):
    while(1): ## internet hızına göre elementin bulunması için geçecek zamanı bilmiyoruz onun için bu yapıyı kullanıyorum.
        try:
            driver.find_element(By.XPATH, xpathURL ).click() # bulunca tıklama ve break yapma
            break
        except:
            time.sleep(1)

def getElementFunction(xpathURL):
    e = 1 # elementi return ettirebilmemiz için objeyi eşitliyorum bunu tryda doğrudan return yaparsam none türüne düşebilir
    while(1):
        try:
            e = driver.find_element(By.XPATH, xpathURL)
            break
        except:
            time.sleep(1)
    return e


username = getElementFunction('//*[@id="loginForm"]/div/div[1]/div/label/input') # Kullanıcı adı olan yeri alma
password = getElementFunction('//*[@id="loginForm"]/div/div[2]/div/label/input') # Parola kısmını alma 

# Kullanıcı adını girme , parola girme ve butona basma
username.send_keys("Kullanıcı adını gir") # Kullanıcı adını yolla
password.send_keys("Parolanı Gir") # Parolayı yolla 


clickFunctions('//*[@id="loginForm"]/div/div[3]/button/div') # giriş butonuna tıklama
time.sleep(5) 

#anasayfa 
driver.get("https://www.instagram.com/direct/new/") # mesajlar kısmını açma

time.sleep(2) #sayfanın yüklenmesini bekleme
clickFunctions('/html/body/div[6]/div/div/div/div[3]/button[2]') # bildirimleri kapata tıklama

messagePage = getElementFunction('/html/body/div[2]/div/div/div[2]/div[1]/div/div[2]/input') #kullanıcı adı girme yerini bulma
messagePage.send_keys("emreakins0")# kullanıcı adını girme

clickFunctions('/html/body/div[2]/div/div/div[2]/div[2]/div/div/div[3]/button') # kullanıcıyı seçme

clickFunctions('/html/body/div[2]/div/div/div[1]/div/div[2]/div/button') #ilete tıklama

messageArea =getElementFunction('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea') #mesaj alanını bulma
messageArea.send_keys("Merhaba bu ebb'nin  hazırladığı test kodudur")# mesaj alanını doldurma

clickFunctions('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button') #gönder butonuna tıklama
