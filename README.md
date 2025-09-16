# Insurance Premium Prediction Web Application

This project is a web-based Insurance Premium Prediction system built with Django and machine learning. It enables users to estimate insurance premiums based on personal and lifestyle data, leveraging a trained Random Forest Regressor model.

## Features

- User registration and login
- Insurance premium prediction using a trained ML model
- Data analysis and visualization (Jupyter Notebook)
- Informative landing page and contact form
- Admin interface for managing users and data

## Project Structure

```
insurance/
├── home/                # Django app with views, models, urls
├── insurance/           # Django project settings, urls, wsgi/asgi
├── static/              # Static files, ML model, dataset, notebook
├── templates/           # HTML templates
├── db.sqlite3           # SQLite database
├── manage.py            # Django management script
```

## Getting Started

### 1. Clone the Repository

```sh
git clone https://github.com/yourusername/insurance-premium-prediction.git
cd insurance-premium-prediction/insurance
```

### 2. Create and Activate a Virtual Environment

```sh
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies

```sh
pip install -r requirements.txt
```

> **Note:** If `requirements.txt` is missing, install at least:
> ```
> pip install django scikit-learn pandas numpy matplotlib seaborn joblib
> ```

### 4. Apply Database Migrations

```sh
python manage.py migrate
```

### 5. Create a Superuser (Optional, for Admin Access)

```sh
python manage.py createsuperuser
```

### 6. Run the Development Server

```sh
python manage.py runserver
```

Visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser.

### 7. Using the Application

- Register a new user or log in.
- Navigate to the "Prediction" page to input your data and get a premium estimate.
- Explore other pages like About, Contact, etc.

## Machine Learning Model

- The model is trained in the Jupyter notebook [`static/insurance_premium_prediction.ipynb`](static/insurance_premium_prediction.ipynb) using the dataset [`static/insurance.csv`](static/insurance.csv).
- The trained model is saved as [`static/random_forest_regressor`](static/random_forest_regressor) using `joblib`.

## Customization

- To retrain the model, open the notebook, run the cells, and update the saved model file.
- Update templates in [`templates/`](templates/) for UI changes.

## License

This project is for educational purposes.

---

**Project Team:**  
B.Tech CS & AI • Lumbini Technological University  
Contact: [@purnaacharya](https://www.purnaacharya.com.np)
