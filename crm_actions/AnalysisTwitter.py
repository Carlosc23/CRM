from textblob import TextBlob
import sys, tweepy
import matplotlib.pyplot as plt
import twitterCredentials
from tweepy import OAuthHandler

import re


def porcentaje(total,valor):
    return 100*(float(valor)/float(total))

def sentimentAnalysis(termino,numero):
    auth = OAuthHandler(twitterCredentials.CONSUMER_KEY, twitterCredentials.CONSUMER_SECRET)
    auth.set_access_token(twitterCredentials.ACCESS_TOKEN, twitterCredentials.ACCESS_TOKEN_SECRET)

    api = tweepy.API(auth)


    tweets= tweepy.Cursor(api.search,q=termino).items(numero)

    positivo =0
    negativo = 0
    neutral=0
    polaridad=0

    for tweet in tweets:
        analysis=TextBlob(tweet.text)
        polaridad+=analysis.sentiment.polarity
        if(analysis.sentiment.polarity==0):
            neutral+=1
        elif(analysis.sentiment.polarity<0):
            negativo+=1
        elif(analysis.sentiment.polarity>0):
            positivo+=1
    positivo=porcentaje(numero,positivo)
    neutral = porcentaje(numero,neutral)
    negativo=porcentaje(numero,negativo)

    positivo=format(positivo,'.2f')
    neutral=format(neutral,'.2f')
    negativo=format(negativo,'.2f')

    print("termino"+termino+"analizando"+str(numero)+"tweets")
    if(polaridad==0):
        print("Neutral")
    elif(polaridad<0):
        print("Negativo")
    elif(polaridad>0):
        print("Positivo")

    print(positivo)
    print(negativo)
    print(neutral)
    labels=['Positivo['+str(positivo)+'%]','Neutral['+str(neutral)+'%]','Negativo['+str(negativo)+'%]']
    size=[positivo,neutral,negativo]
    colors=["red","yellow","green"]

    patches,text=plt.pie(size,colors=colors,startangle=90)
    plt.legend(patches,labels,loc="best")
    plt.title("termino"+" "+termino+" "+"analizando"+" "+str(numero)+" "+"tweets")
    plt.axis('equal')
    plt.tight_layout()
    return plt.savefig("image.png")



