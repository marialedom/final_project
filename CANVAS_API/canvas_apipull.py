import datetime
import uuid
import time
import matplotlib.font_manager

class Task:
    status_mapping = {0: "To-Do", 1: "In Progress", 2: "Complete"}

    def __init__(self):
        self.id = str(uuid.uuid4())
        self.title = input("Enter the title of the task: ")
        self.description = input("Enter the description: ")
        self.subject = input("Enter the subject: ")
        self.due_date = self.parse_due_date(input("Enter the due date (YYYY-MM-DD): "))
        self.topics = input("Enter topics (comma-separated): ").split(', ')
        self.status = 0  # Default status is "To-Do"
        self.priority_rating = self.get_priority_rating()
        self.pomodoro_timer = None  # Pomodoro timer attribute
        self.notes_font = None
        self.notes_font_size = None
        self.notes_font_color = None

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

    def start_pomodoro(self, work_minutes=25, break_minutes=5):
        work_minutes = int(input("Enter Pomodoro work duration in minutes (default is 25): ") or work_minutes)
        break_minutes = int(input("Enter break duration in minutes (default is 5): ") or work_minutes)

        self.pomodoro_timer = datetime.datetime.now() + datetime.timedelta(minutes=work_minutes)
        print(f"Pomodoro timer started for {work_minutes} minutes.")

        self.customize_notes()

        time.sleep(work_minutes * 60)
        print("Pomodoro work session completed.")

        self.pomodoro_timer = datetime.datetime.now() + datetime.timedelta(minutes=break_minutes)
        print(f"Break timer started for {break_minutes} minutes.")

        time.sleep(break_minutes * 60)
        print("Break session completed.")

        self.stop_pomodoro()

    def customize_notes(self):
        print("Customize your notes:")
        self.notes_font = input(f"Enter font (choose from {', '.join(get_available_fonts())}): ")
        self.notes_font_size = input("Enter font size (e.g., 12, 14): ")
        self.notes_font_color = input("Enter font color (e.g., red, #00FF00): ")

    def stop_pomodoro(self):
        self.pomodoro_timer = None

    def add_note(self, note):
        self.notes.append({"timestamp": datetime.datetime.now(), "note": note})

    def as_dict(self):
        return {
            "ID": self.id,
            "Title": self.title,
            "Description": self.description,
            "Subject": self.subject,
            "Due Date": self.due_date.strftime('%Y-%m-%d'),
            "Topics": self.topics,
            "Status": self.status_mapping[self.status],
            "Priority rating": self.priority_rating,
            "Pomodoro Timer": self.pomodoro_timer.strftime('%Y-%m-%d %H:%M:%S') if self.pomodoro_timer else None,
            "Notes": {
                "Font": self.notes_font,
                "Font Size": self.notes_font_size,
                "Font Color": self.notes_font_color
            }
        }

def get_available_fonts():
    fonts = [f.name for f in matplotlib.font_manager.fontManager.ttflist]
    return fonts

class ToDoList:
    def __init__(self):
        self.tasks = {}

    def add_task(self, task):
        self.tasks[task.id] = task

    def get_task(self, task_id):
        return self.tasks.get(task_id)

    def get_all_tasks(self, sort_key='due_date', ascending=True):
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

# Create ToDoList instance
to_do_list = ToDoList()

# Add a task to the list
task1 = Task()
to_do_list.add_task(task1)

# Sort tasks by due date in ascending order
sorted_duedate = to_do_list.get_all_tasks(sort_key='due_date', ascending=False)

# Display sorted task details
for task in sorted_duedate:
    print(task.as_dict())
