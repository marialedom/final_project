# # create a dictionary with all tasks = To-Do List

# to_do_list = {}
# filters = ["due date", "subject", "priority level", "status"]

# #simplified id

# class Task:

#     status = {0: "To-Do", 1: "In Progress", 2: "Complete"}

#     def __init__(self, task_id, status, title, description, subject, due_date_s, TOPICS=None, priority_rating_init=None):
#         self.id = task_id ##no idea if this is correct, or best way to generate ids

#         self.status = status
        
#         self.title = title

#         self.description = description

#         self.subject = subject

#         self.due_date_s = due_date_s #DUE DATE AS A STRING IN FORMAT

#         if TOPICS is None:
#             self.topics = []

#         if priority_rating_init is None:
#             self.priority_rating = 0


#     def set_duedate(self, due_date_s: str):
#         import maya
#         self.due_date = maya.parse(due_date_s).datetime()
#         return self.due_date
    

#     def get_priority_rating(self):
#         """Function takes the current date and the due date of an assignment to rate it in priority from 1 (not priority) to 5 (highest priority)
#         """
#         # Assuming 'current_date' is a variable representing the current date
#         import maya
#         import datetime
        
#         if self.priority_rating == 0:
#             current_date = datetime.datetime.now()
            
#             # Calculate the time difference between current date and due date
#             time_difference = self.due_date - current_date

#             # Assign priority rating based on time difference
#             if time_difference.days < 0:
#                 self.priority_rating = 2 # Past due, lowest priority
#             elif time_difference.days <= 3:
#                 self.priority_rating = 5  # Due within 3 days, highest priority
#             elif time_difference.days <= 7:
#                 self.priority_rating = 4  # Due within 7 days, high priority
#             else:
#                 self.priority_rating = 3  # Other cases, medium priority

#         else: 
#             self.priority_rating = self.priority_rating

#             return self.priority_rating
        

    

#     def task_details_add(self):
        
#         to_do_list[self.id] = {"ID": self.id, "Title": self.title, "Description": self.description, "Subject": self.subject, "Due Date": self.due_date, "Topics": self.topics, "Status": self.task_status, "Priority rating": self.priority_rating} 

#         return(f" Title: {self.id}, Description: {self.description}, Subject: {self.subject}, Due Date: {self.due_date}, Topics: {self.topics},Status: {self.task_status}, Priority_rating: {self.priority_rating}")
    


# ### calculate priority level/order based on due date and priority rating

