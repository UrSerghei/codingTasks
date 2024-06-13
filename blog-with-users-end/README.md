# Blog Project

Welcome to the Serghei's Blog Project! This README file will guide you through the steps to set up and run your blog application using Python and Flask.

## Table of Contents

1. [Introduction](#introduction)
2. [Features](#features)
3. [Technologies Used](#technologies-used)
4. [Installation](#installation)
5. [Usage](#usage)
6. [Project Structure](#project-structure)
7. [Routes](#routes)
8. [Contributing](#contributing)

## Introduction

The Blog Project is a simple web application built using Python and Flask. It allows users to create, read, update, and delete blog posts. This project is designed to help you learn the basics of web development with Flask.

## Features

- User authentication (login and registration)
- Create, read, update, and delete blog posts
- View all posts on the homepage
- Individual post pages with comments
- Basic styling with Bootstrap

## Technologies Used

- Python
- Flask
- SQLAlchemy (for database ORM)
- Flask-WTF (for form handling)
- Flask-Login (for user authentication)
- Flask-Migrate (for database migrations)
- Jinja2 (for templating)
- Bootstrap (for styling)

## Installation

Follow these steps to set up the project on your local machine:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/blog-project.git
   cd blog-project
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment:**
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

5. **Set up the database:**
   ```bash
   flask db init
   flask db migrate -m "Initial migration."
   flask db upgrade
   ```

6. **Run the application:**
   ```bash
   flask run
   ```

7. Open your web browser and navigate to `http://127.0.0.1:5000`.

## Usage

1. **Register** a new user account.
2. **Login** with your credentials.
3. **Create** a new blog post.
4. **View** all blog posts on the homepage.
5. **Edit** or **delete** your blog posts.
6. **Logout** when done.

## Project Structure

```
blog-project/
│
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── routes.py
│   ├── forms.py
│   ├── templates/
│   │   ├── base.html
│   │   ├── index.html
│   │   ├── login.html
│   │   ├── register.html
│   │   ├── post.html
│   │   ├── create_post.html
│   │   ├── edit_post.html
│   └── static/
│       └── styles.css
├── migrations/
├── tests/
├── venv/
├── .env
├── .gitignore
├── config.py
├── requirements.txt
└── run.py
```

## Routes

- `/` - Homepage (list all posts)
- `/register` - Register a new user
- `/login` - Login page
- `/logout` - Logout page
- `/post/<id>` - View a single post
- `/post/new` - Create a new post
- `/post/<id>/edit` - Edit a post
- `/post/<id>/delete` - Delete a post

## Contributing

Contributions are welcome! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature-branch-name`
3. Make your changes and commit them: `git commit -m 'Add new feature'`
4. Push to the branch: `git push origin feature-branch-name`
5. Create a pull request.



Happy coding! If you have any questions or feedback, feel free to open an issue or contact the project maintainers.
```