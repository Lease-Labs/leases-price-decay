from web3 import Web3, EthereumTesterProvider

provider_url = 'https://matic-mumbai.chainstacklabs.com'

# mumbai
bnft_contract_address = '0xDBbdE73c748544aF88Ab1f88dF87869685A6175e'
marketplace_contract_address = '0xED3a5dE5Bc0a6f06259D4dBBc8E7595D2EDAe6eE'

w3 = Web3(Web3.HTTPProvider(provider_url))