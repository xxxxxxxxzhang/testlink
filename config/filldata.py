from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import sys
<<<<<<< HEAD

def login(host):
    firefox_opt = webdriver.FirefoxOptions()
    firefox_opt.add_argument("--headless")
    driver = webdriver.Firefox(options=firefox_opt)
=======
import time

def login(host):
    firefox_opt = webdriver.FirefoxOptions()
    time.sleep(10)
    firefox_opt.add_argument("--headless")
    driver = webdriver.Firefox(firefox_options=firefox_opt)
    #driver = webdriver.Firefox()
>>>>>>> 4bbfa3c6f7172728365a0d3ea7cd33cef2648eff
    url = host + '/index.php'
    driver.get(url)

    driver.find_element_by_id("tl_login").clear()
    driver.find_element_by_id("tl_login").send_keys("user")
    driver.find_element_by_id("tl_password").clear()
    driver.find_element_by_id("tl_password").send_keys("bitnami")
    driver.find_element_by_id("tl_login_button").click()
    driver.switch_to.frame("mainframe")
<<<<<<< HEAD
    WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.NAME, 'tprojectName')))
=======
    #WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.NAME, 'tprojectName')))
>>>>>>> 4bbfa3c6f7172728365a0d3ea7cd33cef2648eff
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
<<<<<<< HEAD
    crstname=driver.find_element_by_name("CSRFName")

    csrftoken = driver.find_element_by_name("CSRFToken")
    #csrftoken=driver.find_element_by_xpath("/html/body/div[3]/div/form/input[2]")
    #login_form = driver.find_element_by_xpath("/html/body/div[2]/span[2]/a[1]")
    #print(login_form.text)
    # cookie = driver.get_cookies()
    # print("hehehhe",cookie)
    # print('cookie是：',cookie[0]['name'])
    # print('cookie是：',cookie[1]['value'])
    # data = '$CSRFName=CSRFGuard_2120888389&CSRFToken=df62d051e2a4aab3d0a31046d077ec2e59d7e948734e0899639e77692abc78c9148daba1b84c044296b0593e5794ffb0f71bba5bc54d677917f93668b2b08b08&' \
    #        'doAction=editUser&firstName=user&lastName=Administrator&emailAddress=user%40example.com&locale=zh_CN'
    #
    # response = requests.post('http://$http://192.168.56.105/lib/usermanagement/userInfo.php', headers=headers,
    #                          cookies=cookies, data=data, verify=False)
=======
    

>>>>>>> 4bbfa3c6f7172728365a0d3ea7cd33cef2648eff


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usages:exp.py blog_host')
        exit(0)
    h = sys.argv[1]
<<<<<<< HEAD
    #h = 'http://192.168.56.105:8001/'
=======
>>>>>>> 4bbfa3c6f7172728365a0d3ea7cd33cef2648eff
    login(h)
