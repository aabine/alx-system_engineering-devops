#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""
import sys
import requests


def get_employee_todo_progress(employee_id):
    """
    Retrieves and displays the completed tasks of an employee.

    Args:
        employee_id (int): The ID of the employee.
    Raises:
        ValueError: If the employee ID is not a valid integer.
    """
    base_url = "https://jsonplaceholder.typicode.com"
    users_url = f"{base_url}/users"
    todos_url = f"{base_url}/todos"

    try:
        user_resp = requests.get(f"{users_url}/{employee_id}")
        user_resp.raise_for_status()

        user = user_resp.json()

        todos_resp = requests.get(f"{todos_url}?userId={employee_id}")
        todos_resp.raise_for_status()

        todos = todos_resp.json()

        completed = [todo for todo in todos if todo['completed']]
        print("Employee {} is done with tasks({}/{}):".format(
            user['username'], len(completed), len(todos)))
        for todo in completed:
            print(f"\t{todo['title']}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
    else:
        try:
            employee_id = int(sys.argv[1])
            get_employee_todo_progress(employee_id)
        except ValueError:
            print("Please enter a valid integer for the employee ID.")
