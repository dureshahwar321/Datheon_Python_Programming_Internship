
import csv

# Stock Portfolio Performance Tracker

# Ask how many stocks the user wants to enter
num_stocks = int(input("How many stocks do you want to add? "))


# Initialize portfolio totals
portfolio_investment = 0
portfolio_value = 0


# Store information about all stocks
stocks_data = []



# Repeat for each stock
for i in range(num_stocks):

    print("\nStock Number:", i + 1)

    stock_name = input("Enter stock symbol: ")
    buy_price = float(input("Enter buying price per share: "))
    quantity = int(input("Enter number of shares: "))
    current_price = float(input("Enter current stock price: "))

    # Calculate investment
    total_investment = buy_price * quantity

    # Calculate current market value
    current_value = current_price * quantity

    
   # Add each stock's values to portfolio totals
    portfolio_investment = portfolio_investment + total_investment
    portfolio_value = portfolio_value + current_value
     

    # Calculate profit or loss
    profit_loss = current_value - total_investment

    # Calculate percentage gain or loss
    percentage = (profit_loss / total_investment) * 100

    
    # Store stock information
    stocks_data.append([
        stock_name,
        buy_price,
        quantity,
        current_price,
        total_investment,
        current_value,
        profit_loss,
        percentage
    ])


    # Display results
    print("\nPortfolio Performance")
    print("Stock Symbol:", stock_name)
    print("Total Investment:", total_investment)
    print("Current Market Value:", current_value)
    print("Profit/Loss:", profit_loss)
    print("Percentage Gain/Loss:", percentage, "%")

# Calculate overall portfolio performance
overall_profit_loss = portfolio_value - portfolio_investment

if portfolio_investment > 0:
    overall_percentage = (overall_profit_loss / portfolio_investment) * 100
else:
    overall_percentage = 0

# Display overall portfolio summary
print("\n========== Portfolio Summary ==========")
print("Total Investment:", portfolio_investment)
print("Total Current Value:", portfolio_value)
print("Overall Profit/Loss:", overall_profit_loss)
print("Overall Gain/Loss Percentage:", overall_percentage, "%")


# Save portfolio data to a CSV file
with open("portfolio_summary.csv", "w", newline="") as file:

    writer = csv.writer(file)

    # Write column headings
    writer.writerow([
        "Stock Symbol",
        "Buying Price",
        "Quantity",
        "Current Price",
        "Total Investment",
        "Current Value",
        "Profit/Loss",
        "Percentage"
    ])

    # Write stock data
    writer.writerows(stocks_data)

    # Write overall portfolio summary
    writer.writerow([])
    writer.writerow(["Portfolio Summary"])
    writer.writerow(["Total Investment", portfolio_investment])
    writer.writerow(["Total Current Value", portfolio_value])
    writer.writerow(["Overall Profit/Loss", overall_profit_loss])
    writer.writerow(["Overall Percentage", overall_percentage])

print("\nPortfolio summary saved successfully!")

