#Universidad del Valle de Guatemala
#Nombre: Marlon Fuentes y Carlos Calderon
#Funcion: Obtencion de tweets
#Modulo: tweepy
import tweepy
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy import Cursor
from tweepy import API
import twitterCredentials


class TwitterClient():
    def __init__(self,twitter_user=None):
        self.auth = TwitterAuthenticator().authenticate()
        self.twitter_client=API(self.auth)
        self.twitter_user=twitter_user

    def getTweets(self):
        tweets=[]
        try:
            for tweet in Cursor(self.twitter_client.user_timeline, id=self.twitter_user).items():
                #for i in lista:
                if (not tweet.retweeted) and ('RT @' not in tweet.text): #and (i in tweet.text):
                    tweets.append(tweet.text)
            return tweets
        except Exception as e:
            print("User Not Found")

    def getFollowers(self):
        followers=[]
        try:
            for i in Cursor(self.twitter_client.followers_ids,id=self.twitter_user).items():
                followers.append(i)
            return len(followers)
        except Exception as e:
            print("Followers empty")
    def getFavorites(self):
        favorites=[]
        try:
            for i in Cursor(self.twitter_client.favorites,id=self.twitter_user).items():
                favorites.append(i.text)
            return favorites
        except Exception as e:
            print("Followers empty")
class TwitterAuthenticator():

    def authenticate(self):
        auth = OAuthHandler(twitterCredentials.CONSUMER_KEY, twitterCredentials.CONSUMER_SECRET)
        auth.set_access_token(twitterCredentials.ACCESS_TOKEN, twitterCredentials.ACCESS_TOKEN_SECRET)
        return auth

class TwitterStreamer():

    def __init__(self):
        self.TwitterAuthenticator = TwitterAuthenticator()

    def stream_tweets(self,filename, hashtag):
        listener = TwitterListener(filename)
        auth = self.TwitterAuthenticator.authenticate()
        stream = Stream(auth, listener)
        stream.filter(track=hashtag)


class TwitterListener(StreamListener):
    def __init__(self, filename):
        self.filename=filename


    def on_data(self,data):
        try:
            with open(self.filename,'a') as tf:
                tf.write(data)
            return True
        except BaseException as e:
            print("Error:%s"%str(e))
        return True

    def on_error(self,status):
        if status ==420:
            return False
        if status==404:
            return False
        print(status)



   # tweeterStreamer= TwitterStreamer()
    #tweeterStreamer.stream_tweets(filename,hashtag)

