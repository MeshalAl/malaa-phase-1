""" Market Service """
"""_summary_
this file to write any business logic for the Market
"""
import requests
import json

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

        querystring = {"symbol": symbol,"format":"json","outputsize":"30"}

        response = requests.get(url, headers=headers, params=querystring)

        assert response.status_code == 200,  f"Request failed with status code {response.status_code}"

        try:
           response_json = response.json()
           price = response_json.get("price")
           assert price, "Reponse returned Symbol price at 0."
            # add validator here, raise on validator error.

           price_data.append({"symbol": symbol, "price": price})
        except json.JSONDecodeError as e:
            assert False, f"Failed to parse response JSON: {e}"

    return price_data
