import random
MAX_LINES = 3
MIN_BET = 10

ROWS = 3
COLS= 3

symbol_count = {"A": 3,
                "B": 4,
                "C": 6,
                "D": 8}

symbol_value = {"A": 5,
                "B": 4,
                "C": 3,
                "D": 2}


def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines


def spin_slot(rows,cols,symbols):
    all_symbols = []

    for symbol,symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)

    return columns


def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if (
                i != len(columns) - 1
            ):  # Compare with len(columns) - 1 to avoid IndexError
                print(f"{column[row]}", end=" | ")
            else:
                print(f"{column[row]}", end="")
        print()  # Move to the next line after printing a row


def deposit():
    while True:
        amount = input("Enter the amount you want to deposit: ")

        if amount.isdigit():  # checking if the input entered is digit or not
            amount = int(amount)  # converting the entered input to integer

            if amount < 10:
                print("The amount should be higher than 10$")
            else:
                break  # break the loop if all the conditions met
        else:
            print("Please enter The Valid amount!\n")

    return amount

def get_num_of_lines():
    while True:
        lines = input(f"Enter the lines you want to bet on (1-{str(MAX_LINES)}): ")

        if lines.isdigit():  # checking if the input entered is digit or not
            lines = int(lines)  # converting the entered input to integer

            if 1 >= lines <= MAX_LINES:
                print("Enter the valid Number of Lines!")
            else:
                break  # break the loop if all the conditions met 
        else:
            print("Please enter The Valid Number!\n")

    return lines

def get_bet():
    while True:
        amount = input("What would you like to bet on each line? ")

        if amount.isdigit():  # checking if the input entered is digit or not
            amount = int(amount)  # converting the entered input to integer

            if amount < MIN_BET:
                print("The amount must be higher than 10$")
            else:
                break  # break the loop if all the conditions met
        else:
            print("Please enter The Valid Number!\n")

    return amount


def spin(balance):
    lines = get_num_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(
                f"You do not have enough to bet that amount, your current balance is: ${balance}"
            )
        else:
            break

    print(
        f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}"
    )

    slots = spin_slot(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won on lines:", *winning_lines)
    print(f"Your total winning is ${winnings}.")
    return winnings - total_bet

def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press enter to play (q to quit).")
        if answer == "q":
            break
        balance += spin(balance)

    print(f"You left with ${balance}")




if __name__ == "__main__":
    main()
    

