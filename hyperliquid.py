import requests
from getPrice import get_price_and_supply

def send_telegram_message(message):
    bot_token = '7353127945:AAH4dcBGH-pPbm5ABv0tEO4Cu6_Pv5iJXRQ'
    chat_id = '2073678371/118'
    url = f'https://api.telegram.org/bot{bot_token}/sendMessage'
    payload = {
        'chat_id': chat_id,
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

def check_conditions(item, token_price, circulating_supply):
    try:
        s_value = float(item['action']['twap']['s']) * float(token_price)
        ended_value = item.get('ended', None)
        mcap_token = float(circulating_supply) * float(token_price)

        if (s_value >= (mcap_token * 0.00001)) and (ended_value is None):
            return True
        else:
            return False
    except KeyError as e:
        print(f"Key error: {e}")
        return False

def getTwap(token):
    token_price, circulating_supply = get_price_and_supply(token)
    if token_price and circulating_supply:
        data = get_twap_data(token)
        if data:
            for item in data:
                if check_conditions(item, token_price, circulating_supply):
                    print(f"Matching TWAP data found for {token}:")
                    action_type = "Buy" if item['action']['twap']['b'] else "Sell"
                    twap_value = round(float(item['action']['twap']['s']) * float(token_price))
                    message = f"{action_type} TWAP {twap_value}$ token {token}"
                    print(message)
                    send_telegram_message(message)
        else:
            print(f"Failed to retrieve TWAP data for {token}.")
    else:
        print(f"Failed to retrieve price or supply for {token}.")
