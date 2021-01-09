import requests
import bs4

url = 'https://jadwalsholat.pkpu.or.id/?id=287'
content = requests.get(url)

soup = bs4.BeautifulSoup(content.text, 'html.parser')
tableLights = soup.findAll('tr', attrs={'class': 'table_light'})
tableDarks = soup.findAll('tr', attrs={'class': 'table_dark'})
tableHighlight = soup.find('tr', attrs={'class': 'table_highlight'})

arrData = []

count = 0
while count < 15:
    if count <= 3:
        arrData.append(tableLights[count])
        arrData.append(tableDarks[count])
    if count == 3:
        arrData.append(tableHighlight)
    if count >= 4:
        arrData.append(tableDarks[count])
        arrData.append(tableLights[count])
    count += 1

print(arrData)
print("=" * 50)

for i in arrData:
    strFix = i.get_text()

    data = {
        'tanngal': strFix[0:2],
        'shubuh':  strFix[2:7],
        'dzuhur':  strFix[7:12],
        'ashar':  strFix[12:17],
        'maghrib':  strFix[17:22],
        'isya':  strFix[22:27],
    }

    print(data)
