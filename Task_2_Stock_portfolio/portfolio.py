
import csv

# Read stock symbols and company names from CSV
companies = {}

with open("constituents.csv", "r", encoding="utf-8-sig", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        symbol = row["Symbol"]
        company = row["Security"]

        companies[symbol] = company
 
# Read sample current prices from CSV
stock_prices = {}

with open("stock_prices.csv", "r", encoding="utf-8-sig", newline="") as file:
    reader = csv.DictReader(file)
    

    for row in reader:
        symbol = row["Symbol"]
        price = float(row["CurrentPrice"])

        stock_prices[symbol] = price
       


# Stock Portfolio Performance Tracker

# Ask how many stocks the user wants to enter

# Ask how many stocks the user wants to enter
while True:
    try:
        num_stocks = int(input("How many stocks do you want to add? "))

        if num_stocks > 0:
            break
        else:
            print("Number of stocks must be greater than 0.")

    except ValueError:
        print("Invalid input! Please enter a whole number.")



# Initialize portfolio totals
portfolio_investment = 0
portfolio_value = 0


# Store information about all stocks
stocks_data = []
portfolio = {}


# Repeat for each stock
for i in range(num_stocks):

    print("\nStock Number:", i + 1)

    
    stock_name = input("Enter stock symbol: ").strip().upper()

    
    if stock_name not in companies:
        print("Stock symbol not found in S&P 500 dataset.")
        continue

    if stock_name not in stock_prices:
        print("Price not found in stock_prices.csv")
        continue

    print("Company:", companies[stock_name])


    
    while True:
        try:
            buy_price = float(input("Enter buying price per share: "))

            if buy_price > 0:
                break
            else:
                print("Buying price must be greater than 0.")

        except ValueError:
            print("Invalid input! Please enter a valid number.")

    
    while True:
        try:
            quantity = int(input("Enter number of shares: "))

            if quantity > 0:
                break
            else:
                print("Quantity must be greater than 0.")

        except ValueError:
            print("Invalid input! Please enter a whole number.")

    
    # Look up current price from sample CSV
    if stock_name in stock_prices:
        current_price = stock_prices[stock_name]
        print("Sample Current Price:", current_price)
    else:
        print("Price not found in stock_prices.csv")
        print("Please enter a stock listed in the sample price file.")
        continue


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
    if total_investment > 0:
        percentage = (profit_loss / total_investment) * 100
    else:
        percentage = 0


    
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
     
    # Store portfolio position in a dictionary
    portfolio[stock_name] = {
        "buy_price": buy_price,
        "quantity": quantity,
        "current_price": current_price,
        "investment": total_investment,
        "current_value": current_value,
        "profit_loss": profit_loss,
        "percentage": percentage
    }


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

