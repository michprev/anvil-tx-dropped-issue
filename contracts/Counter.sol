// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract Counter {
    uint public count;

    function increment() public {
        count += 1;
    }

    function setCount(uint _count) public {
        count = _count;
    }

    function decrement() public {
        count -= 1;
    }
}