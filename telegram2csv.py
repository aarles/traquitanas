
# É necessário passar o caminho para o arquivo 'result.json' gerado pela exportação de dados do Telegram.
#
# python3 telegram2csv.py <result.json>

import json
import numpy as np 
import pandas as pd 
from sys import argv
import time

t = time.localtime()
tempo = time.strftime('%d-%b-%y_%H%M', t)

def load_json(arq):
    return json.loads(open(arq).read())

base = load_json(argv[1])    

mensagens = base['messages']

pddf = pd.DataFrame(mensagens)

pddf.to_csv(tempo + '_convert.csv')
