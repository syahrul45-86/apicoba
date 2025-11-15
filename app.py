
from config import app, db
from routes.user_bp import user_bp

@app.route("/")
def home():
    return {"message": "User API is running"}

app.register_blueprint(user_bp)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)

handler = app  # untuk Vercel
