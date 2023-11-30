# create a dictionary with all tasks = To-Do List

to_do_list = {}
filter = ["due date", "subject", "priority level", "status"]

#simplified id

class Task:
    
    def __init__(self, id, filter, status, priority_rating, title, description, subject, due_date, TOPICS = None):
        self.status = status
        self.priorityrating = priority_rating
        self.filter = filter
        self.title = title
        self.description = description
        self.subject = subject
        self.duedate = due_date
        self.id = id ##no idea if this is correct, or best way to generate ids
        if TOPICS == None:
            self.topics = []
    
    def new_task_todo(self, id, filter, title, description, subject, due_date, TOPICS):
        
        to_do_list[self.id] = {"ID": self.id, "Title": self.title, "Description": self.description, "Subject": self.subject, "Due Date": self.due_date, "Topics": self.topics} #missing status and priority rating
        print(f"Your '{self.title}' task has been added to your To-Do List")





        
### calculate priority level/order based on due date and priority rating
    