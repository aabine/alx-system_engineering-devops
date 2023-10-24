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
    if not isinstance(employee_id, int):
        raise ValueError("Employee ID must be an integer.")

    # Retrieve user data
    user_data = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{employee_id}").json()

    # Retrieve completed tasks for the employee
    get_content_from_user = requests.get(
        "https://jsonplaceholder.typicode.com/todos",
        params={"userId": employee_id}).json()

    # Filter completed tasks
    completed_tasks = [task for task in get_content_from_user
                       if task["completed"]]

    # Print employee progress
    print("Employee {} is done with tasks({}/{}):".format(
        user_data["name"], len(completed_tasks), len(get_content_from_user)))
    for task in completed_tasks:
        print(f"\t{task['title']}")


if __name__ == "__main__":
    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)
