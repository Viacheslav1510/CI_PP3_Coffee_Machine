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


ingredients = get_drink_ingredients(1)
print(ingredients)