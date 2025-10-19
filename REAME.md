# 🎬 Movie Review API

A full-stack **Movie Review Web Application** built with **Django** and **Django REST Framework (DRF)**.  
Users can browse movies, read and post reviews, and view trailers — with data fetched from both the **local database** and the **OMDb API**.

---

## 🚀 Features

### 🎥 Movies
- Add, list, and view movie details  
- Fetch additional movie data (title, genre, description, release date, poster)  
- Display posters using URLs or OMDb API links  
- Integrated YouTube trailers for each movie  

### 📝 Reviews
- Authenticated users can add reviews and ratings (1–5)  
- Edit or delete own reviews  
- View all reviews per movie  
- Validation ensures ratings stay between 1 and 5  

### 🔐 Authentication
- User registration and login  
- Each user can manage only their own reviews  

### 🌐 REST API
Built with **Django REST Framework**, the backend exposes API endpoints for integration or frontend use.

| Endpoint | Method | Description |
|-----------|---------|-------------|
| `/api/movies/` | GET | List all movies |
| `/api/movies/<id>/` | GET | Retrieve a single movie |
| `/api/reviews/` | GET, POST | List or create reviews |
| `/api/reviews/<id>/` | GET, PUT, DELETE | Retrieve, update, or delete a review |

---

## 🧱 Project Structure

movie_review_api/
│
├── movies/
│ ├── models.py
│ ├── views.py
│ ├── serializers.py
│ └── urls.py
│
├── reviews/
│ ├── models.py
│ ├── views.py
│ ├── serializers.py
│ └── urls.py
│
├── users/
│ ├── models.py
│ ├── forms.py
│ ├── views.py
│ └── urls.py
│
├── templates/
│ └── base.html
│
├── static/
│ └── css, js, images
│
├── requirements.txt
└── manage.py


---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/movie-review-api.git
cd movie-review-api

2️⃣ Create Virtual Environment
python -m venv venv
source venv/bin/activate   # For Linux/Mac
venv\Scripts\activate      # For Windows

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Run Migrations
python manage.py makemigrations
python manage.py migrate

5️⃣ Create Superuser (optional)
python manage.py createsuperuser

6️⃣ Run Server
python manage.py runserver


Then visit 👉 http://127.0.0.1:8000

🔑 Environment Variables

Create a .env file in the project root for API keys (if used):

OMDB_API_KEY=your_omdb_api_key
YOUTUBE_API_KEY=your_youtube_api_key

🌍 Deployment

This project can be deployed on Heroku, Render, or PythonAnywhere.

Example (Heroku)
heroku create movie-review-api
git push heroku main

🧠 Tech Stack

Backend: Django, Django REST Framework

Frontend: HTML, CSS, JavaScript, Bootstrap

Database: SQLite (default)

External APIs: OMDb API, YouTube API

Deployment: Heroku / Render

👨‍💻 Author

James Kamau
🎓 KCA University — Department of Technology
📘 Course: Software Development
💬 Project: Design and Implementation of a Movie Review API

📄 License

This project is licensed under the MIT License.

🌟 Acknowledgements

OMDb API

YouTube Data API

Django REST Framework