from brownie import accounts, config, Contract, EasyToken
from scripts.helpful_scripts import get_account


def main():
    account = get_account()
    erc20_address = "0x870ee7564f1F369CAE49DB91a0b63CCE477f986e" #Insert ERC20 Address/contract here
    recipient = "0x9428B391c6A49FAAC542C0FaDF8A5FF85822afeF" #Insert address of recipient here
    # This will be how many tokens to send in WEI
    amount = 1000000000000000000  # 1 token
    erc20 = Contract.from_abi("Arbitrary ERC20", erc20_address, abi=EasyToken.abi)
    tx = erc20.transfer(recipient, amount, {"from": account})
    tx.wait(1)