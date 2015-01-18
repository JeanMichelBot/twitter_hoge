# coding:utf-8
from twython import Twython, TwythonError, TwythonRateLimitError
from settings import *
import time
from datetime import datetime

# Requires Authentication as of Twitter API v1.1
twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
print("Authentication Succeeded...")

user_timeline = []
# Function used to get tweet data
def get_tweet (**params):
    print("get_tweet()")
    global user_timeline
    try:
        # Get user_timeline
        user_timeline = twitter.get_user_timeline(**params)
        print("User Timeline Acquired...")
    except TwythonError as e:
        print(e)

# Function used to print tweet data
def print_tweet (tweet):
    print("print_tweet()")
    if tweet != None:
        for i in tweet:
            print("ID : " + str(i['id']) + "\t" + "Remaining API : " + str(api))
    else : 
        print("No tweets!")

# Get tweet data and remaining API 
get_tweet(
        screen_name = 'jeanmichel_bot',
        include_rts = True,
        count = 2,
        #since_id = 0,
        #max_id = 0
)
print("get_tweet()")
api = int(twitter.get_lastfunction_header('X-Rate-limit-remaining'))
# Get tweet data while remaining API > 0 
max_id = user_timeline[-1]['id'] - 1
while  api > 0:
    print_tweet(user_timeline)
    get_tweet(
            screen_name = 'jeanmichel_bot',
            include_rts = True,
            count = 2,
            #since_id = 0,
            max_id = max_id
    )
    max_id = user_timeline[-1]['id'] - 1
    api = api - 1

    if api == 0 :
        start = time.time()
        end = int(twitter.get_lastfunction_header('X-Rate-limit-Reset'))
        rem = end - start + 5
        print("Remaining API : " + str(api) )
        print("Please wait " + str(rem) + "sec")
        time.sleep(rem)

