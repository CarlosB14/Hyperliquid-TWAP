import os
import requests
from dotenv import load_dotenv
from getPrice import get_price_and_supply

# Cargar variables de entorno desde el archivo .env
load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')
MESSAGE_THREAD_ID = os.getenv('MESSAGE_THREAD_ID')

def send_telegram_message(message):
    url = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage'
    payload = {
        'chat_id': CHAT_ID,
        'message_thread_id': MESSAGE_THREAD_ID,
        'text': message
    }
    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        print("Message sent successfully")
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"Other error occurred: {err}")

def get_twap_data(token):
    base_url = "https://api.hypurrscan.io/twap/"
    url = f"{base_url}{token}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad status codes
        data = response.json()  # Parse the JSON response
        return data
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")  # Handle HTTP errors
    except Exception as err:
        print(f"Other error occurred: {err}")  # Handle other errors
    return None

def check_conditions(total_s_value, mcap_token):
    return total_s_value >= (mcap_token * 0.005)

def getTwap(token):
    token_price, circulating_supply = get_price_and_supply(token)
    if token_price and circulating_supply:
        data = get_twap_data(token)
        if data:
            buy_twap_total = 0
            sell_twap_total = 0
            for item in data:
                if item.get('ended', None) is None:  # Verificar que el TWAP no haya finalizado
                    s_value = float(item['action']['twap']['s']) * float(token_price)
                    if item['action']['twap']['b']:
                        buy_twap_total += s_value
                    else:
                        sell_twap_total += s_value
            
            mcap_token = float(circulating_supply) * float(token_price)
            
            if check_conditions(buy_twap_total, mcap_token):
                buy_percentage = (buy_twap_total / mcap_token) * 100
                buy_message = f"Buy TWAP {round(buy_twap_total)}$ token {token} ({round(buy_percentage, 2)}% of circulating supply)"
                print(buy_message)
                send_telegram_message(buy_message)
                
            if check_conditions(sell_twap_total, mcap_token):
                sell_percentage = (sell_twap_total / mcap_token) * 100
                sell_message = f"Sell TWAP {round(sell_twap_total)}$ token {token} ({round(sell_percentage, 2)}% of circulating supply)"
                print(sell_message)
                send_telegram_message(sell_message)
        else:
            print(f"Failed to retrieve TWAP data for {token}.")
    else:
        print(f"Failed to retrieve price or supply for {token}.")
