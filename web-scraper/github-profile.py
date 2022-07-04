import requests
from bs4 import BeautifulSoup

github_user = input('Input GitHub Username: ')
url = 'https://github.com/' + github_user

request = requests.get(url)

soup = BeautifulSoup(request.content, 'html.parser')

profile_image = soup.find('img', {'alt': 'Avatar'})['src']

print(profile_image)
