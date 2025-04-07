import streamlit as st
from utils.portfolio import get_live_price
import datetime

st.set_page_config(page_title="📈 Indian Stock Portfolio Tracker", layout="wide")
st.title("📈 Indian Stock Portfolio Tracker")

st.markdown("Track your Indian stock investments in real-time with live prices and performance breakdown.")

# --- Input form for manual entry ---
with st.form("txn_form"):
    col1, col2, col3 = st.columns(3)
    with col1:
        symbol = st.text_input("Stock Symbol (e.g., TCS.NS)")
    with col2:
        txn_date = st.date_input("Transaction Date", value=datetime.date.today())
    with col3:
        txn_type = st.selectbox("Type", ["BUY", "SELL"])

    qty = st.number_input("Quantity", min_value=1)
    price = st.number_input("Price per Share (₹)", min_value=0.0, format="%.2f")
    submitted = st.form_submit_button("Add Transaction")

    if submitted and symbol:
        st.success(f"{txn_type} {qty} shares of {symbol} at ₹{price} on {txn_date}")
    elif submitted:
        st.error("Please enter a valid stock symbol.")

# --- Live Price Check ---
st.subheader("🔍 Check Live Stock Price")
check_symbol = st.text_input("Enter Indian Stock Symbol (e.g., INFY.NS):")

if check_symbol:
    price = get_live_price(check_symbol)
    if price:
        st.success(f"Current Price of {check_symbol}: ₹{price:.2f}")
    else:
        st.error("Failed to fetch price. Try a valid NSE symbol like RELIANCE.NS")
