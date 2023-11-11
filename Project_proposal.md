# Project ideas - Final Project Proposal


—**The Big Idea**: What is the main idea of your project? What topics will you explore and what will you accomplish? Describe your minimum viable product (MVP) and your stretch goal.

In this revised website project, our central focus is on leveraging the Canvas API to develop highly functional and user-friendly productivity calendar. The primary goal is to seamlessly integrate with Canvas, presenting all assignments and task in an organized calendar and list format. Users will benefit from a consolidated view of their academic or work related tasks directly within the website. The key functionalities include retrieving tasks from Canvas, arranging them in an calendar and list layout and providing the option for users to add their own tasks. The list will be organized by level of priority based on the data given from calendar on the assignment, the level of difficulty to preform the assignment, the due date and the amount of workload for other classes or work. While the initial scope centers on Canvas integration and calendar organization, we have decided to view Pomodoro timer and OneDrive attachment features as potential extensions, allowing the users to enhance the platform capabilities. The minimum viable product will encompass Canvas API integration, task display in both calendar and list formats, and an interface for adding personalized tasks. The aim of our project is to optimize task management by prioritizing simplicity and efficiency. 

—**Learning Objectives**: Since this is a team project, you may want to articulate both shared and individual learning goals.

Shared learning goals (not any different individual goals):

- Applying general Python and API concepts to website building
- Creating functional back-end program with file management and data pulls from APIs
- Designing attractive user interface (that appeals to student demographic)
- Collaboration in Programming/Developing
- Formatting website so that it can be shared

—**Implementation Plan**: This part may be somewhat ambiguous initially. You might have identified a library or a framework that you believe would be helpful for your project at this early stage. If you're uncertain about executing your project plan, provide a rough plan describing how you'll investigate this information further.

- **Flask** or **Django** can be used to build the HTLM website
- **JavaScript Calendar** front-end library: [https://fullcalendar.io/](https://fullcalendar.io/)
- **Canvas API**: [https://canvas.instructure.com/doc/api/](https://canvas.instructure.com/doc/api/)

Canvas has an API, with which we will be able to connect data to our program and manipulate it

**`/courses`**: Retrieve information about courses.

**`/users`**: Retrieve information about users.

**`/assignments`**: Manage assignments.

**`/enrollments`**: Manage course enrollments.

**`/grades`**: Retrieve and update grade

- **OAuth2 Library** (`oauthlib`) for authentication purposes for Canvas and possible OneDrive.

—**Project Schedule**: You have 6 weeks (roughly) to finish the project. Draft a general timeline for your project. Depending on your project, you might be able to provide a detailed schedule or only an overview. Preparation of a longer project is also accompanied by present uncertainty, and this schedule will likely require revisions as the project progresses.

AGILE Project Schedule

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

—**Collaboration Plan**: How will you collaborate with your teammates on this project? Will you divide tasks and then incorporate them separately? Will you undertake a comprehensive pair program? Explain how you'll ensure effective team collaboration. This may also entail information on any software development methodologies you anticipate using (e.g. agile development). Be sure to clarify why you've picked this specific organizational structure.

—**Risks and Limitations**: What do you believe is the most significant threat to this project's success?

- **Time**: Time limitations might be the most significant constraint, along with collaboration from a distance; Although Github is a great resource for collaborative working, neither of us have developed in a team and remotely before, so we can anticipate a learning curve for this project.
- **API Functionality:**  We haven’t used the Canvas API before, and accessing a key along might take some time/be challenging.
- ****************************************Authentication****************************************  and ******Privacy/security:******  We anticipate that it will be a challenge to implement the right authentication method and code in a manner that maximizes privacy/security. Since users will need to log into Canvas, it will be challenging and new to navigate through this aspect of the program.

—**Additional Course Content**: What topics do you believe will be beneficial to your project?

The **authentication** and **privacy/security** topics would be beneficial for our project.