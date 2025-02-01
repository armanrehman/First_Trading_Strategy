
# Stock Trading Strategy with Moving Averages

This project implements a simple stock trading strategy based on the 10-day (MA10) and 50-day (MA50) moving averages. The strategy makes buy/sell decisions by comparing the two moving averages:  
- **Buy (long position)**: When MA10 crosses above MA50.
- **Sell (exit position)**: When MA10 crosses below MA50.

The project calculates profits based on these decisions and tracks cumulative wealth over time. It visualizes the results using three plots:
1. Stock price and moving averages.
2. Profit or loss over time.
3. Cumulative wealth from profits.

The user can specify a custom date range for the analysis.

## Features

- **Moving Averages**: Calculates 10-day and 50-day moving averages (MA10 and MA50).
- **Trading Logic**: Executes buy (1) or no action (0) based on MA10 and MA50.
- **Profit Calculation**: Tracks the profit or loss for each buy/sell decision.
- **Wealth Tracking**: Tracks cumulative wealth over time as profits accumulate.
- **Visualization**: Plots showing stock price, profit/loss, and cumulative wealth.
- **example.csv**: CSV file to conveniently test is also attached, however any CSV with stock information will work

## Requirements

- Python 3.x
- `pandas` for data manipulation.
- `matplotlib` for data visualization.

## Run using:
code runner or python3 trading.py

## Process
You will be prompted to input the following:
- Stock data file name: Path to the CSV file (e.g., stock_data.csv).
- Start date: The start date of the analysis period in dd/mm/yyyy format.
- End date: The end date of the analysis period in dd/mm/yyyy format.

## The Code will:
- Calculate the 10-day and 50-day moving averages.
- Execute buy/sell decisions based on the strategy.
- Display three plots:
- Stock Price and Moving Averages: Shows the stock price and moving averages over time.
- Profit/Loss Over Time: Tracks the daily profit or loss.
- Cumulative Wealth: Shows the cumulative wealth from profits over time.
- The total wealth gained at the end of the period will also be printed.

### Image below showcases the graph made when example.csv is executed over entire date range

![Example_Graph](https://github.com/user-attachments/assets/882f42d3-b224-449f-a828-c5291e4f01a5)





