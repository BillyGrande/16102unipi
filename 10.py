import time
import datetime
import requests
from operator import itemgetter

print('Give date (DD/MM/YYYY/)')
udate = raw_input()
print('Give currencies (seperated with commas)')
ucny = raw_input()

tsmp = time.mktime(datetime.datetime.strptime(udate, "%d/%m/%Y").timetuple())
lcny = [x.strip() for x in ucny.split(',')]

prices = []
for cny in lcny:
    parameters = { "fsym" : cny, "tsyms": "EUR", "ts": int(tsmp) }
    response = requests.get("https://www.cryptocompare.com/api/data/pricehistorical" , params=parameters)
    data = response.json()
    try:
        price = data["Data"][0]['Price']
        prices.append(price)
    except IndexError:
        prices.append(0)

combined = zip(lcny,prices)
#print combined
result = sorted(combined, key=itemgetter(1), reverse=True)
#print result

for out in result:
    print(out[0] + ': ' + str(out[1]) + ' EUR \n')


    
    
    
