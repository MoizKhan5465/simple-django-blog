# Simple Django Blog

A beginner-friendly Django blog project with authentication, blog CRUD, likes, comments, and profile stats.

## Features

- User registration and login/logout
- Custom user model (`accounts.User`)
- Welcome email on new registration (via Django signals)
- Create, edit, and delete blog posts
- Public blog feed for logged-in users
- Like/unlike blog posts
- Add comments on blog posts
- Profile page with:
  - User's own blogs
  - Total likes received
  - Total comments received

## Tech Stack

- Python
- Django 6
- SQLite (default DB)
- Bootstrap 5 (templates)

## Project Structure

```
BlogwebMainFolder/
├── BlogProject/         # Project settings and root URLs
├── BlogUpload/          # Blog app (posts, likes, comments)
├── accounts/            # Auth app (register/login/logout + signals)
├── db.sqlite3
└── manage.py
```

## Setup Instructions

### 1) Clone repository

```bash
git clone https://github.com/MoizKhan5465/simple-django-blog.git
cd simple-django-blog
```

### 2) Create and activate virtual environment

```bash
python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
```

### 3) Install dependencies

```bash
pip install django python-dotenv
```

### 4) Configure environment variables

Create a `.env` file in project root:

```env
EMAIL_HOST_USER=your_email@gmail.com
EMAIL_HOST_PASSWORD=your_app_password
```

> Note: Use Gmail App Password (not your normal Gmail password) if 2FA is enabled.

### 5) Run migrations

```bash
python manage.py migrate
```

### 6) (Optional) Create admin user

```bash
python manage.py createsuperuser
```

### 7) Start development server

```bash
python manage.py runserver
```

Open: `http://127.0.0.1:8000/`

## Routes

### Accounts

- `/` → Login
- `/register/` → Register
- `/logout/` → Logout

### Blog

- `/blogs/` → Create blog
- `/blogs/display/` → Feed
- `/blogs/profile/` → Profile
- `/blogs/edit_blog/<id>/` → Edit blog
- `/blogs/delete_blog/<id>/` → Delete blog
- `/blogs/like/<id>/` → Like/Unlike
- `/blogs/comment/<id>/` → Add comment

## Notes

- `LOGIN_URL` is set to `accounts:login`.
- Blog and profile pages require authentication.
- Comment model class is currently named `comments` in code.

## Author

Built by Moiz Khan as a first Django project.