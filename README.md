# Knapsack Optimizer Service

---
**Source Code**: <a href="https://github.com/arpitgupta1090/api-python-knapsack-optimiser" target="_blank">https://github.com/arpitgupta1090/api-python-knapsack-optimiser </a>

---

## Introduction

1. The **Knapsack Problem** : Given a set of items, each with a weight and a value, determine which items to include in the collection so that the total weight is less than or equal to a given limit and the total value is as large as possible.
2. There are 2 types of Knapsack problem:
   1. 0-1 knapsack problem.
   2. Partial knapsack problem.

3. This application provides an API to solve the Knapsack problem based on the following details provided by the user:
   1. Type of Knapsack problem.
   2. The capacity of the knapsack.
   3. the values and weights of each item in the knapsack. (Please read the API section for more details.)

## API

1. This application uses REST API with request and response in json format.
2. The format of the request json body and the output response (success and error) with examples are provided on the homepage of the application.
3. Please visit <a href="http://localhost:5000" target="_blank">this link</a> (home page "/" ) for more details on API documentation, once you start the app on your machine.
4. You can also use following <a href="http://localhost:5000/tryit" target="_blank">link</a> (swagger doc "/tryit") to try out the API.


## Installation

1. To install and run the application on your machine, follow the simple steps:
   1. Clone the github repository source code from the link provided above.
   2. move to the folder "api-python-knapsack-optimiser" and run the command: `docker-compose up --build` .

## Usage

1. Use the url: `http://<BASE_URL>/` for the OpenAPI documentation.
2. Hit the url: `http://<BASE_URL>/api/optimiser` with a post request and valid payload to get optimised data for your knapsack problem (refer to API doc on home page).

    ### Unit Testing
    Run the following command `pytest -cov --cov-report:html:coverage-report` to run the unit test cases. A coverage report will be generated in 'coverage-report folder'.

## Structure

Please refer this [link](structure.md) for code structure. 