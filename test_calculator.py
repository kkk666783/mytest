import pytest
from account import Account
@pytest.fixture
def account():
    acc=Account("alcie")
    yield acc
    acc.close()

@pytest.mark.parametrize("amount,expect_balance",[(100,100),(50,50)])
def test_deposit(account, amount, expect_balance):
    assert account.deposit(amount) == expect_balance
def test_deposit_zero(account):
    with pytest.raises(ValueError):
        account.deposit(0)
def test_deposit_multiple_times(account):
    assert account.deposit(100) == 100   # 第一次存 100
    assert account.deposit(50) == 150    # 再存 50，累计 150
    assert account.deposit(25) == 175    # 再存 25，累计 175      
def test_withdraw(account):
    account.deposit(100)
    assert account.withdraw(20) == 80
def test_withdraw_insufficient(account):
    account.deposit(10)               
    with pytest.raises(ValueError, match="Insufficient funds"):
        account.withdraw(50)
def test_deposit_after_close(account):
    account.close()                      
    with pytest.raises(RuntimeError, match="Account is closed"):
        account.deposit(100)            


def test_withdraw_after_close(account):
    account.close()
    with pytest.raises(RuntimeError, match="Account is closed"):
        account.withdraw(10)
