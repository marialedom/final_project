import datetime
import uuid

class Task:
    status_mapping = {0: "To-Do", 1: "In Progress", 2: "Complete"}

    def __init__(self, title, description, subject, due_date_s, topics=None):
        self.id = str(uuid.uuid4())
        self.title = title
        self.description = description
        self.subject = subject
        self.due_date = self.parse_due_date(due_date_s)
        self.topics = topics if topics else []
        self.status = 0  # Default status is "To-Do"
        self.priority_rating = self.get_priority_rating()

    def parse_due_date(self, due_date_s):
        # Assuming the date string is in the format 'YYYY-MM-DD'
        return datetime.datetime.strptime(due_date_s, '%Y-%m-%d')

    def get_priority_rating(self):
        current_date = datetime.datetime.now()
        time_difference = self.due_date - current_date

        if time_difference.days < 0:
            return 2  # Past due, lowest priority
        elif time_difference.days <= 3:
            return 5  # Due within 3 days, highest priority
        elif time_difference.days <= 7:
            return 4  # Due within 7 days, high priority
        else:
            return 3  # Other cases, medium priority

    def as_dict(self):
        return {
            "ID": self.id,
            "Title": self.title,
            "Description": self.description,
            "Subject": self.subject,
            "Due Date": self.due_date.strftime('%Y-%m-%d'),
            "Topics": self.topics,
            "Status": self.status_mapping[self.status],
            "Priority rating": self.priority_rating
        }


class ToDoList:
    def __init__(self):
        self.tasks = {}

    def add_task(self, task):
        self.tasks[task.id] = task

    def get_task(self, task_id):
        return self.tasks.get(task_id)

    def get_all_tasks(self):
        return list(self.tasks.values())

    def update_task(self, task_id, updated_data):
        task = self.get_task(task_id)
        if task:
            for key, value in updated_data.items():
                setattr(task, key, value)

    def filter_tasks(self, filter_key, filter_value):
        filtered_tasks = []
        for task in self.tasks.values():
            if getattr(task, filter_key) == filter_value:
                filtered_tasks.append(task)
        return filtered_tasks


# Create an instance of ToDoList
to_do_list = ToDoList()

# Create a new task
task1 = Task("Task 1", "Description 1", "Subject 1", "2023-01-01", ["topic1", "topic2"])

# Add the task to the to-do list
to_do_list.add_task(task1)

# Update the task status
to_do_list.update_task(task1.id, {'status': 1})

# Filter tasks by status
in_progress_tasks = to_do_list.filter_tasks('status', 1)

# Display task details
for task in in_progress_tasks:
    print(task.as_dict())

