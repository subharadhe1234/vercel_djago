from web3 import Web3
import json


# Connect to the Ethereum network
web3 = Web3(Web3.HTTPProvider('https://eth-sepolia.g.alchemy.com/v2/6J-rjkgtXR-v62tdRHJ5mJLFdFWPdiqD'))
netID="11155111"
# Get block by number
# block_number = 123456  # Replace with the desired block number or use 'latest'
# block = w3.eth.get_block(block_number)
# web3 =Web3(Web3.HTTPProvider('HTTP://127.0.0.1:7545'))

# contract_address='0x23d1f9D9F1aB041e5FdFD231d7fFC835cd3ee6c8'
# networkID=web3.eth.account
# print(networkID)
path=r'D:\jango webapp\blockchin_djngo\build\contracts\SimpleStorage.json'

with open(path) as f:
    file=json.load(f)
    abi=file['abi']
    contract_address=file["networks"][netID]["address"]
    
    # print(abi)
    # print(contract_address)

contract=web3.eth.contract(address=contract_address,abi=abi)
print(contract)

getval=contract.functions.getter().call()
# setval=contract.functions.setter(10).transact({'from':"0x5c5185d8081478a6A4538842b6C93044CEe8d2D2"})
print(getval)
# Set the value using the setter function
try:
    # Ensure the sender account is unlocked or use a private key to sign the transaction
    sender_address = "0x5c5185d8081478a6A4538842b6C93044CEe8d2D2"
    private_key = "8ed060404aafb12b0e13b4c6ea5d64e2b93f728a79a09813352f2a6d8c962e25"  # Replace with the actual private key

    # Build transaction dictionary
    tx = contract.functions.setter(10).transact({
        'from': sender_address,
        # 'nonce': web3.eth.getTransactionCount(sender_address),
        'gas': 2000000,
        'gasPrice': web3.toWei('50', 'gwei'),
    })

    # Sign and send the transaction
    signed_tx = web3.eth.account.signTransaction(tx, private_key)
    tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
    receipt = web3.eth.waitForTransactionReceipt(tx_hash)
    print(f"Transaction receipt: {receipt}")
except Exception as e:
    print(f"Error sending transaction: {e}")