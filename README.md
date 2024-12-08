# E-commerce Product Management Application

This project is a simple e-commerce product management application built with **Django** (backend) and **Vue.js** (frontend). It allows users to add, update, delete, and search for products, and includes features like pagination and stock management.

---

## Prerequisites

Ensure you have the following installed:
- **Python** (Version 3.9 or later)
- **Node.js** (Version 14 or later)
- **npm** or **yarn**
- **MySQL**

---

## Backend Setup (Django)

### 1. Configure the Environment
1. Navigate to the backend directory:
   ```bash
   cd ecommerce_backend
   ```
2. Create a virtual environment:
   ```bash
   python3 -m venv env
   ```
3. Activate the virtual environment:
   - On Linux/Mac:
     ```bash
     source env/bin/activate
     ```
   - On Windows:
     ```bash
     env\Scripts\activate
     ```
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### 2. Configure the Database

Update the `DATABASES` configuration in `ecommerce_backend/settings.py` with your MySQL credentials:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'your_database_name',
        'USER': 'your_username',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

### 3. Apply Migrations

Run the following commands:

```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. Run the Development Server

Start the backend server:

```bash
python manage.py runserver
```

The backend will be accessible at `http://127.0.0.1:8000`.

---

## Frontend Setup (Vue.js)

### 1. Configure the Environment

Navigate to the frontend directory:

```bash
cd ecommerce_frontend
```

Install dependencies:

```bash
npm install
```

### 2. Launch the Frontend

Start the development server:

```bash
npm run serve
```

The frontend will be accessible at `http://127.0.0.1:8001`.

---

## Environment Variables

### Backend

Set up a `.env` file in the backend directory to securely manage sensitive information like database credentials.

### Frontend

Update the axios base URL in `src/services/api.js` to match your backend server URL:

```javascript
const axiosInstance = axios.create({
  baseURL: "http://127.0.0.1:8000/api/",
});
```

---

## Usage

1. Open the frontend in your browser: `http://127.0.0.1:8001`.
2. Use the interface to manage products:
   - **Add Products**: Click the "Add Product" button and fill out the form.
   - **Update Products**: Click "Update" next to a product to modify its details.
   - **Delete Products**: Click "Delete" to remove a product.
   - **Search**: Use the search bar to filter products by name.
   - **Pagination**: Navigate between pages using the pagination controls.

---

## Project Structure

### Backend

```bash
ecommerce_backend/
├── ecommerce_backend/        # Django project settings
├── catalog/                  # App for managing products
├── env/                      # Virtual environment
├── manage.py                 # Django management script
└── requirements.txt          # Python dependencies
```

### Frontend

```bash
ecommerce_frontend/
├── public/                   # Static files
├── src/
│   ├── components/           # Vue.js components
│   ├── views/                # Page views
│   ├── services/             # Axios API service
│   └── App.vue               # Main app component
├── package.json              # Node.js dependencies
└── vue.config.js             # Vue.js configuration
```

---

## Commands Overview

### Backend

- **Activate environment:**
  ```bash
  source env/bin/activate  # Linux/Mac
  env\Scripts\activate     # Windows
  ```
- **Install dependencies:**
  ```bash
  pip install -r requirements.txt
  ```
- **Run server:**
  ```bash
  python manage.py runserver
  ```

### Frontend

- **Install dependencies:**
  ```bash
  npm install
  ```
- **Start server:**
  ```bash
  npm run serve
  ```

---

## Contributors

Rami Rachdi