import requests
import json
 

URL = "http://127.0.0.1:8000/storenum/"
def get_record(id=None):
    data = {}
    if id is not None:
        data['id'] = id 
        json_obj = json.dumps(data)
        res = requests.get(url=URL, data=json_obj)
        data = res.json()
        print("Data from get request: ", data)
#get_record()

def post_record():
    try:
        payload = {'even_field':9}
        json_obj = json.dumps(payload)
        res = requests.post(url=URL, data=json_obj)
        data = res.json()
        print("Data from post request: ",data)
    except Exception as e:
        print("Enable to make a request. Please check your input!")
post_record()
