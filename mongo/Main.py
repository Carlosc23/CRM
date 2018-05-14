from tweet_streamer import *
import json

if __name__=="__main__":
    lista=[]
    hashtag=["obama"]
    filename="tweets.txt"
    twitter_client = TwitterClient('pycon')
    tweets=twitter_client.getTweets(1)

