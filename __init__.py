from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from blueprints import rest

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Shar_mistha1@localhost/fess'
app.config['SECRET_KEY'] = 'atrociousLord123'

db = SQLAlchemy(app=app)
app.register_blueprint(rest, url_prefix='/rest')

@app.route("/")
@app.route("/<garbage>")
def frontend(garbage=''):
    from models import Post
    view = len(Post.query.all())
    return render_template("index.html", view=view)
