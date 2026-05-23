import yfinance as yf

# Télécharger données Apple
data = yf.download("AAPL", start="2015-01-01", end="2024-01-01")

print(data.head())