import requests

if __name__ == '__main__':
    response = requests.get('https://api.privatbank.ua/p24api/pubinfo?exchange&coursid=11')
    exchange_rate = response.json()
    print(exchange_rate)
