import requests
from bs4 import BeautifulSoup

url = 'https://detik.com'
try:
    req = requests.get(url)
    if req.status_code == 200:
        print(f'Success ! Response Status = {req.status_code}')

        soup = BeautifulSoup(req.text, features='html.parser')
        print(f'Result {url}')
        print(f'Title: {soup.title.string}')
    else:
        print(f'Error = {req.status_code}')

except Exception as e:
    print(f'Error {e}')

print('=' * 25)
print('Program End !')
