from bs4 import BeautifulSoup
import requests

import requests
headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:78.0)   Gecko/20100101 Firefox/78.0", 
"Referer": "https://www.google.com"}
url = "https://brainly.pl"
response = requests.get(url, headers=headers)




# response.content
#response.json()
#response.text

soup = BeautifulSoup(response.content, 'html.parser')
