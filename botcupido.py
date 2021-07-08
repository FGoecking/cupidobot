from os import read, write
import tweepy
import time
import random

#keys
api_key = ''
api_secret_key = ''
access_token = ''
secret_access_token = ''

#autentificação
auth = tweepy.OAuthHandler(api_key, api_secret_key)
auth.set_access_token(access_token, secret_access_token)

#chamada da api
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

procurar = ['#Solteiro', '#Solteira', '#Solteire', '#solteiro']
p = "solteiro"
mencoes = api.mentions_timeline()
print(mencoes[0].text)

def checarTexto(mencoes):
       for item in procurar:
        if item in mencoes[0].text:
            print("achei")
            return True
        else:
            print("nao achei")

def dar_qrt(checarTexto):
    if checarTexto == True:
        tweepy.retweet()
        print("dei rt")

dar_qrt(checarTexto(mencoes))

