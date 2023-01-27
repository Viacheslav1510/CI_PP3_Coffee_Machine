class Account:
    """
    Create account to log in user
    Get account name, email and bonus
    """
    def __init__(self, name, email, bonus):
        self.name = name
        self.email = email
        self.bonus = bonus

    def acc_string(self):
        name = self.name
        email = self.email
        bonus = self.bonus
        return f"{name}, your bonus is {bonus}. Your email is: {email}"
    
    # get values
    def get_name(self):
        return self.name

    def get_email(self):
        return self.email

    def get_bonus(self):
        return self.bonus
