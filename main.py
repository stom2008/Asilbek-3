from flask import Flask, render_template, request 
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime 
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"

db = SQLAlchemy(app)

class Mevalar(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nomi = db.Column(db.String(100), nullable=False)
    narxi = db.Column(db.Integer, nullable=False)
    yaratilgan_vaqt = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"Meva nomi: {self.nomi}"

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        nomi = request.form.get("nomi")
        narxi = request.form.get("narxi")
        meva = Mevalar(nomi=nomi, narxi=narxi)
        db.session.add(meva)
        db.session.commit()
    return render_template("index.html")

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)

