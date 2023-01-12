import requests
import pymongo
def test_scrapping():
    response = requests.get("http://127.0.0.1:8000/facebook/lifemovie")
    if response.status_code == 200:
        print("API call is successful")

    else:
        print("API call is failed")

    return response.json()

res = test_scrapping()
print(res)




