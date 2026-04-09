import pytest
from project import take_out_cookies ,add_cookies,show_balance
def main():
    test_take_out_cookies
    test_add_cookies
    test_show_balance
def test_show_balance():
    balance=0
    result=show_balance(balance)
    assert result=="You currently have 0 cookies in the jar"
    balance=20
    result=show_balance(balance)
    assert result=="You currently have 20 cookies in the jar"

def test_add_cookies():
    balance, message = add_cookies(10, 5)
    assert balance == 15
    assert message == "Added 5 cookies to the jar"

    balance, message = add_cookies(10, -5)
    assert balance == 10
    assert message == "Number of cookies must be greater than zero"


def test_take_out_cookies():
    balance, message = take_out_cookies(10, 5)
    assert balance == 5

    balance, message = take_out_cookies(10, 15)
    assert balance == 10
    assert message == "You don't have that many cookies"



if __name__=="__main__":
    main()
