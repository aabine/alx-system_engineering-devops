#!/usr/bin/python3
"""Python script to export user's tasks in JSON format."""

import json
import requests
import sys


def convert_to_json(user_id: int) -> None:
    """Converts JSON data to JSON format for a specific user."""
    user_url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={user_id}"

    try:
        with requests.get(user_url) as user_resp:
            user_data = json.loads(user_resp.content.decode())
        with requests.get(todos_url) as todos_resp:
            todos = json.loads(todos_resp.content.decode())

        tasks = []
        for todo in todos:
            task = {
                "task": todo["title"],
                "completed": todo["completed"],
                "username": user_data["username"]
            }
            tasks.append(task)

        data = {
            str(user_id): tasks
        }

        with open(f"{user_id}.json", "w") as json_file:
            json.dump(data, json_file)
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <user_id>")
    else:
        try:
            user_id = int(sys.argv[1])
            convert_to_json(user_id)
        except ValueError:
            print("Invalid user ID. Please provide an integer value.")
