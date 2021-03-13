import bs4
import requests

url = 'https://id.carousell.com/carousell_id/'

contents = requests.get(url)

print(contents.text)

response = bs4.BeautifulSoup(contents.text, "html.parser")
print(response)