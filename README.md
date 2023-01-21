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