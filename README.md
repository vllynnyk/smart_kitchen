# 🍽️ Smart Kitchen

[🔗 View on GitHub](https://github.com/vllynnyk/smart_kitchen)  
[🚀 Live Demo on Render](https://smart-kitchen-kytp.onrender.com)    

**Smart Kitchen** is a Django-based web application for managing dishes, ingredients, and cooks.  
It provides a modern and responsive interface, ideal for both personal use and restaurant kitchens.

---

## ✨ Features

- ✅ Full CRUD functionality for dishes and cooks
- 🧂 Manage ingredients and assign them to dishes
- 📂 Categorize dishes by type
- 🔍 Filter dishes by category or ingredients
- 🎨 Clean and responsive UI using **Bootstrap 5.3**
- 📋 Enhanced forms powered by **django-crispy-forms** and `crispy-bootstrap5`
- 🔐 Authentication and user access control

---

## 🛠️ Installation

1. **Clone the repository**
```bash
git clone https://github.com/vllynnyk/smart_kitchen.git
cd smart_kitchen
```

2. **Create and activate a virtual environment**
```bash
python -m venv venv
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate
```
3. **Install dependencies**
```bash
pip install -r requirements.txt
# Or install manually:
pip install django crispy-forms crispy-bootstrap5
```
1. **Apply database migrations**
```bash
python manage.py migrate
```
1. **Run the development server**
```bash
python manage.py runserver

A default superuser has already been created.
Use the following credentials to log in:

Username: admin
Password: 1234pass
```
---

## 🧱 Tech Stack

- **Python** 3.10+
- **Django** 4.x
- **Bootstrap** 5.3
- **django-crispy-forms**
- **crispy-bootstrap5**
- **SQLite** (default database, can be replaced with PostgreSQL or others)

---

## 🧪 Testing

To run tests locally, execute:

```bash
python manage.py test
```

---

## 🤝 Contributing

Contributions are welcome!

To contribute to this project:

1. **Fork** the repository  
2. **Create a new branch**  
```bash
git checkout -b feature/your-feature
```
3. **Make your changes**
4. **Commit and push**
```bash
git push origin feature/your-feature
```
5. **Open a Pull Request and describe your changes**
