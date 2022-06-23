# Combining CSV data with API

### Name: Diana Zawislak

### UCID: DZ29

## Introduction

The purpose of this unit is to familiarize you with parameterized tests, using the Pandas' library to get information
from a CSV file. This unit will begin to prepare you to make your own api over the next few assignments. The app will
ask a user for the city they are interested in, and then it will look up the population in the worldcities.csv file using
the Pandas library. It will then send the city to the weather API to get the current conditions and print the population
and current conditions for the user to view on the console.

## Unit Video - [Watch Here](https://youtu.be/1KCiHnc9D2w)

## Readings and References
1. https://www.howtogeek.com/348960/what-is-a-csv-file-and-how-do-i-open-it/
2. https://pandas.pydata.org/docs/user_guide/10min.html


## Setup Steps to Complete the Assignment

1. Put your name and UCID at the top of this file where indicated
2. Clone this repo and run pip install -r requirements.txt to install the dependencies
3. Download the world cities BASIC I.E. FREE! CSV file [here](https://simplemaps.com/data/world-cities) and unzip it and
   place the worldcities.csv in a data folder in the root directory of your app.
4. Signup for RapidAPI - [here](https://rapidapi.com/auth/sign-up)
5. Subscribe to the Weather api here - [here](https://rapidapi.com/weatherapi/api/weatherapi-com/)
6. Put that Rapid API key in the .env file using "RAPID_API_KEY=<your key>" syntax
### Run the app
Run the app to see how it works "python app\__init__py" <-reverse the slash on a mac/linux
### IMPORTANT - THE APP ONLY LOADS THE FIRST 5 CITIES IN THE CSV FILE TO MAKE IT PERFORMANT FOR TESTING

## Assignment Tasks
Tasks 1, 2, 3. will have successfully pass if you complete the setup instructions above.
1. 10 Points - Tests that the file is in the correct location (instructor provided)*
2. 10 Points - Tests that the population can be retrieved within the first 5 records of the file (instructor provided)*
3. 10 Points - Test that the weather API returns a response for the city requested (instructor provided)*
4. 35 Points - Use existing function in the app that gets the current condition and write a test in test task 4 to verify the
    current condition was retrieved. The condition will change, just check if the condition text field exists in the
    response and that it is not empty/null
5. 35 Points - Create a new function in the app and a test in task 5 and a test to get the longitude and latitude of a location from the csv file.  Try using parameterized queries

### *These will pass as long as you properly set up the app - Tasks 1,2, and 3

## Submission Instructions

Submit the link to your GitHub classroom repo to Canvas i.e. the link to what you are probably looking at right now
