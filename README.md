# ISBN App

This is a **full-stack web application** for searching books by ISBN. It consists of a **React frontend** and a **Django backend**, both hosted on Render.

**Frontend URL:** [https://isbn-app-frontend.onrender.com](https://isbn-app-frontend.onrender.com/)
**Backend URL:** [https://isbn-app.onrender.com](https://isbn-app.onrender.com/)

**Note: Application is hosted in Render it take few min for both Frontend and Backend app please hit both url before start working with frontend live demo**

---

## Description

The ISBN App allows users to search for books using their ISBN numbers. The app works as follows:

1. **Search via Open Library API**

   * When a user enters an ISBN, the app first searches for the book in own db if not fould use the [Open Library API](https://openlibrary.org/developers/api).
   * The API returns information about the book such as title, author, pages, publisher, short_description, and source etc.

2. **Save to Local Database**

   * After retrieving the book information, the app saves the data to its **own Django backend database (SQLite DB)**.
   * This ensures that frequently searched books are stored locally, allowing faster access in the future.

3. **Frontend Interaction**

   * The React (Vite) frontend handles user interactions, displays search results, and communicates with the backend API.
   * Environment variables in the frontend (like `VITE_API_URL`) are used to point to the Django backend.

---

## Features

* Search for books by ISBN
* first search in own database if not found
* Fetch book information from Open Library API (if not available in own DB)
* Save searched books to own database
* Hosted on Render for easy access

---

## Tech Stack

* **Frontend:** React (Vite), axios
* **Backend:** Django, Django REST Framework
* **Database:** SQLite DB
* **Deployment:** Render

---

## Usage

1. Open the frontend: [https://isbn-app-frontend.onrender.com](https://isbn-app-frontend.onrender.com/)
2. Enter an ISBN number in the search box.
3. The app fetches book information from Open Library and stores it in the backend own database.

--- 

## Project Structure

```
isbn-app/
│
├─ bookmandala_proj/         # Django backend
│  ├─ manage.py              # Django management script
│  ├─ requirements.txt       # Python dependencies
│  ├─ db.sqlite3             # SQLite (used for demo purpose only)
│  ├─ bookmandala_proj/      # Django project settings and wsgi
│  │  ├─ settings.py
│  │  ├─ urls.py
│  │  └─ wsgi.py
│  └─ books/                 # Your Django apps
│     ├─ models.py
│     ├─ views.py
│     ├─ services.py         # Core logic for handling and fetching book data
│     └─ serializers.py
│     └─ urls.py
│
├─ bookmandala_frontend/     # React (Vite) frontend
│  ├─ package.json
│  ├─ vite.config.js
│  ├─ public/                # Public assets
│  ├─ src/                   # React source code
│  │  ├─ pages/              # contain BookSearch.jsx which is main page
│  │  └─ main.jsx
│  └─ dist/                  # Production build folder
│
└─ README.md                 # Project documentation
```

