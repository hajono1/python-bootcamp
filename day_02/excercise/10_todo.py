tasks = []

def create(tasks: list[str], task: str):
    tasks.append(task)
def read(tasks: list[str], index: int) -> str:
    return tasks [index]
def update(tasks: list[str], index: int, new_task: str):
    tasks[index] = new_task
def delete(tasks: list[str], index: int):
    tasks.pop(index)

create(tasks, "Buy milk")
create(tasks, "Do homework")
create(tasks, "Sleep")
assert "Buy milk" in tasks
assert read(tasks, 1) == "Do homework"
update(tasks, 0, "Buy coffee")
assert "Buy milk" not in tasks
assert "Buy coffee" in tasks
delete(tasks, 2)
assert "Sleep" not in tasks
assert len(tasks) == 2