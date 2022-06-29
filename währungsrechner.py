from bs4 import BeautifulSoup
import requests

r = requests.get('https://www.iban.com/exchange-rates')
soup = BeautifulSoup(r.content, 'html.parser')

währungen = []
wechselkurs = []
währungsname = []

währungstabelle = soup.find('table', class_='table table-bordered table-hover downloads')
trs = währungstabelle.find_all('tr')
for tr in trs:
    for img in tr.find_all('img'):
        währungen.append(img['alt'].lower())

for tr in trs:
    for strong in tr.find_all('strong'):
        wechselkurs.append(strong.text)

aktueller_wechselkurs = dict(zip(währungen, wechselkurs))

währungsauswahl = input(str(währungen) + '\n\n' + 'Wähle eine Währung aus: ')
menge = input('Welche Menge: ')
for w1, w2 in aktueller_wechselkurs.items():
    if währungsauswahl in w1:
        print(int(menge)*float(w2))