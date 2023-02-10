
from __future__ import annotations

from dataclasses import dataclass 
from typing import List, Optional, overload, Union, Callable
from typing_extensions import Literal

from woke.testing.core import Contract, Library, Address, Account, Chain, RequestType
from woke.testing.internal import TransactionRevertedError
from woke.testing.primitive_types import *
from woke.testing.transactions import LegacyTransaction

from enum import IntEnum



class Counter(Contract):
    _abi = {b'\x06f\x1a\xbd': {'inputs': [], 'name': 'count', 'outputs': [{'internalType': 'uint256', 'name': '', 'type': 'uint256'}], 'stateMutability': 'view', 'type': 'function'}, b'+\xae\xce\xb7': {'inputs': [], 'name': 'decrement', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xd0\x9d\xe0\x8a': {'inputs': [], 'name': 'increment', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, b'\xd1Nb\xb8': {'inputs': [{'internalType': 'uint256', 'name': '_count', 'type': 'uint256'}], 'name': 'setCount', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}}
    _deployment_code = "608060405234801561001057600080fd5b50610244806100206000396000f3fe608060405234801561001057600080fd5b506004361061004c5760003560e01c806306661abd146100515780632baeceb71461006f578063d09de08a14610079578063d14e62b814610083575b600080fd5b61005961009f565b60405161006691906100fe565b60405180910390f35b6100776100a5565b005b6100816100c0565b005b61009d6004803603810190610098919061014a565b6100db565b005b60005481565b60016000808282546100b791906101a6565b92505081905550565b60016000808282546100d291906101da565b92505081905550565b8060008190555050565b6000819050919050565b6100f8816100e5565b82525050565b600060208201905061011360008301846100ef565b92915050565b600080fd5b610127816100e5565b811461013257600080fd5b50565b6000813590506101448161011e565b92915050565b6000602082840312156101605761015f610119565b5b600061016e84828501610135565b91505092915050565b7f4e487b7100000000000000000000000000000000000000000000000000000000600052601160045260246000fd5b60006101b1826100e5565b91506101bc836100e5565b92508282039050818111156101d4576101d3610177565b5b92915050565b60006101e5826100e5565b91506101f0836100e5565b925082820190508082111561020857610207610177565b5b9291505056fea2646970667358221220b525be757a954e4344d2591fe390363c28a911e4b87f8690664dcc1c3acb933564736f6c63430008120033"

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: int = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: Literal[False] = False, chain: Optional[Chain] = None) -> Counter:
        ...

    @overload
    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: int = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: Literal[True] = True, chain: Optional[Chain] = None) -> LegacyTransaction[Counter]:
        ...

    @classmethod
    def deploy(cls, *, from_: Optional[Union[Account, Address, str]] = None, value: int = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool = False, chain: Optional[Chain] = None) -> Union[Counter, LegacyTransaction[Counter]]:
        return cls._deploy([], return_tx, Counter, from_, value, gas_limit, {}, chain)

    @classmethod
    def deployment_code(cls) -> bytes:
        return cls._get_deployment_code({})

    @overload
    def count(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: int = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: Literal[False] = False, request_type: RequestType = 'call') -> uint256:
        ...

    @overload
    def count(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: int = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: Literal[True] = True, request_type: RequestType = 'call') -> LegacyTransaction[uint256]:
        ...

    def count(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: int = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool = False, request_type: RequestType='call') -> Union[uint256, LegacyTransaction[uint256]]:
        """
        Returns:
            uint256
        """
        return self._transact("06661abd", [], return_tx, uint256, from_, to, value, gas_limit) if not request_type == 'call' else self._call("06661abd", [], return_tx, uint256, from_, to, value, gas_limit)

    @overload
    def increment(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: int = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: Literal[False] = False, request_type: RequestType = 'tx') -> None:
        ...

    @overload
    def increment(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: int = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: Literal[True] = True, request_type: RequestType = 'tx') -> LegacyTransaction[None]:
        ...

    def increment(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: int = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool = False, request_type: RequestType='tx') -> Union[None, LegacyTransaction[None]]:
        return self._transact("d09de08a", [], return_tx, type(None), from_, to, value, gas_limit) if not request_type == 'call' else self._call("d09de08a", [], return_tx, type(None), from_, to, value, gas_limit)

    @overload
    def setCount(self, _count: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: int = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: Literal[False] = False, request_type: RequestType = 'tx') -> None:
        ...

    @overload
    def setCount(self, _count: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: int = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: Literal[True] = True, request_type: RequestType = 'tx') -> LegacyTransaction[None]:
        ...

    def setCount(self, _count: uint256, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: int = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool = False, request_type: RequestType='tx') -> Union[None, LegacyTransaction[None]]:
        """
        Args:
            _count: uint256
        """
        return self._transact("d14e62b8", [_count], return_tx, type(None), from_, to, value, gas_limit) if not request_type == 'call' else self._call("d14e62b8", [_count], return_tx, type(None), from_, to, value, gas_limit)

    @overload
    def decrement(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: int = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: Literal[False] = False, request_type: RequestType = 'tx') -> None:
        ...

    @overload
    def decrement(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: int = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: Literal[True] = True, request_type: RequestType = 'tx') -> LegacyTransaction[None]:
        ...

    def decrement(self, *, from_: Optional[Union[Account, Address, str]] = None, to: Optional[Union[Account, Address, str]] = None, value: int = 0, gas_limit: Union[int, Literal["max"], Literal["auto"]] = "max", return_tx: bool = False, request_type: RequestType='tx') -> Union[None, LegacyTransaction[None]]:
        return self._transact("2baeceb7", [], return_tx, type(None), from_, to, value, gas_limit) if not request_type == 'call' else self._call("2baeceb7", [], return_tx, type(None), from_, to, value, gas_limit)

Counter.count.selector = b'\x06f\x1a\xbd'
Counter.increment.selector = b'\xd0\x9d\xe0\x8a'
Counter.setCount.selector = b'\xd1Nb\xb8'
Counter.decrement.selector = b'+\xae\xce\xb7'
