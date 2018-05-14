from module2_actions import *
import pymongo
import json
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy import Cursor
from tweepy import API
import twitterCredentials

connection = pymongo.MongoClient()
db=connection["twitter"]
colection = db.tweets


username=input("ingrese")
twitter_client = TwitterClient(username)
tweets=twitter_client.getTweets()
followers = twitter_client.getFollowers()
favorites = twitter_client.getFavorites()
print(favorites)
username={}
username["tweets"]=tweets
username["numeroDeFollowers"]=followers
username["favoritos"]=favorites



