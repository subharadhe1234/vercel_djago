// SPDX-License-Identifier: MIT 
pragma solidity  ^0.8.0;

contract SimpleStorage{
    int a=0;
    string b ="radhe";
    // uint256 b;

    function setter(int _a) public{
        a = _a;
    } 
    function getter() public view returns(int){
        return a;

    }
    function getAdd() public view returns(address){
        return msg.sender;
    }
}
