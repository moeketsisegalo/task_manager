# Task Manager

This project contains code for a task management application. It can be run both on an IDE and using a Dockerfile.

## Getting Started

These instructions will guide you on how to set up and run the code on your local machine.

### Prerequisites

- [Python](https://www.python.org/downloads/) installed on your machine.
- Docker installed on your machine if you want to run the code using Docker.

### Running on an IDE

1. Clone the repository to your local machine.

```bash
git clone https://github.com/moeketsisegalo/task_manager.git
```
2. Open your preferred IDE and navigate to the project directory.

3. Run the code using the IDE's run or debug functionality.


### Running with Docker
1. Clone the repository to your local machine if you haven't done so already.
```
git clone https://github.com/moeketsisegalo/task_manager.git
```
2. Navigate to the project directory.

3. Build the Docker image by running the following command:
```
docker build -t task-manager .
```
4.Once the image is built successfully, you can run a container using the following command:
```
docker run -it task-manager
```
## Usage
1. Run the task_manager.py file using a Python interpreter.
2. The program will prompt you with options to register a user, add a task, view all tasks, or generate reports.
3.To register a user, select the option and provide a new username and password when prompted.
4. To add a task, select the option and enter the required details such as the username of the assigned person, task title, description, due date, date assigned, and task completion status.
5. To view all tasks, select the option, and it will display all the tasks in an easy-to-read format.
6. To view your tasks, select the option, and it will display your tasks along with task numbers.
7. To edit a task, enter the task number when prompted. You can mark the task as complete, change the assigned username, or update the due date.
8. To generate reports, select the option, and it will display various statistics, including the number of tasks, number of completed tasks, number of incomplete tasks, number of overdue tasks, and the percentage of incomplete tasks.
Note: Make sure you have both the user.txt and tasks.txt files in the same directory as the task_manager.py file for the program to read and write the data correctly.
