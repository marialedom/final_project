# create a dictionary with all tasks = To-Do List

to_do_list = {}
filters = ["due date", "subject", "priority level", "status"]
status = {0: "To-Do", 1: "In Progress", 2: "Complete"}


#simplified id

class Task:
      
    def __init__(self, task_id, filters, status, title, description, subject, due_date_s, TOPICS = None):
        self.id = task_id ##no idea if this is correct, or best way to generate ids

        self.status = status

        self.filter = filters

        self.title = title

        self.description = description

        self.subject = subject

        self.due_date_str = due_date_s #DUE DATE AS A STRING IN FORMAT

        if TOPICS == None:
            self.topics = []

    def set_duedate(self, due_date_s: str):
        import maya
        self.due_date = maya.parse(due_date_s).datetime()
        return self.due_date


    
    # def get_priority_rating(self, due_date_s):
    #     """Function takes the current date and the due date of an assingment to rate it in priority from 1 (not priority) 5 (highest priority)
    #     """
    #     import maya 
    #     # maya.parse(due_date_s).slang_time()
    #     self.due_date = maya.parse(due_date_s).datetime()


    #     self.priority_rating = self.duedate_rating 

    #     return self.priority_rating



    def new_task_todo(self, id, filter, title, description, subject, due_date, TOPICS):
        
        to_do_list[self.id] = {"ID": self.id, "Title": self.title, "Description": self.description, "Subject": self.subject, "Due Date": self.due_date, "Topics": self.topics} #missing status and priority rating
        print(f"Your '{self.title}' task has been added to your To-Do List")




### calculate priority level/order based on due date and priority rating

