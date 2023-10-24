# API Project Overview

In this project, I engaged in practical exercises involving the usage of APIs. Specifically, I worked with the [JSONPlaceholder REST API](https://jsonplaceholder.typicode.com/). Throughout this project, I gained valuable experience in collecting data from this API and exporting it in both CSV and JSON formats.

## Project Tasks :page_with_curl:

### Task 0: Gathering Data from the API

- Script: [0-gather_data_from_an_API.py](./0-gather_data_from_an_API.py)
- Description: A Python script designed to retrieve and display information regarding the to-do list progress of a specified employee ID.
- Usage: `python3 0-gather_data_from_an_API.py <employee ID>`
- Output Format: `Employee <employee name> is done with tasks (<# completed tasks>/<total # tasks>)`

### Task 1: Exporting to CSV

- Script: [1-export_to_CSV.py](./1-export_to_CSV.py)
- Description: A Python script for exporting to-do list information of a specified employee ID to a CSV format.
- Usage: `python3 1-export_to_CSV.py <employee ID>`
- Output File Name: `<user id>.csv`
- CSV Format: `"<user id>","<username>","<task completed status>","<task title>"`

### Task 2: Exporting to JSON

- Script: [2-export_to_JSON.py](./2-export_to_JSON.py)
- Description: A Python script for exporting to-do list information of a specified employee ID to JSON format.
- Usage: `python3 2-export_to_JSON.py <employee ID>`
- Output File Name: `<user id>.json`
- JSON Format: `{ "<user id>": [ {"task": "<task title>", "completed": <task completed status>, "username": "<username>"}, ... ]}`

### Task 3: Dictionary of List of Dictionaries

- Script: [3-dictionary_of_list_of_dictionaries.py](./3-dictionary_of_list_of_dictionaries.py)
- Description: A Python script that exports to-do list information for all employees to JSON format.
- Usage: `python3 3-dictionary_of_list_of_dictionaries.py`
- Output File Name: `todo_all_employees.json`
- JSON Format: `{ "<user id>": [ {"username": "<username>", "task": "<task title>", "completed": <task completed status>}, {"username": "<username>", "task": "<task title>", "completed": <task completed status>}, ... ], "<user id>": [ {"username": "<username>", "task": "<task title>", "completed": <task completed status>}, {"username": "<username>", "task": "<task title>", "completed": <task completed status>}, ... ]}`
