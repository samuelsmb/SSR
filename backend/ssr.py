import requests




print(len(data))
print(data[0]['events'])
for i in range(len(data)):
  print(data[i]['issuerName'])
# print(data[1]["issuerName"])

class SSR:
  def __init__(self) -> None:


    URL = "https://ssr.finanstilsynet.no/api/v2/instruments/"

    r = requests.get(url=URL)

    self.data = r.json()


  
  def getEvents(self):
    pass
