import requests

# Free Currency
FREE_CURRENCY_URI = 'https://freecurrencyapi.net/api/v2/latest?apikey=80e4c990-64ba-11ec-a0db-433f7c105da7'

def get_currency_rate(currency):
    response = requests.get(FREE_CURRENCY_URI)
    if response.status_code != 200:
        print(f"unexpected status code {response.status_code}. stopping...")
        raise
    body = response.json()
    data = body['data'][str.upper(currency)]
    return data

