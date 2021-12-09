from brownie import accounts, config, EasyToken
from brownie.network import account

initial_supply = 1000000000000000000000000

def main():
    account = accounts.add(config['wallets']['from_key'])
    erc20 = EasyToken.deploy(initial_supply, {'from': account}, publish_source=True)
