🎬 Movie Review API (Django Project)

📖 Overview

This project is a Django-based web application that allows users to browse and search movies using the OMDb API.
It’s part of a larger system that will eventually include user authentication and review management features.

⚙️ Features

    🔍 Search for movies using keywords

    🎥 View detailed movie information fetched from the OMDb API

    🖼️ Display movie posters dynamically

    🧑‍💬 (Upcoming) Add, edit, and delete user reviews

    🔐 (Upcoming) User registration and login system

🏗️ Project Structure
    movie_review_api/
    │
    ├── movie_review_api/      # Main project folder
    │   ├── settings.py
    │   ├── urls.py
    │   └── ...
    │
    ├── movies/                # App for fetching and displaying movies
    │   ├── models.py
    │   ├── views.py
    │   ├── urls.py
    │   └── templates/movies/
    │
    ├── reviews/               # App for managing movie reviews (coming soon)
    │
    ├── users/                 # App for user authentication (coming soon)
    │
    ├── static/                # Static files (CSS, images, JS)
    │
    ├── templates/             # Base templates (like base.html)
    │
    └── manage.py

🧩 Technologies Used

Python 3

Django 5

OMDb API

HTML, CSS

(Upcoming) JavaScript, Bootstrap

✨ Future Improvements

Add user registration/login system

Allow users to add movie reviews

Display ratings and likes

Add pagination to movie list