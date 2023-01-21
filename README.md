# COFFEE MACHINE PROGRAM<img src="https://cdn-icons-png.flaticon.com/512/9416/9416142.png" style="width: 50px;height:50px;">

**Developer: Slava Kondriianenko**

💻 [Visit live website](https://ci-pp3-coffee-machine.herokuapp.com/)

![Mockup image]()

## About

This is a command-line program for the Coffee Machine


## Table of Contents
- [COFFEE MACHINE PROGRAM](#coffee-machine-program)
  - [About](#about)
  - [Table of Contents](#table-of-contents)
  - [Project Goals](#project-goals)
    - [User Goals](#user-goals)
    - [Site Owner Goals](#site-owner-goals)
  - [User Experience](#user-experience)
    - [Target Audience](#target-audience)
    - [User Requirements and Expectations](#user-requirements-and-expectations)
    - [User Manual](#user-manual)
      - [Program started](#program-started)
      - [Drink chosen](#drink-chosen)
      - [Drink prepared](#drink-prepared)
      - [Report](#report)
      - [Off](#off)
  - [User Stories](#user-stories)
    - [Users](#users)
    - [Coffee machine Owner](#coffee-machine-owner)
  - [Technical Design](#technical-design)
    - [Flowchart](#flowchart)


## Project Goals

### User Goals

- Order favourite coffee
- Easy menu to order coffee
- Be able to insert money to buy coffee

### Site Owner Goals

- Create program to let user order coffee
- Ensure that users understand the ways to make coffee
- Create a program that gives feedback to the user whilst program running

## User Experience

### Target Audience

- People, who loves coffee
- Coffee machine makers, who want software for their machines

### User Requirements and Expectations

- A simple, error-free program
- Straightforward navigation
- Feedback through program running

### User Manual

<details><summary>Click here to view instructions</summary>

#### Program started
- On the top of the program user can see logo and question what want user to drink
- Program checks wrong input, rises an error if it wrong and shows allowed inputs
- Coffee machine allows: '1', '2', '3' for choosing drink, 'off' and 'report' to off machine or see profit and resourses left respectively
                                    
#### Drink chosen
- Program checks if there are enough resourses in coffee machine to make drink
- Program asks to insert coins by number input
- Coffee machine asks how many 20c, 50c and 1€ user will insert
  - if inserted money enough program makes choosen drink and gives user change
  - if inserted money not enough program raises massage about refund money and how much drink costs

#### Drink prepared
- Program updates resourses in google sheet 
- Program updates profit in google sheet according to the cost of the drink
- Program raises massage about prepared drink

#### Report
- User can check report about resourses left and profit
- To see report user should type "report" in main menu
- User have to enter their email to pass report menu
  - this feature can be used in future to pass report menu for an authorised users only 

#### Off
- To stop program user can type "off" in main menu
</details>

## User Stories

### Users
1. I want to have clear options to select drink
2. I want to be able to insert money 
3. I want to get change if I insert more money than drink cost
4. I want to receive a real time feedback throughout the program running
5. I want to see report
6. I want to be able to turn off the coffee machine

### Coffee machine Owner
7. I want users to easily select options from the menu
8. I want the user to get feedback in case of wrong input
9. I want collect profit after user insert money
10. I want to let user to see report after authorization
11. I want to validate wrong email input
12. I want to update google sheets while user makes their drink

## Technical Design

### Flowchart

The following flowchart summarises the structure and logic of the application.

<details><summary>Flowchart</summary>
<img src="docs/flowchart.png">
</details>
