# 🎰 Python Slot Machine

A simple command-line **Slot Machine Game** written in Python. The player deposits money, places bets on up to 3 lines, spins a 4x4 slot grid, and wins based on matching symbols across selected lines.


## 📜 Features

* 4x4 slot machine grid
* Bet on 1 to 3 horizontal lines
* Random symbol generation with different probabilities
* Configurable symbol payout values
* Input validation for deposits and bets
* Win/loss calculation with balance tracking


## 🎮 How to Play

1. **Deposit** an amount of money to begin.
2. Choose how many lines (1-3) to bet on.
3. Enter your **bet per line**.
4. The slot machine spins, and you **win** based on matching symbols in the same row.
5. Continue spinning or **press `q` to quit**.


## 🧮 Winnings

Each symbol has a payout multiplier:

| Symbol | Count (Chance) | Value (Payout Multiplier) |
| ------ | -------------- | ------------------------- |
| A      | 2              | 5×                        |
| B      | 4              | 4×                        |
| C      | 6              | 3×                        |
| D      | 8              | 2×                        |

To win on a line, all 4 symbols in that line must match.


## ▶️ Run the Game

Make sure you have **Python 3** installed.
Then, run the game using the command line:

```bash
python slot_machine.py
```


## 📂 File Structure

```bash
slot_machine.py       # Main game logic
```


## 🛠️ Customization

* You can adjust the **ROWS** and **COLS** constants for different grid sizes.
* Change `symbol_count` to affect probability.
* Modify `symbol_value` to change payouts.


## 🧠 Concepts Used

* Functions and modular design
* Loops and conditionals
* Random module (`random.choice`)
* Lists and dictionaries
* Input validation and error handling


## 📝 License

This project is for educational and personal use. Feel free to modify and expand it!