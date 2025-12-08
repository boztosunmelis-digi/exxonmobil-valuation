import yfinance as yf

def get_market_price(ticker: str) -> float:
    """
    Fetch the latest closing price for a given ticker using yfinance.
    """
    data = yf.Ticker(ticker)
    hist = data.history(period="1d")
    if hist.empty:
        raise ValueError(f"No price data returned for ticker {ticker}.")
    return float(hist["Close"].iloc[0])
