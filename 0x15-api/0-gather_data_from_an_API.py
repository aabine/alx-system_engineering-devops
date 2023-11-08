#!/usr/bin/python3
"""Python script to display employee todo progress."""
import requests
import sys


def get_employee_todo_progress(user_id):
    """
    Retrieves the progress of a given employee's tasks from a remote API.

    Parameters:
        user_id (int): The ID of the employee whose tasks are to be retrieved.

    Raises:
        ValueError: If the user_id is not an integer.

    Returns:
        None
    """
    if not isinstance(user_id, int) or user_id is None:
        raise ValueError("Employee ID must be an integer.")

    url = "https://jsonplaceholder.typicode.com/"

    try:
        with requests.get(f"{url}users/{user_id}") as user:
            user_data = user.json()

        with requests.get(f"{url}todos", params={"userId": user_id}) as tasks:
            tasks_data = tasks.json()

        completed_tasks = [task for task in tasks_data if task["completed"]]

        print("Employee {} is done with tasks({}/{}):".format(
            user_data["name"], len(completed_tasks), len(tasks_data)
        ))
        for task in completed_tasks:
            print("\t {}".format(task["title"]))

    except requests.exceptions.RequestException as e:
        print("An error occurred:", str(e))


if __name__ == "__main__":
    user_id = int(sys.argv[1])
    get_employee_todo_progress(user_id)
