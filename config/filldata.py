from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import sys
import time

def login(host):
    firefox_opt = webdriver.FirefoxOptions()
    time.sleep(10)
    firefox_opt.add_argument("--headless")
    driver = webdriver.Firefox(firefox_options=firefox_opt)
    #driver = webdriver.Firefox()
    url = host + '/index.php'
    driver.get(url)

    driver.find_element_by_id("tl_login").clear()
    driver.find_element_by_id("tl_login").send_keys("user")
    driver.find_element_by_id("tl_password").clear()
    driver.find_element_by_id("tl_password").send_keys("bitnami")
    driver.find_element_by_id("tl_login_button").click()
    driver.switch_to.frame("mainframe")
    #WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.NAME, 'tprojectName')))
    driver.find_element_by_name("tprojectName").clear()
    driver.find_element_by_name("tprojectName").send_keys("NewTest")
    driver.find_element_by_name("tcasePrefix").clear()
    driver.find_element_by_name("tcasePrefix").send_keys("1")
    driver.find_element_by_xpath('//*[@id="item_view"]/tbody/tr[16]/td/div/input[3]').click()
    driver.switch_to.parent_frame()
    titlebar=driver.switch_to.frame("titlebar")
    print("titlebar", titlebar)
    driver.find_element_by_xpath("/html/body/div[2]/span[2]/a[1]").click()
    driver.switch_to.parent_frame()
   
    mainframe=driver.switch_to.frame("mainframe")
    print("mainframe",mainframe)
    Select(driver.find_element_by_xpath("/html/body/div/form[1]/table/tbody/tr[5]/td/select")).select_by_value('zh_CN') 
    driver.find_element_by_xpath("/html/body/div/form[1]/div/input").click()
    



if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usages:exp.py blog_host')
        exit(0)
    h = sys.argv[1]
    login(h)
