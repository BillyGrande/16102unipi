import requests
import json

def KeywordSaving (key,p):
    parameters = { "q": key, "type": "beer", "key": "4b9cf1ce5dd3698db3760f0e803df6f6", "format": "json" , "p":p}
    print(p)
    response = requests.get("https://api.brewerydb.com/v2/search" , params=parameters)
    data = response.json()
    return data

def Counting(word,input_string):
    in_st = input_string.split()
    counter = in_st.count(word)
    return counter

print("Δώσε λέξεις κλειδιά (χωρισμένες με κόμμα)")
words = input()
keywords = [x.strip() for x in words.split(',')]

NOP = [] #nop = numberOfPages
bName = []
bDes= []
bId = []
found = []
for key in keywords:
    p=0
    data = KeywordSaving(key,str(p));
    try:
        lp=data["numberOfPages"]
        lp = int(lp)
        NOP.append(lp)
        while p < lp:
            p = p + 1
            data = KeywordSaving(key,str(p));
            for beer in data["data"]:
                bName.append(beer["name"])
                bId.append(beer["id"])
                try:
                    bDes.append(beer["description"])
                except KeyError:
                    bDes.append(' ')
    except KeyError:
        data="" 
        NOP.append(0)

for key in keywords:
    if key == keywords[0]:
        for des in bDes:
            found.append(Counting(key,des))
    else:
        ind = 0
        for des in bDes:
            found[ind] = found[ind] + Counting(key,des)
            ind = ind +1

maxvalue = max(found)
indices = [i for i, x in enumerate(found) if x == maxvalue]

print("Οι μπύρες με τις περισσότερες λέξεις κλειδια είναι")
for index in indices:
    print(bName[index])

print("Οι λέξεις κλειδιά εμφανίσητκαν " + str(maxvalue) + " φορές")
