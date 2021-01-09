import requests
import bs4

url = 'https://jadwalsholat.pkpu.or.id/?id=287'
content = requests.get(url)

res = bs4.BeautifulSoup(content.text, 'html.parser')
# print(res)
data = res.find_all('tr', 'table_highlight')
# print(data[0])
data = data[0]

sholat = {}
i = 0
for d in data:
    if i == 1:
        sholat['subuh'] = d.get_text()
    if i == 2:
        sholat['zuhur'] = d.get_text()
    if i == 3:
        sholat['ashar'] = d.get_text()
    if i == 4:
        sholat['maghrib'] = d.get_text()
    if i == 5:
        sholat['isya'] = d.get_text()

    i += 1

print(sholat)
