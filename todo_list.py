print("Welcome back to the to-do list app!")

tasks = {
    "learn math" : 1
}

while True: 
    user_input = input("Do you want to add or remove a task (A/R)? ")
    if user_input == "A":
        add_task = input("Describe the task you want to add: ")
        for key, value in tasks.copy().items():
            value = value + 1
            tasks[add_task] = value
        print(tasks)
    elif user_input == "R":
        pass
    else:
        print("Sorry, invalid input. Please try again.")