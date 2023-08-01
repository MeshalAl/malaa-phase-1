""" Market Service """
"""_summary_
this file to write any business logic for the Market
"""

import requests
from market_schema import MarketRequest, MarketResponse, MarketUserResponse

def get_market_data():

    url = "https://twelve-data1.p.rapidapi.com/price"
    # todo: set keys as env variable.
    headers = {
        "X-RapidAPI-Key": "ef06b307c5mshb8a93533838541ep157e8djsn59020e08e0a9",
        "X-RapidAPI-Host": "twelve-data1.p.rapidapi.com"
    }

    symbols = ['AAPL','MSFT','GOOG','AMZN','META']
    price_data = []
    for symbol in symbols:

        MarketRequest(symbol=symbol)
        querystring = {"symbol": symbol,"format":"json","outputsize":"30"}

        response = requests.get(url, headers=headers, params=querystring)

        assert response.status_code == 200,  f"Request failed with status code {response.status_code}"

        try:
            response = MarketResponse(price=response.json().get("price"))

            price_data.append({"symbol": symbol, "price": response.price})

            MarketUserResponse(price_list=price_data)
        except ValueError as e:
            print(e.json())

    return price_data
