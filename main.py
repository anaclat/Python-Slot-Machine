MAX_LINES = 3
MAX_BET  = 100
MIN_BET = 1

def deposit():
    while True:
        amount = input('What would you like to deposit? $')
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print(f'Amount must be greater than 0.')
        else:
            print(f'Please enter a number.')
    return amount


def numbers_of_line():
    while True:
        lines = input('Enter the number of lines to bet on (1-'  + str(MAX_LINES)  + '): ')
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print(f'Enter a valid numbers of lines.')
        else:
            print(f'Please enter a number.')
    return lines

def get_bet():
    while True:
        amount = input('What would you like to bet on each line? $')
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET  <= amount <= MAX_BET:
                break
            else:
                print(f'Amount must be between ${MIN_BET} and ${MAX_BET}.')
        else:
            print(f'Please enter a number.')
    return amount


def main():
    balance =  deposit()
    lines = numbers_of_line()
    bet = get_bet()
    total_bet = bet * lines
    print(f'You are betting ${bet} on {lines} line(s). Total bet is equal to: ${total_bet}.')
    print(balance,lines)

main()