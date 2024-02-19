from decimal import Decimal


from account import Account


def test_account_initial_balance():
    account = Account("Dayo Akintola", Decimal(0.00))
    assert account.get_balance() == 0.00

def test_account_has_name():
    account = Account("Dayo Akintola", Decimal(0.00))
    assert account.get_name() == "Dayo Akintola"


def test_account_can_deposit():
    account = Account("Dayo Akintola", Decimal(0.00))
    assert account.get_balance() == 0.00
    account.deposit(500)
    # account.withdraw(300)
    assert account.get_balance() == 500


def test_account_can_withdraw():
    account = Account("Dayo Akintola", Decimal(0.00))
    assert account.get_balance() == 0.00
    account.deposit(500)
    account.withdraw(300)
    assert account.get_balance() == 200
