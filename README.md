# FastAPI CRUD
This is a simple CRUD (Create, Read, Update, Delete) To-Do List application built with FastAPI and MongoDB using Motor as the async MongoDB driver.

# Features
1. Add new tasks
2. Retrieve all tasks
3. Retrieve a specific task by ID
4. Update a task by ID
5. Delete a task by ID

# Requirements
1. Python 3.8+
2. MongoDB
3. FastAPI
4. Motor (async MongoDB driver)

# Installation
Clone the repository:

```bash
git clone https://github.com/bob-hawkins/FastAPI-CRUD.git
cd FastAPI-CRUD

```

# Create a virtual environment and activate it:
Make sure that you open your editor as an administrator in order to create the virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

```

# Install the dependencies:
```bash
pip install -r requirements.txt
```
Make sure you have MongoDB installed locally in your machine

# Running the Application
To start the FastAPI server, run:
```bash
uvicorn app:app --reload
```
This will start the server on ```http://127.0.0.1:8000```