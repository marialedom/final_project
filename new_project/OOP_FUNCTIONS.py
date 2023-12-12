import datetime
import uuid

class Task:
    """
    Task(s) have the following attributes:
    id
    title
    description
    subject
    due_date
    topic
    status
    priority_rating

    Some of its functions include:
    parse_due_date(self, due_date_s)
    get_priority_rating(self)
    as_dict(self)
    """
    status_mapping = {0: "To-Do", 1: "In Progress", 2: "Complete"}

    def __init__(self, title, description, subject, due_date_s, topics=None):
        """Initializing object

        Args:
            title (str): title for the task
            description (str): a description of the task
            subject (str): subject or category of the tasks
            due_date_s (date): date that the task is due by 
            topics (str, optional): List of topics that the task relate to. Defaults to None.
        """
        self.id = str(uuid.uuid4())
        self.title = title
        self.description = description
        self.subject = subject
        self.due_date = self.parse_due_date(due_date_s)
        self.topics = topics if topics else []
        self.status = 0  # Default status is "To-Do"
        self.priority_rating = self.get_priority_rating()

    # def parse_due_date(self, due_date_s):
    #     # Assuming the date string is in the format 'YYYY-MM-DD'
    #     return datetime.datetime.strptime(due_date_s, '%Y-%m-%d')

    def get_priority_rating(self):
        """
        Takes the object and returns an index indicating the level of priority for the task 

        if returns...
        2: Past due, lowest priority
        3: medium priority
        4: Due within 7 days, high priority
        5: Due within 3 days, highest priority

        """
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
        """
        shows task's information as dictionary 
        """
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
    """
    ToDoList is a collection of tasks
    It includes the following functions:
    add_task(self, task)
    get_task(self, task_id)
    get_all_tasks(self, sort_key='due_date', ascending=True)
    update_task(self, task_id, updated_data)
    filter_tasks(self, filter_key, filter_value)
    """
    def __init__(self):
        """
        Initializing ToDoList by creating a list with tasks
        """
        self.tasks = {}

    def add_task(self, task):
        """
        Takes object and task as arguments, adds tasks to list 
        """
        self.tasks[task.id] = task
        return(self)

    def get_task(self, task_id):
        """
        Takes self and task_id as parameters. Returns task Title based on task id.
        """
        return self.tasks.get(task_id)

    def get_all_tasks(self, sort_key='due_date', ascending=True): # SORTED BY DUE DATE
        """
        Takes object, sort_key, and ascending as True or False

        This function returns all tasks sorted by the sort key
        """
        sorted_tasks = sorted(self.tasks.values(), key=lambda x: getattr(x, sort_key), reverse=not ascending)
        return sorted_tasks

    def update_task(self, task_id, updated_data):
        """
        This function takes object, task_id, and updated_data to return an edited task with a new priority rating.
        """
        task = self.get_task(task_id)
        if task:
            for key, value in updated_data.items():
                setattr(task, key, value)

    def filter_tasks(self, filter_key, filter_value):
        """
        This function takes object, filter_key, and filter_value to filter tasks in the to-do list

        """
        filtered_tasks = []
        for task in self.tasks.values():
            if getattr(task, filter_key) == filter_value:
                filtered_tasks.append(task)
        return filtered_tasks

