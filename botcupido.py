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

def fraseAleatoria(genero: str) -> str:
    gen = genero
    if gen.lower() == "#solteiro":
        p1 = ['para este gostoso', 'para este lindo', 'para esta belezura', 'para este chuchuzinho', 'para este colorido da capricho']
        escolha = random.choice(p1)
        return escolha
    elif gen.lower() == "#solteira":
        p1 = ['para esta gostosa', 'para esta linda', 'para esta belezura', 'para esta pitchuquinha', 'para este docinho']
        escolha = random.choice(p1)
        return escolha
    elif gen.lower() == "#solteire":
        p1 = ['para este gostose', 'para este linde', 'para esta belezura', 'para este docinho', 'para este colorido da capricho']
        escolha = random.choice(p1)
        return escolha

def namorade(genero: str) -> str:
    gen = genero
    if gen == '#garotos':
        namo = 'Um namoradinho'
        return namo
    elif gen == '#garotas':
        namo = 'Uma namoradinha'
        return namo
    elif gen == '#garotos':
        namo = 'Ume namoradinhe'
        return namo

def checarTexto(mencoes):
    for item in procurar:
        if item in mencoes[0].text:
            print("achei")
            return True
        else:
            print("nao achei")

def dar_qrt(genero:str, namo:str):
    #tweepy.retweet()
    pass

dar_qrt(checarTexto(mencoes))
escolha = fraseAleatoria('#solteire')
print(escolha)
namo = namorade('#garotos')
print(namo)
'''p1 = ['Um namoradinho', 'Uma namoradinha', 'Ume namoradinhe']'''