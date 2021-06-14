# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

PATH = "C:\Dev club\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://moodle.iitd.ac.in/login/index.php")
user = driver.find_element_by_id("username")
user.send_keys("xxxxx")


problem = driver.find_element_by_id("login").text
l=problem.split("\n")
f=l[3].split(" ")
if f[2].isdigit():
    if f[3]=="+":
        o=int(f[2])+int(f[4])
    if f[3]=="-":
        o=int(f[2])-int(f[4])
else:
    if f[2]=="first":
        o=int(f[4])
    else: o=int(f[6])

captcha= driver.find_element_by_id("valuepkg3")
captcha.clear()
captcha.send_keys(o)


pas = driver.find_element_by_id("password")
pas.send_keys("xxxxx")

driver.find_element_by_id("loginbtn").click()