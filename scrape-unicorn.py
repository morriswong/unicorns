import json
import requests
import pandas as pd
from bs4 import BeautifulSoup

url = 'https://www.cbinsights.com/research-unicorn-companies'

# html = urlopen(url)
html = requests.get(url).text
soup = BeautifulSoup(html, "html.parser")

table = soup.find_all("div", {"class" : "contents"})

head = []
for item in table:
    headers = item.find_all('th')
    rows = item.find_all('td')
    for header in headers:
        head.append(header.text)
    for row in rows:
        print (row.text)

print (head)
# pd.Series(data = head)
# pd.DataFrame(data = head)
