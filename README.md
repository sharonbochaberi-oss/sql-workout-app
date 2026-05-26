# sql-workout-app
Build a complete backend API for a workout application using Flask, SQLAlchemy, and Marshmallow,

# Workout Tracker API

## Project Description

Workout Tracker API is a Flask-based RESTful API designed for personal trainers and fitness enthusiasts to manage workouts and exercises.

The application allows users to:

- Create workouts
- Create exercises
- Add exercises to workouts
- Track sets, reps, and duration
- View relationships between workouts and exercises
- Delete workouts and exercises

This project demonstrates:

- Flask backend development
- SQLAlchemy ORM relationships
- Marshmallow serialization/deserialization
- Database migrations using Flask-Migrate
- Table constraints and validations
- RESTful API design principles

---

# Technologies Used

- Python 3
- Flask
- Flask SQLAlchemy
- Flask Migrate
- Marshmallow
- SQLite
- Pipenv

---

# Installation Instructions

## 1. Clone the Repository

```bash
git clone <https://github.com/sharonbochaberi-oss/sql-workout-app.git>
cd sql-workout-app
```

---

## 2. Install Dependencies

```bash
pipenv install
```

Activate the virtual environment:

```bash
pipenv shell
```

---

# Database Setup

Navigate into the server directory:

```bash
cd server
```

---

## Initialize Migrations

```bash
export FLASK_APP=app.py
flask db init
```

---

## Create Migration

```bash
flask db migrate -m "initial migration"
```

---

## Apply Migration

```bash
flask db upgrade
```

---

## Seed the Database

```bash
python3 seed.py
```

---

# Run Instructions

From inside the `server` directory:

```bash
python3 app.py
```

The server runs on:

```bash
http://127.0.0.1:5555
```

---

# API Endpoints

## Workout Endpoints

---

### GET /workouts

Returns a list of all workouts.

Example Response:

```json
[
  {
    "id": 1,
    "date": "2026-05-26",
    "duration_minutes": 60,
    "notes": "Leg day"
  }
]
```

---

### GET /workouts/<id>

Returns a single workout and associated exercises.

---

### POST /workouts

Creates a new workout.

Example Request Body:

```json
{
  "date": "2026-05-26",
  "duration_minutes": 45,
  "notes": "Upper body workout"
}
```

---

### DELETE /workouts/<id>

Deletes a workout and associated workout exercises.

---

# Exercise Endpoints

---

### GET /exercises

Returns all exercises.

---

### GET /exercises/<id>

Returns a single exercise and associated workouts.

---

### POST /exercises

Creates a new exercise.

Example Request Body:

```json
{
  "name": "Bench Press",
  "category": "Strength",
  "equipment_needed": true
}
```

---

### DELETE /exercises/<id>

Deletes an exercise and associated workout exercises.

---

# WorkoutExercise Endpoint

---

### POST /workouts/<workout_id>/exercises/<exercise_id>/workout_exercises

Adds an exercise to a workout with sets, reps, and duration information.

Example Request Body:

```json
{
  "reps": 10,
  "sets": 4,
  "duration_seconds": 60
}
```

---

# Validations and Constraints

This project includes:

## Table Constraints

- Required fields using `nullable=False`
- Unique exercise names using `unique=True`
- Foreign key constraints

## Model Validations

- Workout duration must be greater than 0
- Exercise name must be at least 2 characters
- Reps and sets must be positive integers

## Schema Validations

- Marshmallow required field validation
- Length validation
- Numeric range validation

---

# Author
ouko sharon bochaberi.

```