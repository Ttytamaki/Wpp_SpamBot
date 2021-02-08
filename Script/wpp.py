# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 23:28:25 2021

@author: Dutt
"""


import selenium as sln
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys


# chrome driver 
options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_argument("--disable-extensions")
options.add_argument("window-size=1200x600")
browser = webdriver.Chrome(ChromeDriverManager().install(), chrome_options = options)



# Navigating to the login
browser.get('https://web.whatsapp.com/')
    # Defining Web whatsapp;

#Finding the tags by name
WebDriverWait(browser, 120)
    # Wait 40 seconds
inputRdy = input("Web Wpp Conected? y/n: ")

WebDriverWait(browser, 200)


if inputRdy in ("Y", "y"):
    chat = browser.find_element_by_xpath('/html/body/div[1]/div/div/div[3]/div/div[1]/div/label/div/div[2]')
    inputName = input("Enter name to Spam: ")
    chat.send_keys(inputName)
    chat.send_keys(Keys.ENTER)
#  browser.find_element_by_css_selector("span[title='" + input("Enter name to spam: ") + "']").click()
elif inputRdy in ("N", "n"):
    print("Please, connect Web Whatsapp.")
    inputRdy = input("Web Wpp Connected? y/n: ")
    while inputRdy in ("n", "N"):
        print("Please, connect Web Whatsapp.")
        inputRdy = input("Web Wpp Connected? y/n: ") 
    if inputRdy in ("Y", "y"):
        chat = browser.find_element_by_xpath('/html/body/div[1]/div/div/div[3]/div/div[1]/div/label/div/div[2]')
        inputName = input("Enter name to Spam: ")
        chat.send_keys(inputName)
        chat.send_keys(Keys.ENTER)
    

# browser.find_element_by_css_selector("span[title='" + input("Enter name to spam: ") + "']").click()
    # Name who you are going to mess with;
inputString = input("Enter message to send: ")
    # Input the message you wish to send;
inputTime = int(input("How many times: "))
    # How many times do you want to send it?

i = 0
while(i < inputTime+1):
    browser.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(inputString)
    browser.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button').click()
    i += 1

inputAgain = input("Wanna go again? y/n: ")
if inputAgain in ("n", "N"):
        print("Buh-bye")     
        browser.close() 
        
while inputAgain in ("y", "Y"):
    chat = browser.find_element_by_xpath('/html/body/div[1]/div/div/div[3]/div/div[1]/div/label/div/div[2]')
    inputName = input("Enter name to Spam: ")
    chat.send_keys(inputName)
    chat.send_keys(Keys.ENTER)
    inputString = input("Enter message to send: ")
    inputTime = int(input("How many times: "))
    
    i = 0
    while(i < inputTime+1):
        browser.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(inputString)
        browser.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button').click()
        i += 1
    inputAgain = input("Wanna go Again: y/n ")
    if inputAgain in ("n", "N"):
        print("Buh-bye")     
        browser.close() 

    
    