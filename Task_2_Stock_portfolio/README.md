# Stock Portfolio Performance Tracker

## Project Description
This project is developed as part of the Datheon Python Programming Internship.

The Stock Portfolio Performance Tracker is a Python-based application that helps users calculate and track the performance of their stock investments.

## Features
- Accepts multiple stock ticker symbols.
- Takes buying prices and share quantities as user input.
- Reads company names from the S&P 500 dataset.
- Automatically retrieves sample stock prices from a CSV file.
- Stores stock information using Python dictionaries.
- Calculates total invested capital and current market value.
- Calculates profit/loss and percentage gain/loss for each stock.
- Displays overall portfolio performance.
- Exports the portfolio summary to a CSV file.

## Technologies Used
- Python 3
- CSV module
- File Handling
- Dictionaries
- Loops and Conditional Statements

## Project Files
- `portfolio.py` — Main Python program.
- `constituents.csv` — S&P 500 company names and ticker symbols.
- `stock_prices.csv` — Sample stock prices used for calculations.
- `portfolio_summary.csv` — Generated portfolio performance report.
- `README.md` — Project documentation.

## How to Run
1. Download or clone the repository.
2. Open the `Task_2_Stock_portfolio` folder in Command Prompt.
3. Make sure `constituents.csv` and `stock_prices.csv` are in the same folder as `portfolio.py`.
4. Run the following command:

   `py portfolio.py`

5. Enter the number of stocks, ticker symbols, buying prices, and share quantities.
6. View the calculated portfolio performance.
7. Open `portfolio_summary.csv` to see the saved results.

## Example
Stock Symbol: AAPL

Buying Price: 150

Quantity: 5

Sample Current Price: 180

Total Investment: 750

Current Market Value: 900

Profit: 150

Percentage Gain: 20%

## Note
The project uses sample stock prices from `stock_prices.csv` for educational purposes. These are not real-time market prices.

## Internship
Datheon Python Programming Internship — Task 2
