from project.task import Task


class Section:

    def __init__(self, name: str):
        self.name = name
        self.tasks: list[Task] = []

    def add_task(self, new_task: Task) -> str:
        if new_task in self.tasks:
            return f"Task is already in the section {self.name}"
        else:
            self.tasks.append(new_task)
            return f"Task {new_task.details()} is added to the section"

    def complete_task(self, task_name: str) -> str:
        try:
            task = [el for el in self.tasks if el.name == task_name][0]
            task.completed = True
            return f"Completed task {task_name}"
        except IndexError:
            return f"Could not find task with name {task_name}"

    def clean_section(self) -> str:
        completed_tasks = [el for el in self.tasks if el.completed]
        not_completed_tasks = [el for el in self.tasks if not el.completed]
        self.tasks = not_completed_tasks
        return f"Cleared {len(completed_tasks)} tasks."

    def view_section(self) -> str:
        result = f"Section {self.name}:\n"
        result += "\n".join([el.details() for el in self.tasks])
        return result


# Example Usage
task = Task("Make bed", "27/05/2020")

print(task.change_name("Go to University"))
print(task.change_due_date("28.05.2020"))
task.add_comment("Don't forget laptop")
print(task.edit_comment(0, "Don't forget laptop and notebook"))
print(task.details())

section = Section("Daily tasks")
print(section.add_task(task))

second_task = Task("Make bed", "27/05/2020")
print(section.add_task(second_task))

print(section.clean_section())
print(section.view_section())
