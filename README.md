# 📈 Indian Stock Portfolio Tracker

A clean, minimal web-based application to **track and visualize your Indian stock investments** in real-time.  
Built using Python, Streamlit, and Yahoo Finance (yfinance).

## 🚀 Features

- 📊 Live portfolio tracking using real-time NSE stock data  
- 📝 Manual transaction input (Buy/Sell)  
- 📥 CSV upload support (coming soon)  
- 💸 Calculates current value, investment, and returns  
- 📈 Live stock price checker  
- 🧠 Modular structure for future expansion  
- 📂 Local session-based storage (can be extended to DB)  

## 🛠️ Tech Stack

- Python 3.7+
- Streamlit – for web UI
- yfinance – stock data from Yahoo Finance
- pandas – data manipulation
- plotly – for charts and visuals (coming in next phases)

## 📦 Setup Instructions

1. Clone the repo:

```bash
git clone https://github.com/your-username/indian-portfolio-tracker.git
cd indian-portfolio-tracker
```

2. Create and activate virtual environment:

```bash
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the Streamlit app:

```bash
streamlit run app.py
```

## 📋 Sample Transaction Format

CSV file example:
```
Symbol,Date,Type,Quantity,Price
TCS.NS,2024-01-10,BUY,5,3600
INFY.NS,2024-02-15,BUY,10,1400
```

## 📌 Roadmap

- ✅ Basic app with manual input  
- 🔄 Add CSV upload  
- 📈 Portfolio allocation and growth charts  
- 💡 Return metrics (XIRR, Total Return)  
- 🔒 Optional login + DB persistence  
- 📊 Benchmark comparison (e.g., NIFTY50)

## 🧠 Ideal For

- Indian retail investors  
- Beginners managing stocks outside Zerodha/Groww  
- Students building personal finance projects  
- Python + Finance portfolio building  

---

Crafted with ❤️ by [Hafeez Baig](https://hafeezbaig.in)

