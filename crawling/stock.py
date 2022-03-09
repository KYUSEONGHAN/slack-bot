import requests as re

def get_stock_info():
    # url = 'https://finance.daum.net/domestic/market_cap'
    url = 'https://finance.daum.net/api/search/ranks?limit=10'

    headers = {
        'Referer': 'http://finance.daum.net',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Mobile Safari/537.36'
    }

    response = re.get(url, headers=headers).json()
    result = []

    for data in response['data']:
        result.append({'순위': data['rank'], '종목명': data['name'], '현재가': data['tradePrice']})

    return '\n'.join(map(str, result))