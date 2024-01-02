import psutil
from time import sleep
from random import randint
from datetime import datetime

def imprimir_mensagem_colorida(codigo_cor, mensagem):
    # Função fictícia para imprimir mensagens coloridas no console
    print(f"\033[{codigo_cor}m{mensagem}\033[0m")

def obter_estado_bateria():
    global valor, cor, verificar

    bateria = psutil.sensors_battery()
    percentual_carga = bateria.percent

    if percentual_carga > valor:
        cor = 93 if cor == 91 else 91
        agora = datetime.now()
        hora = agora.strftime("%H:%M:%S")
        valor = percentual_carga
        imprimir_mensagem_colorida(str(cor), f'O percentual subiu de {valor} para {percentual_carga} às {hora}')

    elif percentual_carga < valor:
        cor = 93 if cor == 91 else 91
        agora = datetime.now()
        hora = agora.strftime("%H:%M:%S")
        valor = percentual_carga
        imprimir_mensagem_colorida(str(cor), f'O percentual desceu de {valor} para {percentual_carga} às {hora}')

valor = 0
cor = 0
verificar = 0

while True:
    sleep(2)
    obter_estado_bateria()
