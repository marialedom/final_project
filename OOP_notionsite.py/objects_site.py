# create a dictionary with all tasks = To-Do List
import maya

to_do_list = {}
filters = ["due date", "subject", "priority level", "status"]
status = {0: "To-Do", 1: "In Progress", 2: "Complete"}


#simplified id

class Task:
      
    def __init__(self, task_id, status, title, description, subject, due_date_s, TOPICS=None):
        self.id = task_id ##no idea if this is correct, or best way to generate ids

        self.status = status
        
        self.title = title

        self.description = description

        self.subject = subject

        self.due_date_s = due_date_s #DUE DATE AS A STRING IN FORMAT

        if TOPICS is None:
            self.topics = []


    def set_duedate(self, due_date_s: str):
        import maya
        self.due_date = maya.parse(due_date_s).datetime()
        return self.due_date
    

    def get_priority_rating(self):
        """Function takes the current date and the due date of an assignment to rate it in priority from 1 (not priority) to 5 (highest priority)
        """
        # Assuming 'current_date' is a variable representing the current date
        import maya
        current_date = maya.datetime.now()
        
        # Calculate the time difference between current date and due date
        time_difference = self.due_date - current_date

        # Assign priority rating based on time difference
        if time_difference.days < 0:
            self.priority_rating = 2 # Past due, lowest priority
        elif time_difference.days <= 3:
            self.priority_rating = 5  # Due within 3 days, highest priority
        elif time_difference.days <= 7:
            self.priority_rating = 4  # Due within 7 days, high priority
        else:
            self.priority_rating = 3  # Other cases, medium priority

        return self.priority_rating

    

    def diplay_task_details(self):
        
        to_do_list[self.id] = {"ID": self.id, "Title": self.title, "Description": self.description, "Subject": self.subject, "Due Date": self.due_date, "Topics": self.topics} #missing status and priority rating
        print(f"Your '{self.title}' task has been added to your To-Do List")




### calculate priority level/order based on due date and priority rating

