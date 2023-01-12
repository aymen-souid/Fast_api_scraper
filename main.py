from fastapi import FastAPI
from facebook_scraper import get_posts
import uvicorn
import pymongo
import json

app = FastAPI()




client = pymongo.MongoClient('mongodb://127.0.0.1:27017/')


@app.get("/facebook/{username}",
         summary="Please specify the key topic for which you wish to scrape Facebook posts.")
async def scraping_function(username: str):

        # if we choose a value less than 2, we risk of not getting data from this code instruction
        facebook_posts = list(get_posts(username,
                                        pages=3))
        for post in facebook_posts:
            mydb = client['Scraping']
            information = mydb.facebookposts

            #save only values with type list
            record = {k:v for k,v in post.items() if type(v)!=list}
            record['username'] = username

            information.insert_one(record)

        last_main_infos = {
            "username": record['username'],
            'text': record['text'],
            'likes': record['likes'],
            'comments': record['comments'],
            'shares': record['shares']
        }

        return {"last_main_infos":last_main_infos}


if __name__ == '__main__':
    uvicorn.run(app, port=8000, host="127.0.0.1")