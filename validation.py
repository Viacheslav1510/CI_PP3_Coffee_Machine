from email_validator import validate_email, EmailNotValidError
from colors import Color as Col


def get_email():
    """
    Gets email from user input
    """
    while True:
        email = input(Col.YELLOW + "Please enter your email to pass: ").strip()

        if vaidate_email_input(email):
            break
    
    return email


def vaidate_email_input(email):
    """
    Validates user email adress
    """
    try: 
        validate_email(email)
        return True
    except EmailNotValidError as error:
        print(Col.RED + f"\n{error}")
        print(Col.RED + "Please try again.\n")


def validate_data(value):
    """
    Validates user input
    """
    allowed_inputs = ['1', '2', '3', 'off', 'report']
    try:
        if value not in allowed_inputs:
            raise ValueError(
                "Coffee machine allows: '1', '2', '3' for choosing drink,\n \
                                    'off' and 'report'"
            )
    except ValueError as error:
        print(Col.RED + f"\nInvalid data - {error}, please try again.\n")
        return False

    return True