# 🪙 Crypto Price Fetcher using Binance API

This project fetches the **live price of any cryptocurrency** (like BTC, ETH) using the **Binance public API**. It's written in Python and uses simple `requests` for API calls.

---

## 🚀 Features

- Get real-time price of any cryptocurrency (e.g., BTCUSDT, ETHUSDT)
- Uses Binance public API (no API key required)
- Simple and clean Python code
- Easy to customize and extend

---

## 🧰 Requirements

- Python 3.7+
- pip

### Install Required Libraries


pip install requests python-dotenv
📁 Project Structure

crypto_price_fetcher/
│
├── .env               # Store your OpenAI key here (if needed)
├── main.py            # Main Python script
├── README.md          # This file
⚙️ How to Use
Clone the repo or copy the code

Create a .env file (optional)

env
OPENAI_API_KEY=your-openai-key-here  # Only needed if you're using GPT later


The current price of BTCUSDT is 65432.78 USD.

🔒 Security Note
⚠️ Never share your API key publicly. Always store it in .env and load using dotenv.








