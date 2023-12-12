# final_project
## Team members: Maria Dominguez &amp; Natalie Guillamon

This project aims to create a simple task manager that users can interact with to simplify productivity. 

## Table of Contents

- [final\_project](#final_project)
  - [Team members: Maria Dominguez \& Natalie Guillamon](#team-members-maria-dominguez--natalie-guillamon)
  - [Table of Contents](#table-of-contents)
  - [Project Overview](#project-overview)
  - [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [OOP\_FUNCTIONS.py](#oop_functionspy)
    - [app\_2.py](#app_2py)
  - [Usage \& Features](#usage--features)
    - [1- OOP\_FUNCTIONS.py](#1--oop_functionspy)
    - [2- app\_2.py](#2--app_2py)
    - [3- templates/dashboard.html](#3--templatesdashboardhtml)
  - [Contributing](#contributing)
  - [Acknowledgments](#acknowledgments)
  - [Learnings](#learnings)

## Project Overview

Our goal with this project is to create a dashboard with some "widgets" that best simplify task management. Our project allows users to input notes and tasks to a to-do list, all of which are displayed in the dashboard. There is also a Pomodoro timer for users to track 25 minutes of productivity, followed by a break. Our academic goal with this project is to code a webapp where the back-end must get and post ifnormation from the user, and update in real time. Our overall vision for this webapp would be for a visually-appealing, interactive platform that is simple and features components that users might not think of tracking when managing tasks but might improve their time-management abilities. 

## Getting Started

The user will have to dowload the "new_project" folder of this repository and templates (dashboard.html) to run this project locally. This project is written in Python 3.11, html and Javascript, therefore, these need to be installed/understood.

### Prerequisites

This code requires the packages:

### OOP_FUNCTIONS.py
-datetime
-uuid

### app_2.py

-Flask
-jinja2
-OOP_FUNCTIONS.py

## Usage & Features

This project has 3 separate files that are relevant to its current functionality:

### 1- OOP_FUNCTIONS.py

This file defines the Class functions for "Task()" and "ToDoList()". Some of the functions within this tasks are not necessarily being used in the other two files or do not provide functionality yet, but we had defined them to structure our way of thinking about lists, tasks and their actions.

### 2- app_2.py

This file uses Flask to define the app routes for the program. app_2.py describes how user input will be collected (GET), and displayed (POST). Functions in this file are meant to update the page for each action taken, whether that be an added task, or timer started, or list filtered.


### 3- templates/dashboard.html

This file is the html template for the webapp. The htlm begins with some style features to make the interface more appealing, and then works through assigning forms, buttons, and different functions within the webapp. Lastly, at the bottom of this file, is the JavaScript built to provide some of these features with functionality (ex: Pomodoro timer running, Notes staying in the page, Filtering taking place)


## Contributing

To contribute, make sure that you contribution aligns with the project's goal and two main aspect we want each widget to meet: Simplicity, and  Functionality. This program is meant to serve as a quick solution to task management, a simplified aesthetic and functional method of prioritization can allow the mind to declutter for a focused approach. 

Feel free to make pull request if your contributions align with this philosophy.


## Acknowledgments

This project takes inspiration from certain features offered by notion and aims to replicate them in an automized way for a more user-friendly approach. ChatGPT was used for code organization in OOP and to generate htlm and javascript code for the webapp. 

## Learnings

We weren't able to implement most of the fucntions we initially proposed, and our aesthetics & functionality are still a work in progress. However, a good framework and base for a full-on application was set through this script and could serve as a prototype. 

A huge learning was the need for several iterations during the coding proccess. We now understand why so many programming teams use agile methods and scrums, as we repetitedly had to go back and forth with different aspect of the code, and yet wouldn't have been able to proceed any part without testing the other. The co-dependency between each piece of the code suggests that the best approach is to implement one feature at a time and check for its functionality. Although it isn't always possible to plan for an implementation order, it is best to remain conservative and go feature by feature, rather than sturcture all features and later have to edit them.

Additionally, this process brought our attention to data storing. We kept/keep getting errors when using the "add tasK" button that are most likely relating to data not being stored properly (or not being assinged the right destination). This is a very essential part of building a webapp that we tend to be oblivious to when interacting with one. Given the difficulty we had with this, we revaluated our data structure and realized that it is very hard to implement each aspect of the webapp without think of the others as well. That is to say, whenever we created (for example) a dictionary, it might be the most appropriate data structure if we were coding only for python, but for a webapp the way that information will be taken, written in, and displayed might be best represented in another way (say as its own variable, or just as an object)

As you can observe while inspecting and experimenting with our code, there is a considerable amount of disregarded code still present. This indicates a substantial process of trial and error. We attempted various approaches learned in class and eventually settled on those that enabled our code to flow and work seamlessly. The most significant pivot in the project was the decision not to proceed with the idea of using the Canvas API. This choice was influenced by privacy issues associated with its implementations and the unavailability of access to the Canvas Key Developer.
