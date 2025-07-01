from mod import app, db

# Create tables before running
with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
