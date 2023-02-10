from woke.testing import *
from pytypes.contracts.Counter import Counter

@default_chain.connect()
def test_multiple_txs():
    default_chain.default_tx_account = default_chain.accounts[0]
    counter = Counter.deploy()

    # temporarily disable automine
    with default_chain.change_automine(False):
        tx1 = counter.increment(return_tx=True, gas_limit="auto")
        default_chain.gas_price = 100000
        tx2 = counter.increment(return_tx=True, gas_limit="auto")
        default_chain.gas_price = 0
        tx3 = counter.increment(return_tx=True, gas_limit="auto")

        assert len(default_chain.blocks["pending"].txs) == 3

    default_chain.mine()

    print([len(block.txs) for block in default_chain.blocks])

    assert tx1.block == tx2.block == tx3.block
    assert tx1.block.txs == [tx2, tx1, tx3]