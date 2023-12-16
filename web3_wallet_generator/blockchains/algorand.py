import os
import json
from algosdk import account, mnemonic

class Algorand:
    def generate_wallet(self, wallet_name=None):
        # Generate a new private key and address
        private_key, address = account.generate_account()

        # Convert the private key to a 25-word mnemonic
        mnemonic_phrase = mnemonic.from_private_key(private_key)

        # Create the wallet
        wallet = {
            'private_key': private_key,
            'address': address,
            'mnemonic_phrase': mnemonic_phrase
        }

        # Create the directory if it doesn't exist
        directory = 'wallets/algorand'
        if not os.path.exists(directory):
            os.makedirs(directory)

        # If no wallet name is provided, generate a default one
        if wallet_name is None:
            wallet_number = 1
            wallet_name = f'wallet_{wallet_number}'
            while os.path.exists(f'{directory}/{wallet_name}.json'):
                wallet_number += 1
                wallet_name = f'wallet_{wallet_number}'

        # Save the wallet information to a JSON file
        with open(f'{directory}/{wallet_name}.json', 'w') as file:
            json.dump(wallet, file)

        return wallet