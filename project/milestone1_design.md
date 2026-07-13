# Course Project Milestone 1 – Problem Analysis and Algorithm Design

**File Name:** milestone1_design.md  
**Creation Date:** July 12, 2026  
**Author:** Reece R. Czarnecki  
**Class:** CS344 Python Programming  

## Problem Description

For my course project, I plan to create a simple stock portfolio tracker and analyzer. The program will allow a user to enter multiple stock positions, including the stock symbol, number of shares owned, purchase price, and current price. The program will then calculate the total value, gain or loss, and percentage return for each position and for the full portfolio.

The intended user is an individual investor who wants a quick way to review a small portfolio without using a full brokerage platform or spreadsheet. This project is useful because it turns basic financial information into a clear summary and helps the user identify which positions are performing well and which positions may need attention.

The program will use a menu so the user can add stock positions, view the portfolio, display a summary, and exit the program. Decisions will be used to validate user choices and classify positions as gains, losses, or break-even. Loops will allow the user to enter multiple positions and continue using the program until choosing to quit.

For the first version, all stock information will be entered manually. The program will not connect to live market data or automatically save information between sessions. It will assume that share amounts and prices are valid positive numbers and that the portfolio is small enough to store in memory while the program is running.

## Inputs and Outputs

### Inputs

The program will receive the following inputs from the user:

- A menu choice
- Stock symbol
- Number of shares owned
- Purchase price per share
- Current price per share
- A choice to continue entering positions or return to the main menu

### Outputs

The program will produce the following outputs:

- The current value of each stock position
- The original cost of each stock position
- The dollar gain or loss for each position
- The percentage return for each position
- A label showing whether the position is a gain, loss, or break-even
- Total portfolio cost
- Total portfolio value
- Total portfolio gain or loss
- Total portfolio percentage return

### Example Input and Output

**Sample input:**

```text
Stock symbol: AAPL
Number of shares: 10
Purchase price per share: 180
Current price per share: 195
```

**Desired output:**

```text
AAPL
Shares: 10
Original cost: $1,800.00
Current value: $1,950.00
Gain/Loss: $150.00
Return: 8.33%
Status: Gain
```

## Algorithm Overview

1. **Display the main menu.**  
   Show the user options to add a stock position, view all positions, display a portfolio summary, or exit the program.

2. **Get and validate the user's menu choice.**  
   Ask the user to select an option. A decision will check whether the choice is valid, and the program will display an error message if it is not.

3. **Add a stock position.**  
   Ask the user for the stock symbol, number of shares, purchase price, and current price. The program will validate that the share amount and prices are greater than zero.

4. **Store the stock information.**  
   Save each position in a list so multiple stocks can be tracked during the same program session. A loop will allow the user to add more than one position.

5. **Calculate results for each position.**  
   Calculate original cost, current value, dollar gain or loss, and percentage return for every stock in the portfolio.

6. **Classify each position.**  
   Use decisions to label the position as a gain if the return is positive, a loss if the return is negative, or break-even if the return is zero.

7. **Display all stock positions.**  
   Use a loop to process each stored position and print a formatted summary for each stock.

8. **Calculate the full portfolio summary.**  
   Add together the original costs and current values of all positions. Use these totals to calculate the total dollar gain or loss and total portfolio return.

9. **Repeat until the user exits.**  
   Continue displaying the main menu in a loop until the user chooses the exit option.

## Planned Structure and Functions

### `display_menu()`

This function will display the main program options. It will not require any parameters and will print the menu to the screen.

### `get_menu_choice()`

This function will ask the user to select a menu option and validate the choice. It will take no parameters and return the user's valid menu selection.

### `add_position(portfolio)`

This function will collect the stock symbol, shares, purchase price, and current price from the user. It will take the portfolio list as a parameter and add a new stock position to it.

### `calculate_position(position)`

This function will calculate the original cost, current value, gain or loss, and percentage return for one stock. It will take one stock position as a parameter and return the calculated results.

### `display_positions(portfolio)`

This function will display all stored stock positions and their calculated results. It will take the portfolio list as a parameter and print the information for each position.

### `calculate_portfolio_summary(portfolio)`

This function will calculate the total cost, total value, total gain or loss, and total percentage return for the entire portfolio. It will take the portfolio list as a parameter and return the portfolio totals.

### `display_portfolio_summary(portfolio)`

This function will display the complete portfolio summary in a clear format. It will take the portfolio list as a parameter and print the final totals and performance information.

