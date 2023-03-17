import webbrowser
import requests

# przyklad działania:
# pageurl – pobrana strona, date-data w formacie rok miesiac dzien np. 20230126
# zapytanie do api:
# http://archive.org/wayback/available?url=example.com&timestamp=20060101
pageurl = input('podaj strone: ')
date1 = input('podaj date: ')
date2 = input('podaj date: ')
date3 = input('podaj date: ')
url1 = "http://archive.org/wayback/available?url=" + pageurl + "&timestamp=" + str(date1)
url2 = "http://archive.org/wayback/available?url=" + pageurl + "&timestamp=" + str(date2)
url3 = "http://archive.org/wayback/available?url=" + pageurl + "&timestamp=" + str(date3)
response1 = requests.get(url1)
response2 = requests.get(url2)
response3 = requests.get(url3)
d1 = response1.json()
d2 = response2.json()
d3 = response3.json()
page1 = d1["archived_snapshots"]["closest"]["url"]
page2 = d2["archived_snapshots"]["closest"]["url"]
page3 = d3["archived_snapshots"]["closest"]["url"]
webbrowser.open(page1)
webbrowser.open(page2)
webbrowser.open(page3)