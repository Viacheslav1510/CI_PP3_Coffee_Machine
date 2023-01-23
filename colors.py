from colorama import init

# Initializes Colorama
init(autoreset=True)


class Color:
    """
    Define colors for input and output
    """
    YELLOW = "\033[1;33;48m"
    RED = "\033[1;31;48m"
    GREEN = "\033[1;32;48m"
    BLUE = "\033[1;34;48m"
    UPDATE = "\033[38;5;88m"
    LOGO_R = "\033[38;5;52m"
    LOGO_P = "\033[38;5;89m"
    LOGO_V = "\033[38;5;93m"
