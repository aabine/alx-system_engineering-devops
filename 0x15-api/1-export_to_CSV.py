#!/usr/bin/python3
"""Python script to export user's tasks in CSV format."""
import csv
import json
import sys
import requests


def convert_to_csv(user_id: int):
    """Converts JSON data to CSV format for a specific user."""
    base_url = "https://jsonplaceholder.typicode.com"
    users_url = f"{base_url}/users/{user_id}"
    todos_url = f"{base_url}/todos?userId={user_id}"

    try:
        with requests.get(users_url) as user_resp:
            user_data = json.loads(user_resp.content.decode())
        with requests.get(todos_url) as todos_resp:
            todos = json.loads(todos_resp.content.decode())

        with open(f"{user_id}.csv", "w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            for todo in todos:
                writer.writerow([user_id,
                                 user_data['username'],
                                 todo['completed'],
                                 todo['title']])
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <user_id>")
    else:
        try:
            user_id = int(sys.argv[1])
            convert_to_csv(user_id)
        except ValueError:
            print("Invalid user ID. Please provide an integer value.")
