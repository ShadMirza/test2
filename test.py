
#Import Libraries
import requests
import json
from time import time, sleep
import datetime
#url source is Cowin API - https://apisetu.gov.in/public/api/cowin
while True:
    response=requests.get("https://cdn-api.co-vin.in/api/v2/admin/location/states")
    data=response.json()
    message_string=json.dumps(data)
    requests.get("https://api.telegram.org/bot1917545795:AAEZLwtmBumgTnZ4iF5aSjqzZvj-gVAtC7c/sendMessage?chat_id=-508413228&text="+message_string)
    sleep(30 - time() % 30)
    # time.sleep(10)
