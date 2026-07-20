# Course Project Milestone 2 - Status

**File Name:** milestone2_status.md
**Author:** Reece R. Czarnecki
**Class:** CS344 Python Programming

## What's implemented so far

- Full menu loop (add position / view positions / view summary / exit) matching the Milestone 1 design.
- `add_position()` collects symbol, shares, purchase price, and current price, with validation so shares/prices must be positive numbers and the symbol can't be blank.
- `calculate_position()` computes original cost, current value, gain/loss, and percent return for a single stock, and classifies it as Gain, Loss, or Break-even.
- `display_positions()` loops through every stored position and prints a formatted summary for each.
- `calculate_portfolio_summary()` / `display_portfolio_summary()` total the cost, value, and gain/loss across all positions and classify the portfolio overall.
- Basic testing: ran the program with multiple positions (a gaining stock and a losing stock), with an empty portfolio, and with invalid input (non-numeric menu choice, out-of-range choice, non-numeric share count, negative share count, blank symbol) to confirm the validation loops and calculations behave as expected.

## Planned for later weeks

- Persisting the portfolio between sessions (currently everything is stored in memory and lost on exit, as noted in the Milestone 1 design).
- Optionally pulling live current prices instead of manual entry.
- Ability to edit or remove an existing position instead of only adding new ones.

## Issues / questions encountered

- No major issues. One small design decision: if a position's original cost is $0 the percent-return calculation would divide by zero, so that case is guarded and just reports 0% - this shouldn't come up in normal use since share count and price are both required to be greater than zero.
