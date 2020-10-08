import requests
import sys
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def login(host):
    firefox_opt = webdriver.FirefoxOptions()
    firefox_opt.add_argument("--headless")
    driver = webdriver.Firefox(options=firefox_opt)
    url = host + '/index.php'
    driver.get(url)
    WebDriverWait(driver, 10).until(lambda x: x.find_element_by_id("tl_login"))
    driver.find_element_by_id("tl_login").clear()
    driver.find_element_by_id("tl_login").send_keys("user")
    driver.find_element_by_id("tl_password").clear()
    driver.find_element_by_id("tl_password").send_keys("bitnami")
    driver.find_element_by_id("tl_login_button").click()
    wait = WebDriverWait(driver, 10)
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@name="mainframe"]' )))
    time.sleep(20)
    driver.switch_to.parent_frame()
    driver.switch_to.frame("mainframe")
    driver.find_element_by_xpath('/html/body/div[3]/div[2]/a[4]').click()
    driver.find_element_by_xpath('/html/body/div/div/form/input[7]').click()
    csrfguard = driver.find_element_by_xpath('/html/body/div/form[1]/input[1]')
    csrfguard_name = csrfguard.get_attribute('name')
    csrfguard_value = csrfguard.get_attribute('value')
    csrfname = driver.find_element_by_xpath('/html/body/div/form[1]/input[2]')
    csrf_name = csrfname.get_attribute('name')
    csrf_value = csrfname.get_attribute('value')
    print(csrf_name, ':', csrf_value)
    cookie = driver.get_cookies()
    phpsession = cookie[0]['value']
    testlink_cookie = cookie[1]['value']
    print("phpsession:", phpsession)
    print("testlink_cookie", testlink_cookie)
    f = open("temp", 'w+')
    print("{phpsession}".format(phpsession=phpsession), file=f)
    print("{testlink_cookie}".format(testlink_cookie=testlink_cookie), file=f)

    
    
if __name__ == '__main__':
   
    if len(sys.argv) != 2:
        print('Usages:exp.py blog_host')
        exit(0)
    
    h = sys.argv[1]
    #h="http://192.168.56.105:8001"
    print("host is ",h)
    login(h)
  
    #exp2(h)