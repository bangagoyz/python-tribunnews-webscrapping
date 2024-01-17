from bs4 import BeautifulSoup
import requests
import json
url = "Your Tribunnews Link"

a = 0
isi = ""
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}
pageToScrape = requests.get(url, headers=headers)

soup = BeautifulSoup(pageToScrape.text, 'html.parser' )
getContentDiv = soup.find("div", attrs={"class":"side-article txt-article multi-fontsize"})
getPenulisDiv = soup.find("div", attrs={"id":"penulis"})
getEditorDiv = soup.find("div", attrs={"id":"editor"})

title = soup.find("h1", attrs={"id":"arttitle"}).text
image = soup.find("img", attrs={"class":"imgfull"})
konten = getContentDiv.find_all('p', attrs={"class": False})
penulis = getPenulisDiv.find("a").text
editor = getEditorDiv.find("a").text
for x in konten:
    content = str(x.get_text(strip=True))
    a += 1
    if (a>2):
        isi += content
        



hasil = {
    "Judul": title,
    "link photo": image['src'],
    "konten": isi,
    "penulis": penulis,
    "editor" : editor
}

jsonn = json.dumps(hasil, indent= 4)
print (jsonn)

with open('webScrapping.json', 'w', encoding='utf-8') as f:
    json.dump(hasil, f, ensure_ascii=False, indent= 4)