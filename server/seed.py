from app import app
from models import db, Exercise, Workout, WorkoutExercise
from datetime import date

with app.app_context():

    print("Clearing database...")

    WorkoutExercise.query.delete()
    Exercise.query.delete()
    Workout.query.delete()

    db.session.commit()

    print("Seeding database...")

    squat = Exercise(
        name="Squat",
        category="Strength",
        equipment_needed=True
    )

    pushup = Exercise(
        name="Push Up",
        category="Bodyweight",
        equipment_needed=False
    )

    run = Exercise(
        name="Running",
        category="Cardio",
        equipment_needed=False
    )

    db.session.add_all([squat, pushup, run])
    db.session.commit()

    workout1 = Workout(
        date=date.today(),
        duration_minutes=60,
        notes="Leg day workout"
    )

    workout2 = Workout(
        date=date.today(),
        duration_minutes=30,
        notes="Cardio session"
    )

    db.session.add_all([workout1, workout2])
    db.session.commit()

    we1 = WorkoutExercise(
        workout_id=workout1.id,
        exercise_id=squat.id,
        reps=10,
        sets=4,
        duration_seconds=0
    )

    we2 = WorkoutExercise(
        workout_id=workout2.id,
        exercise_id=run.id,
        reps=1,
        sets=1,
        duration_seconds=1800
    )

    db.session.add_all([we1, we2])
    db.session.commit()

    print("Database seeded successfully!")