import requests
import json


def innit():
    """
    Loading data from finanstilsynet api to get shorting positions from stocks registrered in the OSBX
    """

  
    URL = "https://ssr.finanstilsynet.no/api/v2/instruments/"

    r = requests.get(url=URL)

    data = r.json()

    with open("sample.json",  "w") as outfile:
       json.dump(data, outfile)

    #test
    print(len(data))
    print(data[0]['events'])


    for i in range(len(data)):
        print(data[i]['issuerName'])
        # print(data[1]["issuerName"])




class SSR:
	def __init__(self) -> None:

		self.stocks = open("issuers.txt")
    
    	# self.data = r.json()


	def getIssuerName(self):
		pass
  
  	
	def getEvents(self):
		pass


# innit()