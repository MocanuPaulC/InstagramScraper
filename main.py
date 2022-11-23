from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from random import Random

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

username=input("instagram Username: ")
password=input("password: ")

accountStr=input("accounts to scrape (please use the following format 'username,username,username' and hit enter when you're done:")

accounts_to_search=accountStr.split(sep=',')

browser = webdriver.Chrome()
browser.implicitly_wait(5)

browser.get('https://www.instagram.com/')
browser.implicitly_wait(10)
cookiesBtn=browser.find_element(By.CLASS_NAME,"_a9--._a9_0")
rand=Random()

cookiesBtn.click()



login_link = browser.find_element(By.CLASS_NAME,"_aa4b._add6._ac4d")
login_link.send_keys(username)

pass_input=browser.find_element(By.NAME,"password")
pass_input.send_keys(password)

login_btn=browser.find_element(By.CLASS_NAME,"_acan._acap._acas")

Login_button = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "_acan._acap._acas"))).click()
sleep(6)

notNow=browser.find_element(By.CLASS_NAME,"_acan._acao._acas")
sleep(8)
notNow.click()

WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "_a9--._a9_0"))).click()

allPosts=[]
for i in range(0,len(accounts_to_search)):
    SearchBar = browser.find_element(By.CLASS_NAME, "_aauy")
    SearchBar.send_keys(accounts_to_search[i])
    sleep(2)
    SearchBar.clear()
    sleep(2)
    SearchBar.send_keys(accounts_to_search[i])
    sleep(2)
    account=browser.find_element(By.CLASS_NAME,'_abm4')
    accountClickable=account.find_element(By.CSS_SELECTOR,'a')
    accountClickable.click()
    sleep(3)
    linePhotos = browser.find_elements(By.CLASS_NAME, "_ac7v._aang")
    threePhotos=[]
    hrefLinks=[]

    for line in linePhotos:
        threePhotos=line.find_elements(By.CLASS_NAME,"_aabd._aa8k._aanf")

        for photo in threePhotos:
            hrefLinks.append(photo.find_element(By.CSS_SELECTOR,'a').get_property("href"))
    allPosts.append(hrefLinks.copy())

    hrefLinks.clear()
    linePhotos.clear()
    sleep(4)



# here we cycle through the posts found
for links in allPosts:
    for link in links:
        browser.get(link)
        browser.implicitly_wait(10)
        # to get tags and likes
        # likes=
        # tags=
        sleep(3)

sleep(100)

sleep(5)

browser.close()