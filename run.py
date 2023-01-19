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


def main():
    choice_prompt = "What would you like?\n"
    choice_prompt += "espresso(1)/cappuccino(2)/latte(3): "
    choice = input(choice_prompt)
    ingredients = get_drink_ingredients(choice)
    resourses_remain = check_resources(ingredients)
    update_resources(resourses_remain)


main()