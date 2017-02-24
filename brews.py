#Connect to brewery
#Send requesr and fetch
#Save Data
#Parse data

import requests
import json

print("Δώσε λέξεις κλειδιά (χωρισμένες με κόμμα)")
words = input()
keywords = [x.strip() for x in words.split(',')]

def KeywordSaving (key):
	parameters = { "q": key, "type": "beer", "key": "4b9cf1ce5dd3698db3760f0e803df6f6", "format": "json"}
	response = requests.get("https://api.brewerydb.com/v2/search" , params=parameters)
	print(response.status_code)
	data = response.json()
	print(data)
	return data

def SavingFiles (key,data):
	file = key+".txt"
	with open(file , "w") as outfile:
		json.dump(data, outfile)

for key in keywords:
	KeywordSaving(key)