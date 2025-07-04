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

deposit()