#!/usr/bin/env python3

import requests
url = "https://checkip.amazonaws.com/"

resp = requests.get(url)

print(resp.text)