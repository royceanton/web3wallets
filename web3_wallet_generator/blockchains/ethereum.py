import os
import json
from eth_account import Account

class Ethereum:
    def generate_wallet(self, wallet_name=None):
        account = Account.create()

        wallet = {
            'private_key': account.privateKey.hex(),
            'address': account.address
        }

        directory = 'wallets/ethereum'
        if not os.path.exists(directory):
            os.makedirs(directory)

        if wallet_name is None:
            wallet_number = 1
            wallet_name = f'wallet_{wallet_number}'
            while os.path.exists(f'{directory}/{wallet_name}.json'):
                wallet_number += 1
                wallet_name = f'wallet_{wallet_number}'

        with open(f'{directory}/{wallet_name}.json', 'w') as file:
            json.dump(wallet, file)

        return wallet