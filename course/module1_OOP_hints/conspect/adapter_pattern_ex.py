import requests


class RequestConnection:
    def __init__(self, request):
        self.request = request

    def get_json_from_url(self, url: str):
        return requests.get(url).json()


class ApiClient:
    def __init__(self, fetch: RequestConnection):
        self.fetch = fetch

    def get_data(self, url):
        return self.fetch.get_json_from_url(url)


def data_adapter(data: list[dict]):
    adapted = []
    for curr in data:
        new_dict = {
            curr.get('ccy'): {
                'buy': curr.get('buy'),
                'sale': curr.get('sale'),
            }
        }
        adapted.append(new_dict)
    return adapted


def pretty_view(data: list[dict[str, dict[str, str]]]):
    pattern = '|{:^10}|{:^10}|{:^10}|'
    print(pattern.format('currency', 'sale', 'buy'))
    for el in data:
        currency, *_ = el.keys()
        sale = el.get(currency).get('sale')
        buy = el.get(currency).get('buy')
        print(pattern.format(currency, sale, buy))


if __name__ == '__main__':
    api_client = ApiClient(RequestConnection(requests))

    data_from_pb_site = api_client.get_data('https://api.privatbank.ua/p24api/pubinfo?exchange&coursid=11')
    print(data_from_pb_site)
    print()
    adapted_data = data_adapter(data_from_pb_site)
    print(adapted_data)
    print()
    pretty_view(adapted_data)

# [{'ccy': 'EUR', 'base_ccy': 'UAH', 'buy': '38.90000', 'sale': '40.48583'}, {'ccy': 'USD', 'base_ccy': 'UAH', 'buy': '36.56860', 'sale': '37.45318'}]
#
# [{'EUR': {'buy': '38.90000', 'sale': '40.48583'}}, {'USD': {'buy': '36.56860', 'sale': '37.45318'}}]
#
# | currency |   sale   |   buy    |
# |   EUR    | 40.48583 | 38.90000 |
# |   USD    | 37.45318 | 36.56860 |
