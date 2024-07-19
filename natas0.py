#!/usr/bin/env python

import requests
import re

username = 'natas0'
password = username

url = 'http://%s.natas.labs.overthewire.org' % username

# Make a GET request to the URL with basic authentication
response = requests.get(url, auth=(username, password))

# Check if the request was successful (status code 200)
if response.status_code == 200:
    content = response.text
    
    # Use re.search to find the password pattern
    match = re.search(r'<!--The password for natas1 is (.*) -->', content)
    
    if match:
        # Print the first group of the match, which is the password
        print("The password for natas1 is:", match.group(1))
    else:
        print("Password pattern not found in the response.")
else:
    print(f"Failed to retrieve content. Status code: {response.status_code}")
