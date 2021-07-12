from os import read, write
import tweepy
import random
from gerarfrases import fraseAleatoria

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

procurar = ['#Solteiro', '#Solteira', '#Solteire']
mencoes = api.mentions_timeline()


def retornarURL(urllocal) -> str:
    '''
    Pega o namespace do tweet junto com o ID do tweet e retorna como um link
    para que possa ser feito um quote
    '''
    json = urllocal[0]._json
    tweet_id = json.get('id')
    tweet_namespace = json.get('user')
    namespace = tweet_namespace.get('screen_name')
    print(namespace)

    url = ('https://twitter.com/%s/status/%s?s=20' % (namespace, tweet_id))
    return url

def retornarTexto(urllocal) -> str:

    gen = ['#solteiro', '#solteira', '#solteire']
    namo = ['#namorada', '#namorado', '#namorade']
    i, j = 'string', 'string'
    json = urllocal[0]._json
    tweet_text = json.get('text')
    print(tweet_text)
    
    for i in gen:
        if i in tweet_text:
            genero = i
            for j in namo:
                if j in tweet_text:
                
                    namor = j
                    print(genero)
                    print(namor)
                    frase = fraseAleatoria(genero, namor)
                    return frase
                
            
    


url = retornarURL(mencoes)
texto = retornarTexto(mencoes)

tweet = texto+' '+ url
api.update_status(tweet)




'''def checarTexto(mencoes):
    for item in procurar:
        if item in mencoes[0].text:
            print("achei")
            return True
        else:
            print("nao achei")
    
    
    print(json.get('text'))'''


