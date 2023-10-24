#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""
import requests
import sys


def get_employee_todo_progress(employee_id):
    """
    Retrieves and displays the completed tasks of an employee.

    Args:
        employee_id (int): The ID of the employee.
    Raises:
        ValueError: If the employee ID is not a valid integer.
    """
    if not isinstance(employee_id, int):
        raise ValueError("Employee ID must be an integer.")

    # Get content from Api response
    url = "https://jsonplaceholder.typicode.com/"
    get_user = requests.get(url + "users/{}".format(employee_id))
    get_tasks = requests.get(f"{url}todos", params={"userId": employee_id})

    # Get data from response
    user_data = get_user.json()
    tasks_data = get_tasks.json()

    # Get completed tasks
    completed_tasks = [task for task in tasks_data if task["completed"]]

    # Print completed tasks
    print("Employee {} is done with tasks({}/{}):".format(
        user_data["name"], len(completed_tasks), len(tasks_data)
    ))
    for task in completed_tasks:
        print("\t {}".format(task["title"]))


if __name__ == "__main__":
    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)
