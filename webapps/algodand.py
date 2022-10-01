from algosdk import account, mnemonic
from algosdk.constants import microalgos_to_algos_ratio
from algosdk.future.transaction import PaymentTxn, AssetConfigTxn
from algosdk.v2client import algod

#algorand account 
def algod_client():
    """Initialise and return an algod client"""

    algod_address = "https://testnet-algorand.api.purestake.io/ps2"

    algod_token = "XycLijM8J6aGrHCed8Tld3hNKfHFxWpF9eQ1d2gQ"
    headers = {
        "X-API-Key": algod_token,
    }

    return algod.AlgodClient(algod_token, algod_address, headers)


def create_account():
    """Create account and return its mnemonic"""

    private_key, address = account.generate_account()
    return mnemonic.from_private_key(private_key)


def get_balance(address):
    """Returns the given address balance in algos converted from microalgos"""
    account_info = algod_client().account_info(address)
    balance = account_info.get('amount') / microalgos_to_algos_ratio

    return balance


def send_txn(sender, quantity, receiver, note, sk):
    """Create and sign a transaction. Quantity is assumed to be in algorands, not microalgos"""

    quantity = int(quantity * microalgos_to_algos_ratio)
    params = algod_client().suggested_params()
    note = note.encode()
    try:
        unsigned_txn = PaymentTxn(sender, params, receiver, quantity, None, note)
    except Exception as err:
        print(err)
        return False
    signed_txn = unsigned_txn.sign(sk)
    try:
        txid = algod_client().send_transaction(signed_txn)
    except Exception as err:
        print(err)
        return False

    # wait for confirmation
    try:
        wait_for_confirmation(txid, 4)
        return True
    except Exception as err:
        print(err)
        return False


# utility for waiting on a transaction confirmation
def wait_for_confirmation(transaction_id, timeout):
    start_round = algod_client().status()["last-round"] + 1
    current_round = start_round

    while current_round < start_round + timeout:
        try:
            pending_txn = algod_client().pending_transaction_info(transaction_id)
        except Exception as err:
            print(err)
            return
        if pending_txn.get("confirmed-round", 0) > 0:
            return pending_txn
        elif pending_txn["pool-error"]:
            raise Exception(
                'pool error: {}'.format(pending_txn["pool-error"]))
        algod_client().status_after_block(current_round)
        current_round += 1
    raise Exception(
        'pending tx not found in timeout rounds, timeout value = : {}'.format(timeout))


def create_asset(
        creator,
        asset_name,
        unit_name,
        total,
        decimals,
        default_frozen,
        url,
        sk
):
    """Creates an asset, returns the newly created asset ID"""
    params = algod_client().suggested_params()

    txn = AssetConfigTxn(
        sender=creator,
        sp=params,
        total=total,
        default_frozen=default_frozen,
        unit_name=unit_name,
        asset_name=asset_name,
        manager=creator,
        reserve=creator,
        freeze=creator,
        clawback=creator,
        url=url,
        decimals=decimals)

    # Sign with secret key of creator
    stxn = txn.sign(sk)

    # Send the transaction to the network and retrieve the txid.
    txid = algod_client().send_transaction(stxn)

    try:
        wait_for_confirmation(txid, 4)
    except Exception as err:
        print(err)
        return None

    try:
        ptx = algod_client().pending_transaction_info(txid)
        asset_id = ptx["asset-index"]
        return asset_id
    except Exception as err:
        print(err)
        return None
