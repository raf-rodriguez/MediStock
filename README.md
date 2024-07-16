# MediStock

MediStock is a web application that acts as a medical equipment organizer, simplifying medical management for companies or organizations. Its function is like an agenda, structured to keep track of medical equipment expenses. Streamlines organization by allowing users to manage storage, track medications and medical equipment.

#Technology used
The frontend is built using ReactJS and Tailwind CSS Framework

The backend is built using Django REST Framework which interacts with a database.

# Installation instructions

Previous requirements:

Node.js and npm (or thread): Download and install Node.js (version 14 or higher) from the official website https://nodejs.org/en/about/previous-releases. This will also install npm, the Node.js package manager. Alternatively, you can use yarn as a package manager if you prefer.
Python (version 3.7 or higher): Get Python from the official website https://www.python.org/downloads/.
Git (optional): If you plan to clone the project from a version control system such as GitHub, install Git https://www.git-scm.com/downloads.

Steps:
Clone the repository. If you don’t have the project code yet, clone it using Git:

git clone https://github.com/raf-rodriguez/capstone-project

Navigate to the project directory: cd capstone-project

Set up the Django backend:

Create a virtual environment (recommended): It is recommended to isolate project dependencies using a virtual environment. Here’s how to create one using venv:
python -m venv backend_env

Activate the virtual environment: source backend_env/bin/activate # Linux/macOS backend_endv\Scripts\activate.bat # Windows

Run database migrations python manage.py migrate
Configure the interface

Navigate to the frontend directory: cd frontend

Install react.js dependencies npx create-react-app (medistock)

#executing the project
Run the Django backend: python manage.py runserver

Run the react.js interface: npm start
