# WestermannWebcodeHelper
Alpha-Version eines (privaten) 🛠 Tools, dass über Webcodes bei Westermann die zugehörigen Materialien 🔽 herunterlädt.

## Das Tool für den Download der Webressourcen über einen Webcode

Das Tool benötigt die Module [requests](https://pypi.org/project/requests/) und [beautifulsoup4](https://pypi.org/project/beautifulsoup4/).

```python
from bs4 import BeautifulSoup
import requests


def download(webcode):
    url = "https://www.westermann.de/webcode"
    payload = {'webcode': webcode}
    # Die Seite mit dem Webcode aufrufen und die Zielseite erfragen
    web = requests.post(url, data=payload, allow_redirects=False)
    location = web.headers['Location']
    zieladresse = "https://www.westermann.de" + location
    # Die Zielseite aufrufen und den Link auf die Webressource erfragen
    web = requests.get(zieladresse)
    soup = BeautifulSoup(web.text, "html5lib")
    links = soup.find_all("a")
    ressource = ""
    for link in links:
        if "backend" in link["href"]:
            ressource = "https://www.westermann.de" + link["href"]
    # Die Seite mit der Ressource aufrufen, die Ressource herunterladen
    web = requests.get(ressource, allow_redirects=True)
    with open(f"{webcode}.doc", "wb") as f:
        f.write(web.content)

def main():
    # Sprache und Kommunikation im öffentlichen Raum (2022)
    webcodes = ['SNG-22788-999', 'SNG-22788-990', 'SNG-22788-909', 'SNG-22788-100', 'SNG-22788-111', 'SNG-22788-110',
                'SNG-22788-101', 'SNG-22788-001', 'SNG-22788-011', 'SNG-22788-008', 'SNG-22788-800', 'SNG-22788-088',
                'SNG-22788-888', 'SNG-22788-808', 'SNG-22788-880', 'SNG-22788-222', 'SNG-22788-900', 'SNG-22788-202',
                'SNG-22788-022', 'SNG-22788-220', 'SNG-22788-444', 'SNG-22788-400', 'SNG-22788-404', 'SNG-22788-044',
                'SNG-22788-440', 'SNG-22788-333', 'SNG-22788-300', 'SNG-22788-303', 'SNG-22788-330', 'SNG-22788-033',
                'SNG-22788-030', 'SNG-22788-555', 'SNG-22788-666', 'SNG-22788-600', 'SNG-22788-606', 'SNG-22788-660',
                'SNG-22788-066', 'SNG-22788-060', 'SNG-22788-777', 'SNG-22788-700', 'SNG-22788-750', 'SNG-22788-850',
                'SNG-22788-150', 'SNG-22788-002', 'SNG-22788-500', 'SNG-22788-000', 'SNG-22788-090', 'SNG-22788-009',
                'SNG-22788-099']
    for webcode in webcodes:
        download(webcode)

if __name__ == "__main__":
    main()
```

## Webcode-Liste aufbauen 

Westermann verwendet eine Kennung für ein Medium bestehend aus der Buchstabenfolge SNG, einem Bindestrich, einer Kennung für das jeweilige Medium ohne führende 0, einem Bindestrich und dann eine dreistellige Nummer für die eigentliche Webressource. Nachfolgendes kleines Tool kann helfen, eine Webcodeliste aufzubauen, wenn man nur die dreistelligen Nummern erfasst:

```python
webcodes = "999 990".split(" ")
webcode = "SNG-22788-"

result = []
for code in webcodes:
    result.append("".join([webcode, code]))

print(result)
```
## Webcode-Listen für einzelne Veröffentlichungen des Verlags

### EinFach Deutsch, Unterrichtsmodell, Sprache und Kommunikation im öffentlichen Raum … ohne Rassismus und Diskriminierung (2022)

```python
webcodes = ['SNG-22788-999', 'SNG-22788-990', 'SNG-22788-909', 'SNG-22788-100', 'SNG-22788-111', 'SNG-22788-110',
            'SNG-22788-101', 'SNG-22788-001', 'SNG-22788-011', 'SNG-22788-008', 'SNG-22788-800', 'SNG-22788-088',
            'SNG-22788-888', 'SNG-22788-808', 'SNG-22788-880', 'SNG-22788-222', 'SNG-22788-900', 'SNG-22788-202',
            'SNG-22788-022', 'SNG-22788-220', 'SNG-22788-444', 'SNG-22788-400', 'SNG-22788-404', 'SNG-22788-044',
            'SNG-22788-440', 'SNG-22788-333', 'SNG-22788-300', 'SNG-22788-303', 'SNG-22788-330', 'SNG-22788-033',
            'SNG-22788-030', 'SNG-22788-555', 'SNG-22788-666', 'SNG-22788-600', 'SNG-22788-606', 'SNG-22788-660',
            'SNG-22788-066', 'SNG-22788-060', 'SNG-22788-777', 'SNG-22788-700', 'SNG-22788-750', 'SNG-22788-850',
            'SNG-22788-150', 'SNG-22788-002', 'SNG-22788-500', 'SNG-22788-000', 'SNG-22788-090', 'SNG-22788-009',
            'SNG-22788-099']
```

## Möglichkeiten zur Mitarbeit 

Ein GUI für das Tool könnte technisch weniger versierten Nutzerinnen und Nutzern helfen.

Weitere Webcode-Listen könnten zunächst direkt via Pull Requests der Readme.md-Datei hinzugefügt werden. 