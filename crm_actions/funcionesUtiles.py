from module2_actions import *
import pymongo
import json
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy import Cursor
from tweepy import API
import twitterCredentials

import re


connection = pymongo.MongoClient()
db=connection["twitter"]
collection = db.tweets


def ingresarTwitter(theUsername):
    twitter_client = TwitterClient(theUsername)
    tweets=twitter_client.getTweets()
    followers = twitter_client.getFollowers()
    favorites = twitter_client.getFavorites()
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

def retornarFollowers(user):
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


def retornarListaTweetsCategoria(categorias):
    lista=[]
    listaResultado=[]
    dic={}
    for j in categorias:
        regex=re.compile("^"+j,re.IGNORECASE)
        for i in collection.find({"tweets": {"$regex": regex}}, {"tweets": {"$elemMatch": {"$regex": regex}}}):
            lista.append(i)
        dic = lista.pop()
        listaResultado.append(dic["tweets"])
    return listaResultado

def todosLosTweets():
    lista=[]
    listaResultado=[]
    for i in collection.find({},{"_id":0,"tweets":1}):
        lista.append(i)
    listaDeListas= [d['tweets'] for d in lista]
    listaResultado=[]
    for row in listaDeListas:
        for elem in row:
            listaResultado.append(elem)
    return listaResultado
def influencers():
    listaUsers=[]
    for i in db.tweets.find({"numeroDeFollowers":{"$gt":1000}},{"_id":1}):
        listaUsers.append(i["_id"])
    return listaUsers
a=influencers()
print(a)
