
def to_do(chores):
    """This fxn has to print the chores to be done"""
    print("\nYour goal is to complete the following before the end of the day:")
    for chore in chores:
        print(f"\t-{chore}")
    print("GOOD LUCK!!")


def uncompleted(jobs_done, chores):
    """This fxn compares the list of chores done and not done and
    displays the uncompleted ones"""
    for chore in chores:
        if chore not in jobs_done:
            print(f"\t~{chore.title()} is left")

        elif chore in jobs_done:
            continue


def main():
    print("\n\t\tHello!, welcome to your TO DO LIST.")
    # Retrieving the tasks to be completed from user
    tasks = []
    list_length = int(input("How many tasks do you have to complete today?\n"))
    for i in range(list_length):
        task = input(f"Please, Enter Task {i + 1}: ")
        tasks.append(task)

    to_do(tasks)  # To display the different tasks to be done

    # Retrieving tasks already completed
    state = True
    while state:
        tasks_done = []
        print("\n(Answer after at least 1 task is done)")
        number_done = int(input("How many chores have you completed?\n"))
        if (number_done <= 0) or (number_done > list_length):
            print("Error")
            print("Number of tasks not valid")
            continue

        for i in range(number_done):
            task_done = input("Enter task done: ")
            tasks_done.append(task_done)

        # To compare and display the tasks left
        if number_done == list_length:
            print("\n\t\t\t~~~~Verifying~~~~")
            for task_done in tasks_done:
                if task_done in tasks:
                    print(f"\t-{task_done.title()} was carried out successfully.")
            print("\nCongratulations,To do list COMPLETED!!")
            state = False

        else:
            print("\nNicely done but:")
            uncompleted(tasks_done, tasks)
            print("KEEP PUSHING!!")


main()

