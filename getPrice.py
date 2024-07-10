import requests

def get_data(url, payload):
    headers = {"Content-Type": "application/json"}
    response = requests.post(url, headers=headers, json=payload)
    response.raise_for_status()
    return response.json()

def get_price_and_supply(token_name):
    base_url = "https://api.hyperliquid.xyz/info"
    
    # Obtener el contexto de los activos del mercado spot
    spot_context_payload = {"type": "spotMetaAndAssetCtxs"}
    spot_context = get_data(base_url, spot_context_payload)
    
    # Buscar el token en el universo para obtener su índice
    token_index = None
    for token in spot_context[0]['tokens']:
        if token['name'] == token_name:
            token_index = token['index']
            break
    
    if token_index is None:
        print(f"{token_name} token not found in spot metadata.")
        return None, None
    
    # Buscar el precio de marca y la oferta circulante del token en el contexto del mercado spot
    for universe in spot_context[0]['universe']:
        if token_index in universe['tokens']:
            for asset in spot_context[1]:
                if asset['coin'] == universe['name']:
                    markPx = asset.get('markPx')
                    circulatingSupply = asset.get('circulatingSupply')
                    if markPx and circulatingSupply:
                        print(f"The mark price of {token_name} is: {markPx}")
                        print(f"The circulating supply of {token_name} is: {circulatingSupply}")
                        return markPx, circulatingSupply
                    else:
                        print(f"{token_name} mark price or circulating supply not found.")
                        return None, None

    print(f"{token_name} mark price not found in the spot context.")
    return None, None
