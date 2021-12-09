from brownie import accounts, config, TokenERC20
from brownie.network import account

initial_supply = 100000000000000000
token_name = "Token"
token_symbol = "TOK"

def main():
    account = accounts[0]
    erc20 = TokenERC20.deploy(initial_supply, token_name, token_symbol, {'from': account})
