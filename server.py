from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost:5432'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    last_name = db.Column(db.String(128))

    def __repr__(self):
        return self.name + " " + self.last_name

@app.route('/')
def home():
    results = Person.query.all()
    return str(results)

def seed_data():
    db.session.add(Person(name='George'))
    db.session.commit()

if __name__ == '__main__':
    app.run()