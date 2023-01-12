import requests
import pymongo
def test_scrapping():
    response = requests.get("http://0.0.0.0:8000/facebook/NintendoSwitch")
    if response.status_code == 200:
        print("API call is successful")

    else:
        print("API call is failed")

    return response.json()

res = test_scrapping()
print(res)




