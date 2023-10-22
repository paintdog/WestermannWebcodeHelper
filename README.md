# WestermannWebcodeHelper
Alpha-Version eines 🛠 Tools, dass über Webcodes bei Westermann die zugehörigen Materialien 🔽 herunterlädt.

## Webcode-Liste aufbauen 

Westermann verwendet eine Kennung für ein Medium bestehend aus der Buchstabenfolge SNG, einem Bindestrich, einer Kennung für das jeweilige Medium ohne führende 0, einem Bindestrich und dann eine dreistellige Nummer für die eigentliche Webressource. Nachfolgendes kleines Tool kann helfen, eine Webcodeliste aufzubauen, wenn man nur die dreistelligen Nummern erfasst:

```
webcodes = "999 990".split(" ")
webcode = "SNG-22788-"

result = []
for code in webcodes:
    result.append("".join([webcode, code]))

print(result)
```
## Webcode-Listen für einzelne Veröffentlichungen des Verlags

### EinFach Deutsch, Unterrichtsmodell, Sprache und Kommunikation im öffentlichen Raum … ohne Rassismus und Diskriminierung (2022)

```
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
