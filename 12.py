import re
import requests
s_t= []
def UserInput():
	print('Τι θα είχες όρεξη να φάς;')
	search = input()
	s_t.append(search)
	return search

def DataR():
	parameters = {"key" :"6a3101af1f6b2f8cdfeef2a58539afc2", "q" : UserInput() }
	response = requests.get("http://food2fork.com/api/search",params=parameters)
	data = response.json()
	return data

def Recipe(data):
	parameters = {"key" :"6a3101af1f6b2f8cdfeef2a58539afc2", "rId" : data["recipe_id"] }
	response = requests.get("http://food2fork.com/api/get" , params=parameters)
	data = response.json()
	return data

def FindCommon(list1,list2):
	common = list(set(list1).intersection(list2))
	return common

def Beer(food):
	parameters = {"food" : food}
	response= requests.get("https://api.punkapi.com/v2/beers" , params=parameters)
	data = response.json()
	return data

count = 0

while count == 0:
	data = DataR();
	count = data['count']
	if count == 0:
		print("Δεν μπορώ να βρώ συνταγή :( Ξαναπροσπάθησε κάτι άλλο.")
		s_t.pop()


result = data['recipes'][0]
recipe = Recipe(result);

rSearch = s_t[0]
rTitle = recipe["recipe"]["title"]

mystr = 'This is a string, with words!'
wordList = re.sub("[^\w]", " ",  mystr).split()

ls = wordList = re.sub("[^\w]", " ",  rSearch).split()
lt = wordList = re.sub("[^\w]", " ",  rTitle).split()

common = FindCommon(ls,lt);

fterm = []
if common:
	for term in common:
		blist = Beer(term);
		if blist:
			fterm.append(len(blist))
		else:
			fterm.append(0)
	status = 1
else:
	for term in lt:
		blist = Beer(term);
		if blist:
			fterm.append(len(blist))
		else:
			fterm.append(0)
	status = 2

index = fterm.index(max(fterm))
if status == 1:
	beers = Beer(common[index])
else:
	beers = Beer(lt[index])

try: 
	beer = beers[0]
	name = beer["name"]
except IndexError:
	beer = "Δεν βρέθηκε μπύρα για αυτό το φαϊ. Πιες μια amstel"
	status = 0
	name = "Δεν βρέθηκε μπύρα για αυτό το φαϊ. Πιες μια amstel :P"

print("Μπύρα: " + name)
print("Συνταγή: " + recipe["recipe"]["title"])
ing = recipe["recipe"]["ingredients"]
print("Υλικά:")
for ingredinet in ing:
	print(ingredinet)
print("Url συνταγής: " + recipe["recipe"]["source_url"])
