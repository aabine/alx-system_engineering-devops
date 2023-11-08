#!/usr/bin/python3
import aiohttp
import asyncio
import json

async def fetch_and_convert_to_json():
    user_url = "https://jsonplaceholder.typicode.com/users"
    todos_url = "https://jsonplaceholder.typicode.com/todos"

    async with aiohttp.ClientSession() as session:
        async with session.get(user_url) as user_resp, session.get(todos_url) as todos_resp:
            user_data = await user_resp.json()
            todos_data = await todos_resp.json()

    user_tasks = {}  # Create a dictionary to hold the user tasks data
    for user in user_data:
        user_id = user["id"]
        username = user["username"]
        # Filter todos for the current user and format them as specified
        user_tasks[user_id] = [
            {
                "username": username,
                "task": todo["title"],
                "completed": todo["completed"]
            }
            for todo in todos_data if todo["userId"] == user_id
        ]

    with open("todo_all_employees.json", "w") as json_file:
        # Serialize the user_tasks dictionary to JSON
        json.dump(user_tasks, json_file)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(fetch_and_convert_to_json())
