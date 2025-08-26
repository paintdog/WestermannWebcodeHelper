#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests


# https://www.westermann.de/backend/buchlink/aufrufen/978-3-14-109677-4/1000324819
# https://www.westermann.de/backend/buchlink/aufrufen/978-3-14-109677-4/1000324820

URL = "https://www.westermann.de"


def beautify(description):
    description = description.replace("?"," ").replace(":",";").replace("/","-")
    description = description.replace("Baustein","BS")
    description = description.replace("Arbeitsblätter","AB")
    description = description.replace("Arbeitsblatt","AB")
    description = description.replace("Zusatzmaterial","ZM")
    return description


def build(url):
    return URL + str(url)


def download(webcode):
    url = "https://www.westermann.de/webcode"
    payload = {'webcode': webcode}
    # Die Seite mit dem Webcode aufrufen und die Zielseite erfragen
    web = requests.post(url, data=payload, allow_redirects=False)
    location = web.headers['Location']
    zieladresse = "https://www.westermann.de" + location
    # Die Zielseite aufrufen und als soup bereitstellen
    web = requests.get(zieladresse)
    soup = BeautifulSoup(web.text, "html5lib")

    # Die Buchlinks abrufen und bereitstellen
    buchlinks = soup.find_all("div", attrs={"class" : "buchlink"})
    
    # Wir arbeiten jetzt die Buchlinks ab
    description = None
    link        = None
    for buchlink in buchlinks:
        p_items = buchlink.find_all("p")
        for p_item in p_items:
            if p_item.find("a"):
                link_element = build(p_item.find("a")["href"])
                print("URL!", link_element)
                web = requests.get(link_element, allow_redirects=True)
                if "Word" in p_item.find("a").text:
                    with open(f"{description} [{webcode}].doc", "wb") as f:
                        f.write(web.content)
                    flag = False
                elif "PDF" in p_item.find("a").text:
                    with open(f"{description} [{webcode}].pdf", "wb") as f:
                        f.write(web.content)
                else:
                    print("")
                    print("ERROR - unbekannter Dateityp.")
                    print(p_item.text)
                    print("")
            else:
                description = beautify(p_item.get_text(strip=True))
                print(description)
        # input(">>>")


def main():
    # Sprache und Kommunikation im öffentlichen Raum (2022)
    webcodes = ['WES-109677-636', 'WES-109677-282', 'WES-109677-885', 'WES-109677-705', 'WES-109677-204',
                'WES-109677-513', 'WES-109677-401', 'WES-109677-962', 'WES-109677-166', 'WES-109677-311',
                'WES-109677-667', 'WES-109677-722', 'WES-109677-827', 'WES-109677-771', 'WES-109677-999',
                'WES-109677-440', 'WES-109677-337', 'WES-109677-187', 'WES-109677-855', 'WES-109677-617',
                'WES-109677-222', 'WES-109677-079', 'WES-109677-483', 'WES-109677-323', 'WES-109677-599',
                'WES-109677-911', 'WES-109677-798', 'WES-109677-266', 'WES-109677-199', 'WES-109677-652',
                'WES-109677-067', 'WES-109677-554', 'WES-109677-681', 'WES-109677-491', 'WES-109677-384',
                'WES-109677-142', 'WES-109677-952', 'WES-109677-777', 'WES-109677-755', 'WES-109677-110',
                'WES-109677-255']
    # webcodes = ['WES-109677-999']
    for webcode in webcodes:
        download(webcode)

if __name__ == "__main__":
    main()
