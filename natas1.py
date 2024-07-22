#!/usr/bin/env python

import requests
import re

username = 'natas1'
password = '0nzCigAq7t2iALyvU9xcHlYN4MlkIwlq'

# Construct the URL using the username
url = 'http://%s.natas.labs.overthewire.org' % username

# Send a GET request to the URL with basic authentication
response = requests.get(url, auth=(username, password))

# Check if the request was successful
if response.status_code == 200:
    content = response.text
    
    # Use regular expressions to find the password for the next level (natas2)
    matches = re.findall(r'The password for natas2 is (.*)', content)
    
    if matches:
        # Extract the password for natas2
        password_natas2 = matches[0]
        print("The password for natas2 is:", password_natas2)
    else:
        print("Password not found in the response content.")
else:
    print(f"Failed to retrieve URL: {url}. Status code: {response.status_code}")
