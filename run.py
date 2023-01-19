import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('coffee_machine')


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
        print("Sorry there is not enough ingredients for your drink")
        return False


def update_resources(data):
    """
    Receives a list of the rest of the ingredients.
    Update resources worksheet with data provided
    """
    print("Updating resources ... ")
    resources_worksheet = SHEET.worksheet('resources')
    resources_worksheet.append_row(data)
    print("Resources updated successfully\n")


def insert_money():
    """
    Returns the total calculated from coins inserted.
    """
    print("\nPlease insert coins")
    total = int(input("How many 20c: ")) * 0.2
    total += int(input("How many 50c: ")) * 0.5
    total += int(input("How many 1€: "))
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
        print(f"There is not enough money. Drink costs {drink_cost}€.\n\
        Money refunded")
        return False


def update_profit(value):
    """
    Receives a drink cost value.
    Adds drink cost to previous profit value
    Updates profit worksheet row with data provided
    """
    print("Collecting profit ...")
    profit_worksheet = SHEET.worksheet("profit")
    profit_column = SHEET.worksheet("profit").get_all_values()
    previous_profit = [int(num) for num in profit_column[-1]]
    new_profit = [value]
    up_profit = [pre + new for pre, new in zip(previous_profit, new_profit)]
    profit_worksheet.append_row(up_profit)
    print("Profit updated.\n")


def make_coffee(index):
    """
    Makes coffee if all statements are True
    """
    print("Making your coffee ...")
    drink_name = SHEET.worksheet("menu").col_values(int(index))[0]
    print(f"Here is your {drink_name}☕. Enjoy!\n")


def report():
    """
    Prints report for resources and profit
    """
    resources_data = SHEET.worksheet("resources").get_all_values()
    coffee = resources_data[-1][0]
    water = resources_data[-1][1]
    milk = resources_data[-1][2]
    print(f"Remains: coffee - {coffee}g, water - {water}ml, milk - {milk}ml")
    profit_data = SHEET.worksheet("profit").get_all_values()
    print(f"All profit: {profit_data[-1][0]}€")


def main():
    is_on = True
    while is_on:
        choice_prompt = "What would you like?\n"
        choice_prompt += "espresso(1)/cappuccino(2)/latte(3): "
        choice = input(choice_prompt)
        if choice == 'off':
            print("See you soon!")
            is_on = False
        elif choice == 'report':
            report()
        else:
            ingredients = get_drink_ingredients(choice)
            if check_resources(ingredients):
                drink_cost = get_drink_cost(choice)
                user_money = insert_money()
                if check_transaction(user_money, drink_cost):
                    remain_ingredients = check_resources(ingredients)
                    update_resources(remain_ingredients)
                    update_profit(drink_cost)
                    make_coffee(choice)


main()