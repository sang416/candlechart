# Importing necessary modules for backend and data handling
import yfinance as yf
from flask import Flask, render_template, jsonify
import pandas as pd

app = Flask(__name__)

# Function to get the recent 6 months of data from Yahoo Finance for ticker 380170
def get_ticker_data():
    ticker = '381170.KS'  # Assuming ticker is related to Korean exchange
    stock = yf.Ticker(ticker)
    hist = stock.history(period='3mo')
    hist.reset_index(inplace=True)
    return hist

# Route to fetch stock data and render the chart page
@app.route('/')
def index():
    return render_template('index.html')

# Route to provide JSON data for the JavaScript side to generate chart
@app.route('/data')
def data():
    df = get_ticker_data()
    current_price = df['Close'].iloc[-1]
    json_data = {
        "Date": df['Date'].astype(str).tolist(),
        "Open": df['Open'].tolist(),
        "Close": df['Close'].tolist(),
        "High": df['High'].tolist(),
        "Low": df['Low'].tolist(),
        "CurrentPrice": current_price
    }
    return jsonify(json_data)

if __name__ == "__main__":
    app.run(debug=True)