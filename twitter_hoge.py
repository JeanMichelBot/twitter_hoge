# coding:utf-8
from twython import Twython, TwythonError, TwythonRateLimitError
from settings import *
import time
from datetime import datetime

# Requires Authentication as of Twitter API v1.1
twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
print("Authentication Succeeded...")

# Function used to get tweet data
def get_tweet (**params):
	print("get_tweet()")
	global user_timeline
	try:
		# Get user_timeline
		user_timeline = twitter.get_user_timeline(screen_name = screen_name, include_rts = include_rts, count = count, since_id = since_id, max_id = since_id)
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
get_tweet()
print("get_tweet()")
api = int(twitter.get_lastfunction_header('X-Rate-limit-remaining'))

# Get tweet data while remaining API > 0 
while  api > 0:
	print_tweet(user_timeline)
	get_tweet()
	api = api - 1

if api == 0 :
	start = time.time()
	end = float(twitter.get_lastfunction_header('X-Rate-limit-Reset'))
	rem = (end - start)/1000
	print("Remaining API : " + str(api) )
	print("Please wait " + str(rem) + "sec")