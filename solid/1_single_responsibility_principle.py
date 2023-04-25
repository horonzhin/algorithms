# Single Responsibility Principle (SRP) - принцип единичной ответственности.
# Каждый класс должен выполнять только те цели ради которых он создается.

# wrong
class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def authenticate(self, email, password):
        # authenticate the user
        pass


# correct
class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password


class Authenticator:
    def authenticate(self, email, password):
        # authenticate the user
        pass
