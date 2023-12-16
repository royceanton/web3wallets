import os
import json
import hashlib

import bech32
import ecdsa
import hdwallets
import mnemonic

class Cosmos:
    DEFAULT_DERIVATION_PATH = "m/44'/118'/0'/0/0"
    DEFAULT_BECH32_HRP = "cosmos"

    class BIP32DerivationError(Exception):
        pass

    def seed_to_privkey(self, seed: str, path: str = DEFAULT_DERIVATION_PATH) -> bytes:
        seed_bytes = mnemonic.Mnemonic.to_seed(seed, passphrase="")
        hd_wallet = hdwallets.BIP32.from_seed(seed_bytes)
        derived_privkey = hd_wallet.get_privkey_from_path(path)
        return derived_privkey

    def privkey_to_pubkey(self, privkey: bytes) -> bytes:
        privkey_obj = ecdsa.SigningKey.from_string(privkey, curve=ecdsa.SECP256k1)
        pubkey_obj = privkey_obj.get_verifying_key()
        return pubkey_obj.to_string("compressed")

    def pubkey_to_address(self, pubkey: bytes, *, hrp: str = DEFAULT_BECH32_HRP) -> str:
        s = hashlib.new("sha256", pubkey).digest()
        r = hashlib.new("ripemd160", s).digest()
        five_bit_r = bech32.convertbits(r, 8, 5)
        assert five_bit_r is not None, "Unsuccessful bech32.convertbits call"
        return bech32.bech32_encode(hrp, five_bit_r)

    def generate_wallet(self, blockchain='cosmos', wallet_name=None):
        # Generate a new private key and public key
        while True:
            phrase = mnemonic.Mnemonic(language="english").generate(strength=256)
            try:
                privkey = self.seed_to_privkey(phrase, path=self.DEFAULT_DERIVATION_PATH)
                break
            except self.BIP32DerivationError:
                pass
        pubkey = self.privkey_to_pubkey(privkey)

        # Hash the public key and get the address
        address = self.pubkey_to_address(pubkey, hrp=self.DEFAULT_BECH32_HRP)

        # Create the wallet
        wallet = {
            'private_key': privkey.hex(),
            'address': address
        }

        # Create the directory if it doesn't exist
        directory = f'wallets/{blockchain}'
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