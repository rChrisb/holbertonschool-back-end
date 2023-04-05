#!/usr/bin/python3
"""Gather data from an API"""

import json
import requests
from sys import argv


api_url = "https://jsonplaceholder.typicode.com"

if __name__ == "__main__":
    all_users = requests.get(f"{api_url}/users").json()
    """ user_info = requests.get(f"{api_url}/users/{argv[1]}").json()
    todo_list = requests.get(f"{api_url}/todos?userId={argv[1]}").json()

    done_tasks = []
    for task in todo_list:
        if task['completed'] is True:
            done_tasks.append(task)
    number_of_done_tasks = len(done_tasks)
    total_number_of_tasks = len(todo_list)
    employee_name = user_info["name"]

    print(f"Employee {employee_name} is done with tasks\
({number_of_done_tasks}/{total_number_of_tasks}):")
    for task in done_tasks:
        print(f"\t {task['title']}") """

    todo_dict = {}
    for user in all_users:
        user_id = user["id"]
        user_name = user["username"]
        todo_list = requests.get(f"{api_url}/todos?userId={user_id}").json()
        new_todo_list = []
        for task in todo_list:
            task_dict = {"username": user_name, "task": task["title"],
                         "completed": task["completed"]}
            new_todo_list.append(task_dict)
        todo_dict[user_id] = new_todo_list
    with open("todo_all_employees.json", "w") as file:
        json.dump(todo_dict, file)
