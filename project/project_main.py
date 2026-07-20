"""
Course Project Milestone 2 - Stock Portfolio Tracker and Analyzer
Author: Reece R. Czarnecki
Class: CS344 Python Programming

A simple command-line program that lets a user add stock positions
(symbol, shares, purchase price, current price), then view each
position's performance and an overall portfolio summary. Built from
the design in milestone1_design.md.

Menu-driven structure:
    1) Add a stock position
    2) View all positions
    3) View portfolio summary
    4) Exit

Each stock position is stored as a dictionary with keys:
    "symbol", "shares", "purchase_price", "current_price"
"""


def display_menu():
    """Print the main menu options. Takes no parameters, returns nothing."""
    print("\n===== Stock Portfolio Tracker =====")
    print("1) Add a stock position")
    print("2) View all positions")
    print("3) View portfolio summary")
    print("4) Exit")


def get_menu_choice():
    """
    Prompt the user for a menu selection and validate it.
    Loops until the user enters an integer from 1-4.
    Returns the valid choice as an int.
    """
    while True:
        raw_choice = input("Select an option (1-4): ").strip()
        try:
            choice = int(raw_choice)
        except ValueError:
            print("That's not a valid number. Please enter 1, 2, 3, or 4.")
            continue

        if choice in (1, 2, 3, 4):
            return choice
        else:
            print("Please choose a number between 1 and 4.")


def get_positive_float(prompt):
    """
    Ask the user for a number and keep asking until it's a valid
    number greater than zero. Returns the value as a float.
    """
    while True:
        raw_value = input(prompt).strip()
        try:
            value = float(raw_value)
        except ValueError:
            print("Please enter a valid number.")
            continue

        if value > 0:
            return value
        else:
            print("Please enter a number greater than zero.")


def add_position(portfolio):
    """
    Collect one stock position from the user (symbol, shares,
    purchase price, current price) and append it to the portfolio
    list. Takes the portfolio list as a parameter; returns nothing.
    """
    symbol = input("Stock symbol: ").strip().upper()
    while symbol == "":
        symbol = input("Symbol can't be blank. Stock symbol: ").strip().upper()

    shares = get_positive_float("Number of shares: ")
    purchase_price = get_positive_float("Purchase price per share: ")
    current_price = get_positive_float("Current price per share: ")

    position = {
        "symbol": symbol,
        "shares": shares,
        "purchase_price": purchase_price,
        "current_price": current_price,
    }
    portfolio.append(position)
    print(f"Added {symbol} to your portfolio.")


def calculate_position(position):
    """
    Calculate the original cost, current value, gain/loss, percentage
    return, and status (Gain/Loss/Break-even) for one stock position.
    Takes a single position dict as a parameter and returns a dict of
    the calculated results.
    """
    original_cost = position["shares"] * position["purchase_price"]
    current_value = position["shares"] * position["current_price"]
    gain_loss = current_value - original_cost

    if original_cost > 0:
        pct_return = (gain_loss / original_cost) * 100
    else:
        pct_return = 0.0

    # Decision: classify the position based on its return
    if pct_return > 0:
        status = "Gain"
    elif pct_return < 0:
        status = "Loss"
    else:
        status = "Break-even"

    return {
        "original_cost": original_cost,
        "current_value": current_value,
        "gain_loss": gain_loss,
        "pct_return": pct_return,
        "status": status,
    }


def display_positions(portfolio):
    """
    Display every stored stock position along with its calculated
    results. Takes the portfolio list as a parameter; returns nothing.
    """
    if not portfolio:
        print("\nYour portfolio is empty. Add a position first.")
        return

    print("\n----- Your Stock Positions -----")
    # Loop through each stored position and print a formatted summary
    for position in portfolio:
        results = calculate_position(position)
        print(f"\n{position['symbol']}")
        print(f"Shares: {position['shares']:g}")
        print(f"Original cost: ${results['original_cost']:,.2f}")
        print(f"Current value: ${results['current_value']:,.2f}")
        print(f"Gain/Loss: ${results['gain_loss']:,.2f}")
        print(f"Return: {results['pct_return']:.2f}%")
        print(f"Status: {results['status']}")


def calculate_portfolio_summary(portfolio):
    """
    Calculate the total cost, total value, total gain/loss, and total
    percentage return across the whole portfolio. Takes the portfolio
    list as a parameter and returns a dict of the totals.
    """
    total_cost = 0.0
    total_value = 0.0

    # Loop through each position and add its cost/value to the running totals
    for position in portfolio:
        results = calculate_position(position)
        total_cost += results["original_cost"]
        total_value += results["current_value"]

    total_gain_loss = total_value - total_cost

    if total_cost > 0:
        total_pct_return = (total_gain_loss / total_cost) * 100
    else:
        total_pct_return = 0.0

    return {
        "total_cost": total_cost,
        "total_value": total_value,
        "total_gain_loss": total_gain_loss,
        "total_pct_return": total_pct_return,
    }


def display_portfolio_summary(portfolio):
    """
    Display the complete portfolio summary (totals across all
    positions). Takes the portfolio list as a parameter; returns
    nothing.
    """
    if not portfolio:
        print("\nYour portfolio is empty. Add a position first.")
        return

    summary = calculate_portfolio_summary(portfolio)

    # Decision: classify the overall portfolio the same way as a single position
    if summary["total_pct_return"] > 0:
        overall_status = "Gain"
    elif summary["total_pct_return"] < 0:
        overall_status = "Loss"
    else:
        overall_status = "Break-even"

    print("\n----- Portfolio Summary -----")
    print(f"Number of positions: {len(portfolio)}")
    print(f"Total portfolio cost: ${summary['total_cost']:,.2f}")
    print(f"Total portfolio value: ${summary['total_value']:,.2f}")
    print(f"Total gain/loss: ${summary['total_gain_loss']:,.2f}")
    print(f"Total return: {summary['total_pct_return']:.2f}%")
    print(f"Overall status: {overall_status}")


def main():
    """Coordinate the overall program flow by calling the other functions."""
    portfolio = []  # list of stock position dicts, kept in memory for this session

    # Loop until the user chooses to exit
    while True:
        display_menu()
        choice = get_menu_choice()

        if choice == 1:
            add_position(portfolio)
        elif choice == 2:
            display_positions(portfolio)
        elif choice == 3:
            display_portfolio_summary(portfolio)
        elif choice == 4:
            print("\nThanks for using the Stock Portfolio Tracker. Goodbye!")
            break


if __name__ == "__main__":
    main()
