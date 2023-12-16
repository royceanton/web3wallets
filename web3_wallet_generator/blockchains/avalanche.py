import os
import json
import binascii
from coincurve import PrivateKey
from sha3 import keccak_256

class Avalanche:
    def generate_wallet(self, wallet_name=None):
        # Generate a new private key
        private_key = PrivateKey()
        private_key_hex = private_key.to_hex()

        # Get the public key
        public_key = private_key.public_key.format(compressed=False)[1:]

        # Hash the public key and get the address
        address = '0x' + keccak_256(public_key).hexdigest()[-40:]

        # Create the wallet
        wallet = {
            'private_key': private_key_hex,
            'address': address
        }

        # Create the directory if it doesn't exist
        directory = 'wallets/avalanche'
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