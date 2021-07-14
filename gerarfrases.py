import random

def genero(genero: str) -> str:
    gen = genero.lower()
    if gen == "#solteiro":
        p1 = ['para este gostoso', 'para este lindo', 'para esta belezura', 'para este chuchuzinho', 'para este colorido da capricho']
        escolha = random.choice(p1)
        return escolha
    elif gen == "#solteira":
        p1 = ['para esta gostosa', 'para esta linda', 'para esta belezura', 'para esta pitchuquinha', 'para este docinho']
        escolha = random.choice(p1)
        return escolha
    elif gen == "#solteire":
        p1 = ['para este gostose', 'para este linde', 'para esta belezura', 'para este docinho', 'para este colorido da capricho']
        escolha = random.choice(p1)
        return escolha
    else:
        return 'para essa pessoa'

def namorade(namorade: str) -> str:
    gen_namo = namorade.lower()
    if gen_namo == '#namorado':
        namo = 'Um namoradinho'
        return namo
    elif gen_namo == '#namorada':
        namo = 'Uma namoradinha'
        return namo
    elif gen_namo == '#namorade':
        namo = 'Ume namoradinhe'
        return namo
    else:
        namo = 'Um amor'
        return namo

def fraseAleatoria(gene:str, namo:str) -> str:
    gen = genero(gene)
    gen_namo = namorade(namo)
    frase =  ("%s %s"% (gen_namo, gen))
    return frase