import os
import requests
from dotenv import load_dotenv

# .env file se API key load karo
load_dotenv()

# (Agar tum GPT se sawal karoge to ye key lagegi — abhi hum sirf Binance se data le rahe hain, is liye optional hai)
openai_api_key = os.getenv("secret key")
# Binance API se crypto price lene wala function
def get_crypto_price(symbol="BTCUSDT"):
    url = f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return f"The current price of {symbol} is {data['price']} USD."
    else:
        return "Failed to fetch data from Binance."

# Function ko call karo aur result print karo
if __name__ == "__main__":
    symbol = "BTCUSDT"  # ya "ETHUSDT"
    print(get_crypto_price(symbol))
