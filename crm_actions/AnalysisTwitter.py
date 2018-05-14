from textblob import TextBlob
import sys, tweepy
import matplotlib.pyplot as plt
import twitterCredentials
from tweepy import OAuthHandler

def percentage(parte,entero):
    return 100*float(parte)/float(entero)


auth = OAuthHandler(twitterCredentials.CONSUMER_KEY, twitterCredentials.CONSUMER_SECRET)
auth.set_access_token(twitterCredentials.ACCESS_TOKEN, twitterCredentials.ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

term = input("keyword/hashtag")
tweets= tweepy.Cursor(api.search,q=term,lang="es").items(100)

positivo = 0
negativo =0
neutral =0
polaridad =0
contador=0
for tweet in tweets:
    contador+=1
    analysis= TextBlob(tweet.text)
    polaridad = analysis.sentiment.polarity
    if (analysis.sentiment.polarity==0):
        neutral=0
    elif (analysis.sentences.polarity<0.00):
        negativo=negativo+1
    elif(analysis.sentences.polarity>0.00):
        positivo=positivo+1
positivo = percentage(positivo,contador)
negativo = percentage(negativo,contador)
neutral = percentage(neutral,contador)

positivo = format(positivo,'.2f')
negativo = format(negativo,'.2f')
neutral = format(neutral,'.2f')

labels=['Positive ['+str(positivo)+'%]','Neutral ['+str(neutral)+'%]','Negative ['+str(negativo)+'%]']
sizez=[positivo,neutral,negativo]
colors=["red","yellow","green"]

patches,texts=plt.pie(sizez,colors=colors,startangle=90)

plt.legend(patches,labels,loc="best")
plt.title("Resultado")
plt.axis('equal')
plt.tight_layout()
plt.show()
