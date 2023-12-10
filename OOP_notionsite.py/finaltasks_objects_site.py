import datetime
import uuid

to_do_list = {}

class Task:
    status_mapping = {0: "To-Do", 1: "In Progress", 2: "Complete"}

    def __init__(self, title, description, subject, due_date_s, topics=None):
        self.id = str(uuid.uuid4())  # Use UUID for a more sophisticated ID
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

    def task_details_add(self):
        to_do_list[self.id] = {
            "ID": self.id,
            "Title": self.title,
            "Description": self.description,
            "Subject": self.subject,
            "Due Date": self.due_date.strftime('%Y-%m-%d'),
            "Topics": self.topics,
            "Status": self.status_mapping[self.status],
            "Priority rating": self.priority_rating
        }

        return f"Title: {self.title}, Description: {self.description}, Subject: {self.subject}, Due Date: {self.due_date}, Topics: {self.topics}, Status: {self.status_mapping[self.status]}, Priority Rating: {self.priority_rating}"

# Example usage:
task1 = Task("Task 1", "Description 1", "Subject 1", "2023-12-12", ["topic1", "topic2"])
print(task1.task_details_add())

