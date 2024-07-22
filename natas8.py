
#!/usr/bin/env python

import requests
import re

username = 'natas8'
password = 'xcoXLmzMkoIP9D7hlgPlh9XD7OgLAe5Q'

url = 'http://%s.natas.labs.overthewire.org/' % username

try:
    session = requests.Session()
    response = session.post(url, data={"secret": "oubWYf2kBq", "submit": "submit"}, auth=(username, password))

    content = response.text

    # Uncomment the line below to print the entire content of the response
    # print(content)

    # Using regular expression to find the password for natas9
    matches = re.findall(r'natas9 is (.*)', content)

    if matches:
        password_natas9 = matches[0].strip()  # Strip any leading or trailing whitespace
        print("Password for natas9:", password_natas9)
    else:
        print("Password for natas9 not found in the response.")
except requests.exceptions.RequestException as e:
    print("An error occurred:", e)
