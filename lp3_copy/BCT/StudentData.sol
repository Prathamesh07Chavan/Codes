// SPDX-License-Identifier: MIT
// Specifies the license of the smart contract

pragma solidity ^0.8.20;
// Specifies the Solidity compiler version

contract StudentData {
    // Creates a smart contract named StudentData

    struct Student {
        // Structure used to store details of one student

        string id;
        // Stores the student's ID

        string name;
        // Stores the student's name

        uint8 age;
        // Stores the student's age
        // uint8 stores a small positive integer

        string course;
        // Stores the student's course
    }

    Student[] private students;
    // Array used to store multiple Student records
    // private means the array can be accessed only inside the contract

    event StudentAdded(string id, string name, string course);
    // Event generated when a new student is added

    event FallbackCalled(address sender, uint256 value, string message);
    // Event generated when fallback or receive function is triggered

    function addStudent(
        string memory _id,
        string memory _name,
        uint8 _age,
        string memory _course
    ) public {
        // Function used to add a new student

        students.push(Student(_id, _name, _age, _course));
        // Adds the student's details to the students array

        emit StudentAdded(_id, _name, _course);
        // Generates an event showing that the student was added
    }

    function getStudent(
        uint256 index
    ) public view returns (
        string memory,
        string memory,
        uint8,
        string memory
    ) {
        // Function used to get student details using array index
        // view means this function only reads data

        require(index < students.length, "Invalid index");
        // Checks whether the given index exists
        // If the index is invalid, the call fails

        Student memory s = students[index];
        // Gets the student at the given index and stores it temporarily

        return (s.id, s.name, s.age, s.course);
        // Returns the student's ID, name, age and course
    }

    function getTotalStudents() public view returns (uint256) {
        // Function used to find the total number of students

        return students.length;
        // Returns the number of students stored in the array
    }

    fallback() external payable {
        // Fallback function
        // Called when no matching function is found
        // payable allows the contract to receive Ether

        emit FallbackCalled(
            msg.sender,
            msg.value,
            "Fallback function triggered!"
        );
        // Generates an event when the fallback function is triggered
        // msg.sender = address that called the contract
        // msg.value = amount of Ether sent
    }

    receive() external payable {
        // Receive function handles plain Ether sent to the contract
        // without any function call data

        emit FallbackCalled(
            msg.sender,
            msg.value,
            "Receive function triggered!"
        );
        // Generates an event when Ether is received directly
    }
}