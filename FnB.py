
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

ls = rSearch.strip()
lt = rTitle.strip()

common = FindCommon(ls,lt);

found = []
fterm = []
for term in common:
	list = Beer(term);
	if list:
		fterm.append(len(list))
	else:
		fterm.append(0)

"""
Λοιπόν σε αυτό το κομμάτι θα δίνω τις διαθέσιμες λέξεις (απο τις λίστες) στον χρήστη, ώστε να επιλέξει εκέινες (μέχρι 2) που θεωρέι κατάλληλες για την μπύρα του.
Έπειτα αν δεν βρίσκω από το συνδυασμό αυτών των 2, θα πάιρνω απότελεσμα από την πρωτη πιο σημαντική. Αν δεν υπαρχουν κοινες λεξεις θα του δίνω την δυνατότηα, να 
επιλέξει από όλες τις λέξεις. Θα διαλέγω την πρώτη μπύρα κάθε φορά. Αν δεν βρίσκω καμια κατάλληλη μπύρα θα προσφέρω την επιλογή για επιλογή τυχαίας ή να δώσει
αλλη λέξη κλειδί.

"""


