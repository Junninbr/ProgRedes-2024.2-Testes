
import requests
import time
import threading


API_TOKEN ='7359699123:AAH43iixaUcoYnsL5f_KiaK0jKDtFZ0n_K4'  
API_URL = f'https://api.telegram.org/bot{API_TOKEN}/'



def mensagens_telegram():
    offset = 0
    while True:
        print("procurando novas mensagens")
        resposta = requests.get(f'{API_URL}getUpdates?offset={offset}')
        mensagens = resposta.json().get('result', [])
        for mensagem in mensagens:
            chat_id = mensagem['message']['chat']['id']
            user_name = mensagem['message']['chat']['first_name']
            text = mensagem['message']['text']
            clientes_telegram = set()
            clientes_telegram.add(chat_id)
            lista_clientes_telegram = list(clientes_telegram)
            print(lista_clientes_telegram[0])
            
            print(f"Nova mensagem de {user_name} ({chat_id}): {text}")
            offset = mensagem['update_id'] + 1
        time.sleep(2)

print("ligado")
t = threading.Thread(target=mensagens_telegram)
t.start()
