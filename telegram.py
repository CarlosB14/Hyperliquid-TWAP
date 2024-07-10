import requests
import json

# Obtener actualizaciones del bot
def get_updates(bot_token, offset=None):
    url = f'https://api.telegram.org/bot{bot_token}/getUpdates'
    params = {'offset': offset} if offset else {}
    response = requests.get(url, params=params)
    response.raise_for_status()
    updates = response.json()
    return updates

# Extraer chat_id y message_thread_id de las actualizaciones
def extract_ids(updates):
    chat_id = None
    message_thread_id = None
    
    if 'result' in updates:
        for result in updates['result']:
            if 'message' in result and 'message_thread_id' in result['message']:
                chat_id = result['message']['chat']['id']
                message_thread_id = result['message']['message_thread_id']
                break
    
    return chat_id, message_thread_id

# Enviar mensaje al tópico específico
def send_message_to_topic(bot_token, chat_id, message_thread_id, text):
    url = f'https://api.telegram.org/bot{bot_token}/sendMessage'
    payload = {
        'chat_id': chat_id,
        'message_thread_id': message_thread_id,
        'text': text
    }
    response = requests.post(url, json=payload)
    response.raise_for_status()
    return response.json()

bot_token = '7353127945:AAH4dcBGH-pPbm5ABv0tEO4Cu6_Pv5iJXRQ'
updates = get_updates(bot_token)

# Imprimir las actualizaciones para depuración
print(json.dumps(updates, indent=4))

chat_id, message_thread_id = extract_ids(updates)
print(f"Channel ID: {chat_id}")
print(f"Topic ID: {message_thread_id}")

# Envía un mensaje al tópico específico
if chat_id and message_thread_id:
    send_message_to_topic(bot_token, chat_id, message_thread_id, 'Hello, Topic!')
