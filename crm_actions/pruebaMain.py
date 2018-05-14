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
collection = db.tweets


def ingresarTwitter(theUsername):
    twitter_client = TwitterClient(theUsername)
    tweets=twitter_client.getTweets()
    followers = twitter_client.getFollowers()
    favorites = twitter_client.getFavorites()
    print(tweets)
    print(followers)
    print(favorites)
    username={}
    username["_id"]=theUsername
    username["tweets"]=tweets
    username["numeroDeFollowers"]=followers
    username["favoritos"]=favorites

    collection.insert(username)

def retornarTweets(user):
    lista = []
    var={}
    for i in collection.find({"_id":user}, {"_id": 0, "tweets": 1}):
        lista.append(i)
    var = lista.pop()
    return var["tweets"]

def retornarTweets(user):
    lista = []
    var={}
    for i in collection.find({"_id":user}, {"_id": 0, "numeroDeFollowers": 1}):
        lista.append(i)
    var = lista.pop()
    return var["numeroDeFollowers"]

def retornarFavs(user):
    lista = []
    var={}
    for i in collection.find({"_id":user}, {"_id": 0, "favoritos": 1}):
        lista.append(i)
    var = lista.pop()
    return var["favoritos"]

