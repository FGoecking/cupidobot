from time import sleep
import tweepy
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



def retornarURL(json) -> str:
    '''
    Pega o namespace do tweet junto com o ID do tweet e retorna como um link
    para que possa ser feito um quote
    '''
    jason = json[0]._json
    tweet_id = jason.get('id')
    tweet_namespace = jason.get('user')
    namespace = tweet_namespace.get('screen_name')
    print(namespace)

    url = ('https://twitter.com/%s/status/%s?s=20' % (namespace, tweet_id))
    return url

def retornarTexto(json) -> str:
    '''
    Busca uma # entre as listas de # e chama a função para criar a frase aleatória
    do tweet, retornando a frase aleatória (string)
    '''

    gen = ['#solteiro', '#solteira', '#solteire']
    namo = ['#namorada', '#namorado', '#namorade']
    i, j = 'string', 'string'
    jason = json[0]._json
    tweet_text = jason.get('text')
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
                
            
    
def checarImagem(json):
    '''
    Verifica se um tweet marcando o bot tem ou não imagem
    '''
    jason = json[0]._json
    entities = jason.get('entities')
    media = entities.get('media')
    if media != None:
        return True
    else:
        return False

def retornarID(json):
    jason = json[0]._json
    tweet_id = jason.get('id')
    return tweet_id

def retornarArroba(json):
    jason = json[0]._json
    tweet_user = jason.get('user')
    tweet_arroba = tweet_user.get('screen_name')
    return tweet_arroba

mencoes = api.mentions_timeline()


while True:
    mencoes = api.mentions_timeline()
    checando = checarImagem(mencoes)
    if checando == True:
        texto = retornarTexto(mencoes)
        url = retornarURL(mencoes)
        tweet = ("%s %s"% (texto, url))
        api.update_status(tweet)
        print('retuitado')
    elif checando != True:
        tweet_arroba = retornarArroba(mencoes)
        tweet_id = retornarID(mencoes)
        tweet = ('@%s Use uma fotinha para chamar atenção!' % (tweet_arroba))
        api.update_status(status=tweet, in_reply_to_status_id=tweet_id)
        print('tweet sem fotinha')
    sleep(120)


