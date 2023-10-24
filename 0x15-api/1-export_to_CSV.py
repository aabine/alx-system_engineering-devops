#!/usr/bin/python3
"""Exports to-do list information for a given employee ID to CSV format."""
import csv
import requests
import sys

def export_user_tasks_to_csv(user_id):
    # Base URL for the JSONPlaceholder API
    base_url = "https://jsonplaceholder.typicode.com/"
    
    # Make a request to get the user's data
    user = requests.get(base_url + "users/{}".format(user_id)).json()
    username = user.get("username")
    
    # Make a request to get the user's to-do list
    todos = requests.get(base_url + "todos", params={"userId": user_id}).json()
    
    # Create and write to the CSV file
    with open("{}.csv".format(user_id), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        
        # Use a list comprehension to write each task's information
        [writer.writerow([user_id, username, t.get("completed"), t.get("title")]) for t in todos]

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <user_id>")
    else:
        try:
            user_id = sys.argv[1]
            export_user_tasks_to_csv(user_id)
        except ValueError:
            print("Invalid user ID. Please provide an integer value.")
