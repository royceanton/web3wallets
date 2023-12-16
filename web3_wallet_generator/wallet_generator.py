from .blockchains import Ethereum, Avalanche, Cosmos, Algorand

class WalletGenerator:
    def __init__(self):
        self.blockchains = {
            'ethereum': Ethereum(),
            'avalanche': Avalanche(),
            'cosmos': Cosmos(),
            'algorand': Algorand()
        }

    def generate_wallet(self, blockchain, wallet_name=None):
        return self.blockchains[blockchain].generate_wallet(wallet_name)