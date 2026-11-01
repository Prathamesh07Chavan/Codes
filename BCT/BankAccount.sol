// SPDX-License-Identifier: MIT
// Specifies the license of the smart contract

pragma solidity ^0.8.0;
// Specifies that Solidity version 0.8.0 or above can be used

contract BankAccount {
    // Creates a smart contract named BankAccount

    mapping(address => uint256) private balances;
    // Stores the balance of each user's wallet address
    // address = user's wallet address
    // uint256 = balance amount in Wei
    // private = can be accessed only inside this contract

    // Deposit money
    function deposit() public payable {
        // Creates a public function named deposit
        // payable allows this function to receive Ether

        balances[msg.sender] += msg.value;
        // Adds the deposited Ether to the user's balance
        // msg.sender = address of the person calling the function
        // msg.value = amount of Ether sent with the transaction
    }

    // Withdraw money
    function withdraw(uint256 amount) public {
        // Creates a public function named withdraw
        // amount = amount of Ether to withdraw

        require(balances[msg.sender] >= amount, "Insufficient balance");
        // Checks whether the user has enough balance
        // If balance is insufficient, the transaction fails

        balances[msg.sender] -= amount;
        // Subtracts the withdrawal amount from user's balance

        (bool success, ) = payable(msg.sender).call{value: amount}("");
        // Sends the requested Ether amount to the user's address
        // payable makes the address capable of receiving Ether
        // call is used to transfer Ether

        require(success, "Transfer failed");
        // Checks whether the Ether transfer was successful
        // If transfer fails, the transaction is reverted
    }

    // Show balance
    function showBalance() public view returns (uint256) {
        // Creates a function to display the user's balance
        // view means it only reads data and does not change it
        // returns uint256 means it returns a number

        return balances[msg.sender];
        // Returns the balance of the person calling the function
    }
}