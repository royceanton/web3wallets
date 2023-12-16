from .blockchains import Ethereum, Avalanche, Cosmos

class WalletGenerator:
    def __init__(self):
        self.blockchains = {
            'ethereum': Ethereum(),
            'avalanche': Avalanche(),
            'cosmos': Cosmos(),
        }

    def generate_wallet(self, blockchain, wallet_name=None):
        return self.blockchains[blockchain].generate_wallet(wallet_name)