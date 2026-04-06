from app import app, db
from app.models import User  # or your model

with app.app_context():
    users = User.query.all()
    for u in users:
        print(u.id, u.username, u.email)