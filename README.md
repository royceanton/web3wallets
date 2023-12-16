# Web-3-Wallet-Generator

Web-3-Wallet-Generator is a Python project that allows you to generate wallets for various blockchains. It currently supports Ethereum, Avalanche, and Cosmos, with plans to support more blockchains in the future.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/Web-3-Wallet-Generator.git
```

2. Navigate to the project directory:

```
cd Web-3-Wallet-Generator
```

3. Create a Python virtual environment:

```
python3 -m venv web3-env
```

4. Activate the virtual environment:

    On Unix or MacOS:
    ```
    source web3-env/bin/activate
    ```

    On Windows:
    ```
    .\web3-env\Scripts\activate
    ```

5. Install the necessary packages:

```
pip install bech32 ecdsa hdwallets mnemonic
```

## Usage

You can use the `WalletGenerator`  class to generate a wallet for a specific blockchain. Here's an example:

```python
from web_3_wallet_generator import WalletGenerator

wallet_generator = WalletGenerator()
wallet = wallet_generator.generate_wallet('ethereum')
```

After running this code, you'll find a new JSON file in the wallets directory. This file contains the public and private keys for the Ethereum wallet.

## Supported Blockchains

| Blockchain | Supported | Status |
|------------|-----------|--------|
| Ethereum   | Yes       | ✅     |
| Avalanche  | Yes       | ✅     |
| Cosmos     | Yes       | ✅     |
| Bitcoin    | Planned   | 🚧     |
| Polkadot   | Planned   | 🚧     |
| ...        | ...       | ...    |

## Contributing
Contributions are welcome! Please read the [contributing guidelines](CONTRIBUTING.md) first.

## License
This project is licensed under the terms of the [MIT license](LICENSE).

