import flask
import flask_sqlalchemy
import flask_restless
from flask_cors import CORS

app = flask.Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = flask_sqlalchemy.SQLAlchemy(app)

class Pet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode, unique=True)
    image_url = db.Column(db.Unicode)

db.create_all()

manager = flask_restless.APIManager(app, flask_sqlalchemy_db=db)

manager.create_api(Pet, methods=['GET', 'POST', 'DELETE'])

app.run()