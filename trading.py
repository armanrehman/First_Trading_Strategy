import pandas as pd
import matplotlib.pyplot as plt

file_path = input("Enter the stock data file name (including .csv): ")
start_date = input("Enter the start date (format: dd/mm/yyyy): ")
end_date = input("Enter the end date (format: dd/mm/yyyy): ")

stock_data = pd.read_csv(file_path)

stock_data['Date'] = pd.to_datetime(stock_data['Date'], format='%d/%m/%Y')
stock_data.set_index('Date', inplace=True)

start_date = pd.to_datetime(start_date, format='%d/%m/%Y')
end_date = pd.to_datetime(end_date, format='%d/%m/%Y')
stock_data = stock_data.loc[start_date:end_date]

stock_data['MA10'] = stock_data['Close'].rolling(10).mean()
stock_data['MA50'] = stock_data['Close'].rolling(50).mean()

stock_data = stock_data.dropna()

stock_data['Shares'] = [1 if stock_data.loc[x, 'MA10'] > stock_data.loc[x, 'MA50'] else 0 for x in stock_data.index]

stock_data['Close1'] = stock_data['Close'].shift(-1)

stock_data['Profit'] = [
    stock_data.loc[x, 'Close1'] - stock_data.loc[x, 'Close'] if stock_data.loc[x, 'Shares'] == 1 else 0
    for x in stock_data.index
]

stock_data = stock_data.dropna()

stock_data['Wealth'] = stock_data['Profit'].cumsum()

fig, axes = plt.subplots(3, 1, figsize=(10, 12))

axes[0].plot(stock_data['MA10'], label='MA10')
axes[0].plot(stock_data['MA50'], label='MA50')
axes[0].plot(stock_data['Close'], label='Close')
axes[0].legend()
axes[0].set_title(f"Stock Price and 10-Day Moving Average from {start_date.strftime('%d/%m/%Y')} to {end_date.strftime('%d/%m/%Y')}")

axes[1].plot(stock_data['Profit'], label='Profit')
axes[1].axhline(y=0, color='red', linestyle='--', label="Zero Profit Line")
axes[1].legend()
axes[1].set_title("Profit Over Time")

axes[2].plot(stock_data['Wealth'], label='Cumulative Wealth')
axes[2].legend()
axes[2].set_title(f"Cumulative Wealth from Profits")

plt.tight_layout()
plt.show()
print(f"Total wealth gained: {stock_data['Wealth'].iloc[-1]:.2f}")
