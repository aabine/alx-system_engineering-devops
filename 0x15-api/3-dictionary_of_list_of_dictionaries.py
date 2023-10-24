#!/usr/bin/python3
"""Python script to export user's tasks in JSON format."""

import json
import requests


def convert_to_json() -> None:
    """Converts JSON data to JSON format for all users and their tasks."""
    user_url = "https://jsonplaceholder.typicode.com/users"
    todos_url = "https://jsonplaceholder.typicode.com/todos"

    try:
        with requests.get(user_url) as user_resp:
            users = json.loads(user_resp.content.decode())
        with requests.get(todos_url) as todos_resp:
            todos = json.loads(todos_resp.content.decode())

        user_tasks = {}

        for user in users:
            user_id = user["id"]
            username = user["username"]
            user_tasks[user_id] = [
                {
                    "username": username,
                    "task": todo["title"],
                    "completed": todo["completed"]
                }
                for todo in todos if todo["userId"] == user_id
            ]

        with open("todo_all_employees.json", "w") as json_file:
            json.dump(user_tasks, json_file)
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    convert_to_json()
