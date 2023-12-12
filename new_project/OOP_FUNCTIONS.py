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

    def get_all_tasks(self, sort_key='due_date', ascending=True): # SORTED BY DUE DATE
        sorted_tasks = sorted(self.tasks.values(), key=lambda x: getattr(x, sort_key), reverse=not ascending)
        return sorted_tasks

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

