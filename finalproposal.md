# The Big Idea
In this revised website project, our central focus is on leveraging the Canvas API to develop a highly functional and user-friendly productivity calendar. The primary goal is to seamlessly integrate with Canvas, presenting all assignments and tasks in an organized calendar and list format. Users will benefit from a consolidated view of their academic or work-related tasks directly within the website. The key functionalities include retrieving tasks from Canvas, arranging them in a calendar and list layout, and providing the option for users to add their own tasks. The list will be organized by level of priority based on the data given from the calendar on the assignment, the level of difficulty to perform the assignment, the due date, and the amount of workload for other classes or work. While the initial scope centers on Canvas integration and calendar organization, we have decided to view Pomodoro timer and OneDrive attachment features as potential extensions, allowing the users to enhance the platform capabilities. The minimum viable product will encompass Canvas API integration, task display in both calendar and list formats, and an interface for adding personalized tasks. The aim of our project is to optimize task management by prioritizing simplicity and efficiency.

## Learning Objectives 
### Shared learning goals (not any different individual goals):
- Applying general Python and API concepts to website building
- Creating functional back-end program with file management and data pulls from APIs
- Designing attractive user interface that appeals to student demographic
- Collaboration in Programming and Developing
- Formatting website so that it can be shared

### Implementation Plan
- **Flask** or **Django** can be used to build the HTLM website
- **JavaScript Calendar** front-end library: https://fullcalendar.io/
- **Canvas API**: https://canvas.instructure.com/doc/api/
  - **`/courses`**: Retrieve information about courses.
  - **`/users`**: Retrieve information about users.
  - **`assignments`**: Manage assignments.
  - **`enrollments`**: Manage course enrollments.
  - **`grades`**: Retrieve and update grade
- **OAuth2 Library** (`oauthlib`) for authentication purposes for Canvas and possible OneDrive

### Project Schedule
#### AGILE Project Schedule
| Tentative Due Date | Task | Description | Status |
| --- | --- | --- | --- |
| Week 0 | Project proposal & UI design |  |  |
|  | - Complete project proposal |  | In progress |
|  | - Clarify features & functionality |  |  |
|  | - Sketch user interface/visual prototype |  |  |
| Week 1 | API implementation/data pull |  |  |
|  | - Access Canvas API |  |  |
|  | - Define data structure in data pull |  |  |
|  | - Consider additional features |  |  |
| Week 2 | Template coding |  |  |
|  | - Create HTML templates using Flask/Django |  |  |
|  | - Implement API data pulls and added data features |  |  |
|  | - Develop the basic structure of the website |  |  |
| Week 3 | HTML website (simple version) |  |  |
|  | - Develop a simplified version of the HTML website interface |  |  |
|  | - Test functionality |  |  |
|  | - Ensure the basic version is ready |  |  |
| Week 4 | Calendar and List Views |  |  |
|  | - Implement different calendar and list views |  |  |
|  | - Integrate priority-based task organization |  |  |
| Week 5 | Additional Features |  |  |
|  | - Add the option to add courses/categories |  |  |
|  | - Explore Pomodoro timer integration |  |  |
| Week 6 | Final Testing and Refinement |  |  |
|  | - Test all functionalities |  |  |
|  | - Address any bugs or issues |  |  |
|  | - Finalize UI/UX |  |  |
|  | - Prepare for project submission |  |  |

#### Collaboration Plan
Our team will foster a collaborative environment by implementing agile approaches to collaboration strategies. We’ll begin by dividing the task based on our individual strengths, interests, and expertise, which ensures that both team members are participating in an area of the project where they feel most comfortable and successful. Regular check-ins, scheduled daily or every other day, will provide a platform for team discussion, progress updates, and issue resolution. For complex tasks, we’ll employ pair programming and the rubber duck method in order to help each other out and understand the code or function we are trying to achieve. We are working in short-week cycles in order to adapt to our work and school schedule; this also allows us to assess our progress most often. We are also effectively communicating by using WhatsApp, which allows us to video call and text, which is also offered in the desktop version and allows for seamless communication.

##### Risks and Limitations
- **Time**: Time limitations might be the most significant constraint, along with collaboration from a distance. Although Github is a great resource for collaborative working, neither of us have developed in a team nor remotely before, so we can anticipate a learning curve for this project.
- **API Functionality:** We haven’t used the Canvas API before, and accessing a key might take some time or be challenging.
- **Authentication and Privacy/Security:** We anticipate that it will be a challenge to implement the right authentication method and code in a manner that maximizes privacy and security. Since users will need to log into Canvas, it will be challenging and new to navigate through this aspect of the program.

###### Additional Course Content
The **authentication** and **privacy/security** topics would be beneficial for our project.
