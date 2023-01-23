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
    - [Languages](#languages)
    - [Frameworks \& Tools](#frameworks--tools)
    - [Libraries](#libraries)
      - [Python Libraries](#python-libraries)
      - [Third Party Libraries](#third-party-libraries)
  - [Features](#features)
    - [Program started](#program-started-1)
    - [Drink choosen](#drink-choosen)
    - [Money inserted](#money-inserted)
    - [Drink Prepared](#drink-prepared-1)


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

### Languages

- [Python](https://www.python.org/) programming language for the logic of the program

### Frameworks & Tools

- [Diagrams.net](https://app.diagrams.net/) was used to draw program flowchart
- [Google Sheets](https://www.google.co.uk/sheets/about/) were used to store drinks menu, resources and profit
- [Google Cloud Platform](https://cloud.google.com/cloud-console/) was used to manage access and permissions to the Google Services such as Google auth, sheets etc.
- [GitHub](https://github.com/) was used as a remote repository to store project code
- [Heroku Platform](https://dashboard.heroku.com/) was used to deploy the project into live environment

### Libraries

#### Python Libraries

- [unittest](https://docs.python.org/3/library/unittest.html) - used to carry out testing on single units in validation.py file

#### Third Party Libraries

- [colorama](https://pypi.org/project/colorama/) - Used this library to add color to the terminal and enhance user experience. I marked warning/error information with color red and user feedback with blue and green. Yellow color used for email verification. 
- [email_validator](https://pypi.org/project/email-validator/) - This library used to validate if user email input is of the form name@</span>example.com
- [gspread](https://docs.gspread.org/en/latest/) - Used gspread to add and manipulate data in the Google spreadsheet and to interact with Google APIs
- [google.oauth2.service_account](https://google-auth.readthedocs.io/en/master/) - This module used to set up the authentification needed to access the Google API and connect my Service Account with the Credentials function. A creds.json file is created with all details the API needs to access the google account.

## Features

### Program started
- User can see logo of the program
- User can choose their favourite drink
- User can off the machine or look at report
- User stories covered: 1, 7
<details>
<summary>Program started Screenshot</summary>
<img src="docs/features/program_started.png">
</details>

### Drink choosen
- If resources sufficient:
  - User can see message insert coins to buy coffee
  - Program ask user hom many 20c, 50c and 1€ coins user insert
  - User stories covered: 2
  <details>
  <summary>Resources enough Screenshot</summary>
  <img src="docs/features/enough_resources.png">
  </details>

- If resources not enough:
  - User receive a message that resources is not enough to make drink
  - User stories covered: 4
  <details>
  <summary>Resources not enough Screenshot</summary>
  <img src="docs/features/no_resources.png">
  </details>

### Money inserted
- If money enough to buy drink
  - User receive their change
  - User see message about updating profit and resources
  - User see message that their drink prepared
  - User stories covered: 3, 4, 9
  <details>
  <summary>Money enough Screenshot</summary>
  <img src="docs/features/money_enough.png">
  </details>
- If money not enough to make coffee:
  - User notified that not enough money to buy drink 
  - User can see message about drink cost
  - User can choose their drink again
  - User stories covered: 8      
  <details>
  <summary>Resources not enough Screenshot</summary>
  <img src="docs/features/money_not_enough.png">
  </details>

### Drink Prepared
- Program updates resources worksheet
- Program updates profit worksheet
- Program gives a feedback about updating worksheet
- User stories covered: 9, 12
<details>
<summary>Update Resources Screenshot</summary>
<img src="docs/features/update_resources.png">
</details>
<details>
<summary>Update Profit Screenshot</summary>
<img src="docs/features/update_profit.png">
</details>
<details>
<summary>Update Program Feedback Screenshot</summary>
<img src="docs/features/update_feedback.png">
</details>