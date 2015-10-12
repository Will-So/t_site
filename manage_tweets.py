import os
import twitter


CONSUMER_KEY = os.environ['CONSUMER_KEY']
CONSUMER_SECRET = os.environ['CONSUMER_SECRET']
OAUTH_TOKEN = os.environ['OAUTH_TOKEN']
OAUTH_SECRET = os.environ['OAUTH_SECRET']

twitter_api = twitter.Api(CONSUMER_KEY, CONSUMER_SECRET, OAUTH_TOKEN, OAUTH_SECRET)


US_WOE_ID = 23424977

# trinity = twitter_api.search.tweets.search(q='trinity', geocode=US_WOE_ID)
# trinity = twitter_api.search.tweets.search(q='trinity')
# print trinity

twitter_api.