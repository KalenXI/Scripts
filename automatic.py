token = "xxxxxxx" #Put API token from Automatic here.

import requests
from datetime import datetime
import json

addMonth = 2592000

startDate = datetime(2018,11,1,0,0).timestamp() #Put the date you want to start exporting from here
endDate = startDate + addMonth

datafile = open('data.json', 'a')

while endDate < datetime(2020,6,2,0,0).timestamp():
    url = "https://api.automatic.com/trip/?limit=250&started_at__gte=" + str(startDate) + "&started_at__lte=" + str(endDate)
    print("URL: " + url)
    headers = {"Authorization": "Bearer " + token}
    print("Headers: " + str(headers))

    tripjson = requests.get(url, headers=headers).json()
    tripjson["results"]
    json.dump(tripjson["results"], datafile)
    startDate = endDate
    endDate = startDate + addMonth

#Once the data is exported, do a search and replace for all instances of "][" and replace them with "," to get valid JSON.