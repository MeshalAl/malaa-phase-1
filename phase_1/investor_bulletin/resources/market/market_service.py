""" Market Service """
"""_summary_
this file to write any business logic for the Market
"""
import os
import requests
from resources.market.market_schema import MarketRequest, MarketResponse, MarketPriceResponse

def get_market_data():

    url = "https://twelve-data1.p.rapidapi.com/price"
    # todo: set keys as env variable.
    headers = {
        "X-RapidAPI-Key": str(os.environ.get('RAPID_API_KEY')),
        "X-RapidAPI-Host": str(os.environ.get('RAPID_API_HOST'))
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

            MarketPriceResponse(price_list=price_data)
        except ValueError as e:
            print(e.json())

    return price_data
