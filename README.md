# Student Information System

A Python-based Student Information System developed as a **Cloud Computing Midterm Examination project**. The system demonstrates CRUD operations, modular programming, JSON data persistence, error handling, logging, unit testing, and GitHub version control.

## Project Description

The Student Information System is a console-based application designed to manage student records efficiently. It allows users to add, view, update, delete, and search student information through a simple command-line interface.

The project follows a modular structure by separating the main application, student model, student services, utilities, data storage, logging, and testing components.

## Features

* Add student records
* View all student records
* View a student by ID
* Update student information
* Delete student records
* Search students
* Validate 7-digit student IDs
* Prevent duplicate student IDs
* Store student records in JSON format
* Log application activities
* Handle invalid user input and errors
* Perform unit testing
* GitHub-based version control

## Search Function

The search feature allows users to find students using:

* Student ID
* Student name
* Email
* Course

## Technologies Used

* **Python 3**
* **JSON**
* **Git**
* **GitHub**
* **Visual Studio Code**

## Project Structure

```text
cloud2midtermexam/
│
├── config/
│   └── config.json
│
├── data/
│   └── students.json
│
├── logs/
│   └── app.log
│
├── src/
│   ├── __init__.py
│   ├── main.py
│   │
│   ├── models/
│   │   ├── __init__.py
│   │   └── student.py
│   │
│   ├── services/
│   │   ├── __init__.py
│   │   └── student_service.py
│   │
│   └── utils/
│       ├── __init__.py
│       ├── config.py
│       └── logger.py
│
├── tests/
│   └── test_student_service.py
│
├── .gitignore
└── requirements.txt
```

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/joanamarieguibao/cloud2midtermexam.git
```

### 2. Navigate to the Project Folder

```bash
cd cloud2midtermexam
```

### 3. Run the Application

```bash
python -m src.main
```

## Running the Tests

To run the unit tests:

```bash
python -m unittest discover -s tests -v
```

## GitHub Integration

GitHub is used for version control and source-code management throughout the development of the project.

The repository allows the project files to be:

* Stored remotely
* Tracked through Git commits
* Updated through version control
* Organized using branches
* Integrated with feature development
* Documented through the README file

## Data Storage

Student information is stored locally using a JSON file:

```text
data/students.json
```

This allows student records to persist even after the application is closed.

## Logging

Application activities and important events are recorded in:

```text
logs/app.log
```

Logging helps monitor system activities and assists in identifying errors during development and testing.

## Testing

Unit tests are included in the `tests` directory to verify the functionality of the student management services.

Test file:

```text
tests/test_student_service.py
```

## Project Purpose

This project demonstrates the application of programming concepts, software development practices, data persistence, testing, and GitHub-based version control in developing a functional Student Information System.

## Repository

**GitHub Repository:**
`https://github.com/joanamarieguibao/cloud2midtermexam`
