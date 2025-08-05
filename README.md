# Code Review System
# Code Review System - Backend

A simple backend API built with Django and Django REST Framework for a code review platform where users can publish code snippets with issues and others can comment to help solve them.

---

## Features

- Create, list, and view code posts (title, code, description, language, author).
- Add comments to posts.
- RESTful API endpoints for easy frontend integration.
- Admin panel to manage posts and comments.
- CORS enabled for cross-origin requests during development.

---

## Technologies Used

- Python 3.x
- Django 5.x
- Django REST Framework
- django-cors-headers

---

## Getting Started

### Prerequisites

- Python 3.8 or higher installed on your system
- Git installed

---

### Installation

1. **Clone the repository**

```bash
git clone https://github.com/kushal867/code-review.git
cd code-review
Create a virtual environment

bash
Copy
Edit
python -m venv venv
Activate the virtual environment

Windows

bash
Copy
Edit
venv\Scripts\activate
macOS/Linux

bash
Copy
Edit
source venv/bin/activate
Install dependencies

bash
Copy
Edit
pip install -r requirements.txt
If requirements.txt is not present, install packages manually:

bash
Copy
Edit
pip install django djangorestframework django-cors-headers
Apply database migrations

bash
Copy
Edit
python manage.py migrate
Create a superuser (admin account)

bash
Copy
Edit
python manage.py createsuperuser
Run the development server

bash
Copy
Edit
python manage.py runserver
Usage
Once the server is running, the API is available at http://127.0.0.1:8000/.

API Endpoints
Endpoint	HTTP Method	Description
/api/posts/	GET	List all code posts
/api/posts/	POST	Create a new code post
/api/posts/<id>/	GET	Retrieve details of a post
/api/comments/	POST	Add a comment to a code post

Admin Panel
Visit the admin panel to manage posts and comments:

arduino
Copy
Edit
http://127.0.0.1:8000/admin/
Use your superuser credentials to log in.

Configuration
CORS (Cross-Origin Resource Sharing)
To allow your frontend (React, HTML, or other) to access the API during development, this project uses django-cors-headers.

Make sure the following is added to settings.py:

python
Copy
Edit
INSTALLED_APPS += [
    'corsheaders',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
] + MIDDLEWARE

CORS_ALLOW_ALL_ORIGINS = True  # WARNING: For development only, consider restricting origins in production
Project Structure
bash
Copy
Edit
codereview/
├── codereview/               # Project settings & configurations
│   ├── __init__.py
│   ├── settings.py           # Django settings
│   ├── urls.py               # Project URL routing
│   └── wsgi.py
├── review/                   # Main app containing models, views, serializers
│   ├── migrations/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py             # CodePost, Comment models
│   ├── serializers.py        # DRF serializers
│   ├── urls.py               # App-specific routes
│   └── views.py              # API views
├── db.sqlite3                # SQLite database file
├── manage.py                 # Django management script
├── requirements.txt          # Python dependencies


