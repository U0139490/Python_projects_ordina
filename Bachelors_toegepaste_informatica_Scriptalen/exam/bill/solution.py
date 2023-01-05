# Write your solution in this file
import json

catalog = {}

with open("catalog.json",'r') as f:
    catalog = json.load(f)

totalPrices = {}
with open("orders.json",'r') as f:
    data = json.load(f)
    for dicOrders in data:
        if dicOrders['credit_card'] in totalPrices:
            for boeknumber in dicOrders['items']:
                totalPrices[dicOrders['credit_card']] += catalog[boeknumber]
        
        if dicOrders['credit_card'] not in totalPrices:
            totalPrices[dicOrders['credit_card']] = 0
            for boeknumber in dicOrders['items']:
                totalPrices[dicOrders['credit_card']] += catalog[boeknumber]


sort = sorted(totalPrices.items(), key=lambda x:(x[0],x[1]))
with open('output.txt','w') as out:
    for key,value in sort:
        out.write(key)
        out.write (" ")
        out.write(str(value))
        out.write("\n")