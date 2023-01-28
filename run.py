import os
import gspread
from google.oauth2.service_account import Credentials
import validation as val
from colors import Color as Col
from accounts import Account as customer

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('coffee_machine')


def clear():
    """
    Clears output after call
    """
    os.system('clear')


def logo():
    """
    Prints program logo
    """
    print(Col.LOGO_V + "Welcome to:")
    print(" ")
    print(Col.LOGO_R + "  ****                                    ")
    print(Col.LOGO_R + " **    *     ****     ****    ***  *****  **** ")
    print(Col.LOGO_R + " **        **    **  **     **     *      *    ")
    print(Col.LOGO_P + " **        **    **  ****   ****   ****   **** ")
    print(Col.LOGO_P + " **    *   **    **  **     **     *      *    ")
    print(Col.LOGO_P + "  *****      ****    **     **     *****  **** ")
    print(" ")
    print(Col.LOGO_V + "                ******  **   **      **   **** ")
    print(Col.LOGO_V + "                  **         ** *  * **   *    ")
    print(Col.LOGO_V + "                  **    **   **  *   **   **** ")
    print(Col.LOGO_V + "                  **    **   **      **   *    ")
    print(Col.LOGO_V + "                  **    **   **      **   **** ")
    print(" ")


def get_drink_ingredients(index):
    """
    Gets user input and returns ingredients integer list
    """
    drink_column = SHEET.worksheet("menu").col_values(int(index))[1:4]
    ingredients = [int(value) for value in drink_column]
    return ingredients


def get_drink_cost(index):
    """
    Gets user input and returns drink integer cost
    """
    drink_cost = SHEET.worksheet("menu").col_values(int(index))[-1]
    return int(drink_cost)


def check_resources(ingredients):
    """
    Gets ingredients for drinks, checks is it enough resources to make coffee
    and returns the rest of the ingredients
    """
    resources = SHEET.worksheet("resources").get_all_values()
    resources_last_row = resources[-1]
    resources_int = [int(value) for value in resources_last_row]

    if resources_int > ingredients:
        remain = [res - ing for res, ing in zip(resources_int, ingredients)]
        return remain
    else:
        print(Col.RED + "Sorry there is not enough ingredients for your drink")
        return False


def update_resources(data):
    """
    Receives a list of the rest of the ingredients.
    Update resources worksheet with data provided
    """
    print(Col.UPDATE + "Updating resources ... ")
    resources_worksheet = SHEET.worksheet('resources')
    resources_worksheet.append_row(data)
    print(Col.UPDATE + "Resources updated successfully\n")


def insert_money():
    """
    Returns the total calculated from coins inserted.
    """
    print(Col.BLUE + "\nPlease insert coins")
    while True:
        try:
            coins_20 = input(Col.BLUE + "How many 20c: ")
            if coins_20.isnumeric():
                coins_20 = int(coins_20) * 0.2
                break
            raise ValueError(Col.RED + "Invalid input")
        except ValueError as error:
            print(f"{error}")
    while True:
        try:
            coins_50 = input(Col.BLUE + "How many 50c: ")
            if coins_50.isnumeric():
                coins_50 = int(coins_50) * 0.5
                break
            raise ValueError(Col.RED + "Invalid input")
        except ValueError as error:
            print(f"{error}")
    while True:
        try:
            euros = input(Col.BLUE + "How many 1€: ")
            if euros.isnumeric():
                euros = int(euros)
                break
            raise ValueError(Col.RED + "Invalid input")
        except ValueError as error:
            print(f"{error}")
    total = coins_20 + coins_50 + euros
    return total


def check_transaction(money_received, drink_cost):
    """
    Checks if enough money to buy drink
    Refunds user money if money received more than drink costs
    Returns drink cost if transaction successfull
    """
    if money_received > drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is your change {change}€\n")
        return drink_cost

    elif money_received == drink_cost:
        print("Thanks for exact change!\n")
        return drink_cost

    else:
        message = f"There is not enough money. Drink costs {drink_cost}€.\n"
        message += "Money refunded"
        print(Col.RED + message)
        return False


def update_profit(value):
    """
    Receives a drink cost value.
    Adds drink cost to previous profit value
    Updates profit worksheet row with data provided
    """
    print(Col.UPDATE + "Collecting profit ...")
    profit_worksheet = SHEET.worksheet("profit")
    profit_column = SHEET.worksheet("profit").get_all_values()
    previous_profit = [int(num) for num in profit_column[-1]]
    new_profit = [value]
    up_profit = [pre + new for pre, new in zip(previous_profit, new_profit)]
    profit_worksheet.append_row(up_profit)
    print(Col.UPDATE + "Profit updated.\n")


def make_coffee(index):
    """
    Makes coffee if all statements are True
    """
    print(Col.UPDATE + "Making your coffee ...")
    drink_name = SHEET.worksheet("menu").col_values(int(index))[0]
    print(Col.BLUE + f"Here is your {drink_name}☕. Enjoy!\n")


def report():
    """
    Prints report for resources and profit
    """
    resources_data = SHEET.worksheet("resources").get_all_values()
    message = f"\nRemains: \nCoffee: {resources_data[-1][0]}g,"
    message += f" Water: {resources_data[-1][1]}ml,"
    message += f" Milk: {resources_data[-1][2]}ml."
    print(Col.UPDATE + message)
    profit_data = SHEET.worksheet("profit").get_all_values()
    print(Col.UPDATE + f"All profit: {profit_data[-1][0]}€\n")


def create_customer():
    """
    Creates customer account inside bonuses worksheet
    """
    customer_acc = []
    while True:
        name = input(Col.YELLOW + "Enter your name: ").title()
        if not name.isalpha():
            print(Col.RED + "Enter real name, please")
        else:
            break
    email = val.get_email()
    bonus = 0
    customer_acc.append(name)
    customer_acc.append(email)
    customer_acc.append(bonus)
    account_holder = customer(name, email, bonus)
    SHEET.worksheet('bonuses').append_row(customer_acc)
    return account_holder


def validate_user():
    """
    Gets values from bonuses worksheet
    Cheks user authorised or not
    Creates new customer if user not authorised
    Returns user holder
    """
    customer_data = SHEET.worksheet('bonuses').get_all_values()[1:]
    email_input = val.get_email()
    client = [row for row in customer_data if email_input == row[1]]
    if len(client) == 0:
        message = "\nSeems you don't have an account\n"
        print(message + "Create an account to receive bonuses\n")
        new_account = create_customer()
        return new_account
    else:
        name = client[0][0]
        email = client[0][1]
        bonus = client[0][2]
        account_to_update = customer(name, email, bonus)
        return account_to_update


def update_bonus(account):
    """
    Updates bonus cell in worksheet
    """
    bonus = account.bonus
    account_holder = SHEET.worksheet('bonuses').find(account.email)
    SHEET.worksheet('bonuses').update_cell(account_holder.row, 3, bonus)


def is_drink_free(account, drink_cost):
    """
    Cheks is enough bonuses to get a free drink
    If enough - returns True
    If not enough - returns False
    """
    name = account.get_name()
    email = account.get_email()
    bonus = int(account.get_bonus())
    if bonus > 0 and bonus/drink_cost >= 2:
        new_bonus = bonus - drink_cost * 2
        customer_to_update = customer(name, email, new_bonus)
        update_bonus(customer_to_update)
        print(Col.GREEN + "\nYour drink is free today!\n")
        return True
    else:
        return False


def user_regard(account, drink_cost):
    """
    Updates user bonus according to ordered drink cost
    """
    print(Col.GREEN + f"Your reward is {drink_cost} points\n")
    bonus = int(account.get_bonus()) + drink_cost
    name = account.get_name()
    email = account.get_email()
    customer_to_update = customer(name, email, bonus)
    update_bonus(customer_to_update)


def get_user_bonus(account):
    """
    Gets user bonus in worksheet and prints hint for the user
    """
    bonus = account.get_bonus()
    print(Col.UPDATE + f"\nYour bonus is {bonus}")
    print(Col.UPDATE + "You need to have to get free drink:")
    print(Col.UPDATE + "4 - for espresso, 6 - for cappuccino, 8 - for latte\n")


def main():
    """
    Run all program functions
    """
    print(Col.YELLOW + "Hello\nLog in to continue please")
    user = validate_user()
    clear()
    logo()
    is_on = True
    while is_on:
        choice_hint = Col.GREEN + f"{user.get_name()}, what would you like?\n"
        choice_hint += Col.GREEN + "espresso(1)/cappuccino(2)/latte(3): "
        choice = input(choice_hint)
        if val.validate_data(choice):
            if choice == 'off':
                print("See you soon!")
                is_on = False
            elif choice == 'report':
                report()
            elif choice == 'bonus':
                user = validate_user()
                get_user_bonus(user)
            else:
                ingredients = get_drink_ingredients(choice)
                drink_cost = get_drink_cost(choice)
                if check_resources(ingredients):
                    if is_drink_free(user, drink_cost):
                        remain_ingredients = check_resources(ingredients)
                        update_resources(remain_ingredients)
                        make_coffee(choice)
                    else:
                        user_money = insert_money()
                        if check_transaction(user_money, drink_cost):
                            remain_ingredients = check_resources(ingredients)
                            update_resources(remain_ingredients)
                            update_profit(drink_cost)
                            user_regard(user, drink_cost)
                            make_coffee(choice)


main()
