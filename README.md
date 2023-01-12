# Fast_api_scraper

 FastAPI web service that allows scraping Facebook posts by specifying a main topic of the post. The service uses the facebook_scraper package to scrape posts and the pymongo package to save the scraped posts in a MongoDB collection called facebookposts.
 
 The code first creates a MongoClient instance, which will allow you to connect to a MongoDB server running on the localhost on port 27017.

Then, it defines an endpoint /facebook/{username} that accepts a post_main_topic parameter. The endpoint uses the get_posts function from the facebook_scraper package to scrape posts from Facebook based on the provided main topic and the pages parameter is set to 3, so the function will scrape 3 pages of data.
